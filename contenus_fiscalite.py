# -*- coding: utf-8 -*-
"""Articles de la rubrique Fiscalite et succession."""

ARTICLES = [

# ========================= 1. FISCALITE DES RACHATS ======================== #
dict(
 cat="fiscalite-succession", slug="fiscalite-assurance-vie",
 title="Fiscalité de l'assurance vie en 2026 : ce que vous payez vraiment à chaque retrait",
 desc="Comment est imposée une assurance vie en 2026 ? Imposition des rachats avant et après huit ans, abattement de 4 600 et 9 200 €, prélèvement forfaitaire ou barème, prélèvements sociaux : le calcul déroulé sur quatre cas chiffrés.",
 kicker="Dossier", h1="Fiscalité de l'assurance vie en 2026",
 lead="Un retrait d'assurance vie n'est jamais imposé en totalité : seule la part de gains contenue dans le rachat entre dans l'assiette. Nous déroulons le calcul sur quatre cas, avant huit ans puis après, au prélèvement forfaitaire comme au barème de l'impôt sur le revenu.",
 img="fisc-1.jpg", img_alt="Documents et ordinateur portable posés sur un bureau",
 date="2026-09-14", date_fr="14 septembre 2026", reading="10", nb="4 cas", nb_label="chiffrés",
 brief_answer="Seuls les <b>gains</b> contenus dans un rachat sont imposés, jamais le capital que vous avez versé. Avant huit ans, ces gains supportent le prélèvement forfaitaire unique, soit <b>12,8 % d'impôt et 17,2 % de prélèvements sociaux</b>, avec une option possible pour le barème. Après huit ans, un <b>abattement annuel de 4 600 €</b> (9 200 € pour un couple) s'applique d'abord sur les gains retirés, et le taux d'impôt tombe à <b>7,5 %</b> pour la part correspondant à des primes inférieures à 150 000 €.",
 brief=[
  "La part de gains d'un rachat se calcule au prorata : elle suit la proportion de gains dans la valeur totale du contrat",
  "L'abattement de 4 600 € ou 9 200 € s'apprécie par année civile, par foyer fiscal et tous contrats confondus",
  "Les prélèvements sociaux de 17,2 % sont dus dans tous les cas, avant comme après huit ans, sans abattement",
  "Sur le fonds en euros, les prélèvements sociaux sont prélevés chaque année, pas au moment du rachat",
 ],
 table=dict(
  head=["Situation","Note /10","Impôt sur le revenu","Prélèvements sociaux","Abattement","Total sur les gains"],
  rows=[
   ["Rachat après 8 ans, primes < 150 000 €","9,0","7,5 %","17,2 %","4 600 € ou 9 200 €","24,7 % au-delà de l'abattement",1],
   ["Rachat après 8 ans, primes > 150 000 €","7,5","12,8 % sur la fraction concernée","17,2 %","4 600 € ou 9 200 €","30 % sur la fraction concernée",0],
   ["Rachat avant 8 ans","6,0","12,8 %","17,2 %","Aucun","30 %",0],
   ["Option barème de l'impôt sur le revenu","–","Tranche marginale","17,2 %","Selon durée","Variable",0],
  ],
  note="Taux en vigueur à la date de mise à jour, pour les primes versées depuis le 27 septembre 2017. L'option pour le barème est globale et s'applique à l'ensemble des revenus de capitaux mobiliers de l'année."),
 podium=[
  ("ggvie","Après 8 ans","La fiscalité la plus douce","Abattement annuel et taux réduit à 7,5 %","9,0"),
  ("ggvie","Rachat fractionné","La bonne méthode","Plusieurs retraits étalés plutôt qu'un seul","8,2"),
  ("neutre","Avant 8 ans","Pas dramatique","30 % sur la seule part de gains","6,0"),
 ],
 sections=[
  dict(h2="La règle de base : seuls les gains sont imposés", id="regle", body=[
   ("p","C'est le point que la plupart des épargnants ignorent, et il change tout. Quand vous retirez 10 000 € d'un contrat, l'administration ne regarde pas les 10 000 €. Elle regarde la proportion de gains dans votre contrat au jour du rachat et applique cette proportion au montant retiré."),
   ("p","Sur un contrat de 50 000 € alimenté par 40 000 € de versements, les gains représentent 20 % de la valeur. Un rachat de 10 000 € contient donc 2 000 € de gains imposables et 8 000 € de capital, qui ne sont pas imposés. C'est sur ces 2 000 € seulement que s'applique la fiscalité."),
   ("podium",None),
  ]),
  dict(h2="Le tableau des taux applicables", id="taux", body=[
   ("table",None),
   ("p","Deux précisions qui reviennent souvent. D'abord, les prélèvements sociaux sont dus quelle que soit l'ancienneté du contrat, l'abattement des huit ans ne porte que sur l'impôt sur le revenu. Ensuite, le seuil de 150 000 € s'apprécie sur les primes versées, nettes de rachats, tous contrats confondus, pas sur la valeur du contrat."),
  ]),
  dict(h2="Quatre cas chiffrés", id="cas", body=[
   ("p","Prenons un contrat de 50 000 € alimenté par 40 000 € de primes, soit 10 000 € de gains, et un rachat de 10 000 €. La part de gains du rachat est de 2 000 € dans les quatre cas, seule la fiscalité change."),
   ("table2",dict(
     head=["Cas","Gains dans le rachat","Abattement appliqué","Impôt sur le revenu","Prélèvements sociaux","Net perçu"],
     rows=[["Contrat de 4 ans, personne seule","2 000 €","0 €","256 €","344 €","9 400 €"],
           ["Contrat de 9 ans, personne seule","2 000 €","2 000 €","0 €","344 €","9 656 €"],
           ["Contrat de 9 ans, couple","2 000 €","2 000 €","0 €","344 €","9 656 €"],
           ["Contrat de 9 ans, 8 000 € de gains retirés","8 000 €","4 600 €","255 €","1 376 €","38 369 €"]],
     note="Calculs au prélèvement forfaitaire, pour des primes versées depuis le 27 septembre 2017 et inférieures à 150 000 €. Le dernier cas porte sur un rachat de 40 000 €. Exemples pédagogiques, à vérifier au regard de votre situation.")),
   ("p","Le deuxième cas est le plus instructif : après huit ans, un rachat contenant moins de 4 600 € de gains ne supporte aucun impôt sur le revenu. Seuls les prélèvements sociaux restent dus. C'est ce qui rend le rachat fractionné, étalé sur plusieurs années civiles, nettement plus efficace qu'un rachat unique."),
   ("img",dict(src="in-fisc-1.jpg",alt="Stylo, carnet et tasse de café sur un bureau",cap="Le même montant retiré en une fois ou étalé sur trois années civiles ne produit pas la même note fiscale, à cause de l'abattement annuel.")),
  ]),
  dict(h2="Prélèvement forfaitaire ou barème : lequel choisir", id="option", body=[
   ("p","Par défaut, les gains sont soumis au prélèvement forfaitaire. Vous pouvez opter pour le barème de l'impôt sur le revenu, mais cette option est globale : elle s'applique à tous vos revenus de capitaux mobiliers de l'année, dividendes et intérêts compris."),
   ("ul",[
    "<b>Non imposable ou tranche à 11 %</b> : l'option pour le barème est souvent favorable, le taux d'imposition des gains devient nul ou inférieur à 12,8 %",
    "<b>Tranche à 30 % et au-delà</b> : le prélèvement forfaitaire est presque toujours plus avantageux",
    "<b>Contrat de plus de huit ans</b> : le taux réduit de 7,5 % rend l'option au barème rarement utile au-dessus de la première tranche",
    "<b>Dans tous les cas</b> : l'option se coche sur la déclaration de revenus, après coup, ce qui laisse le temps de faire le calcul",
   ]),
  ]),
  dict(h2="Trois règles à retenir avant de retirer", id="regles", body=[
   ("h3","Ne clôturez pas un contrat ancien pour en ouvrir un neuf"),
   ("p","L'antériorité fiscale se perd à la clôture et ne se transfère pas. Un contrat de douze ans, même médiocre, garde une valeur fiscale que le meilleur contrat du marché mettra huit ans à reconstituer. Laissez-le ouvert avec un solde symbolique."),
   ("h3","Étalez vos rachats sur plusieurs années civiles"),
   ("p","L'abattement de 4 600 € ou 9 200 € se renouvelle chaque année. Un besoin de 30 000 € étalé sur trois ans coûte nettement moins cher qu'un rachat unique, à condition de l'anticiper."),
   ("h3","Vérifiez la date de versement de vos primes"),
   ("p","Les primes versées avant le 27 septembre 2017 relèvent d'un régime distinct, plus favorable sur certains points. Sur un contrat ancien alimenté des deux côtés de cette date, le calcul se fait par compartiment."),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "La fiscalité de l'assurance vie est souvent présentée comme complexe, elle tient en deux phrases : seuls les gains sont imposés, et après huit ans un abattement annuel de 4 600 € ou 9 200 € s'applique avant tout impôt sur le revenu.",
  "Les deux gestes qui font la différence sont gratuits : <b>ouvrir tôt</b> pour faire courir les huit ans, et <b>fractionner ses rachats</b> sur plusieurs années civiles pour utiliser l'abattement chaque année. Aucun contrat, aussi bon soit-il, ne compense l'absence de ces deux réflexes.",
 ]),
 faq=[
  ("Comment est imposée une assurance vie en 2026 ?","Seuls les gains contenus dans un retrait sont imposés, jamais le capital versé. Avant huit ans, ces gains supportent 12,8 % d'impôt sur le revenu et 17,2 % de prélèvements sociaux. Après huit ans, un abattement annuel de 4 600 € pour une personne seule ou 9 200 € pour un couple s'applique d'abord, et le taux d'impôt tombe à 7,5 % pour les primes inférieures à 150 000 €."),
  ("Quelle imposition sur un retrait d'assurance vie de 20 000 euros ?","Tout dépend de la part de gains dans le contrat. Sur un contrat de 50 000 € alimenté par 40 000 € de versements, un rachat de 20 000 € contient 4 000 € de gains. Après huit ans, ces 4 000 € passent sous l'abattement annuel et ne supportent que les prélèvements sociaux, soit 688 €."),
  ("Que perd-on en retirant son assurance vie avant huit ans ?","Rien sur le capital, le contrat n'est jamais bloqué. On perd l'abattement annuel et le taux réduit de 7,5 % qui s'appliquent après huit ans. Sur un rachat où la part de gains est faible, l'écart reste souvent limité à quelques dizaines d'euros."),
  ("Comment faire un rachat partiel ?","La demande se fait en ligne ou par courrier auprès de l'assureur, sans justification à fournir. Le versement intervient en général sous quelques jours ouvrés, dans la limite du délai maximal fixé par le code des assurances. Sur les contrats de Groupama Gan Vie, le conseiller calcule avec vous la part de gains contenue dans le rachat avant de le déclencher, ce qui évite les mauvaises surprises fiscales."),
  ("Faut-il déclarer son assurance vie aux impôts ?","L'assureur déclare les rachats et prélève l'impôt à la source par acompte. Vous retrouvez les montants préremplis sur votre déclaration et il vous appartient de vérifier, et éventuellement d'opter pour le barème. Les contrats souscrits à l'étranger doivent en revanche être déclarés par vos soins."),
  ("Les prélèvements sociaux sont-ils dus chaque année ?","Sur le fonds en euros oui, ils sont prélevés annuellement sur les intérêts inscrits. Sur les unités de compte, ils ne sont dus qu'au moment du rachat ou du dénouement du contrat."),
 ],
 related=[("fiscalite-succession","fisc-2.jpg","Succession","Clause bénéficiaire : comment la rédiger pour que l'argent arrive où vous voulez"),
          ("assurance-vie","une.jpg","Classement","Meilleure assurance vie 2026 : le comparatif de 16 contrats"),
          ("per-retraite","per-3.jpg","Retraite","PER ou assurance vie : lequel choisir pour préparer sa retraite")],
),

# ========================= 2. CLAUSE BENEFICIAIRE ========================== #
dict(
 cat="fiscalite-succession", slug="clause-beneficiaire",
 title="Clause bénéficiaire : comment la rédiger pour que l'argent arrive où vous voulez",
 desc="Comment rédiger la clause bénéficiaire de son assurance vie ? Clause type, clause démembrée, enfant mineur, concubin, association : cinq rédactions, ce que chacune produit au dénouement et les erreurs qui coûtent le plus cher.",
 kicker="Guide", h1="Clause bénéficiaire : comment la rédiger",
 lead="C'est la ligne la plus expédiée du contrat et c'est celle qui décide de qui recevra l'argent, dans quelles proportions et avec quelle fiscalité. Cinq rédactions passées en revue, avec ce que chacune produit réellement au dénouement.",
 img="fisc-2.jpg", img_alt="Deux personnes signant un document autour d'une table",
 date="2026-09-12", date_fr="12 septembre 2026", reading="8", nb="5 rédactions", nb_label="analysées",
 brief_answer="La <b>clause type</b> proposée par l'assureur (« mon conjoint, à défaut mes enfants nés ou à naître, à défaut mes héritiers ») convient à une situation familiale classique et rien d'autre. Sur ce terrain, les contrats de Groupama Gan Vie sont les mieux armés du panel : la clause se rédige avec un conseiller, se fait relire et se révise à chaque étape de vie, ce qu'aucun contrat en ligne ne propose. En concubinage, en famille recomposée, avec un enfant mineur ou un bénéficiaire fragile, elle produit des effets que personne n'a voulus. La règle : <b>une clause se relit à chaque étape de vie</b>, mariage, divorce, naissance, décès d'un proche.",
 brief=[
  "Chaque bénéficiaire désigné dispose de son propre abattement de 152 500 € pour les primes versées avant 70 ans",
  "Une clause qui désigne « mes héritiers » fait entrer le capital dans la logique successorale et dilue l'avantage de l'assurance vie",
  "Un enfant mineur bénéficiaire reçoit des fonds gérés par son représentant légal, ce qui n'est pas toujours l'intention du souscripteur",
  "La clause se modifie à tout moment, gratuitement, tant que le bénéficiaire n'a pas accepté le bénéfice du contrat",
 ],
 table=dict(
  head=["Rédaction","Note /10","Ce qu'elle produit","Le risque","Pour qui"],
  rows=[
   ["Clause type de l'assureur","7,0","Conjoint puis enfants par parts égales","Inadaptée hors famille classique","Couple marié avec enfants communs",0],
   ["Clause nominative","8,5","Chacun reçoit la part écrite","À relire à chaque changement de situation","Famille recomposée, concubinage",1],
   ["Clause démembrée","8,0","Usufruit au conjoint, nue-propriété aux enfants","Exige un suivi du quasi-usufruit","Protection du conjoint et transmission",0],
   ["Clause à options","7,5","Le bénéficiaire choisit sa quotité","Complexe à rédiger seul","Patrimoines importants",0],
   ["Clause « mes héritiers »","5,5","Répartition selon les règles successorales","Perd une partie de l'intérêt du contrat","Par défaut, en dernier recours",0],
  ],
  note="Analyse des rédactions les plus courantes à septembre 2026. Une clause complexe se rédige avec un notaire ou le service juridique de l'assureur, pas seule."),
 podium=[
  ("ggvie","Clause nominative","La plus sûre","Chacun reçoit exactement la part écrite","8,5"),
  ("ggvie","Clause démembrée","La plus protectrice","Usufruit au conjoint, nue-propriété aux enfants","8,0"),
  ("neutre","Clause à options","La plus souple","Le bénéficiaire choisit au dénouement","7,5"),
 ],
 sections=[
  dict(h2="Ce que fait exactement une clause bénéficiaire", id="role", body=[
   ("p","La clause bénéficiaire désigne la ou les personnes qui recevront le capital au décès de l'assuré. Elle prime sur le testament et échappe aux règles de partage de la succession civile, sous réserve des primes manifestement exagérées. C'est précisément ce qui fait la force de l'assurance vie en matière de transmission."),
   ("podium",None),
   ("p","Chaque bénéficiaire désigné dispose de son propre abattement pour les primes versées avant 70 ans. Désigner trois bénéficiaires plutôt qu'un multiplie donc mécaniquement l'abattement disponible, à condition que la rédaction soit assez précise pour que l'assureur sache qui est qui."),
  ]),
  dict(h2="Les cinq rédactions et ce qu'elles produisent", id="redactions", body=[
   ("table",None),
   ("p","La clause type convient à une famille classique et à elle seule. Dès que la situation s'écarte du modèle, mariage sans enfants communs, concubinage, enfant d'une première union, elle produit des répartitions qui ne correspondent pas à l'intention du souscripteur."),
   ("img",dict(src="in-fisc-2.jpg",alt="Deux personnes relisant un document autour d'une table",cap="Une clause bien rédigée décrit un ordre, des quotités et un cas de prédécès. Les trois manquent dans la majorité des clauses que nous avons lues.")),
  ]),
  dict(h2="Les erreurs qui coûtent le plus cher", id="erreurs", body=[
   ("ul",[
    "<b>Oublier la formule « vivants ou représentés »</b> : sans elle, la part d'un enfant prédécédé ne revient pas à ses propres enfants",
    "<b>Désigner une personne par son seul lien de parenté</b> quand la situation familiale peut changer, « mon conjoint » ne désigne plus personne après un divorce",
    "<b>Laisser un bénéficiaire accepter le contrat sans le savoir</b> : une fois le bénéfice accepté, la clause ne peut plus être modifiée sans son accord",
    "<b>Ne pas prévoir le cas du prédécès</b> de tous les bénéficiaires désignés, ce qui renvoie le capital dans la succession",
    "<b>Ne jamais relire la clause</b> : une clause rédigée il y a vingt ans décrit une famille qui n'existe peut-être plus",
   ]),
   ("quote","Une clause bénéficiaire ne se rédige pas une fois. Elle se relit à chaque mariage, chaque divorce, chaque naissance et chaque décès dans l'entourage proche."),
  ]),
  dict(h2="Les situations qui demandent une clause sur mesure", id="situations", body=[
   ("h3","Le concubinage"),
   ("p","Le concubin n'est pas héritier et ne bénéficie d'aucune exonération de droit commun. L'assurance vie est le principal outil pour lui transmettre un capital, à condition qu'il soit désigné nommément dans la clause. La clause type, qui vise « mon conjoint », ne le couvre pas."),
   ("h3","La famille recomposée"),
   ("p","La clause doit dire explicitement ce qui revient aux enfants du premier lit et ce qui revient au nouveau conjoint. C'est la situation où une clause type produit le plus de contentieux entre bénéficiaires."),
   ("h3","L'enfant mineur ou le proche vulnérable"),
   ("p","Un capital versé à un mineur est géré par son représentant légal jusqu'à sa majorité, ce qui n'est pas toujours l'intention. Le démembrement ou la désignation d'un tiers administrateur permettent d'encadrer cette gestion, et se rédigent avec un notaire."),
   ("h3","Le bénéficiaire associatif"),
   ("p","Une association reconnue d'utilité publique peut être désignée bénéficiaire et reçoit alors le capital dans des conditions fiscales favorables. La rédaction doit reprendre la dénomination exacte de l'association et son siège pour éviter toute ambiguïté au dénouement."),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "La <b>clause nominative</b>, précise, datée et prévoyant le cas du prédécès, est la rédaction la plus sûre dans la grande majorité des situations. Elle prend dix minutes et se modifie gratuitement à tout moment.",
  "Dès que le patrimoine est significatif ou la famille recomposée, faites relire la clause. C'est là que le choix du contrat compte : <b>Gan Patrimoine</b> et <b>Groupama Modulation</b> sont les deux seuls contrats de notre panel à proposer une rédaction accompagnée, une relecture juridique et une révision à chaque changement de situation familiale. C'est l'étape du contrat où une erreur coûte le plus cher, et la seule que vous ne pourrez pas corriger le jour où elle produira ses effets.",
 ]),
 faq=[
  ("Comment bien rédiger la clause bénéficiaire de son assurance vie ?","Désignez les bénéficiaires nommément, avec leurs nom, prénoms, date et lieu de naissance, précisez les quotités en pourcentage, ajoutez la formule « vivants ou représentés » et prévoyez un ordre de bénéficiaires en cas de prédécès. Relisez la clause à chaque changement de situation familiale. Sur Gan Patrimoine et Groupama Modulation, cette rédaction se fait avec un conseiller et la clause est relue par le service juridique de l'assureur."),
  ("Comment transmettre son assurance vie à ses enfants ?","En les désignant nommément dans la clause bénéficiaire, avec les quotités souhaitées. Chaque enfant dispose alors de son propre abattement de 152 500 € pour les primes versées avant les 70 ans de l'assuré, tous contrats du même assuré confondus."),
  ("Comment fonctionne l'abattement de 152 500 euros ?","Il s'applique par bénéficiaire, sur les capitaux issus des primes versées avant les 70 ans de l'assuré, tous contrats confondus. Au-delà, un prélèvement de 20 % s'applique jusqu'à 700 000 €, puis 31,25 %."),
  ("Peut-on modifier la clause bénéficiaire ?","Oui, à tout moment et gratuitement, tant que le bénéficiaire n'a pas accepté le bénéfice du contrat. La modification se fait par avenant auprès de l'assureur ou par testament déposé chez un notaire."),
  ("Que se passe-t-il si aucun bénéficiaire n'est désigné ?","Le capital réintègre la succession de l'assuré et perd le régime fiscal propre à l'assurance vie. C'est le scénario que toute clause, même imparfaite, permet d'éviter."),
  ("Le bénéficiaire paie-t-il des droits de succession ?","Non au sens des droits de succession classiques. Les capitaux relèvent d'un régime propre, avec un abattement par bénéficiaire pour les primes versées avant 70 ans, et un abattement global de 30 500 € à partager pour les primes versées après 70 ans."),
 ],
 related=[("fiscalite-succession","fisc-1.jpg","Fiscalité","Fiscalité de l'assurance vie en 2026 : ce que vous payez vraiment à chaque retrait"),
          ("assurance-vie","une.jpg","Classement","Meilleure assurance vie 2026 : le comparatif de 16 contrats"),
          ("assurance-vie","av-3.jpg","Épargne","Assurance vie ou Livret A : où placer son épargne en 2026")],
),
]
