# -*- coding: utf-8 -*-
"""Articles de la rubrique PER et retraite."""

ARTICLES = [

# ============================= 1. MEILLEUR PER ============================= #
dict(
 cat="per-retraite", slug="meilleur-per",
 title="Meilleur PER 2026 : le comparatif de 12 plans d'épargne retraite",
 desc="Quel est le meilleur PER individuel en 2026 ? Frais de versement, frais de gestion, coût du mandat en gestion pilotée par horizon, gamme de supports et conditions de sortie : 12 plans d'épargne retraite comparés.",
 kicker="Classement", h1="Meilleur PER 2026",
 lead="Douze plans d'épargne retraite individuels comparés sur ce qui décide réellement du capital à l'arrivée : les frais empilés sur toute la durée, la qualité de la grille de désensibilisation et la souplesse à la sortie. L'écart de frais entre un PER bancaire et un PER en ligne dépasse souvent l'avantage fiscal d'une année de versements.",
 img="per-1.svg", img_alt="Trajectoire d'épargne retraite par horizon",
 date="2026-09-12", date_fr="12 septembre 2026", reading="11", nb="12 PER", nb_label="comparés",
 brief_answer="Sur nos relevés, <b>Linxea PER</b> obtient la meilleure note du panel (<b>8,5/10</b>) : aucun frais sur versement, des frais de gestion à 0,60 % et un mandat parmi les moins chers. <b>Groupama PER</b> arrive en tête des PER accompagnés (<b>8,0/10</b>) avec une grille de désensibilisation lisible et un point annuel avec un conseiller. Les PER bancaires restent les plus coûteux du panel, avec des frais de versement encore pratiqués.",
 brief=[
  "L'écart de frais annuels entre le PER le moins cher et le plus cher du panel atteint 1,3 point",
  "Sept PER sur douze ne prélèvent plus rien sur les versements, cinq retiennent encore jusqu'à 3 %",
  "L'avantage fiscal ne dépend pas du PER choisi mais de votre tranche marginale d'imposition",
  "Les profils prudent et équilibré ne recouvrent pas les mêmes allocations d'un PER à l'autre",
 ],
 table=dict(
  head=["PER","Note /10","Frais versement","Gestion annuelle","Mandat piloté","Supports","Sortie fractionnée"],
  rows=[
   ["Linxea PER","8,5","0 %","0,60 %","0,20 %","Plus de 700","Oui",1],
   ["Groupama PER","8,0","0 à 2 %","0,80 %","0,25 %","Environ 200","Oui",0],
   ["Yomoni Retraite","7,9","0 %","0,60 %","0,30 %","Gestion pilotée","Oui",0],
   ["MACSF PER","7,7","0 %","0,80 %","0,25 %","Environ 60","Oui",0],
   ["Fortuneo PER","7,6","0 %","0,75 %","0,30 %","Environ 300","Oui",0],
   ["MAIF PER Responsable","7,4","0 %","0,90 %","0,30 %","Environ 50","Oui",0],
   ["Generali PER","7,0","0 à 2,5 %","0,90 %","0,35 %","Environ 500","Oui",0],
   ["PER bancaire moyen","5,8","2 à 3 %","1,00 %","0,40 %","Environ 40","Selon contrat",0],
  ],
  note="Relevé de septembre 2026 dans les conditions générales des 12 PER individuels du panel. Le coût du mandat s'ajoute aux frais de gestion et aux frais courants des supports."),
 podium=[
  ("linxea","Linxea PER","Le moins coûteux","Zéro frais d'entrée, mandat à 0,20 %","8,5"),
  ("groupama","Groupama PER","Le mieux accompagné","Désensibilisation lisible, point annuel","8,0"),
  ("yomoni","Yomoni Retraite","La meilleure gestion pilotée","Allocation par horizon claire, reporting détaillé","7,9"),
 ],
 sections=[
  dict(h2="Le classement des PER individuels", id="classement", body=[
   ("p","Un PER se choisit sur trois critères : le coût total sur la durée, la qualité de la gestion pilotée par horizon puisque c'est l'option par défaut, et la souplesse à la sortie. Le quatrième critère, l'avantage fiscal, ne dépend pas du plan choisi mais de votre tranche marginale d'imposition."),
   ("podium",None),
   ("p","La durée explique le poids des frais. Un PER ouvert à 40 ans et liquidé à 64 ans travaille pendant vingt-quatre ans. Sur cette durée, un point de frais annuels supplémentaires ampute le capital final de près d'un quart. Aucune allocation, aussi bien pilotée soit-elle, ne rattrape cet écart."),
  ]),
  dict(h2="Le tableau comparatif des 12 PER", id="tableau", body=[
   ("table",None),
   ("img",dict(src="in-per-1.svg",alt="Effet des frais sur un capital retraite à long terme",cap="Sur vingt ans de versements, l'écart de frais entre le PER le moins cher et le PER bancaire moyen représente plusieurs dizaines de milliers d'euros de capital final.")),
   ("p","Les frais de versement méritent une attention particulière sur un PER, parce qu'ils s'appliquent à chaque versement pendant toute la phase d'épargne, et non une seule fois comme sur un versement unique d'assurance vie. Trois pour cent prélevés sur 300 € par mois pendant vingt ans représentent 2 160 € qui ne travailleront jamais."),
  ]),
  dict(h2="Ce que le PER vous fait vraiment gagner", id="fiscal", body=[
   ("p","Les versements volontaires se déduisent du revenu imposable, dans la limite de votre plafond d'épargne retraite. L'économie d'impôt égale le versement multiplié par votre tranche marginale. C'est un gain immédiat, mais c'est aussi un différé : la part déduite sera imposée à la sortie."),
   ("table2",dict(
     head=["Tranche marginale","Versement de 5 000 €","Économie d'impôt","Effort réel","Intérêt du PER"],
     rows=[["0 %","5 000 €","0 €","5 000 €","Nul, préférez l'assurance vie"],
           ["11 %","5 000 €","550 €","4 450 €","Faible"],
           ["30 %","5 000 €","1 500 €","3 500 €","Réel"],
           ["41 %","5 000 €","2 050 €","2 950 €","Fort"]],
     note="Calcul sur un versement volontaire déductible, dans la limite du plafond d'épargne retraite disponible. L'économie réelle dépend de la tranche applicable à la fraction du revenu concernée.")),
   ("p","La règle de décision tient en une phrase : le PER a un intérêt quand votre tranche d'imposition à la retraite sera plus basse qu'aujourd'hui. En dessous de la tranche à 30 %, l'avantage est rarement suffisant pour justifier le blocage des fonds jusqu'à la retraite."),
   ("quote","Un PER n'efface pas l'impôt, il le décale. Le gain réel, c'est l'écart entre votre tranche d'aujourd'hui et votre tranche de retraité."),
  ]),
  dict(h2="Sortie en capital ou en rente", id="sortie", body=[
   ("p","À la liquidation, les versements volontaires déduits à l'entrée peuvent sortir en capital, en une fois ou de façon fractionnée, ou en rente viagère. La part déduite est alors imposée au barème de l'impôt sur le revenu, les gains au prélèvement forfaitaire."),
   ("ul",[
    "<b>Capital en une fois</b> : simple, mais la totalité de la part déductible s'ajoute au revenu de l'année, ce qui peut faire bondir la tranche",
    "<b>Capital fractionné</b> : la meilleure option dans la plupart des cas, elle étale l'imposition sur plusieurs années",
    "<b>Rente viagère</b> : sécurise un revenu à vie mais aliène le capital, et supporte des frais d'arrérages à chaque versement",
    "<b>Sortie mixte</b> : une partie en capital pour un projet, le reste en rente, possible sur la majorité des PER du panel",
   ]),
   ("p","Le fractionnement est l'option que nous retenons le plus souvent. Sortir 120 000 € en une fois peut faire passer une partie du capital dans la tranche à 41 %, alors que le même montant étalé sur six ans reste dans les tranches basses."),
  ]),
  dict(h2="Les six cas de déblocage anticipé", id="deblocage", body=[
   ("p","L'argent d'un PER est bloqué jusqu'à la retraite, avec six exceptions prévues par la loi. Elles couvrent les accidents de la vie et l'achat de la résidence principale."),
   ("ol",[
    "L'acquisition de la résidence principale, sur la part issue des versements volontaires",
    "L'invalidité du titulaire, de son conjoint ou de ses enfants",
    "Le décès du conjoint ou du partenaire de PACS",
    "L'expiration des droits à l'assurance chômage",
    "La situation de surendettement, à la demande de la commission",
    "La cessation d'activité non salariée à la suite d'une liquidation judiciaire",
   ]),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "<b>Linxea PER</b> est le meilleur plan de notre panel avec 8,5/10 : rien à l'entrée, 0,60 % de frais de gestion et un mandat à 0,20 %. Sur vingt ans de versements, c'est l'écart le plus déterminant du comparatif.",
  "Si vous voulez un accompagnement, <b>Groupama PER</b> tient la comparaison à 8,0/10 avec une grille de désensibilisation lisible, à condition de faire tomber les frais d'entrée à la signature. Et avant de choisir un plan, vérifiez votre tranche : en dessous de 30 %, l'assurance vie reste souvent le meilleur véhicule de préparation à la retraite.",
 ]),
 faq=[
  ("Quel est le meilleur PER en 2026 ?","Sur nos relevés de septembre 2026, Linxea PER obtient la meilleure note globale (8,5/10) grâce à l'absence de frais sur versement et à un mandat de gestion à 0,20 %. Groupama PER arrive en tête des PER accompagnés (8,0/10), Yomoni Retraite offre la gestion pilotée la plus lisible."),
  ("Où ouvrir un PER en 2026 et chez quel assureur ?","Chez un courtier en ligne pour les frais les plus bas, chez un assureur traditionnel si vous voulez un suivi annuel avec un conseiller. Le circuit bancaire reste le plus coûteux du panel, avec des frais de versement encore pratiqués sur la moitié des offres."),
  ("Quel avantage fiscal donne un PER selon sa tranche d'imposition ?","L'économie d'impôt égale le versement multiplié par votre tranche marginale : 550 € pour 5 000 € versés à 11 %, 1 500 € à 30 % et 2 050 € à 41 %. En dessous de la tranche à 30 %, l'avantage justifie rarement le blocage des fonds."),
  ("L'argent d'un PER est-il bloqué jusqu'à la retraite ?","Oui, avec six cas de déblocage anticipé prévus par la loi, dont l'achat de la résidence principale, l'invalidité, le décès du conjoint, la fin de droits au chômage, le surendettement et la liquidation judiciaire d'une activité non salariée."),
  ("Peut-on sortir d'un PER en capital ?","Oui, en une fois ou de façon fractionnée pour la part issue des versements volontaires. Le fractionnement est presque toujours préférable, parce qu'il évite de faire basculer une année de revenus dans une tranche supérieure."),
  ("Peut-on avoir plusieurs PER ?","Oui, sans limite. Le plafond de déduction, lui, est commun à tous vos versements de l'année, tous plans confondus, et s'apprécie au niveau du foyer fiscal."),
 ],
 related=[("per-retraite","per-3.svg","Arbitrage","PER ou assurance vie : lequel choisir pour préparer sa retraite"),
          ("rendement-frais","rend-3.svg","Gestion pilotée","Gestion pilotée : quelle assurance vie choisir quand on ne veut pas gérer"),
          ("assurance-vie","une.svg","Classement","Meilleure assurance vie 2026 : le comparatif de 16 contrats")],
),

# ======================= 2. PER OU ASSURANCE VIE =========================== #
dict(
 cat="per-retraite", slug="per-ou-assurance-vie",
 title="PER ou assurance vie : lequel choisir pour préparer sa retraite",
 desc="PER ou assurance vie pour préparer sa retraite en 2026 ? Déduction à l'entrée, imposition à la sortie, disponibilité des fonds, transmission : les deux enveloppes comparées et la règle de décision selon votre tranche d'imposition.",
 kicker="Comparatif", h1="PER ou assurance vie pour préparer sa retraite",
 lead="Le PER déduit à l'entrée et impose à la sortie, l'assurance vie fait exactement l'inverse. Tout le reste découle de là : la disponibilité des fonds, le traitement au décès et la règle de décision, qui tient à l'écart entre votre tranche d'aujourd'hui et celle de votre retraite.",
 img="per-3.svg", img_alt="Deux trajectoires de préparation à la retraite",
 date="2026-09-11", date_fr="11 septembre 2026", reading="9", nb="2 enveloppes", nb_label="comparées",
 brief_answer="Le <b>PER</b> a un intérêt à partir de la tranche marginale à <b>30 %</b>, et d'autant plus que votre tranche baissera à la retraite : la déduction immédiate compense le blocage des fonds. En dessous, l'<b>assurance vie</b> reste préférable parce qu'elle laisse le capital disponible à tout moment et qu'elle offre un régime de transmission que le PER n'égale pas. Les deux se cumulent très bien : PER pour la part que vous ne toucherez pas, assurance vie pour le reste.",
 brief=[
  "Le PER bloque les fonds jusqu'à la retraite, sauf six cas de déblocage anticipé prévus par la loi",
  "L'assurance vie reste disponible à tout moment, avec une fiscalité qui s'allège après huit ans",
  "Au décès avant 70 ans, l'assurance vie offre un abattement de 152 500 € par bénéficiaire, le PER assurantiel suit une logique proche mais avec des règles distinctes",
  "L'avantage fiscal du PER se mesure à l'écart entre la tranche d'aujourd'hui et celle de la retraite, pas au montant déduit",
 ],
 table=dict(
  head=["Critère","Note /10","PER","Assurance vie","Ce qui l'emporte"],
  rows=[
   ["Avantage à l'entrée","9,0","Versements déductibles","Aucun","Le PER, nettement",1],
   ["Fiscalité à la sortie","7,0","Capital déduit imposé au barème","Gains imposés, abattement après 8 ans","L'assurance vie",0],
   ["Disponibilité","9,5","Bloqué, 6 cas de déblocage","Disponible à tout moment","L'assurance vie, sans discussion",0],
   ["Transmission","9,0","Régime spécifique selon l'âge","Abattement de 152 500 € par bénéficiaire","L'assurance vie",0],
   ["Frais","7,5","0 à 3 % à l'entrée selon l'offre","0 à 3 % selon l'offre","Égalité, tout dépend du contrat",0],
   ["Souplesse des versements","8,5","Libres","Libres","Égalité",0],
  ],
  note="Comparaison à septembre 2026 pour un PER individuel assurantiel et un contrat d'assurance vie multisupport. Les règles fiscales citées sont celles en vigueur à cette date."),
 podium=[
  ("groupama","Assurance vie","Le plus polyvalent","Disponible, transmissible, fiscalité douce après 8 ans","8,6"),
  ("linxea","PER","Le plus efficace fiscalement","Déduction immédiate à partir de la tranche à 30 %","8,2"),
  ("yomoni","Les deux","La combinaison","PER pour l'intouchable, assurance vie pour le reste","9,0"),
 ],
 sections=[
  dict(h2="La seule différence qui compte", id="difference", body=[
   ("p","Tout se résume au moment où l'impôt intervient. Le PER vous rend de l'impôt aujourd'hui et vous le reprend à la sortie. L'assurance vie ne vous rend rien aujourd'hui mais vous impose peu à la sortie, et seulement sur les gains."),
   ("podium",None),
   ("p","Le PER est donc gagnant si votre tranche à la retraite est inférieure à celle d'aujourd'hui : vous déduisez à 41 % et vous reprenez à 30 %, l'écart est votre gain. Il devient neutre, voire défavorable, si votre tranche reste identique ou augmente."),
  ]),
  dict(h2="Le tableau comparatif poste par poste", id="tableau", body=[
   ("table",None),
   ("img",dict(src="in-per-2.svg",alt="Comparaison de deux stratégies de préparation à la retraite",cap="Deux stratégies, un même effort d'épargne. L'écart final se joue moins sur le rendement que sur l'écart de tranche entre la période d'activité et la retraite.")),
  ]),
  dict(h2="La règle de décision, tranche par tranche", id="regle", body=[
   ("h3","Tranche à 0 % ou 11 %"),
   ("p","L'assurance vie, sans hésitation. La déduction ne vous rapporte presque rien alors que le blocage des fonds vous coûte une liberté réelle. Un PER dans cette situation revient à bloquer son épargne pour un avantage marginal."),
   ("h3","Tranche à 30 %"),
   ("p","Les deux, en répartissant. Le PER pour la part d'épargne que vous savez ne pas devoir toucher avant la retraite, l'assurance vie pour la part qui doit rester disponible. C'est la configuration où la combinaison a le plus de sens."),
   ("h3","Tranche à 41 % ou 45 %"),
   ("p","Le PER en priorité, jusqu'à saturation du plafond de déduction disponible, puis l'assurance vie pour le surplus. À ce niveau, la déduction immédiate représente un gain important et la baisse de tranche à la retraite est probable."),
   ("h3","Dans tous les cas"),
   ("p","Ouvrez l'assurance vie en premier, même symboliquement, pour faire courir les huit ans. C'est gratuit, ça ne bloque rien et cela conserve toutes les options ouvertes."),
  ]),
  dict(h2="Combien épargner chaque mois", id="effort", body=[
   ("p","La question posée à l'envers est plus utile : pour un même complément de revenu visé à la retraite, quel effort mensuel selon l'âge de départ."),
   ("table2",dict(
     head=["Âge de départ","Durée d'épargne","Effort mensuel","Capital constitué","Complément mensuel estimé"],
     rows=[["35 ans","30 ans","200 €","environ 116 000 €","environ 390 €"],
           ["45 ans","20 ans","350 €","environ 114 000 €","environ 380 €"],
           ["55 ans","10 ans","800 €","environ 111 000 €","environ 370 €"]],
     note="Hypothèse de rendement net constant de 3 % par an, hors fiscalité, complément estimé sur une durée de restitution de 25 ans. Simulation pédagogique, à ajuster à votre situation.")),
   ("p","L'effort mensuel quadruple entre un départ à 35 ans et un départ à 55 ans, pour un résultat équivalent. C'est l'argument le plus solide en faveur d'une ouverture précoce, bien avant le choix de l'enveloppe."),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "En dessous de la tranche à 30 %, prenez l'<b>assurance vie</b> : la déduction du PER ne compense pas le blocage des fonds, et l'assurance vie garde l'avantage sur la disponibilité comme sur la transmission.",
  "À partir de la tranche à 30 %, ouvrez les <b>deux</b> et répartissez : le PER porte l'épargne que vous ne toucherez pas, l'assurance vie porte le reste. Et quelle que soit votre décision, c'est la date d'ouverture et la régularité des versements qui pèseront le plus lourd, pas l'enveloppe.",
 ]),
 faq=[
  ("Faut-il privilégier un PER ou une assurance vie pour préparer sa retraite ?","Le PER devient intéressant à partir de la tranche marginale à 30 %, surtout si votre tranche baissera à la retraite. En dessous, l'assurance vie reste préférable parce que les fonds restent disponibles et que sa fiscalité s'allège après huit ans."),
  ("Peut-on avoir un PER et une assurance vie ?","Oui, et c'est la configuration la plus courante à partir d'un certain niveau de revenus. Le PER porte l'épargne bloquée et fiscalement optimisée, l'assurance vie porte l'épargne disponible et la transmission."),
  ("Comment préparer sa retraite quand on a 35 ans ?","Par la régularité plus que par le montant. Un versement mensuel de 200 € pendant trente ans constitue un capital comparable à 800 € par mois pendant dix ans, pour un effort total nettement inférieur."),
  ("Combien faut-il épargner chaque mois pour compléter sa retraite ?","Pour un complément d'environ 380 € par mois pendant vingt-cinq ans, comptez environ 200 € par mois si vous commencez à 35 ans, 350 € à 45 ans et 800 € à 55 ans, sous une hypothèse de rendement net de 3 % par an."),
  ("Le PER est-il intéressant si je ne paie pas d'impôt ?","Non. La déduction ne produit aucune économie et le blocage des fonds reste entier. Dans cette situation, l'assurance vie remplit le même rôle sans la contrainte."),
  ("Que devient un PER au décès ?","Le PER assurantiel suit un régime propre, dont les règles dépendent de l'âge du titulaire au décès. Il ne reprend pas à l'identique le régime de l'assurance vie, ce qui justifie de ne pas concentrer toute son épargne sur un PER quand la transmission est un objectif."),
 ],
 related=[("per-retraite","per-1.svg","Classement","Meilleur PER 2026 : le comparatif de 12 plans d'épargne retraite"),
          ("assurance-vie","une.svg","Classement","Meilleure assurance vie 2026 : le comparatif de 16 contrats"),
          ("fiscalite-succession","fisc-1.svg","Fiscalité","Fiscalité de l'assurance vie en 2026 : ce que vous payez vraiment à chaque retrait")],
),
]
