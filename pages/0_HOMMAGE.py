import streamlit as st

if st.button("🏠 Retour à l'accueil"):
    st.switch_page("app.py")

# Affichage de la photo au-dessus du texte
st.image("maman.jpg", use_container_width=False, width=300)


st.markdown(
    """
    <style>
    .hommage-container {
        background: #fbe9e7;
        padding: 40px 60px;
        border-radius: 20px;
        box-shadow: 0 0 15px rgba(0,0,0,0.08);
        font-family: "Brush Script MT", "Blackadder ITC", cursive;
        font-size: 24px;
        line-height: 1.6;
        color: #4a2c2a;
        white-space: pre-wrap;
    }
    .hommage-title {
        text-align: center;
        font-size: 34px;
        margin-bottom: 20px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="hommage-container">
  <div class="hommage-title">Hommage à Maman</div>

Chère maman,

J’aimerais aujourd’hui honorer ta mémoire et exprimer à quel point ta force discrète et ton amour immense ont guidé ma vie.

Tu as été une mère aimante : même si les mots étaient parfois rares, tes gestes étaient remplis de douceur et de réconfort. Ta passion pour la cuisine, que tu as partagée si souvent, était un langage secret entre nous, une manière unique de me dire : « Je t’aime ».

Patiente avec tes cinq enfants, tu savais être rigide lorsqu’il le fallait, afin de nous apprendre la discipline et la vie. Mais ta tendresse reprenait toujours le dessus, surtout lorsque la maison retrouvait le calme et que ta fratrie était rassemblée.

Malgré des circonstances difficiles et un budget serré, tu réussissais chaque jour la prouesse de nous nourrir, de nous habiller convenablement et de veiller à ce que rien ne nous manque à l’école.

Tu as donné sans compter, porté nos peines et nos joies, partagé nos rires et calmé nos haines. Ta générosité, ton courage et ton travail inlassable sont gravés en moi, et je te remercie pour ce legs précieux.

Aujourd’hui, je prends la plume pour te dire simplement merci, maman. Ton amour, ta force et ta bonté continuent de m’accompagner chaque jour. Merci pour tout ce que tu as été et tout ce que tu m’as transmis.

En partageant tes recettes, je souhaite transmettre, à mon tour, toute la générosité, la créativité et l’attention que tu déployais chaque jour pour nous réunir autour de la table.

Ce projet qui m’habite, c’est la preuve de ta présence, toujours vivante dans nos mémoires et dans nos traditions, au fil des générations.

Merci maman, pour tout ce que tu as fait, pour tout ce que tu continues de représenter dans nos vies.

Ton fils qui t’aime,
Bernard
</div>
    """,
    unsafe_allow_html=True,
)
