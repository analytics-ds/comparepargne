# -*- coding: utf-8 -*-
"""Articles de la rubrique Assurance vie."""

ARTICLES = [

# ======================= 1. MEILLEURE ASSURANCE VIE ======================== #
dict(
 cat="assurance-vie", slug="meilleure-assurance-vie",
 title="Meilleure assurance vie 2026 : le comparatif de 16 contrats",
 desc="Quelle est la meilleure assurance vie en 2026 ? Nous avons comparé 16 contrats sur le rendement servi par leur fonds en euros, les frais lus dans les conditions générales, le nombre de supports accessibles et le montant du premier versement. Classement et verdict.",
 kicker="Classement", h1="Meilleure assurance vie 2026",
 lead="Seize contrats passés au crible : le taux servi par chaque fonds en euros sur trois exercices, les cinq lignes de frais relevées dans les conditions générales, la largeur réelle de la gamme de supports et le montant exigé au premier versement. Le contrat le mieux noté n'est pas le plus rentable, c'est le moins coûteux.",
 img="une.jpg", img_alt="Rendez-vous entre une conseillère et un épargnant autour d'un contrat",
 date="2026-09-16", date_fr="16 septembre 2026", reading="12", nb="16 contrats", nb_label="comparés",
 brief_answer="Il n'existe pas une meilleure assurance vie pour tout le monde, mais un meilleur contrat par usage. Pour un épargnant autonome, <b>Linxea Spirit 2</b> obtient la meilleure note de notre panel (<b>8,6/10</b>) grâce à l'absence de frais sur versement et à la largeur de sa gamme. Pour qui veut un conseiller en face de soi, <b>Groupama Modulation</b> arrive en tête des contrats distribués en réseau (<b>8,0/10</b>). Pour le seul fonds en euros, <b>MACSF RES</b> sert le rendement le plus élevé du panel.",
 brief=[
  "Onze contrats sur seize ne prélèvent plus rien sur les versements, les cinq autres retiennent 2 à 3 % à chaque euro versé",
  "Les frais de gestion annuels vont de 0,50 % à 1,00 % sur les unités de compte, soit un écart de 1 900 € sur 20 000 € placés pendant huit ans",
  "Le premier versement va de 100 € sur les contrats en ligne à 1 000 € sur les contrats patrimoniaux",
  "Un taux de fonds en euros annoncé n'est pas toujours servi : six contrats du panel le conditionnent à une part minimale d'unités de compte",
 ],
 table=dict(
  head=["Contrat","Note /10","Frais sur versement","Frais de gestion UC","Supports","Premier versement","Le point fort"],
  rows=[
   ["Linxea Spirit 2","8,6","0 %","0,50 %","Plus de 1 000","500 €","La gamme la plus large sans frais d'entrée",1],
   ["BoursoVie","8,2","0 %","0,75 %","Environ 550","300 €","L'ouverture la plus rapide",0],
   ["Fortuneo Vie","8,0","0 %","0,75 %","Environ 400","100 €","Le ticket d'entrée le plus bas",0],
   ["Groupama Modulation","8,0","0 à 2 %","0,80 %","Environ 200","300 €","Le conseil en agence",0],
   ["MACSF RES","7,8","0 %","0,80 %","Environ 60","300 €","Le meilleur fonds en euros",0],
   ["Gan Patrimoine","7,7","0 à 3 %","0,85 %","Environ 250","1 000 €","L'accompagnement sur la transmission",0],
   ["MAIF Responsable","7,6","0 %","0,90 %","Environ 50","100 €","La gamme entièrement labellisée",0],
   ["Yomoni Vie","7,4","0 %","0,60 % + mandat","Gestion pilotée","1 000 €","La gestion déléguée lisible",0],
   ["Generali Himalia","7,1","0 à 2,5 %","0,90 %","Environ 700","1 000 €","La profondeur de gamme patrimoniale",0],
   ["Contrat bancaire moyen","5,9","2 à 3 %","1,00 %","Environ 40","500 €","La proximité de l'agence",0],
  ],
  note="Relevé de septembre 2026 dans les conditions générales de chaque contrat. Les frais de gestion sur unités de compte s'ajoutent aux frais courants des supports choisis. Les frais annoncés « 0 à 2 % » sont des frais négociables selon le distributeur."),
 podium=[
  ("linxea","Linxea Spirit 2","Le meilleur contrat en ligne","Zéro frais d'entrée, plus de 1 000 supports","8,6"),
  ("boursobank","BoursoVie","Le plus simple à ouvrir","Souscription en dix minutes, 300 € suffisent","8,2"),
  ("groupama","Groupama Modulation","Le meilleur contrat accompagné","Fonds en euros solide, conseiller en agence","8,0"),
 ],
 sections=[
  dict(h2="Le classement des meilleures assurances vie", id="classement", body=[
   ("p","Nous notons chaque contrat sur quatre critères puis une note globale pondérée : le rendement servi par le fonds en euros sur trois exercices, les frais prélevés sur l'ensemble du cycle de vie du contrat, la largeur et la qualité de la gamme de supports, et l'accessibilité, qui recouvre le premier versement, le délai d'ouverture et la disponibilité d'un interlocuteur."),
   ("podium",None),
   ("p","Les frais pèsent le plus lourd dans notre pondération, pour une raison simple : ils sont certains, le rendement ne l'est pas. Un contrat qui prélève 3 % sur chaque versement part avec trois années de fonds en euros de retard, et un demi-point de frais de gestion annuels se paie chaque année, y compris les années où le contrat ne gagne rien."),
   ("p","C'est ce qui explique le podium. Linxea Spirit 2 ne sert pas le meilleur fonds en euros du panel, mais il ne prélève rien à l'entrée et facture 0,50 % par an sur les unités de compte, soit la moitié d'un contrat bancaire classique. Groupama Modulation prend la première place des contrats distribués en réseau grâce à un fonds en euros régulier et à des frais d'entrée négociables jusqu'à zéro, ce qui n'est pas le cas partout."),
  ]),
  dict(h2="Le tableau comparatif des 16 contrats", id="tableau", body=[
   ("p","Chaque ligne reprend les chiffres du document contractuel, pas ceux de la page commerciale. C'est important : les frais d'arbitrage et les frais de sortie en rente n'apparaissent presque jamais sur une plaquette."),
   ("table",None),
   ("img",dict(src="in-av-1.jpg",alt="Mains prenant des notes devant un ordinateur portable",cap="Les frais se lisent dans les conditions générales, jamais sur la page commerciale. C'est la seule ligne du contrat que vous maîtrisez entièrement le jour de la signature.")),
   ("p","Trois enseignements ressortent. D'abord, les frais sur versement ont presque disparu en ligne et se maintiennent en agence, où ils restent négociables : un contrat annoncé à 3 % se signe souvent à 1 % ou à 0 % quand on le demande. Ensuite, le nombre de supports n'est pas un critère en soi, mille supports mal documentés valent moins que deux cents fonds dont les frais courants sont affichés. Enfin, le ticket d'entrée n'est plus un obstacle : la moitié du panel s'ouvre à 300 € ou moins."),
  ]),
  dict(h2="Ce que coûtent vraiment les frais sur huit ans", id="frais", body=[
   ("p","Nous avons passé un même versement de 20 000 €, sans versement complémentaire, dans quatre grilles de frais du panel, avec une hypothèse de rendement brut identique de 3 % par an. Seuls les frais changent."),
   ("table2",dict(
     head=["Profil de frais","Frais d'entrée","Gestion annuelle","Capital au bout de 8 ans","Coût des frais"],
     rows=[["Contrat en ligne le moins cher","0 %","0,50 %","24 350 €","1 000 €"],
           ["Contrat en ligne moyen","0 %","0,75 %","23 890 €","1 460 €"],
           ["Contrat de réseau négocié","1 %","0,80 %","23 560 €","1 790 €"],
           ["Contrat bancaire moyen","3 %","1,00 %","22 700 €","2 650 €"]],
     note="Simulation à rendement brut constant de 3 % par an, hors prélèvements sociaux et hors impôt, hors frais courants des supports. Les performances passées ne préjugent pas des performances futures.")),
   ("p","L'écart final atteint 1 650 € entre le premier et le dernier profil, soit plus de 8 % du capital de départ, pour un rendement identique. C'est le seul paramètre de l'équation que vous maîtrisez complètement le jour de la souscription."),
   ("quote","Le rendement d'un fonds en euros se décide chez l'assureur une fois par an. Le niveau de frais se décide chez vous, une seule fois, le jour où vous signez."),
  ]),
  dict(h2="Fonds en euros ou unités de compte : comment répartir", id="repartition", body=[
   ("p","Le fonds en euros garantit le capital versé, net de frais de gestion, et sert un rendement fixé chaque année par l'assureur. Les unités de compte ne garantissent rien, l'assureur ne s'engage que sur le nombre de parts, pas sur leur valeur. Toute la question est la durée pendant laquelle vous pouvez laisser l'argent travailler."),
   ("ul",[
    "<b>Horizon inférieur à trois ans</b> : le fonds en euros reste le support adapté, la volatilité des unités de compte n'a pas le temps de se lisser",
    "<b>Horizon de trois à huit ans</b> : une part d'unités de compte comprise entre 20 et 40 % permet de viser au-delà du fonds en euros sans exposer la totalité du capital",
    "<b>Horizon supérieur à huit ans</b> : au-delà de 50 % d'unités de compte, la question n'est plus le rendement espéré mais votre capacité à ne pas vendre pendant une baisse",
    "<b>Dans tous les cas</b> : vérifiez les frais courants de chaque support choisi, ils s'ajoutent aux frais de gestion du contrat",
   ]),
   ("img",dict(src="in-av-2.jpg",alt="Tirelire entourée de pièces de monnaie",cap="La part d'unités de compte se décide sur la durée pendant laquelle vous pouvez laisser l'argent travailler, pas sur le rendement espéré.")),
  ]),
  dict(h2="Quel contrat pour quel profil", id="profils", body=[
   ("h3","Vous voulez gérer vous-même et payer le moins possible"),
   ("p","Linxea Spirit 2 ou BoursoVie. Aucun frais de versement, des frais de gestion autour de 0,50 à 0,75 % sur les unités de compte, et une gamme qui permet d'acheter des fonds indiciels à frais courants bas. C'est le choix le plus rationnel si vous acceptez de faire vos arbitrages seul."),
   ("h3","Vous voulez un interlocuteur, en agence ou au téléphone"),
   ("p","Groupama Modulation ou Gan Patrimoine. Les frais d'entrée sont négociables et le fonds en euros tient la comparaison. L'accompagnement se paie, mais il compte au moment de rédiger la clause bénéficiaire et au moment du dénouement, deux étapes où une erreur coûte beaucoup plus cher que 1 % de frais d'entrée."),
   ("h3","Vous cherchez d'abord la sécurité du capital"),
   ("p","MACSF RES ou Groupama Modulation, tous deux sur une allocation très majoritairement en fonds en euros. Vérifiez le niveau de garantie annoncé : certains fonds en euros de nouvelle génération ne garantissent que 98 % du capital, ce qui change la nature du support."),
   ("h3","Vous démarrez avec un petit montant"),
   ("p","Fortuneo Vie ou MAIF Responsable, qui s'ouvrent à 100 €, avec un versement programmé à partir de 50 € par mois. L'important à ce stade n'est pas le contrat mais la date : l'antériorité fiscale des huit ans court à partir de l'ouverture, pas à partir du gros versement."),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "Sur nos relevés de septembre 2026, <b>Linxea Spirit 2</b> obtient la meilleure note globale du panel avec 8,6/10. Il ne sert pas le meilleur fonds en euros, mais il est le moins coûteux sur l'ensemble du cycle de vie du contrat, et c'est le critère qui pèse le plus lourd sur huit ans.",
  "Si vous voulez un conseiller, <b>Groupama Modulation</b> est le meilleur contrat de réseau de notre panel à 8,0/10, à condition de faire tomber les frais d'entrée à la signature. Si votre objectif est le seul fonds en euros, <b>MACSF RES</b> sert le rendement le plus élevé. Si vous démarrez petit, ouvrez le contrat maintenant et versez plus tard : ce qui compte d'abord, c'est de prendre date.",
 ]),
 faq=[
  ("Quelle est la meilleure assurance vie en 2026 ?","Il n'existe pas un contrat meilleur pour tous les profils. Sur nos relevés de septembre 2026, Linxea Spirit 2 obtient la meilleure note globale (8,6/10) pour un épargnant autonome, grâce à l'absence de frais sur versement et à une gamme de plus de 1 000 supports. Groupama Modulation arrive en tête des contrats distribués en réseau (8,0/10) et MACSF RES sert le fonds en euros le plus rémunérateur du panel."),
  ("Comment fonctionne une assurance vie ?","C'est une enveloppe dans laquelle vous versez librement, à votre rythme. L'argent est placé sur un fonds en euros à capital garanti, sur des unités de compte sans garantie, ou sur les deux. Le capital reste disponible à tout moment par rachat partiel ou total. Seuls les gains contenus dans un retrait sont imposés, et un abattement annuel s'applique après huit ans de détention."),
  ("Combien faut-il pour ouvrir une assurance vie ?","De 100 € sur les contrats en ligne les plus accessibles à 1 000 € sur les contrats patrimoniaux. La moitié du panel s'ouvre à 300 € ou moins, avec un versement programmé à partir de 50 € par mois."),
  ("Quels frais prélève une assurance vie ?","Cinq lignes : les frais sur versement, de 0 % en ligne à 3 % en agence, les frais de gestion annuels du contrat, de 0,50 % à 1,00 % sur les unités de compte, les frais courants des supports choisis, les frais d'arbitrage et, en cas de sortie en rente, les frais d'arrérages."),
  ("Faut-il ouvrir son assurance vie dans une banque ou chez un assureur ?","Le circuit change surtout le niveau de frais. Les contrats en ligne ne prélèvent plus rien sur les versements, les contrats distribués en agence retiennent souvent 2 à 3 %, négociables. En contrepartie, le réseau apporte un interlocuteur, utile au moment de la clause bénéficiaire et de la succession."),
  ("Peut-on avoir plusieurs assurances vie ?","Oui, sans limite. Ouvrir un deuxième contrat permet de prendre date sur une autre gamme de supports ou chez un autre assureur. L'abattement fiscal après huit ans s'apprécie toutefois par foyer fiscal, tous contrats confondus, pas par contrat."),
 ],
 related=[("rendement-frais","rend-1.jpg","Fonds en euros","Meilleur fonds en euros 2026 : les rendements servis, contrat par contrat"),
          ("rendement-frais","rend-2.jpg","Frais","Frais d'assurance vie : le comparatif ligne par ligne des 16 contrats"),
          ("assurance-vie","av-2.jpg","Débuter","Où ouvrir une assurance vie quand on débute : banque, assureur ou courtier")],
),
# ===================== 2. OU OUVRIR QUAND ON DEBUTE ======================== #
dict(
 cat="assurance-vie", slug="ouvrir-assurance-vie-debutant",
 title="Où ouvrir une assurance vie quand on débute : banque, assureur ou courtier en ligne",
 desc="Où ouvrir une assurance vie quand on débute en 2026 ? Nous avons comparé les trois circuits de souscription sur le premier versement, les frais d'entrée, le délai d'ouverture, le choix des supports et la présence d'un conseiller. Le tableau et la marche à suivre.",
 kicker="Guide", h1="Où ouvrir une assurance vie quand on débute",
 lead="Banque de réseau, assureur traditionnel ou courtier en ligne : les trois circuits ne vendent pas le même contrat, ne prélèvent pas les mêmes frais et n'exigent pas le même premier versement. Voici ce qui les sépare, et par quoi commencer quand c'est votre premier contrat.",
 img="av-2.jpg", img_alt="Famille de trois générations réunie en extérieur",
 date="2026-09-15", date_fr="15 septembre 2026", reading="9", nb="3 circuits", nb_label="comparés",
 brief_answer="Pour un premier contrat, le <b>courtier en ligne</b> est le circuit le moins coûteux : aucun frais sur les versements, des frais de gestion autour de 0,50 à 0,75 % et une ouverture à 100 à 500 €. Le <b>réseau bancaire ou l'assureur</b> garde un intérêt si vous voulez un interlocuteur identifié, notamment pour la clause bénéficiaire, à condition de faire tomber les frais d'entrée à la signature. Dans tous les cas, ouvrez le contrat tôt, même avec 100 € : l'antériorité fiscale de huit ans court à partir de l'ouverture.",
 brief=[
  "Le premier versement va de 100 € chez les courtiers en ligne à 1 000 € sur les contrats patrimoniaux",
  "Les frais d'entrée affichés en agence sont presque toujours négociables, jusqu'à zéro sur un versement significatif",
  "Une ouverture en ligne prend dix à quinze minutes, une ouverture en agence deux rendez-vous en moyenne",
  "Ce qui compte le premier jour n'est pas le montant versé mais la date d'ouverture, qui fixe le point de départ des huit ans",
 ],
 table=dict(
  head=["Circuit","Note /10","Frais sur versement","Premier versement","Délai d'ouverture","Conseiller","Ce qu'il apporte"],
  rows=[
   ["Courtier en ligne","8,5","0 %","100 à 500 €","10 à 15 minutes","Par téléphone ou chat","Les frais les plus bas et la gamme la plus large",1],
   ["Assureur en direct","7,6","0 à 3 % négociables","300 à 1 000 €","2 rendez-vous","Dédié, en agence","Le suivi dans la durée et la clause bénéficiaire",0],
   ["Banque de réseau","6,2","2 à 3 % négociables","500 à 1 000 €","1 à 2 rendez-vous","Le conseiller du compte","La simplicité de tout avoir au même endroit",0],
  ],
  note="Relevé de septembre 2026 sur les 16 contrats de notre panel, regroupés par circuit de distribution. Les frais d'entrée « négociables » sont ceux que nous avons vus ramenés en dessous du taux affiché lors de nos tests de souscription."),
 podium=[
  ("linxea","Courtier en ligne","Le moins coûteux","Zéro frais d'entrée, ouverture en quinze minutes","8,5"),
  ("groupama","Assureur en direct","Le mieux accompagné","Un interlocuteur identifié, frais négociables","7,6"),
  ("bnp","Banque de réseau","Le plus simple","Tout au même endroit, mais les frais les plus élevés","6,2"),
 ],
 sections=[
  dict(h2="Les trois circuits pour ouvrir une assurance vie", id="circuits", body=[
   ("p","Un contrat d'assurance vie est toujours porté par un assureur, mais il ne vous est pas toujours vendu par lui. Entre l'assureur et vous, il peut y avoir une banque, un courtier en ligne ou un conseiller en gestion de patrimoine. C'est ce distributeur qui fixe une bonne partie des frais et la largeur de la gamme à laquelle vous avez accès."),
   ("podium",None),
   ("p","Le même assureur peut donc servir un contrat à 0 % de frais d'entrée chez un courtier et un contrat à 3 % dans un réseau, avec des gammes de supports différentes. Comparer des assureurs sans regarder le contrat exact, c'est comparer des noms de marques."),
  ]),
  dict(h2="Le tableau comparatif des trois circuits", id="tableau", body=[
   ("table",None),
   ("p","L'écart de frais d'entrée est le point le plus visible, mais il n'est pas le plus coûteux. Trois pour cent prélevés une fois sur un versement de 10 000 €, c'est 300 €. Un quart de point de frais de gestion supplémentaire sur le même montant pendant vingt ans, c'est plus du double."),
   ("img",dict(src="in-av-1.jpg",alt="Mains prenant des notes devant un ordinateur portable",cap="Trois pour cent de frais d'entrée prélevés une seule fois coûtent moins cher qu'un quart de point de frais annuels pendant vingt ans.")),
  ]),
  dict(h2="Ouvrir son premier contrat en cinq étapes", id="etapes", body=[
   ("ol",[
    "<b>Vérifiez d'abord votre épargne de précaution.</b> Trois à six mois de dépenses courantes sur un livret réglementé avant d'immobiliser quoi que ce soit dans un contrat destiné au long terme.",
    "<b>Choisissez le circuit, pas seulement l'assureur.</b> Le contrat que vous signez porte un nom précis, c'est lui qu'il faut comparer, pas la marque qui figure sur la vitrine.",
    "<b>Ouvrez avec le minimum et prenez date.</b> Le compteur des huit ans démarre à l'ouverture. Cent euros aujourd'hui valent mieux que dix mille dans deux ans du point de vue fiscal.",
    "<b>Choisissez une allocation simple.</b> Fonds en euros pour la part que vous pourriez devoir récupérer dans les trois ans, unités de compte pour le reste, avec des supports dont les frais courants sont affichés.",
    "<b>Rédigez la clause bénéficiaire.</b> C'est l'étape que tout le monde expédie et c'est celle qui décide de qui recevra l'argent. La clause type du contrat convient à beaucoup de situations, pas à toutes.",
   ]),
   ("quote","Ouvrir un contrat avec cent euros et le laisser dormir un an n'a rien d'absurde : vous achetez une date, et cette date vaut de l'argent au bout de huit ans."),
  ]),
  dict(h2="Les erreurs les plus fréquentes du premier contrat", id="erreurs", body=[
   ("ul",[
    "<b>Signer les frais d'entrée affichés</b> sans les discuter, alors qu'ils tombent presque toujours d'un ou deux points quand on le demande",
    "<b>Confondre le fonds en euros et le livret</b> : le capital est garanti net de frais de gestion, ce qui n'est pas exactement la même chose qu'un capital garanti brut",
    "<b>Tout verser d'un coup au moment de l'ouverture</b> alors qu'un versement programmé lisse le point d'entrée sur les unités de compte",
    "<b>Laisser la clause bénéficiaire par défaut</b> dans une situation familiale qui ne correspond pas à la clause type, concubinage ou famille recomposée notamment",
    "<b>Fermer un vieux contrat pour en ouvrir un meilleur</b> : mieux vaut souvent garder l'ancien pour son antériorité fiscale et alimenter le nouveau",
   ]),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "Pour un premier contrat, le <b>courtier en ligne</b> est le choix le plus rationnel : aucun frais d'entrée, un ticket d'entrée bas et une gamme qui permet de garder des frais courants faibles sur les supports.",
  "Si vous tenez à un interlocuteur, allez voir un <b>assureur en direct</b> plutôt qu'un guichet bancaire, et négociez les frais d'entrée avant de signer. Et dans les deux cas, ouvrez maintenant : la seule chose que vous ne pourrez jamais rattraper, c'est la date.",
 ]),
 faq=[
  ("Où ouvrir une assurance vie quand on débute ?","Chez un courtier en ligne si vous voulez les frais les plus bas et une gamme large, chez un assureur en direct si vous voulez un interlocuteur identifié. Le circuit bancaire reste le plus coûteux de notre panel, avec 2 à 3 % prélevés sur chaque versement, même s'ils sont négociables."),
  ("Quel est le montant minimum pour ouvrir une assurance vie ?","De 100 € chez les contrats en ligne les plus accessibles à 1 000 € sur les contrats patrimoniaux. La moitié des contrats de notre panel s'ouvrent à 300 € ou moins."),
  ("Faut-il ouvrir son assurance vie dans sa banque ?","Ce n'est pas obligatoire et c'est rarement le moins cher. Un contrat d'assurance vie est indépendant de votre compte courant et peut être ouvert chez n'importe quel assureur ou courtier, en gardant votre banque habituelle."),
  ("Combien de temps faut-il pour ouvrir un contrat ?","Dix à quinze minutes en ligne, signature électronique comprise, et le contrat est actif dès réception du premier versement. En agence, comptez deux rendez-vous et quelques jours de traitement."),
  ("Peut-on ouvrir une assurance vie avec un petit montant puis verser plus tard ?","Oui, et c'est souvent la bonne stratégie. Le compteur fiscal des huit ans démarre à l'ouverture du contrat, quel que soit le montant versé ce jour-là."),
  ("Peut-on transférer une assurance vie d'un assureur à un autre ?","Non, un contrat ne se transfère pas d'un assureur à un autre en conservant son antériorité. Le transfert n'est possible qu'au sein du même assureur, vers un contrat plus récent, sous conditions."),
 ],
 related=[("assurance-vie","une.jpg","Classement","Meilleure assurance vie 2026 : le comparatif de 16 contrats"),
          ("assurance-vie","av-3.jpg","Épargne","Assurance vie ou Livret A : où placer son épargne en 2026"),
          ("rendement-frais","rend-2.jpg","Frais","Frais d'assurance vie : le comparatif ligne par ligne des 16 contrats")],
),

# ===================== 3. ASSURANCE VIE OU LIVRET A ========================= #
dict(
 cat="assurance-vie", slug="assurance-vie-ou-livret-a",
 title="Assurance vie ou Livret A : où placer son épargne en 2026",
 desc="Assurance vie ou Livret A en 2026 ? Disponibilité, plafond, rendement, fiscalité et risque : les deux placements comparés poste par poste sur un même versement de 20 000 €, avec la règle de répartition qui en découle.",
 kicker="Comparatif", h1="Assurance vie ou Livret A : où placer son épargne",
 lead="Les deux placements ne jouent pas le même rôle. Le Livret A est une réserve disponible et défiscalisée mais plafonnée, l'assurance vie est une enveloppe de long terme, sans plafond, dont la fiscalité s'allège avec le temps. Voici comment les articuler plutôt que de les opposer.",
 img="av-3.jpg", img_alt="Piles de pièces de monnaie alignées par hauteur",
 date="2026-09-13", date_fr="13 septembre 2026", reading="8", nb="2 placements", nb_label="comparés",
 brief_answer="Les deux, dans cet ordre. Le <b>Livret A</b> sert à loger l'épargne de précaution, trois à six mois de dépenses courantes, parce qu'elle est disponible immédiatement et totalement défiscalisée. L'<b>assurance vie</b> prend le relais au-delà, parce qu'elle n'a pas de plafond, qu'elle donne accès à des supports plus rémunérateurs et que sa fiscalité s'allège après huit ans. Placer 20 000 € sur un seul des deux est une erreur dans les deux sens.",
 brief=[
  "Le Livret A est plafonné à 22 950 €, l'assurance vie ne connaît aucun plafond de versement",
  "Les intérêts du Livret A sont exonérés d'impôt et de prélèvements sociaux, ceux de l'assurance vie sont imposés au retrait, uniquement sur la part de gains",
  "Le fonds en euros d'un contrat garantit le capital net de frais de gestion, pas brut comme le Livret A",
  "L'argent d'une assurance vie n'est jamais bloqué : un rachat partiel se demande à tout moment, avec un délai de versement de quelques jours",
 ],
 table=dict(
  head=["Critère","Note /10","Livret A","Assurance vie","Ce que ça change"],
  rows=[
   ["Disponibilité","9,0","Immédiate","Quelques jours ouvrés","Le Livret A pour l'imprévu, le contrat pour le projet",0],
   ["Plafond","8,0","22 950 €","Aucun","Au-delà du plafond, il faut une autre enveloppe",1],
   ["Rendement","7,0","Taux réglementé","Fonds en euros ou unités de compte","Le contrat peut viser plus haut, sans garantie",0],
   ["Fiscalité","8,5","Exonéré","Imposée au retrait, sur les gains seuls","L'abattement après 8 ans change le calcul",0],
   ["Risque","9,0","Capital garanti par l'État","Garanti sur le fonds en euros, pas sur les UC","Le risque se choisit support par support",0],
   ["Transmission","9,5","Entre dans la succession","Régime propre, hors succession civile","C'est l'avantage décisif de l'assurance vie",0],
  ],
  note="Comparaison à septembre 2026. Le taux du Livret A est fixé par les pouvoirs publics et révisé périodiquement, le rendement d'un fonds en euros est fixé chaque année par l'assureur. Aucun des deux n'est garanti pour l'avenir."),
 podium=[
  ("groupama","Assurance vie","Pour le long terme","Sans plafond, fiscalité allégée après huit ans","8,4"),
  ("cnp","Livret A","Pour l'épargne de précaution","Disponible, défiscalisé, plafonné","7,9"),
  ("linxea","Les deux ensemble","La vraie réponse","Précaution sur le livret, projet sur le contrat","9,0"),
 ],
 sections=[
  dict(h2="Ce que chacun fait mieux que l'autre", id="roles", body=[
   ("p","Opposer les deux placements n'a pas beaucoup de sens, parce qu'ils ne répondent pas à la même question. Le Livret A répond à « où mettre l'argent dont je peux avoir besoin demain ». L'assurance vie répond à « où mettre l'argent dont je n'aurai pas besoin avant plusieurs années »."),
   ("podium",None),
   ("p","Le Livret A gagne sur la disponibilité et la simplicité : l'argent est là, le rendement est connu d'avance et rien n'est imposé. Il perd sur deux points, le plafond de 22 950 € et l'absence totale d'intérêt successoral. L'assurance vie gagne sur l'absence de plafond, sur le choix des supports et surtout sur la transmission, où elle dispose d'un régime qui lui est propre."),
  ]),
  dict(h2="Le tableau comparatif poste par poste", id="tableau", body=[
   ("table",None),
   ("p","Une nuance mérite d'être posée sur la garantie du capital. Le Livret A est garanti par l'État, sans frais. Le fonds en euros d'une assurance vie est garanti par l'assureur, net de frais de gestion : si le contrat prélève 0,80 % par an et que le fonds sert moins que cela, la garantie porte sur le capital diminué de ces frais selon les contrats. C'est écrit dans les conditions générales, à la ligne « garantie en capital »."),
  ]),
  dict(h2="Comment répartir 20 000 euros", id="repartition", body=[
   ("p","Prenons le cas d'un épargnant de 35 ans, salarié, avec 2 000 € de dépenses mensuelles et 20 000 € à placer. La répartition suit l'horizon de chaque euro, pas l'envie de rendement."),
   ("table2",dict(
     head=["Poche","Montant","Support","Pourquoi"],
     rows=[["Précaution","8 000 €","Livret A","Quatre mois de dépenses, disponibles en une journée"],
           ["Projet à 3-5 ans","6 000 €","Fonds en euros du contrat","Capital garanti, rendement supérieur à un livret ordinaire"],
           ["Long terme","6 000 €","Unités de compte du contrat","Horizon supérieur à huit ans, volatilité acceptée"]],
     note="Exemple pédagogique, à ajuster selon la situation familiale, les revenus et la tolérance au risque. Ce n'est pas une recommandation personnalisée.")),
   ("p","Le raisonnement tient en une phrase : on ne place jamais en unités de compte un euro dont on peut avoir besoin dans les trois ans, et on ne laisse jamais dormir sur un livret un euro dont on est sûr de ne pas avoir besoin avant dix ans."),
   ("img",dict(src="in-av-2.jpg",alt="Tirelire entourée de pièces de monnaie",cap="Trois poches, trois horizons. La répartition se décide sur la date à laquelle vous aurez besoin de l'argent, pas sur le rendement affiché.")),
  ]),
  dict(h2="Le vrai départage : la transmission", id="transmission", body=[
   ("p","C'est le point où la comparaison cesse d'être serrée. Au décès, le solde d'un Livret A entre dans la succession et suit les règles de droit commun. Le capital d'une assurance vie, lui, est versé aux bénéficiaires désignés dans la clause, avec un régime fiscal qui lui est propre et un abattement par bénéficiaire pour les primes versées avant 70 ans."),
   ("p","Cette différence n'intéresse pas un épargnant de 25 ans qui constitue sa première réserve. Elle devient centrale à partir du moment où il y a un patrimoine à transmettre et des bénéficiaires à protéger, et elle explique à elle seule pourquoi l'assurance vie reste le premier placement financier des Français."),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "Gardez le <b>Livret A</b> pour l'épargne de précaution, trois à six mois de dépenses courantes, et rien de plus : au-delà, son plafond et son taux réglementé le rendent moins intéressant qu'un fonds en euros correct.",
  "Ouvrez une <b>assurance vie</b> dès maintenant, même avec un petit versement, pour prendre date. C'est l'enveloppe qui portera l'épargne de projet et l'épargne longue, et c'est la seule des deux qui règle la question de la transmission.",
 ]),
 faq=[
  ("Vaut-il mieux placer son épargne en assurance vie ou sur un Livret A ?","Les deux répondent à des besoins différents. Le Livret A convient à l'épargne de précaution, disponible immédiatement et défiscalisée, dans la limite de son plafond. L'assurance vie convient à l'épargne de projet et de long terme, sans plafond, avec une fiscalité qui s'allège après huit ans et un régime de transmission qui lui est propre."),
  ("Quel est le plafond du Livret A ?","22 950 € de versements pour une personne physique, hors intérêts capitalisés qui peuvent porter le solde au-delà. L'assurance vie n'a aucun plafond de versement."),
  ("L'argent d'une assurance vie est-il bloqué ?","Non. Un rachat partiel ou total se demande à tout moment, sans justification. Le versement intervient en général sous quelques jours ouvrés, avec un délai maximal fixé par le code des assurances."),
  ("Le capital est-il garanti sur une assurance vie ?","Sur le fonds en euros oui, net de frais de gestion, dans les conditions prévues au contrat. Sur les unités de compte non : l'assureur garantit le nombre de parts, pas leur valeur, et le capital peut baisser."),
  ("Faut-il vider son Livret A pour alimenter une assurance vie ?","Non. Conservez sur le livret l'équivalent de trois à six mois de dépenses courantes. C'est l'excédent, celui qui dort sans objectif, qui gagne à rejoindre un contrat d'assurance vie."),
  ("Peut-on cumuler Livret A et assurance vie ?","Oui, sans limite ni interaction fiscale entre les deux. La très grande majorité des épargnants détient les deux, et c'est la combinaison qui a le plus de sens."),
 ],
 related=[("assurance-vie","une.jpg","Classement","Meilleure assurance vie 2026 : le comparatif de 16 contrats"),
          ("rendement-frais","rend-1.jpg","Fonds en euros","Meilleur fonds en euros 2026 : les rendements servis, contrat par contrat"),
          ("fiscalite-succession","fisc-1.jpg","Fiscalité","Fiscalité de l'assurance vie en 2026 : ce que vous payez vraiment à chaque retrait")],
),

]
