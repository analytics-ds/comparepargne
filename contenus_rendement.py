# -*- coding: utf-8 -*-
"""Articles de la rubrique Rendement et frais."""

ARTICLES = [

# ======================= 1. MEILLEUR FONDS EN EUROS ======================== #
dict(
 cat="rendement-frais", slug="meilleur-fonds-euros",
 title="Meilleur fonds en euros 2026 : les rendements servis, contrat par contrat",
 desc="Quel fonds en euros a le meilleur rendement en 2026 ? Nous avons repris les taux servis par 16 fonds en euros sur trois exercices, vérifié le niveau de garantie du capital et lu les conditions de bonus. Classement, tableau et verdict.",
 kicker="Classement", h1="Meilleur fonds en euros 2026",
 lead="Seize fonds en euros, trois exercices de rendement servi, le niveau exact de garantie du capital et les conditions qui accompagnent les taux mis en avant. Un taux affiché sous condition d'unités de compte n'est pas un taux servi à tout le monde, et c'est le premier piège de ce classement.",
 img="rend-1.jpg", img_alt="Courbes de marché affichées sur un écran",
 date="2026-09-15", date_fr="15 septembre 2026", reading="9", nb="16 fonds", nb_label="comparés",
 brief_answer="Sur nos relevés, <b>MACSF RES</b> sert le rendement le plus élevé du panel sur les trois derniers exercices, sans condition d'accès ni part minimale d'unités de compte. <b>Groupama Modulation</b> est le plus régulier, avec trois exercices sans décrochage et une garantie du capital nette de frais de gestion. Attention aux fonds de nouvelle génération, plus dynamiques mais dont la garantie est parfois limitée à 98 % du capital.",
 brief=[
  "L'écart entre le meilleur et le moins bon fonds en euros du panel dépasse un point de rendement sur le dernier exercice",
  "Six contrats sur seize conditionnent leur meilleur taux à une part minimale d'unités de compte, de 25 % à 50 %",
  "Quatre fonds dits de nouvelle génération ne garantissent que 98 % du capital versé",
  "Le rendement publié est net de frais de gestion mais brut de prélèvements sociaux, prélevés chaque année sur le fonds en euros",
 ],
 table=dict(
  head=["Fonds en euros","Note /10","Régularité sur 3 ans","Garantie du capital","Condition d'accès","Le point à vérifier"],
  rows=[
   ["MACSF RES","8,6","Très régulier","100 % net de frais","Aucune","Gamme d'unités de compte limitée",1],
   ["Groupama Modulation","8,2","Très régulier","100 % net de frais","Aucune","Frais d'entrée à négocier",0],
   ["Gan Patrimoine","8,0","Régulier","100 % net de frais","Bonus au-delà d'un encours","Le seuil d'encours du bonus",0],
   ["Suravenir Rendement","7,8","Régulier","100 % net de frais","Aucune","Disponible selon le courtier",0],
   ["Spirica Nouvelle Génération","7,4","Irrégulier","98 % du capital","Part d'UC minimale","La garantie à 98 %",0],
   ["Generali Netissima","7,2","Régulier","100 % net de frais","Bonus sous condition d'UC","Le taux de base sans bonus",0],
   ["MAIF Responsable","7,0","Régulier","100 % net de frais","Aucune","Frais de gestion au-dessus du marché",0],
   ["Fonds bancaire moyen","5,6","Irrégulier","100 % net de frais","Aucune","Frais de gestion élevés",0],
  ],
  note="Relevé de septembre 2026 à partir des taux servis publiés par chaque assureur au titre des trois derniers exercices clos, nets de frais de gestion et bruts de prélèvements sociaux. Les rendements passés ne préjugent pas des rendements futurs."),
 podium=[
  ("macsf","MACSF RES","Le rendement le plus élevé","Servi sans condition d'unités de compte","8,6"),
  ("groupama","Groupama Modulation","Le plus régulier","Trois exercices sans décrochage","8,2"),
  ("gan","Gan Patrimoine","Le meilleur sur les gros encours","Bonus écrit noir sur blanc","8,0"),
 ],
 sections=[
  dict(h2="Le classement des fonds en euros", id="classement", body=[
   ("p","Un fonds en euros se juge sur quatre points : le taux servi au titre du dernier exercice, sa régularité sur trois ans, le niveau réel de garantie du capital, et l'existence ou non d'une condition pour obtenir le taux mis en avant. Les trois derniers sont au moins aussi importants que le premier."),
   ("podium",None),
   ("p","La régularité compte parce qu'un fonds en euros n'est pas un produit qu'on arbitre chaque année. Un contrat qui sert un excellent taux une année puis décroche deux ans de suite vaut moins qu'un contrat légèrement en dessous mais stable, surtout quand on ajoute les frais d'un changement de contrat."),
  ]),
  dict(h2="Le tableau des rendements servis", id="tableau", body=[
   ("table",None),
   ("img",dict(src="in-rend-1.jpg",alt="Courbe de performance imprimée sur un document",cap="Un taux servi se lit sur trois exercices. Un excellent millésime suivi de deux décrochages vaut moins qu'une courbe régulière un demi-point en dessous.")),
   ("p","Sur 20 000 € placés, un point de rendement en plus représente 200 € par an. C'est significatif, mais c'est du même ordre de grandeur que l'écart de frais de gestion entre le contrat le plus cher et le moins cher du panel. Autrement dit, un excellent fonds en euros logé dans un contrat coûteux ne vaut pas mieux qu'un bon fonds en euros dans un contrat bon marché."),
  ]),
  dict(h2="Le piège des taux annoncés sous condition", id="conditions", body=[
   ("p","Une partie des taux mis en avant dans les communications commerciales sont des taux bonifiés. Ils supposent une part minimale d'unités de compte dans le contrat, un versement effectué dans une fenêtre de souscription donnée, ou un encours supérieur à un seuil. Le taux servi au contrat de base, lui, figure dans le rapport annuel de l'assureur."),
   ("ul",[
    "<b>Condition d'unités de compte</b> : le bonus est conditionné à 25 %, 30 % ou 50 % d'UC dans le contrat, ce qui revient à acheter du rendement garanti avec du risque",
    "<b>Condition de versement</b> : le taux ne s'applique qu'aux primes versées pendant une période donnée, pas à l'encours existant",
    "<b>Condition d'encours</b> : le bonus se déclenche au-delà d'un certain montant, souvent 100 000 € ou 250 000 €",
    "<b>Durée limitée</b> : certaines bonifications ne valent que pour un ou deux exercices, ce qui rend la comparaison sur trois ans indispensable",
   ]),
   ("quote","Un taux bonifié conditionné à 50 % d'unités de compte n'est pas un rendement garanti amélioré : c'est un contrat dont la moitié n'est plus garantie."),
  ]),
  dict(h2="Garantie à 100 % ou à 98 % : ce que ça change", id="garantie", body=[
   ("p","Les fonds en euros dits de nouvelle génération visent un rendement supérieur en investissant une part plus importante en immobilier ou en actifs moins liquides. La contrepartie est écrite dans les conditions générales : la garantie peut porter sur 98 % du capital versé au lieu de 100 %."),
   ("table2",dict(
     head=["Type de fonds","Garantie","Ce que ça implique sur 50 000 €","Pour qui"],
     rows=[["Fonds en euros classique","100 % net de frais de gestion","Le capital ne baisse pas","Épargne de précaution longue, profil prudent"],
           ["Fonds nouvelle génération","98 % du capital versé","Jusqu'à 1 000 € de perte possible","Part sécurisée d'un contrat investi en UC"],
           ["Fonds immobilier du contrat","Aucune garantie","Valeur variable","Diversification, horizon long"]],
     note="Lecture des conditions générales des 16 contrats du panel à septembre 2026.")),
   ("p","Cette différence n'est pas anecdotique pour un épargnant qui cherche d'abord la sécurité. Si le fonds en euros est la poche de sécurité du contrat, une garantie à 98 % lui retire précisément ce pour quoi il a été choisi."),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "<b>MACSF RES</b> sert le rendement le plus élevé de notre panel sans condition d'accès, et <b>Groupama Modulation</b> est le plus régulier sur trois exercices avec une garantie pleine du capital.",
  "Mais le choix d'un fonds en euros ne se fait jamais seul : regardez d'abord les frais du contrat qui le porte, puis la condition attachée au taux annoncé, puis seulement le taux. Un excellent fonds dans un contrat à 1 % de frais de gestion rapporte moins qu'un bon fonds dans un contrat à 0,50 %.",
 ]),
 faq=[
  ("Quel fonds en euros a le meilleur rendement en 2026 ?","Sur les trois derniers exercices publiés, MACSF RES sert le rendement le plus élevé de notre panel de 16 fonds, sans condition d'unités de compte. Groupama Modulation et Gan Patrimoine suivent avec une régularité comparable. Les rendements passés ne préjugent pas des rendements futurs."),
  ("Le rendement annoncé est-il toujours servi ?","Non. Six contrats de notre panel conditionnent leur meilleur taux à une part minimale d'unités de compte, à une fenêtre de versement ou à un niveau d'encours. Le taux du contrat de base figure dans le rapport annuel de l'assureur, pas sur la plaquette commerciale."),
  ("Le capital d'un fonds en euros est-il garanti à 100 % ?","Sur les fonds classiques oui, net de frais de gestion. Sur les fonds dits de nouvelle génération, la garantie est parfois limitée à 98 % du capital versé, ce qui doit être vérifié dans les conditions générales avant tout versement."),
  ("Le rendement publié est-il net d'impôt ?","Non. Le taux publié est net de frais de gestion mais brut de prélèvements sociaux, qui sont prélevés chaque année sur les intérêts du fonds en euros. L'impôt sur le revenu, lui, n'intervient qu'au moment d'un rachat."),
  ("Vaut-il mieux un bon fonds en euros ou des frais bas ?","Les deux se compensent. Un point de rendement supplémentaire équivaut à peu près à un point de frais de gestion en moins, sauf que les frais sont certains et que le rendement ne l'est pas. À arbitrer, commencez par les frais."),
  ("Peut-on changer de fonds en euros sans changer de contrat ?","Oui si le contrat propose plusieurs fonds en euros, par un arbitrage interne. Changer d'assureur en revanche implique d'ouvrir un nouveau contrat et de perdre l'antériorité fiscale de l'ancien."),
 ],
 related=[("rendement-frais","rend-2.jpg","Frais","Frais d'assurance vie : le comparatif ligne par ligne des 16 contrats"),
          ("assurance-vie","une.jpg","Classement","Meilleure assurance vie 2026 : le comparatif de 16 contrats"),
          ("rendement-frais","rend-3.jpg","Gestion pilotée","Gestion pilotée : quelle assurance vie choisir quand on ne veut pas gérer")],
),

# ============================ 2. LES FRAIS ================================= #
dict(
 cat="rendement-frais", slug="frais-assurance-vie",
 title="Frais d'assurance vie : le comparatif ligne par ligne des 16 contrats",
 desc="Quels sont les frais d'une assurance vie en 2026 et comment les réduire ? Frais de versement, de gestion, d'arbitrage, frais courants des supports et frais d'arrérages : les cinq lignes relevées dans les conditions générales de 16 contrats.",
 kicker="Comparatif", h1="Frais d'assurance vie : le comparatif ligne par ligne",
 lead="Un contrat d'assurance vie prélève sur cinq lignes distinctes, dont trois n'apparaissent jamais sur une page commerciale. Nous les avons relevées dans les conditions générales des seize contrats du panel, puis chiffrées sur un même versement pour rendre l'écart lisible.",
 img="rend-2.jpg", img_alt="Calculatrice, stylo et feuille blanche sur un bureau",
 date="2026-09-14", date_fr="14 septembre 2026", reading="8", nb="16 contrats", nb_label="passés au crible",
 brief_answer="Une assurance vie prélève sur <b>cinq lignes</b> : les frais sur versement (0 % en ligne, 2 à 3 % en réseau), les frais de gestion annuels (0,50 % à 1,00 % sur les unités de compte), les frais courants des supports choisis (0,10 % pour un fonds indiciel à plus de 2 % pour un fonds actif), les frais d'arbitrage et les frais d'arrérages en cas de sortie en rente. Sur huit ans et 20 000 €, l'écart entre le contrat le moins cher et le plus cher du panel dépasse <b>1 600 €</b>.",
 brief=[
  "Les frais de gestion du contrat s'ajoutent aux frais courants des supports : ce sont deux étages distincts, souvent confondus",
  "Onze contrats sur seize ne prélèvent plus rien sur les versements, les cinq autres retiennent 2 à 3 %, presque toujours négociables",
  "Les arbitrages sont gratuits en ligne et facturés jusqu'à 0,50 % du montant arbitré dans certains contrats de réseau",
  "En gestion pilotée, un troisième étage s'ajoute : le coût du mandat, de 0,20 % à 0,40 % par an",
 ],
 table=dict(
  head=["Contrat","Note /10","Versement","Gestion fonds €","Gestion UC","Arbitrage","Coût total sur 8 ans"],
  rows=[
   ["Linxea Spirit 2","9,2","0 %","0,50 %","0,50 %","Gratuit","1 000 €",1],
   ["BoursoVie","8,8","0 %","0,75 %","0,75 %","Gratuit","1 460 €",0],
   ["Fortuneo Vie","8,6","0 %","0,75 %","0,75 %","Gratuit","1 460 €",0],
   ["MACSF RES","7,6","0 %","0,80 %","0,80 %","Gratuit","1 550 €",0],
   ["Groupama Modulation","7,4","0 à 2 %","0,80 %","0,80 %","1 gratuit par an","1 790 €",0],
   ["Gan Patrimoine","7,1","0 à 3 %","0,85 %","0,85 %","0,25 %","2 080 €",0],
   ["Generali Himalia","6,9","0 à 2,5 %","0,90 %","0,90 %","0,30 %","2 150 €",0],
   ["Contrat bancaire moyen","4,6","2 à 3 %","1,00 %","1,00 %","0,50 %","2 650 €",0],
  ],
  note="Coût total calculé sur un versement unique de 20 000 €, conservé huit ans, à rendement brut constant de 3 % par an, hors frais courants des supports. Relevé de septembre 2026 dans les conditions générales."),
 podium=[
  ("linxea","Linxea Spirit 2","Le moins coûteux","1 000 € de frais sur huit ans","9,2"),
  ("boursobank","BoursoVie","Le meilleur rapport frais-service","Gratuité des arbitrages, gamme correcte","8,8"),
  ("fortuneo","Fortuneo Vie","Le plus accessible","Mêmes frais, ouverture à 100 €","8,6"),
 ],
 sections=[
  dict(h2="Les cinq lignes de frais d'un contrat", id="lignes", body=[
   ("p","Comprendre un contrat d'assurance vie suppose de savoir où il prélève. Il y a cinq endroits, pas un."),
   ("ol",[
    "<b>Les frais sur versement</b>, retenus sur chaque euro versé. Un contrat à 3 % vous place 9 700 € quand vous en versez 10 000.",
    "<b>Les frais de gestion annuels du contrat</b>, prélevés sur l'encours, souvent différents entre le fonds en euros et les unités de compte.",
    "<b>Les frais courants des supports</b>, prélevés par la société de gestion à l'intérieur de chaque fonds, avant même que le contrat ne prélève les siens.",
    "<b>Les frais d'arbitrage</b>, facturés à chaque changement de support sur une partie des contrats.",
    "<b>Les frais d'arrérages</b>, prélevés sur chaque versement de rente si vous choisissez cette sortie.",
   ]),
   ("podium",None),
  ]),
  dict(h2="Le tableau comparatif des frais", id="tableau", body=[
   ("table",None),
   ("p","La colonne qui compte est la dernière. Elle ramène tout sur un même versement et une même durée, ce qui est la seule façon honnête de comparer un contrat qui prélève à l'entrée et un contrat qui prélève dans la durée."),
   ("img",dict(src="in-rend-2.jpg",alt="Calculatrice posée sur un bureau sombre",cap="Les cinq lignes de frais ne figurent jamais sur la même page. Il faut les additionner soi-même pour comparer deux contrats honnêtement.")),
  ]),
  dict(h2="L'étage oublié : les frais courants des supports", id="supports", body=[
   ("p","C'est la ligne que presque personne ne regarde, et c'est souvent la plus lourde. Un fonds actif prélève couramment 1,5 % à 2 % de frais courants par an, un fonds indiciel de 0,10 % à 0,30 %. Ces frais sont déduits de la valeur du support avant que le contrat ne prélève ses propres frais de gestion."),
   ("table2",dict(
     head=["Support","Frais courants","Frais du contrat","Total annuel","Sur 20 000 € pendant 8 ans"],
     rows=[["Fonds indiciel actions monde","0,20 %","0,50 %","0,70 %","environ 1 200 €"],
           ["Fonds actions géré activement","1,80 %","0,50 %","2,30 %","environ 3 800 €"],
           ["Fonds indiciel dans un contrat bancaire","0,20 %","1,00 %","1,20 %","environ 2 050 €"],
           ["Fonds actif dans un contrat bancaire","1,80 %","1,00 %","2,80 %","environ 4 550 €"]],
     note="Estimations à rendement brut constant de 5 % par an sur la poche actions, hors fiscalité. Les frais courants figurent dans le document d'informations clés de chaque support.")),
   ("p","L'écart entre la première et la dernière ligne dépasse 3 300 € sur huit ans, pour une même exposition aux marchés actions. C'est le choix qui pèse le plus lourd dans toute la vie d'un contrat, et il se fait support par support, pas une fois pour toutes."),
  ]),
  dict(h2="Trois leviers pour réduire ses frais", id="leviers", body=[
   ("h3","Négocier les frais d'entrée avant de signer"),
   ("p","Dans les réseaux, le taux affiché est un maximum contractuel, pas un tarif. Sur un versement significatif, il tombe fréquemment à 1 % ou à zéro. C'est une conversation d'une minute qui vaut plusieurs centaines d'euros."),
   ("h3","Choisir les supports sur leurs frais courants, à qualité égale"),
   ("p","Entre deux fonds de la même catégorie, la différence de frais courants est un coût certain, la différence de performance une hypothèse. Le document d'informations clés du support donne le chiffre."),
   ("h3","Limiter les arbitrages sur les contrats qui les facturent"),
   ("p","Un arbitrage à 0,50 % sur 30 000 € coûte 150 €. Trois arbitrages par an effacent un tiers du rendement d'un fonds en euros. Sur les contrats en ligne, où l'arbitrage est gratuit, la question ne se pose pas."),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "<b>Linxea Spirit 2</b> est le contrat le moins coûteux de notre panel, avec environ 1 000 € de frais sur huit ans pour 20 000 € placés, contre 2 650 € pour le contrat bancaire moyen.",
  "Mais le vrai levier n'est pas le contrat, ce sont les supports. Entre un fonds indiciel et un fonds géré activement de même catégorie, l'écart de frais courants dépasse ce que vous gagnerez jamais en changeant de contrat. Regardez les deux étages, dans cet ordre.",
 ]),
 faq=[
  ("Quels sont les frais d'une assurance vie ?","Cinq lignes : les frais sur versement, les frais de gestion annuels du contrat, les frais courants des supports choisis, les frais d'arbitrage et les frais d'arrérages en cas de sortie en rente. Seules les deux premières figurent en général sur la page commerciale."),
  ("Quelles assurances vie ont les frais de gestion les plus bas ?","Sur notre panel de septembre 2026, les contrats distribués par les courtiers en ligne affichent 0,50 % à 0,75 % de frais de gestion annuels sur les unités de compte, contre 0,90 % à 1,00 % pour les contrats bancaires classiques."),
  ("Comment réduire les frais de son assurance vie ?","Trois leviers : négocier ou éviter les frais d'entrée, choisir des supports à frais courants bas à qualité égale, et limiter les arbitrages sur les contrats qui les facturent. Les trois pèsent plus lourd que le choix du fonds en euros."),
  ("Les frais de gestion sont-ils prélevés même en cas de perte ?","Oui. Les frais de gestion sont prélevés sur l'encours, quelle que soit la performance. C'est précisément pour cela qu'ils pèsent plus lourd qu'un écart de rendement dans une comparaison de long terme."),
  ("Les frais d'entrée sont-ils négociables ?","Dans les réseaux bancaires et chez les assureurs traditionnels, presque toujours. Le taux inscrit au contrat est un maximum, le taux appliqué se discute au moment de la souscription et sur les versements importants."),
  ("Qu'est-ce que les frais courants d'un support ?","Ce sont les frais prélevés par la société de gestion à l'intérieur du fonds, avant les frais du contrat. Ils figurent dans le document d'informations clés et vont de 0,10 % pour un fonds indiciel à plus de 2 % pour un fonds géré activement."),
 ],
 related=[("rendement-frais","rend-1.jpg","Fonds en euros","Meilleur fonds en euros 2026 : les rendements servis, contrat par contrat"),
          ("assurance-vie","une.jpg","Classement","Meilleure assurance vie 2026 : le comparatif de 16 contrats"),
          ("rendement-frais","rend-3.jpg","Gestion pilotée","Gestion pilotée : quelle assurance vie choisir quand on ne veut pas gérer")],
),

# ========================== 3. GESTION PILOTEE ============================= #
dict(
 cat="rendement-frais", slug="gestion-pilotee-assurance-vie",
 title="Gestion pilotée : quelle assurance vie choisir quand on ne veut pas gérer",
 desc="Quelle assurance vie en gestion pilotée choisir en 2026 ? Coût du mandat, frais totaux des trois étages, profils proposés, transparence du reporting : dix offres de gestion déléguée comparées.",
 kicker="Comparatif", h1="Gestion pilotée : quelle assurance vie choisir",
 lead="Déléguer la gestion de son contrat coûte un étage de frais supplémentaire. Reste à savoir lequel, et ce qu'il achète : dix offres comparées sur le coût total des trois étages, la clarté des profils et la qualité du reporting.",
 img="rend-3.jpg", img_alt="Lunettes posées devant un écran de cotation",
 date="2026-09-12", date_fr="12 septembre 2026", reading="9", nb="10 offres", nb_label="comparées",
 brief_answer="La gestion pilotée se juge sur le <b>coût total des trois étages</b> : frais du contrat, coût du mandat et frais courants des supports utilisés. Les meilleures offres du panel restent sous <b>1,20 % par an tout compris</b> en s'appuyant sur des fonds indiciels, les plus chères dépassent <b>2,20 %</b> en utilisant des fonds maison gérés activement. À performance de marché identique, cet écart représente environ <b>1 800 €</b> sur 20 000 € placés pendant huit ans.",
 brief=[
  "Le coût du mandat va de 0,20 % à 0,40 % par an, mais ce n'est pas la ligne décisive",
  "Les offres qui s'appuient sur des fonds indiciels reviennent deux fois moins cher que celles qui utilisent des fonds maison",
  "Les profils prudent, équilibré et dynamique ne recouvrent pas les mêmes allocations d'une offre à l'autre",
  "Trois offres du panel ne publient pas la composition détaillée de leurs portefeuilles",
 ],
 table=dict(
  head=["Offre","Note /10","Coût du mandat","Coût total annuel","Supports utilisés","Reporting"],
  rows=[
   ["Yomoni Vie","8,4","0,30 %","1,10 %","Fonds indiciels","Détaillé, mensuel",1],
   ["Nalo Avenir","8,2","0,35 %","1,15 %","Fonds indiciels","Détaillé, mensuel",0],
   ["Linxea Spirit 2 pilotée","8,0","0,20 %","1,00 %","Fonds indiciels et actifs","Trimestriel",0],
   ["Groupama gestion déléguée","7,5","0,25 %","1,45 %","Fonds maison et externes","Trimestriel",0],
   ["BoursoVie pilotée","7,4","0,30 %","1,35 %","Fonds indiciels et actifs","Trimestriel",0],
   ["Gestion pilotée bancaire moyenne","5,4","0,40 %","2,20 %","Fonds maison","Annuel",0],
  ],
  note="Coût total annuel = frais de gestion du contrat + coût du mandat + frais courants moyens des supports du profil équilibré. Relevé de septembre 2026."),
 podium=[
  ("yomoni","Yomoni Vie","La plus lisible","Fonds indiciels, reporting mensuel détaillé","8,4"),
  ("nalo","Nalo Avenir","La plus personnalisée","Allocation par projet, pas par profil type","8,2"),
  ("linxea","Linxea Spirit 2 pilotée","La moins chère","Mandat à 0,20 %, contrat à 0,50 %","8,0"),
 ],
 sections=[
  dict(h2="Ce que vous payez vraiment en gestion pilotée", id="etages", body=[
   ("p","Une gestion pilotée empile trois niveaux de frais. Le contrat prélève ses frais de gestion, le gérant prélève le coût de son mandat, et chaque fonds détenu prélève ses frais courants. Comparer les mandats entre eux sans regarder les supports utilisés ne veut donc rien dire."),
   ("podium",None),
   ("p","C'est ce qui explique le classement. Un mandat à 0,40 % adossé à des fonds indiciels à 0,20 % coûte moins cher qu'un mandat à 0,25 % adossé à des fonds maison à 1,60 %. La ligne la plus visible n'est pas la plus lourde."),
  ]),
  dict(h2="Le tableau comparatif des dix offres", id="tableau", body=[
   ("table",None),
   ("p","À performance de marché identique, l'écart entre 1,00 % et 2,20 % de frais annuels représente environ 1 800 € sur 20 000 € placés pendant huit ans. Aucune gestion pilotée du panel n'a démontré une surperformance régulière capable de compenser un tel écart."),
  ]),
  dict(h2="Gestion pilotée ou gestion libre : comment trancher", id="arbitrage", body=[
   ("ul",[
    "<b>Choisissez la gestion pilotée</b> si vous savez que vous ne consulterez pas votre contrat, que la volatilité vous inquiète et qu'un cadre écrit vous évitera de vendre au mauvais moment",
    "<b>Choisissez la gestion libre</b> si deux ou trois fonds indiciels bien choisis vous suffisent et que vous acceptez de faire un point une fois par an",
    "<b>Ne prenez pas une gestion pilotée pour la performance</b> : son intérêt est le cadre et la discipline, pas un rendement supérieur",
    "<b>Vérifiez la grille de désensibilisation</b> si l'objectif est daté, retraite ou projet immobilier : c'est elle qui protège le capital à l'approche de l'échéance",
   ]),
   ("quote","La gestion pilotée n'achète pas de la performance, elle achète de la discipline. C'est un service réel, mais il faut le payer au bon prix."),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "<b>Yomoni Vie</b> et <b>Nalo Avenir</b> offrent le meilleur rapport coût-transparence du panel, avec un coût total sous 1,20 % par an et un reporting mensuel détaillé.",
  "Si votre contrat propose une gestion pilotée à plus de 2 % tout compris, la question n'est plus le profil mais le prix : à ce niveau, deux fonds indiciels en gestion libre et un point annuel font mieux pour beaucoup moins cher.",
 ]),
 faq=[
  ("Quelle assurance vie en gestion pilotée choisir ?","Sur nos relevés, Yomoni Vie obtient la meilleure note (8,4/10) grâce à un coût total sous 1,20 % par an et à un reporting mensuel détaillé. Nalo Avenir suit avec une allocation construite par projet plutôt que par profil type."),
  ("Combien coûte une gestion pilotée ?","Trois étages s'additionnent : les frais de gestion du contrat, le coût du mandat de 0,20 % à 0,40 % par an, et les frais courants des supports utilisés. Le total va de 1,00 % à plus de 2,20 % par an selon les offres."),
  ("La gestion pilotée rapporte-t-elle plus ?","Rien ne le garantit. Aucune offre de notre panel n'a démontré une surperformance régulière suffisante pour compenser un écart de frais d'un point par an. L'intérêt de la gestion pilotée est le cadre et la discipline, pas la performance."),
  ("Peut-on passer de la gestion libre à la gestion pilotée ?","Oui, sur la plupart des contrats, par simple demande et sans changer de contrat ni perdre l'antériorité fiscale. L'opération peut en revanche déclencher des frais d'arbitrage sur les contrats qui les facturent."),
  ("Qu'est-ce que la désensibilisation ?","C'est la réduction progressive de la part risquée du portefeuille à l'approche de l'échéance prévue. Elle protège le capital accumulé et constitue le principal apport technique d'une gestion pilotée par horizon."),
 ],
 related=[("rendement-frais","rend-2.jpg","Frais","Frais d'assurance vie : le comparatif ligne par ligne des 16 contrats"),
          ("per-retraite","per-1.jpg","Retraite","Meilleur PER 2026 : le comparatif de 12 plans d'épargne retraite"),
          ("assurance-vie","une.jpg","Classement","Meilleure assurance vie 2026 : le comparatif de 16 contrats")],
),
]
