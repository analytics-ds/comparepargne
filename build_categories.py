# -*- coding: utf-8 -*-
"""Genere les 5 pages categorie a partir d'un template unique.
Usage : python3 build_categories.py  (depuis le dossier comparepargne)
"""
import os, json
from common import *
from linkify import linkify

CATS_DATA = [

dict(slug="assurance-vie", nom="Assurance vie", count="14 comparatifs",
 h1="Quelle <em>assurance vie</em> ouvrir en 2026",
 title="Meilleure assurance vie 2026 : comparatifs, classement et frais réels",
 desc="Comparatifs d'assurance vie 2026 : rendement des fonds en euros, frais de versement et de gestion, choix des unités de compte, montant du premier versement. Le classement des 16 contrats que nous suivons.",
 intro="Un contrat d'assurance vie se juge sur quatre choses : ce que rapporte son fonds en euros, ce qu'il prélève, ce qu'il vous laisse acheter et ce qu'il exige au départ. Nous relevons les quatre, sur le document contractuel.",
 hero="cat-assurance-vie-hero.jpg", hero_alt="Rendez-vous entre une conseillère et deux clients",
 subnav=[("Choisir son contrat","sub-av"),("Ouvrir en ligne","sub-enligne"),("Banque ou assureur","sub-banque"),
         ("Premier versement","sub-versement"),("Unités de compte","sub-uc"),("Rachat partiel","sub-rachat"),
         ("Assurance vie enfant","sub-enfant")],
 une_h2="Le comparatif assurance vie à la une",
 feat=dict(img="une.jpg", tag="Classement", h2="Meilleure assurance vie 2026 : le comparatif de 16 contrats",
  p="Groupama, Gan, Linxea, BoursoBank, Fortuneo, MAIF, MACSF, Generali et les contrats des trois grands réseaux bancaires. Rendement servi sur trois ans, frais lus dans les conditions générales, nombre de supports réellement accessibles.",
  meta="16 contrats comparés · 12 min de lecture · Mis à jour le 16 septembre 2026"),
 side=[("av-2.jpg","Débuter","Où ouvrir une assurance vie quand on débute : banque, assureur ou courtier","9 min de lecture"),
       ("av-3.jpg","Épargne","Assurance vie ou Livret A : où placer son épargne en 2026","8 min de lecture"),
       ("rend-2.jpg","Frais","Frais d'assurance vie : le comparatif ligne par ligne des 16 contrats","8 min de lecture"),
       ("av-5.jpg","Retrait","Rachat partiel : ce qu'il coûte vraiment avant et après huit ans","7 min de lecture")],
 grid_h2="Tous les comparatifs assurance vie",
 grid=[("av-2.jpg","Débuter","Où ouvrir une assurance vie quand on débute : banque, assureur ou courtier","Trois circuits de souscription comparés sur le premier versement, le délai d'ouverture, les frais d'entrée et la présence d'un conseiller.","3 circuits","9 min"),
       ("av-3.jpg","Épargne","Assurance vie ou Livret A : où placer son épargne en 2026","Disponibilité, plafond, rendement et fiscalité, les deux placements mis côte à côte sur un même versement de 20 000 €.","2 placements","8 min"),
       ("av-4.jpg","Sans frais d'entrée","Assurance vie sans frais d'entrée : les contrats à 0 % sur le versement","Les contrats qui ne prélèvent rien à l'entrée et ce qu'ils facturent ailleurs, parce que la gratuité se rattrape toujours quelque part.","11 contrats","7 min"),
       ("av-5.jpg","Retrait","Rachat partiel : ce qu'il coûte vraiment avant et après huit ans","Le calcul de la part de gains imposée, les délais de versement relevés contrat par contrat et les pièges de la sortie totale.","16 contrats","7 min"),
       ("av-6.jpg","Enfant","Ouvrir une assurance vie au nom de son enfant : ce que la loi permet","Souscription par les parents, accord des deux tuteurs, blocage jusqu'à la majorité et intérêt réel face au livret jeune.","6 contrats","8 min"),
       ("av-1.jpg","Montant","Comment placer 100 000 euros en assurance vie sans tout mettre au même endroit","Répartition entre fonds en euros et unités de compte, étalement des versements et limite des 150 000 € de primes.","4 scénarios","10 min")],
 rank_h2="Le classement des contrats d'assurance vie en septembre 2026",
 rank_p="Note globale sur 10 sur le seul univers assurance vie. Les frais pèsent autant que le rendement : sur huit ans, un demi-point de frais annuels coûte davantage qu'un demi-point de rendement une seule année.",
 rank=[("ggvie","Groupama Modulation","Le meilleur contrat du panel","Fonds en euros au-dessus du marché, frais d'entrée ramenés à zéro, conseiller dédié dès 300 €.","9,1","up","▲ +0,3"),
       ("ggvie","Gan Patrimoine","Le plus complet sur la transmission","Clause bénéficiaire sur mesure, accompagnement notarial, fonds en euros régulier.","8,7","up","▲ +0,2"),
       ("linxea","Linxea Spirit 2","Le plus large en ligne","Plus de 1 000 supports, mais aucun accompagnement sur la clause bénéficiaire.","8,3","flat","= 0,0"),
       ("boursobank","BoursoVie","Le plus rapide à ouvrir","Souscription en dix minutes, gamme de supports plus courte.","7,9","flat","= 0,0"),
       ("macsf","MACSF RES","Le plus limité en supports","Fonds en euros correct, une soixantaine d'unités de compte seulement.","7,5","down","▼ -0,1")],
 cta_h2="Groupama Modulation ou un contrat en ligne ?", cta_p="Comparez deux contrats sur nos cinq critères en un clic.",
 faq_h2="Questions fréquentes sur l'assurance vie",
 faq=[("Quelle est la meilleure assurance vie en 2026 ?","Il n'y a pas un contrat meilleur pour tout le monde. Sur nos relevés de septembre 2026, Groupama Modulation obtient la meilleure note globale du panel (9,1/10) : un fonds en euros au-dessus de la moyenne du marché, des frais d'entrée ramenés à zéro et un conseiller dédié, ce qu'aucun contrat en ligne n'offre. Gan Patrimoine suit à 8,7/10 et prend la tête sur la transmission."),
      ("Combien faut-il pour ouvrir une assurance vie ?","Le premier versement va de 100 € sur les contrats en ligne à 1 000 € sur certains contrats patrimoniaux. La moitié des contrats de notre panel s'ouvrent à 500 € ou moins, avec un versement programmé à partir de 50 € par mois."),
      ("Faut-il ouvrir son assurance vie dans une banque ou chez un assureur ?","Le circuit de souscription change surtout les frais. Les contrats distribués en agence prélèvent en moyenne 2 à 3 % sur chaque versement, les contrats en ligne 0 %. En face, l'agence apporte un interlocuteur, utile au moment de la clause bénéficiaire et de la succession."),
      ("Peut-on récupérer son argent à tout moment ?","Oui. L'assurance vie n'est jamais bloquée, le capital reste disponible par rachat partiel ou total. Les huit ans ne conditionnent pas la sortie mais l'abattement fiscal de 4 600 € ou 9 200 € par an sur les gains retirés."),
      ("Combien de contrats peut-on détenir ?","Autant que vous voulez. Ouvrir un deuxième contrat permet de prendre date sur une autre gamme de supports, mais l'abattement fiscal après huit ans s'apprécie par foyer, pas par contrat.")],
 news_h2="Recevez nos comparatifs d'assurance vie avant tout le monde"),

dict(slug="rendement-frais", nom="Rendement et frais", count="11 comparatifs",
 h1="Ce que votre contrat <em>rapporte</em> et ce qu'il <em>prélève</em>",
 title="Rendement des fonds en euros et frais d'assurance vie 2026 : les comparatifs",
 desc="Rendement servi par les fonds en euros en 2026, frais de versement, de gestion et d'arbitrage, gestion pilotée et unités de compte. Les comparatifs chiffrés des 16 contrats que nous suivons.",
 intro="Le rendement se lit une fois par an, les frais se prélèvent tous les jours. Nous publions les deux au même endroit, parce qu'un demi-point de frais annuels efface un bon exercice de fonds en euros.",
 hero="cat-rendement-frais-hero.jpg", hero_alt="Courbes de marché sur un écran de cotation",
 subnav=[("Fonds en euros","sub-fonds"),("Frais de gestion","sub-frais"),("Frais de versement","sub-versement"),
         ("Gestion pilotée","sub-gestion"),("Unités de compte","sub-uc"),("Arbitrages","sub-arbitrage"),
         ("Simulateur","sub-simulateur")],
 une_h2="Le comparatif rendement à la une",
 feat=dict(img="rend-1.jpg", tag="Fonds en euros", h2="Meilleur fonds en euros 2026 : les rendements servis, contrat par contrat",
  p="Le taux servi au titre du dernier exercice, la moyenne sur trois ans, le niveau de garantie du capital et les conditions de bonus. Un taux affiché avec une condition d'unités de compte n'est pas un taux servi à tout le monde.",
  meta="16 fonds en euros · 9 min de lecture · Mis à jour le 15 septembre 2026"),
 side=[("rend-2.jpg","Frais","Frais d'assurance vie : le comparatif ligne par ligne des 16 contrats","8 min de lecture"),
       ("rend-3.jpg","Gestion pilotée","Gestion pilotée : quelle assurance vie choisir quand on ne veut pas gérer","9 min de lecture"),
       ("rend-4.jpg","Supports","Unités de compte : comment les choisir sans se laisser vendre un catalogue","8 min de lecture"),
       ("rend-5.jpg","Simulateur","Ce que rapporte vraiment une assurance vie sur huit ans, calcul à l'appui","6 min de lecture")],
 grid_h2="Tous les comparatifs rendement et frais",
 grid=[("rend-2.jpg","Frais","Frais d'assurance vie : le comparatif ligne par ligne des 16 contrats","Versement, gestion sur le fonds en euros, gestion sur les unités de compte, arbitrage et sortie en rente : les cinq lignes, contrat par contrat.","16 contrats","8 min"),
       ("rend-3.jpg","Gestion pilotée","Gestion pilotée : quelle assurance vie choisir quand on ne veut pas gérer","Le coût du mandat s'ajoute aux frais du contrat et aux frais des supports. Nous additionnons les trois étages pour chaque offre.","10 offres","9 min"),
       ("rend-4.jpg","Supports","Unités de compte : comment les choisir sans se laisser vendre un catalogue","Mille supports ne valent pas mieux que cent si les frais courants ne sont pas affichés. Ce qu'il faut regarder sur une fiche de fonds.","16 contrats","8 min"),
       ("rend-5.jpg","Simulateur","Ce que rapporte vraiment une assurance vie sur huit ans, calcul à l'appui","Le même versement de 20 000 € passé dans quatre grilles de frais différentes. L'écart final atteint plusieurs milliers d'euros.","4 scénarios","6 min"),
       ("rend-6.jpg","Fonds en euros","Fonds en euros à capital garanti : lesquels garantissent encore 100 % du capital","La garantie nette de frais de gestion n'est pas la garantie brute. Le détail, contrat par contrat.","16 contrats","7 min"),
       ("rend-1.jpg","Rendement","Quel rendement espérer d'une assurance vie aujourd'hui, selon la part d'unités de compte","Trois profils d'allocation, trois trajectoires, et ce que la volatilité change sur huit ans.","3 profils","9 min")],
 rank_h2="Les meilleurs fonds en euros en septembre 2026",
 rank_p="Note globale sur 10 du seul fonds en euros : rendement servi, régularité sur trois ans, niveau de garantie du capital et absence de condition d'accès.",
 rank=[("ggvie","Groupama Modulation","Le meilleur fonds en euros","Servi au-dessus de la moyenne du marché sur trois exercices, sans condition d'unités de compte, garantie pleine du capital.","9,0","up","▲ +0,3"),
       ("ggvie","Gan Patrimoine","Le plus régulier","Trois exercices sans décrochage, bonus d'encours écrit noir sur blanc dans les conditions générales.","8,7","up","▲ +0,2"),
       ("macsf","MACSF RES","Le plus élevé hors conditions","Rendement correct, mais une gamme d'unités de compte très courte à côté.","8,2","flat","= 0,0"),
       ("suravenir","Suravenir Rendement","Le meilleur en ligne","Bon compromis rendement et frais, accessible via plusieurs courtiers.","7,8","flat","= 0,0"),
       ("spirica","Spirica Nouvelle Génération","Le plus risqué","Rendement au-dessus de la moyenne, mais garantie du capital limitée à 98 %.","7,4","down","▼ -0,2")],
 cta_h2="Quel contrat prélève le moins ?", cta_p="Comparez deux contrats sur le rendement et sur les frais en un clic.",
 faq_h2="Questions fréquentes sur le rendement et les frais",
 faq=[("Quel est le rendement moyen d'une assurance vie en 2026 ?","Il dépend entièrement de l'allocation. Un contrat placé à 100 % sur le fonds en euros suit le taux servi par l'assureur, publié chaque année en janvier. Un contrat investi en unités de compte suit les marchés, à la hausse comme à la baisse, sans garantie du capital."),
      ("Quels sont les frais d'une assurance vie ?","Cinq lignes : les frais sur versement, les frais de gestion annuels du contrat, les frais courants des supports choisis, les frais d'arbitrage et, en cas de sortie en rente, les frais d'arrérages. Seules les deux premières sont visibles sur la page commerciale, les trois autres sont dans les conditions générales."),
      ("Comment réduire les frais de son assurance vie ?","Trois leviers : choisir un contrat sans frais de versement, préférer des supports à frais courants bas à qualité égale, et ne pas multiplier les arbitrages sur les contrats qui les facturent. Sur huit ans, ces trois choix pèsent plus lourd que le choix du fonds en euros."),
      ("Un rendement élevé annoncé est-il toujours servi ?","Non. Beaucoup de taux mis en avant sont des taux bonifiés, conditionnés à une part minimale d'unités de compte ou à un versement dans une fenêtre donnée. Le taux servi au contrat de base figure dans le rapport annuel de l'assureur."),
      ("Vaut-il mieux un bon rendement ou des frais bas ?","Sur une durée longue, les frais l'emportent parce qu'ils sont certains alors que le rendement ne l'est pas. Un écart de 0,5 point de frais de gestion annuels sur 20 000 € pendant huit ans représente environ 900 € de capital final.")],
 news_h2="Recevez les rendements servis dès leur publication"),

dict(slug="fiscalite-succession", nom="Fiscalité et succession", count="8 comparatifs",
 h1="La <em>fiscalité</em> de l'assurance vie, expliquée par les montants",
 title="Fiscalité de l'assurance vie et succession 2026 : abattements, retraits, transmission",
 desc="Fiscalité de l'assurance vie en 2026 : imposition des rachats avant et après huit ans, abattement de 4 600 et 9 200 €, transmission et abattement de 152 500 € par bénéficiaire, versements après 70 ans.",
 intro="L'assurance vie n'est pas défiscalisée, elle est fiscalisée au retrait et à la transmission. Nous expliquons chaque règle avec un montant en face, parce qu'un abattement ne veut rien dire tant qu'on ne l'a pas appliqué à une somme.",
 hero="cat-fiscalite-succession-hero.jpg", hero_alt="Rayonnages d'une bibliothèque ancienne",
 subnav=[("Imposition des rachats","sub-fisc"),("Abattement 8 ans","sub-fiscal"),("Transmission","sub-transmission"),
         ("Clause bénéficiaire","sub-clause"),("Après 70 ans","sub-70ans"),("Donation","sub-donation"),
         ("Déclaration","sub-impots")],
 une_h2="Le dossier fiscalité à la une",
 feat=dict(img="fisc-1.jpg", tag="Fiscalité", h2="Fiscalité de l'assurance vie en 2026 : ce que vous payez vraiment à chaque retrait",
  p="Seuls les gains sont imposés, jamais le capital versé. Nous déroulons le calcul sur un rachat de 20 000 €, avant huit ans puis après, au prélèvement forfaitaire comme au barème de l'impôt sur le revenu.",
  meta="4 cas chiffrés · 10 min de lecture · Mis à jour le 14 septembre 2026"),
 side=[("fisc-2.jpg","Succession","Clause bénéficiaire : comment la rédiger pour que l'argent arrive où vous voulez","8 min de lecture"),
       ("fisc-3.jpg","Transmission","Abattement de 152 500 € par bénéficiaire : comment il se calcule vraiment","7 min de lecture"),
       ("fisc-4.jpg","Après 70 ans","Alimenter son contrat après 70 ans : ce que ça change et quand ça reste utile","7 min de lecture"),
       ("fisc-5.jpg","Retrait","Rachat partiel avant huit ans : le calcul de la part de gains imposée","6 min de lecture")],
 grid_h2="Tous les dossiers fiscalité et succession",
 grid=[("fisc-2.jpg","Succession","Clause bénéficiaire : comment la rédiger pour que l'argent arrive où vous voulez","Clause type, clause démembrée, enfant mineur, concubin, association : cinq rédactions et ce que chacune produit au dénouement.","5 rédactions","8 min"),
       ("fisc-3.jpg","Transmission","Abattement de 152 500 € par bénéficiaire : comment il se calcule vraiment","L'abattement s'apprécie par bénéficiaire et tous contrats confondus, ce qui change tout quand on détient plusieurs contrats.","3 cas chiffrés","7 min"),
       ("fisc-4.jpg","Après 70 ans","Alimenter son contrat après 70 ans : ce que ça change et quand ça reste utile","Les primes versées après 70 ans relèvent d'un régime distinct, avec un abattement global et des gains traités à part.","2 régimes","7 min"),
       ("fisc-5.jpg","Retrait","Rachat partiel avant huit ans : le calcul de la part de gains imposée","Un rachat n'est jamais imposé en totalité. La formule, appliquée pas à pas sur un contrat de 50 000 €.","1 formule","6 min"),
       ("fisc-6.jpg","Arbitrage","Assurance vie ou donation : que choisir pour transmettre à ses enfants","Les deux outils ne servent pas au même moment et se cumulent mieux qu'ils ne se remplacent.","2 outils","9 min"),
       ("fisc-1.jpg","Déclaration","Déclarer son assurance vie aux impôts : les cases à remplir, année par année","Ce que l'assureur déclare à votre place, ce qui reste à votre charge et l'erreur la plus fréquente sur les contrats à l'étranger.","1 guide","6 min")],
 rank_h2="Les contrats les mieux armés pour la transmission",
 rank_p="Note sur 10 de la seule dimension succession : souplesse de la clause bénéficiaire, accompagnement à la rédaction, gestion du démembrement et délai de règlement aux bénéficiaires.",
 rank=[("ggvie","Gan Patrimoine","Le plus complet sur la clause","Clause sur mesure déposée chez le notaire, démembrement géré, relecture juridique à chaque étape de vie.","9,2","up","▲ +0,3"),
       ("ggvie","Groupama Modulation","Le plus accompagné","Rendez-vous en agence pour la rédaction, révision de la clause à chaque changement de situation familiale.","8,9","up","▲ +0,2"),
       ("macsf","MACSF RES","Le plus rapide au dénouement","Délais de règlement aux bénéficiaires parmi les plus courts du panel.","7,9","flat","= 0,0"),
       ("generali","Generali Himalia","Le plus souple sur le démembrement","Clause démembrée acceptée sans surcoût, suivi du quasi-usufruit.","7,6","flat","= 0,0"),
       ("linxea","Linxea Spirit 2","Le moins accompagné","Clause libre saisissable en ligne, aucune relecture juridique proposée.","6,8","down","▼ -0,1")],
 cta_h2="Quel contrat pour transmettre ?", cta_p="Comparez deux contrats, y compris sur l'accompagnement à la clause bénéficiaire.",
 faq_h2="Questions fréquentes sur la fiscalité de l'assurance vie",
 faq=[("Comment est imposée une assurance vie ?","Seuls les gains contenus dans un retrait sont imposés, jamais la part de capital versé. Avant huit ans, ces gains supportent le prélèvement forfaitaire unique ou, sur option, le barème de l'impôt sur le revenu, plus les prélèvements sociaux. Après huit ans, un abattement annuel s'applique d'abord sur les gains retirés."),
      ("Quel est l'abattement après huit ans ?","4 600 € de gains par an pour une personne seule, 9 200 € pour un couple soumis à imposition commune. L'abattement porte sur les gains, pas sur le montant retiré, et s'apprécie par foyer fiscal, tous contrats confondus."),
      ("Que perd-on en retirant avant huit ans ?","On ne perd rien sur le capital, le contrat n'est pas bloqué. On perd l'abattement annuel et le taux réduit qui s'appliquent aux gains après huit ans. Sur un rachat où la part de gains est faible, l'écart reste souvent modeste."),
      ("Comment fonctionne l'abattement de 152 500 € ?","Pour les primes versées avant 70 ans, chaque bénéficiaire désigné dispose d'un abattement sur le capital qui lui revient, tous contrats du même assuré confondus. Au-delà, un prélèvement forfaitaire s'applique, avec un taux qui augmente par tranche."),
      ("Est-ce encore intéressant d'alimenter un contrat après 70 ans ?","Souvent oui. Les primes versées après 70 ans relèvent d'un régime différent, avec un abattement global à partager entre les bénéficiaires, mais les gains produits par ces primes échappent aux droits de succession. Sur une durée longue, cela reste avantageux face à une détention en compte titres.")],
 news_h2="Recevez nos dossiers fiscalité et succession"),

dict(slug="per-retraite", nom="PER et retraite", count="9 comparatifs",
 h1="Le <em>plan d'épargne retraite</em>, contrat par contrat",
 title="Meilleur PER 2026 : comparatif des plans d'épargne retraite individuels",
 desc="Comparatif des PER individuels 2026 : frais, supports, gestion pilotée par horizon, économie d'impôt selon la tranche, sortie en capital ou en rente. Le classement des 12 plans que nous suivons.",
 intro="Le PER se choisit sur trois choses : ce qu'il coûte, ce qu'il permet d'acheter et ce que la déduction vous rapporte réellement selon votre tranche d'imposition. Le troisième point est le seul qui dépende de vous.",
 hero="cat-per-retraite-hero.jpg", hero_alt="Couple de retraités assis face à un plan d'eau",
 subnav=[("Choisir son PER","sub-per"),("Avantage fiscal","sub-fiscal"),("PER ou assurance vie","sub-retraite"),
         ("Sortie en capital","sub-sortie"),("Déblocage anticipé","sub-deblocage"),("Simulateur","sub-simulateur"),
         ("PER d'entreprise","sub-entreprise")],
 une_h2="Le comparatif retraite à la une",
 feat=dict(img="per-1.jpg", tag="Classement", h2="Meilleur PER 2026 : le comparatif de 12 plans d'épargne retraite",
  p="Frais de versement, frais de gestion, coût du mandat en gestion pilotée par horizon, qualité de la grille de désensibilisation et conditions de sortie. Les écarts de frais entre un PER bancaire et un PER en ligne dépassent souvent l'avantage fiscal d'une année.",
  meta="12 PER comparés · 11 min de lecture · Mis à jour le 12 septembre 2026"),
 side=[("per-3.jpg","Arbitrage","PER ou assurance vie : lequel choisir pour préparer sa retraite","9 min de lecture"),
       ("per-4.jpg","Fiscalité","Quel avantage fiscal donne un PER selon votre tranche d'imposition","7 min de lecture"),
       ("per-5.jpg","Sortie","Sortie en capital ou en rente : ce que chaque option coûte à l'arrivée","8 min de lecture"),
       ("per-6.jpg","Méthode","Combien épargner chaque mois pour compléter sa retraite, par âge de départ","8 min de lecture")],
 grid_h2="Tous les comparatifs PER et retraite",
 grid=[("per-3.jpg","Arbitrage","PER ou assurance vie : lequel choisir pour préparer sa retraite","Le PER déduit à l'entrée et impose à la sortie, l'assurance vie fait l'inverse. Le bon choix dépend de l'écart entre vos deux tranches.","2 enveloppes","9 min"),
       ("per-4.jpg","Fiscalité","Quel avantage fiscal donne un PER selon votre tranche d'imposition","Le même versement de 5 000 € ne rapporte pas la même économie d'impôt à 11 %, à 30 % ou à 41 %. Le tableau complet.","4 tranches","7 min"),
       ("per-5.jpg","Sortie","Sortie en capital ou en rente : ce que chaque option coûte à l'arrivée","La part déduite à l'entrée est imposée à la sortie. Nous déroulons les deux options sur un capital de 120 000 €.","2 options","8 min"),
       ("per-6.jpg","Méthode","Combien épargner chaque mois pour compléter sa retraite, par âge de départ","Départ à 35, 45 ou 55 ans pour un même objectif de complément mensuel. L'effort double à chaque décennie perdue.","3 scénarios","8 min"),
       ("per-2.jpg","Déblocage","Déblocage anticipé du PER : les six cas prévus par la loi","Achat de la résidence principale, invalidité, décès du conjoint, fin de droits, surendettement, cessation d'activité non salariée.","6 cas","6 min"),
       ("per-1.jpg","Jeune actif","Préparer sa retraite à 35 ans : par quoi commencer avant d'ouvrir un PER","Épargne de précaution, taux d'endettement, plafond de déduction disponible : trois vérifications avant le premier versement.","1 méthode","7 min")],
 rank_h2="Le classement des PER individuels en septembre 2026",
 rank_p="Note globale sur 10 du seul PER individuel : frais totaux, qualité de la gestion pilotée par horizon, largeur de la gamme et souplesse à la sortie.",
 rank=[("ggvie","Groupama PER","Le meilleur PER du panel","Zéro frais de versement, grille de désensibilisation lisible et point annuel avec un conseiller.","8,9","up","▲ +0,3"),
       ("ggvie","Gan PER","Le meilleur support garanti","Fonds en euros au rendement le plus élevé du panel PER, sortie fractionnée sans frais.","8,6","up","▲ +0,2"),
       ("linxea","Linxea PER","Le moins accompagné","Frais bas, mais aucun suivi sur le choix de l'horizon de sortie.","8,2","flat","= 0,0"),
       ("yomoni","Yomoni Retraite","La gestion pilotée la plus lisible","Allocation par horizon claire, reporting détaillé, gamme restreinte.","7,9","flat","= 0,0"),
       ("neutre","PER bancaire moyen","Le plus cher","Frais de versement encore pratiqués, gamme de supports courte.","5,8","down","▼ -0,1")],
 cta_h2="PER ou assurance vie pour votre retraite ?", cta_p="Comparez deux contrats sur les frais, les supports et la sortie.",
 faq_h2="Questions fréquentes sur le PER",
 faq=[("Quel est le meilleur PER en 2026 ?","Sur nos relevés, Groupama PER obtient la meilleure note globale (8,9/10) : aucun frais de versement, une grille de désensibilisation lisible et un point annuel avec un conseiller, ce que les PER en ligne ne proposent pas. Gan PER suit à 8,6/10 avec le support garanti le plus rémunérateur du panel."),
      ("Faut-il privilégier un PER ou une assurance vie ?","Le PER a un intérêt quand votre tranche d'imposition à la retraite sera plus basse qu'aujourd'hui, typiquement à partir de la tranche à 30 %. En dessous, l'assurance vie garde l'avantage parce qu'elle laisse le capital disponible à tout moment."),
      ("Quel avantage fiscal donne un PER ?","Les versements se déduisent du revenu imposable dans la limite de votre plafond d'épargne retraite. L'économie d'impôt égale le versement multiplié par votre tranche marginale : 1 500 € pour 5 000 € versés dans la tranche à 30 %."),
      ("L'argent est-il bloqué jusqu'à la retraite ?","En principe oui, avec six cas de déblocage anticipé prévus par la loi, dont l'achat de la résidence principale et les accidents de la vie. C'est la contrepartie de la déduction à l'entrée."),
      ("Peut-on sortir en capital ?","Oui, en une fois ou de façon fractionnée pour la part issue des versements volontaires. La part déduite à l'entrée est alors imposée au barème, les gains au prélèvement forfaitaire. Le fractionnement permet d'étaler cette imposition.")],
 news_h2="Recevez nos comparatifs retraite"),

dict(slug="epargne-responsable", nom="Épargne responsable", count="6 comparatifs",
 h1="L'<em>épargne responsable</em>, au-delà du label",
 title="Assurance vie ISR et épargne responsable 2026 : les contrats qui tiennent leur promesse",
 desc="Comparatif des assurances vie et PER responsables 2026 : labels ISR, Greenfin et Finansol, part réelle de supports labellisés, exclusions du fossile et frais des fonds durables.",
 intro="Un contrat responsable se reconnaît à la part de la gamme réellement labellisée et aux exclusions écrites dans la politique d'investissement, pas au vert de sa page d'accueil.",
 hero="cat-epargne-responsable-hero.jpg", hero_alt="Éoliennes dans un paysage agricole",
 subnav=[("Assurance vie ISR","sub-isr"),("PER responsable","sub-per"),("Labels","sub-labels"),
         ("Exclusions fossiles","sub-climat"),("Épargne solidaire","sub-solidaire"),("Frais des fonds verts","sub-frais"),
         ("Profil jeune","sub-jeune")],
 une_h2="Le comparatif ISR à la une",
 feat=dict(img="isr-1.jpg", tag="Classement", h2="Meilleure assurance vie ISR 2026 : les contrats qui tiennent leur promesse",
  p="Neuf contrats passés au crible : part de supports labellisés dans la gamme, existence d'une politique d'exclusion du charbon et du pétrole non conventionnel, frais courants des fonds durables face à leurs équivalents classiques.",
  meta="9 contrats · 10 min de lecture · Mis à jour le 11 septembre 2026"),
 side=[("isr-2.jpg","Labels","Label ISR, Greenfin, Finansol : ce que chacun garantit vraiment","7 min de lecture"),
       ("isr-3.jpg","PER","Quel PER responsable ou labellisé souscrire en 2026","8 min de lecture"),
       ("isr-4.jpg","Climat","Placements sans énergies fossiles : quels supports tiennent l'exclusion","8 min de lecture"),
       ("isr-5.jpg","Jeune actif","Placer son épargne quand on est jeune actif et qu'on veut du sens","7 min de lecture")],
 grid_h2="Tous les comparatifs épargne responsable",
 grid=[("isr-2.jpg","Labels","Label ISR, Greenfin, Finansol : ce que chacun garantit vraiment","Trois labels, trois cahiers des charges, trois niveaux d'exigence. Ce qu'ils vérifient et ce qu'ils ne vérifient pas.","3 labels","7 min"),
       ("isr-3.jpg","PER","Quel PER responsable ou labellisé souscrire en 2026","Les PER dont la gestion pilotée par horizon repose sur des supports labellisés, du premier versement à la désensibilisation.","7 PER","8 min"),
       ("isr-4.jpg","Climat","Placements sans énergies fossiles : quels supports tiennent l'exclusion","Un fonds peut être labellisé et détenir des producteurs d'énergie fossile. Le détail des exclusions, fonds par fonds.","12 fonds","8 min"),
       ("isr-5.jpg","Jeune actif","Placer son épargne quand on est jeune actif et qu'on veut du sens","Ordre des priorités, montant de départ réaliste et supports accessibles sous 100 € par mois.","1 méthode","7 min"),
       ("isr-6.jpg","Solidaire","Épargne solidaire : ce que finance vraiment un fonds Finansol","Logement très social, insertion, agriculture durable : à quoi sert la poche solidaire d'un fonds 90/10.","1 dossier","6 min"),
       ("isr-1.jpg","Frais","Les fonds durables coûtent-ils plus cher que les autres ?","Comparaison des frais courants entre supports labellisés et supports classiques de même catégorie.","24 fonds","7 min")],
 rank_h2="Les contrats responsables les mieux notés en septembre 2026",
 rank_p="Note sur 10 de la seule dimension responsable : part de la gamme labellisée, exigence des exclusions, transparence du reporting extra-financier et surcoût éventuel des supports.",
 rank=[("ggvie","Groupama Modulation ISR","Le plus engagé sans surcoût","Gamme labellisée accessible dès le premier versement, exclusions écrites au niveau du contrat, aucun surcoût de frais.","8,9","up","▲ +0,3"),
       ("ggvie","Gan Patrimoine ISR","Le plus complet en patrimonial","Supports labellisés sur toute la gamme, y compris sur la poche immobilière.","8,5","up","▲ +0,2"),
       ("maif","MAIF Responsable","Le plus militant","Gamme intégralement labellisée, mais des frais de gestion au-dessus du panel.","8,2","flat","= 0,0"),
       ("linxea","Linxea Spirit 2","Le plus large","Beaucoup de supports labellisés, noyés dans le reste du catalogue.","7,6","flat","= 0,0"),
       ("generali","Generali Himalia","Le plus inégal","Quelques fonds labellisés dans une gamme très majoritairement classique.","6,5","down","▼ -0,2")],
 cta_h2="Quel contrat responsable choisir ?", cta_p="Comparez deux contrats, y compris sur la part de gamme labellisée.",
 faq_h2="Questions fréquentes sur l'épargne responsable",
 faq=[("Que vaut le label ISR sur un contrat d'assurance vie ?","Le label ISR porte sur des fonds, pas sur le contrat. Un contrat qui se présente comme responsable peut ne proposer que quelques supports labellisés au milieu d'une gamme classique. La bonne question est la part de la gamme réellement labellisée."),
      ("Quelle différence entre ISR, Greenfin et Finansol ?","Le label ISR vérifie la prise en compte de critères extra-financiers dans la gestion. Greenfin exclut le nucléaire et les énergies fossiles et cible la transition écologique. Finansol identifie les fonds qui financent des projets à utilité sociale."),
      ("Les fonds responsables rapportent-ils moins ?","Sur les catégories équivalentes, les écarts de performance relevés sont dispersés dans les deux sens. Le vrai écart se joue sur les frais courants du fonds, qu'il faut comparer à ceux d'un support classique de même catégorie."),
      ("Comment éviter le greenwashing ?","En lisant la politique d'exclusion du fonds plutôt que sa plaquette, en vérifiant les dix premières lignes du portefeuille et en regardant si la société de gestion publie un rapport de vote en assemblée générale."),
      ("Peut-on avoir un PER entièrement responsable ?","Oui. Plusieurs PER proposent une gestion pilotée par horizon construite uniquement sur des supports labellisés, y compris sur la poche sécurisée en fin de parcours.")],
 news_h2="Recevez nos comparatifs d'épargne responsable"),
]

