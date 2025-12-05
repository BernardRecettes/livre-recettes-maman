import streamlit as st

# Bouton retour accueil
if st.button("🏠 Retour à l'accueil"):
    st.switch_page("app.py")

st.title("Préface")

st.markdown(
    """
Je vous présente aujourd’hui le livre de recettes d’Adrienne, ma chère maman.
Je l’ai patiemment transformé en version électronique afin que chacun de vous, dans la famille et même au-delà, puisse en profiter et le transmettre à son tour.
Je tiens d’abord à remercier de tout cœur Isabelle, qui a eu, il y a des années, la merveilleuse idée de prendre le livre original de maman pour en faire plusieurs copies. Elle a soigneusement glissé chaque page dans des pochettes protectrices, puis relié le tout dans des cartables. Imaginez le dévouement : cinq exemplaires complets, 240 pages chacun… Un vrai travail de moine qui a permis de préserver ce trésor familial.
Voilà près de vingt ans que maman nous a quittés. Et, trop souvent, j’ai eu l’impression que son livre s’effaçait doucement dans l’oubli. Aujourd’hui, avec l’omniprésence d’Internet, nous cherchons moins ces précieuses traces de nos racines. Pourtant, ce cahier, c’est un peu l’âme de notre mère.
C’est pour cette raison que j’ai entrepris de le retranscrire, afin que ses recettes, ses gestes et son amour puissent rester vivants et accessibles à tous, pour toujours.
Beaucoup d’entre vous le savent : en 2023, un grave accident de travail a bouleversé ma vie. Les séquelles me forcent désormais à une retraite anticipée. Je ne dis pas cela pour me plaindre, mais pour expliquer comment j’ai trouvé, au milieu de ce temps devenu plus vaste, un espace pour me reconstruire. J’ai toujours eu un faible pour l’informatique et les gadgets ; alors, lorsque j’ai retrouvé ce précieux cahier, je me suis lancé un défi : offrir à maman une seconde vie numérique.
Ce projet n’a rien eu de simple. Pour le mener à bien, j’ai dû apprivoiser Microsoft Access et découvrir comment transformer ce livre en une véritable base de données.
Mais, au-delà de la technique, c’est surtout un chemin de rédemption personnelle. Ce n’est pas un geste pour effacer les erreurs d’un passé plus sombre — je sais que certaines blessures demeurent. C’est plutôt une manière de me rapprocher de ce qu’il y a de meilleur en moi : ce désir de donner, de partager, de transmettre. J’ai toujours été, et resterai jusqu’à mon dernier souffle, quelqu’un d’altruiste. Peut-être que cela n’a pas toujours été facile à voir… mais c’est ce que je suis.
En recopiant ces recettes, j’ai souvent souri, parfois éclaté de rire.
Maman écrivait comme elle cuisinait : avec le cœur plus qu’avec la balance.
J’ai croisé des indications savoureuses comme « une quantité de margarine, grosse comme un œuf » ou « deux bonnes poignées de sel ». Des petits clins d’œil qui me rappelaient sa voix, son sourire, sa liberté.
    """
)
