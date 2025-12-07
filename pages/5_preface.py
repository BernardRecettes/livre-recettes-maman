import streamlit as st

# Bouton retour accueil
if st.button("🏠 Retour à l'accueil"):
    st.switch_page("app.py")

st.title("Préface")

st.markdown(
    """

Je vous présente aujourd’hui le livre de recettes d’Adrienne, ma chère maman.
Ce livre n’est pas seulement un recueil de recettes, c’est un morceau de l’histoire de notre famille.

Je l’ai patiemment transformé en version électronique pour que chacun de vous, dans la famille et même au‑delà, puisse en profiter, y puiser des souvenirs et, à son tour, le transmettre.

Je veux d’abord remercier de tout cœur Isabelle, qui a eu, il y a des années dès la perte de notre maman chérie, la merveilleuse idée de prendre le livre original de maman pour en faire plusieurs copies. Elle a glissé chaque page dans des pochettes protectrices, puis relié le tout dans des cartables. Imaginez le dévouement : cinq exemplaires complets, 240 pages chacun… Un véritable travail d’amour qui a permis de préserver ce trésor familial.

Voilà près de vingt ans que maman nous a quittés et, trop souvent, j’ai eu l’impression que son livre s’effaçait doucement dans l’oubli. Avec l’omniprésence d’Internet, nous prenons parfois moins le temps de chercher ces précieuses traces de nos racines, et pourtant ce cahier, c’est un peu l’âme de notre mère. C’est pour cela que j’ai voulu le retranscrire, pour que ses recettes, ses gestes et tout l’amour qu’elle mettait dans sa cuisine restent vivants et accessibles à tous, pour longtemps.

En 2023, un grave accident de travail a bouleversé ma vie et m’a conduit à une retraite anticipée. Je ne le mentionne pas pour me plaindre, mais parce que c’est dans ce nouveau temps qui s’est ouvert devant moi que j’ai trouvé un espace pour me reconstruire.

J’ai toujours aimé l’informatique et les gadgets ; alors, lorsque j’ai retrouvé ce précieux cahier, je me suis donné un défi qui venait du cœur : offrir à maman une seconde vie numérique. Le projet n’a pas été de tout repos. Pour le mener à bien, j’ai apprivoisé Microsoft Access et transformé le livre en base de données : ce fut la version 1.0. Mais il fallait installer Access pour l’utiliser, et je voulais que ce cadeau soit le plus simple possible pour chacun.

J’ai donc créé une version 2.0 avec Excel, qui posait encore les mêmes limites. Alors je me suis lancé un nouveau défi : apprendre le langage Python pour développer une version 3.0, enfin accessible à tous, sans contraintes techniques, comme une porte ouverte sur ce précieux héritage.

Aujourd’hui, c’est avec une grande joie que je peux vous offrir la possibilité de feuilleter ce cahier en version électronique et d’y faire des recherches comme dans une véritable petite bibliothèque familiale. Toutes les recettes ne sont pas encore entrées, mais, jour après jour, le livre se remplit et prend vie à l’écran.

Au‑delà de la technique, ce projet est pour moi un chemin de réconciliation et de douceur. Ce n’est pas une tentative d’effacer les erreurs d’un passé plus sombre — certaines blessures restent — mais une façon de me rapprocher de ce qu’il y a de plus beau en moi : le désir de donner, de partager et de transmettre.

En recopiant ces recettes, il m’est souvent arrivé de sourire, parfois même d’éclater de rire. Maman écrivait comme elle cuisinait : avec le cœur plus qu’avec la balance.
Je suis retombé sur des indications savoureuses comme « une quantité de margarine, grosse comme un œuf », «un brin de beurre » (P74-1) ­­ ou « deux grosse poignées de sel » (P48-1), autant de petits clins d’œil qui faisaient revivre sa voix, son sourire et sa liberté.

Les pages qui m’ont le plus amusé sont sans doute celles des « remèdes de grand‑mère », qui, à mes yeux, devaient surtout fonctionner comme de doux placebos, même si nos ancêtres les préparaient très sérieusement.
Lisez‑les pour le plaisir, et si le cœur vous en dit, osez même les essayer : vous y retrouverez peut‑être un parfum d’autrefois.

J’ai aussi essayé de créer une interface simple, chaleureuse et facile d’emploi pour tout le monde. Dans chaque recette, vous pourrez imprimer en version PDF et découvrir la photo de la page manuscrite originale, pour celles et ceux qui n’ont pas l’un des rares exemplaires à la maison.

À ma connaissance, il n’existe que cinq copies papier de ce livre ; grâce à cette version numérique, c’est comme si nous en ajoutions une de plus, commune à toute la famille. Que vous soyez à la maison, chez des amis ou en camping, il suffira d’un téléphone ou d’une tablette pour retrouver les recettes de Maman.

J’espère que vous aurez plaisir à cuisiner ces recettes, à les partager avec vos enfants et petits‑enfants, et à y ajouter, pourquoi pas, vos propres notes et souvenirs.

N'hésitez pas à m'envoyer vos souvenirs à partager via le bouton "Partager un souvenir" ou si vous voulez envoyer une recette qui mériterait d'être ajouté, cliquez sur "Envoyer un commentaire/une suggestion". Je pourrai les mettres sur l'Application pour que tout le monde puisse en profiter.

Bernard
    """
)
# Bouton retour accueil
if st.button("🏠 Retour à l'accueil", key="retour_bas_preface"):
    st.switch_page("app.py")








