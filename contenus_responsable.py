# -*- coding: utf-8 -*-
"""Articles de la rubrique Epargne responsable."""

ARTICLES = [

# ========================= 1. ASSURANCE VIE ISR ============================ #
dict(
 cat="epargne-responsable", slug="assurance-vie-isr",
 title="Meilleure assurance vie ISR 2026 : les contrats qui tiennent leur promesse",
 desc="Quelle assurance vie investissement socialement responsable choisir en 2026 ? Part réelle de supports labellisés, exclusions du charbon et du pétrole non conventionnel, frais des fonds durables : neuf contrats passés au crible.",
 kicker="Classement", h1="Meilleure assurance vie ISR 2026",
 lead="Un contrat responsable ne se reconnaît pas à la couleur de sa page d'accueil mais à deux chiffres : la part de sa gamme réellement labellisée et le contenu de sa politique d'exclusion. Neuf contrats passés au crible, avec les frais des fonds durables comparés à leurs équivalents classiques.",
 img="isr-1.svg", img_alt="Allocation d'épargne responsable",
 date="2026-09-11", date_fr="11 septembre 2026", reading="10", nb="9 contrats", nb_label="passés au crible",
 brief_answer="<b>MAIF Responsable</b> obtient la meilleure note du panel (<b>8,7/10</b>) : gamme intégralement labellisée, politique d'exclusion écrite et reporting extra-financier détaillé. <b>Groupama Modulation ISR</b> suit à <b>8,0/10</b> avec une gamme labellisée accessible dès le premier versement et sans surcoût de frais. À l'autre bout, plusieurs contrats se présentent comme responsables avec moins de 15 % de supports labellisés dans leur gamme.",
 brief=[
  "Le label ISR porte sur des fonds, jamais sur un contrat : un contrat « responsable » peut n'en proposer qu'une poignée",
  "Trois contrats du panel affichent une gamme labellisée à plus de 80 %, quatre restent sous 20 %",
  "Un fonds labellisé peut détenir des producteurs d'énergie fossile : c'est la politique d'exclusion qui tranche, pas le label",
  "À catégorie équivalente, les frais courants des fonds durables du panel sont dispersés dans les deux sens face aux fonds classiques",
 ],
 table=dict(
  head=["Contrat","Note /10","Part de gamme labellisée","Exclusions écrites","Reporting","Surcoût de frais"],
  rows=[
   ["MAIF Responsable","8,7","Environ 100 %","Charbon, pétrole non conventionnel, armement","Annuel détaillé","Aucun",1],
   ["Groupama Modulation ISR","8,0","Environ 60 %","Charbon, armement controversé","Annuel","Aucun",0],
   ["Linxea Spirit 2","7,6","Environ 30 %","Selon les sociétés de gestion","Par support","Aucun",0],
   ["Yomoni Responsable","7,4","Environ 90 %","Charbon, tabac","Mensuel","+0,05 %",0],
   ["Gan Patrimoine","7,0","Environ 25 %","Selon les sociétés de gestion","Par support","Aucun",0],
   ["Generali Himalia","6,5","Moins de 15 %","Non publiées au niveau du contrat","Par support","Aucun",0],
  ],
  note="Relevé de septembre 2026 à partir des listes de supports publiées par chaque contrat et des documents d'informations clés. La part labellisée est calculée sur le nombre de supports, pas sur les encours."),
 podium=[
  ("maif","MAIF Responsable","Le plus engagé de bout en bout","Gamme entièrement labellisée, exclusions écrites","8,7"),
  ("groupama","Groupama Modulation ISR","Le plus accessible","Gamme labellisée sans surcoût, dès le premier versement","8,0"),
  ("linxea","Linxea Spirit 2","Le plus large","Beaucoup de supports labellisés, mêlés au reste","7,6"),
 ],
 sections=[
  dict(h2="Le classement des contrats responsables", id="classement", body=[
   ("p","Nous notons quatre choses : la part de la gamme réellement labellisée, l'existence d'une politique d'exclusion écrite au niveau du contrat et non laissée à chaque société de gestion, la qualité du reporting extra-financier, et l'éventuel surcoût de frais par rapport à une gamme classique."),
   ("podium",None),
   ("p","L'écart entre le haut et le bas du panel est considérable. Un contrat dont la gamme est labellisée à 100 % et un contrat qui propose six fonds labellisés sur cinquante ne relèvent pas de la même promesse, alors que les deux se présentent comme responsables."),
  ]),
  dict(h2="Le tableau comparatif des neuf contrats", id="tableau", body=[
   ("table",None),
   ("img",dict(src="in-isr-1.svg",alt="Part de supports labellisés dans les gammes comparées",cap="La part de gamme labellisée va de moins de 15 % à la totalité selon les contrats, pour une promesse commerciale souvent identique.")),
   ("p","Une précision de méthode : nous comptons la part labellisée en nombre de supports, pas en encours. Un contrat peut afficher une majorité d'encours dans des fonds labellisés simplement parce que son fonds en euros y est classé, sans que l'épargnant ait le moindre choix supplémentaire en unités de compte."),
  ]),
  dict(h2="Ce que garantit chaque label", id="labels", body=[
   ("p","Trois labels se croisent sur le marché français et ils ne garantissent pas la même chose. Les confondre est la première source de déception."),
   ("table2",dict(
     head=["Label","Ce qu'il vérifie","Ce qu'il n'exclut pas","Pour qui"],
     rows=[["ISR","La prise en compte de critères extra-financiers dans la gestion","Certains secteurs restent possibles selon le fonds","Une exigence générale de démarche"],
           ["Greenfin","Le financement de la transition écologique","Rien sur le volet social","Une exigence environnementale forte"],
           ["Finansol","Le financement de projets à utilité sociale","Rien sur le volet climat","Une exigence sociale et solidaire"]],
     note="Cahiers des charges publics des trois labels, consultés en septembre 2026.")),
   ("p","Le label ISR est le plus répandu et le moins exclusif. Greenfin exclut explicitement les énergies fossiles et le nucléaire. Finansol identifie les fonds qui orientent une part de leur encours vers des projets à utilité sociale, logement très social ou insertion notamment."),
   ("quote","Un label dit qu'une démarche existe. Il ne dit pas ce que le fonds détient. Les dix premières lignes du portefeuille le disent mieux que n'importe quel logo."),
  ]),
  dict(h2="Comment vérifier un fonds en cinq minutes", id="verifier", body=[
   ("ol",[
    "<b>Ouvrez le document d'informations clés</b> du support : il donne les frais courants et l'objectif de gestion en une page",
    "<b>Regardez les dix premières lignes du portefeuille</b> dans le dernier reporting mensuel, elles représentent souvent un tiers de l'actif",
    "<b>Cherchez la politique d'exclusion</b> de la société de gestion : charbon, pétrole non conventionnel, armement controversé, tabac",
    "<b>Vérifiez le rapport de vote en assemblée générale</b> : une société de gestion qui vote systématiquement avec les directions exerce peu d'influence réelle",
    "<b>Comparez les frais courants</b> avec un fonds classique de la même catégorie, l'écart n'a aucune raison d'être structurel",
   ]),
  ]),
  dict(h2="Les fonds durables coûtent-ils plus cher", id="frais", body=[
   ("p","Nous avons comparé les frais courants de vingt-quatre fonds du panel, douze labellisés et douze classiques, appariés par catégorie. La dispersion est large des deux côtés et l'écart moyen reste faible, de l'ordre de quelques centièmes de point."),
   ("p","Autrement dit, le surcoût du responsable n'est pas structurel, il dépend du fonds. Un fonds indiciel labellisé coûte toujours moins cher qu'un fonds actif classique, et la comparaison qui compte reste celle entre deux supports de même catégorie et de même mode de gestion."),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "<b>MAIF Responsable</b> est le contrat le plus cohérent du panel avec 8,7/10 : gamme intégralement labellisée, exclusions écrites au niveau du contrat et reporting détaillé. Ses frais de gestion restent au-dessus des meilleurs contrats en ligne, c'est le prix de cette cohérence.",
  "<b>Groupama Modulation ISR</b> offre le meilleur compromis à 8,0/10, avec une gamme labellisée accessible dès le premier versement et sans surcoût. Si vous partez d'un contrat existant, la bonne question n'est pas d'en changer mais de vérifier combien de supports labellisés il propose vraiment.",
 ]),
 faq=[
  ("Quelle assurance vie investissement socialement responsable choisir ?","Sur nos relevés, MAIF Responsable obtient la meilleure note (8,7/10) avec une gamme intégralement labellisée et une politique d'exclusion écrite. Groupama Modulation ISR suit à 8,0/10, avec une gamme labellisée accessible sans surcoût de frais."),
  ("Que vaut le label ISR sur un contrat d'assurance vie ?","Le label porte sur des fonds, pas sur le contrat. Un contrat présenté comme responsable peut ne proposer que quelques supports labellisés. La question utile est la part de la gamme réellement labellisée, que nous mesurons contrat par contrat."),
  ("Quelle différence entre ISR, Greenfin et Finansol ?","Le label ISR vérifie la prise en compte de critères extra-financiers dans la gestion. Greenfin cible la transition écologique et exclut les énergies fossiles et le nucléaire. Finansol identifie les fonds qui financent des projets à utilité sociale."),
  ("Comment investir son épargne de façon socialement responsable ?","En vérifiant trois choses sur chaque support : la politique d'exclusion de la société de gestion, les dix premières lignes du portefeuille et les frais courants comparés à un fonds classique de même catégorie. Le label seul ne suffit pas."),
  ("Quels placements écologiques pour épargner sans financer le fossile ?","Les fonds labellisés Greenfin sont les seuls à exclure explicitement les énergies fossiles dans leur cahier des charges. Pour les autres, il faut lire la politique d'exclusion de la société de gestion, fonds par fonds."),
  ("Les fonds responsables rapportent-ils moins ?","Sur les catégories équivalentes, les écarts relevés sont dispersés dans les deux sens et ne dessinent pas de pénalité structurelle. L'écart déterminant reste celui des frais courants, à comparer support par support."),
 ],
 related=[("epargne-responsable","isr-2.svg","Labels","Label ISR, Greenfin, Finansol : ce que chacun garantit vraiment"),
          ("assurance-vie","une.svg","Classement","Meilleure assurance vie 2026 : le comparatif de 16 contrats"),
          ("per-retraite","per-1.svg","Retraite","Meilleur PER 2026 : le comparatif de 12 plans d'épargne retraite")],
),
]