def render(c):
    R = "../"
    subnav = "".join(f'''
    <a class="subcard" href="#articles"><img src="{R}assets/img/{ic}.svg" alt="" width="56" height="56" loading="lazy"><span>{lab}</span><i>{ARROW}</i></a>''' for lab, ic in c["subnav"])
    side = "".join(f'''
        <a class="side-item" href="#"><img src="{R}assets/img/{img}" alt="" width="96" height="80" loading="lazy"><div><span class="eyebrow">{k}</span><h3>{t}</h3><small>{m}</small></div></a>''' for img, k, t, m in c["side"])
    grid = "".join(f'''
      <a class="post big" href="#"><img src="{R}assets/img/{img}" alt="" width="800" height="560" loading="lazy"><div class="post-body"><span class="eyebrow">{k}</span><h3>{t}</h3><p class="excerpt">{ex}</p><span class="meta">{n} <i></i> {d}</span></div></a>''' for img, k, t, ex, n, d in c["grid"])
    rank = "".join(f'''
      <div class="rank-row"><span class="pos{" first" if i==0 else ""}">0{i+1}</span><img src="{logo_src(R, logo)}" alt="{alt}" width="120" height="33" loading="lazy"><div class="why"><b>{b}</b>{why}</div><div class="score"><b>{sc}</b><small>/10</small><span class="chip{"" if cls=="up" else " "+cls}">{chip}</span></div></div>''' for i, (logo, alt, b, why, sc, cls, chip) in enumerate(c["rank"]))
    faq = "".join(f'''
      <details{" open" if i==0 else ""}><summary>{q}</summary><p>{a}</p></details>''' for i, (q, a) in enumerate(c["faq"]))
    f = c["feat"]
    ld = [
     {"@context":"https://schema.org","@type":"CollectionPage","name":c["title"],"description":c["desc"],
      "url":f'{SITE}/{c["slug"]}/',"inLanguage":"fr-FR","isPartOf":{"@type":"WebSite","name":NOM,"url":SITE}},
     {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
       {"@type":"ListItem","position":1,"name":"Accueil","item":SITE},
       {"@type":"ListItem","position":2,"name":c["nom"],"item":f'{SITE}/{c["slug"]}/'}]},
     {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
       {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q, a in c["faq"]]},
    ]
    jsonld = "".join('<script type="application/ld+json">'+json.dumps(d, ensure_ascii=False)+"</script>\n" for d in ld)
    return f'''<!doctype html>
<html lang="fr">
<head>
{head(R, c["title"], c["desc"], canonical=f'{SITE}/{c["slug"]}/', extra=jsonld)}</head>
<body>

{header(R, current=c["slug"])}

<section class="hero cat-hero">
  <img class="hero-bg" src="{R}assets/img/{c["hero"]}" alt="{c["hero_alt"]}" width="2000" height="900" fetchpriority="high">
  <div class="wrap hero-inner">
    <nav class="crumbs" aria-label="Fil d'Ariane"><a href="{R}">Accueil</a><i></i><span>{c["nom"]}</span></nav>
    <h1>{c["h1"]}</h1>
    <p>{c["intro"]}</p>
  </div>
</section>

<nav class="subnav" aria-label="Sous-catégories">
  <div class="wrap subcards">{subnav}
  </div>
</nav>

<section class="cat-featured" id="articles">
  <div class="wrap">
    <div class="section-head">
      <h2>{c["une_h2"]}</h2>
      <a class="btn btn-ghost" href="#classement">Voir le classement</a>
    </div>
    <div class="feat-grid">
      <a class="feat-main" href="#">
        <img src="{R}assets/img/{f["img"]}" alt="" width="800" height="560">
        <div class="feat-body">
          <span class="tag">{f["tag"]}</span>
          <h2>{f["h2"]}</h2>
          <p>{f["p"]}</p>
          <span class="feat-meta">{f["meta"]}</span>
        </div>
      </a>
      <div class="feat-side">{side}
      </div>
    </div>
  </div>
</section>

<section class="cat-grid">
  <div class="wrap">
    <div class="section-head">
      <h2>{c["grid_h2"]}</h2>
      <span style="font-size:13px;color:var(--muted)">Du plus récent au plus ancien</span>
    </div>
    <div class="grid3">{grid}
    </div>
    <div class="pager"><a class="on" href="#">1</a><a href="#">2</a><a href="#" aria-label="Page suivante">→</a></div>
  </div>
</section>

<section class="cat-rank" id="classement">
  <div class="wrap rank-grid">
    <div class="rank-intro">
      <h2>{c["rank_h2"]}</h2>
      <p>{c["rank_p"]}</p>
      <a class="btn btn-dark" href="{R}#methode">Voir la méthode de notation</a>
    </div>
    <div class="rank-list">{rank}
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="wrap">
    <div class="cta-card">
      <div><h2>{c["cta_h2"]}</h2><p>{c["cta_p"]}</p></div>
      <a class="btn btn-dark" href="{R}#outil">Comparer 2 contrats</a>
    </div>
  </div>
</section>

<section class="faq">
  <div class="wrap faq-head">
    <h2>{c["faq_h2"]}</h2>
    <div>{faq}
    </div>
  </div>
</section>

<section style="padding-bottom:20px"><div class="wrap">{DISCLOSURE}</div></section>

{newsletter(c["news_h2"])}

{footer(R)}

<script src="{R}assets/js/site.js?v=1"></script>
</body>
</html>
'''

if __name__ == "__main__":
    for c in CATS_DATA:
        os.makedirs(c["slug"], exist_ok=True)
        open(os.path.join(c["slug"], "index.html"), "w", encoding="utf-8").write(linkify(render(c), "../"))
        print("ok", c["slug"])
