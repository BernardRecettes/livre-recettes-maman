import streamlit as st

# CSS DESIGN CULINAIRE
st.markdown("""
<style>
/* FOND ET TYPOGRAPHIE */
.main {
    background: linear-gradient(135deg, #fff7ec 0%, #f5e8c7 100%);
    padding: 2rem;
}

/* TITRES RECETTES */
h1, h2, h3 {
    color: #8B4513 !important;
    font-family: 'Georgia', serif !important;
    text-shadow: 1px 1px 2px rgba(139,69,19,0.3);
}

/* TABLEAUX CLIQUABLES */
.stDataFrame > div > div > div > div {
    border-radius: 15px !important;
    box-shadow: 0 4px 12px rgba(139,69,19,0.15) !important;
}

/* LIGNES SURVOLÉES */
[data-row-hover] {
    background-color: #fff3e0 !important;
    transition: all 0.2s ease !important;
}

/* BOUTONS CULINAIRES */
.stButton > button {
    background: linear-gradient(45deg, #D2691E, #CD853F);
    color: white !important;
    border-radius: 25px !important;
    border: none !important;
    padding: 0.8rem 2rem !important;
    font-weight: bold !important;
    box-shadow: 0 4px 12px rgba(210,105,30,0.3) !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(210,105,30,0.4) !important;
}

/* CASES À COCHER INGRÉDIENTS */
.stCheckbox > label {
    font-size: 16px !important;
    color: #5D4037 !important;
    padding: 8px 12px !important;
    border-radius: 10px !important;
    background: rgba(255,248,220,0.6) !important;
    margin: 4px 0 !important;
}

/* INFOS ET ALERTES */
.stInfo, .stSuccess {
    background: rgba(144,238,144,0.2) !important;
    border-left: 5px solid #228B22 !important;
    border-radius: 10px !important;
}

/* BARRE DE RECHERCHE */
.stTextInput > div > div > input {
    border-radius: 25px !important;
    border: 2px solid #DAA520 !important;
    padding: 12px 20px !important;
    font-size: 16px !important;
}

/* SELECTBOX */
.stSelectbox > div > div > select {
    border-radius: 20px !important;
    border: 2px solid #DAA520 !important;
    padding: 12px !important;
}

/* IMAGES RECETTES */
img {
    border-radius: 20px !important;
    box-shadow: 0 8px 25px rgba(0,0,0,0.2) !important;
}

/* PDF DOWNLOAD */
.download-button {
    background: linear-gradient(45deg, #FF6B35, #F7931E) !important;
    font-size: 18px !important;
}
</style>
""", unsafe_allow_html=True)


st.markdown(
    """
    <style>
    .accueil-titre {
        text-align: center;
        font-size: 30px;
        font-weight: bold;
        color: #5e3b1f;
        margin-bottom: 10px;
    }
    .menu-bar {
        background: #fff7ec;
        border-radius: 20px;
        padding: 12px 20px;
        box-shadow: 0 0 12px rgba(0,0,0,0.15);
        text-align: center;
        margin-top: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='accueil-titre'>Livre de Recettes d'Adrienne Tremblay</div>", unsafe_allow_html=True)

# Image plein centre
st.image("grand_mere.png", use_container_width=False, width=700)


# Bandeau d’options sous l’image
st.markdown("<div class='menu-bar'>Choisissez une façon de découvrir les recettes de Maman :</div>", unsafe_allow_html=True)
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/1_Recherche_par_nom.py", label="🔍 Recherche par titre", icon="🔎")
    st.page_link("pages/2_Recherche_par_categorie.py", label="📂 Recherche par catégorie")
    st.page_link("pages/3_Recherche_par_ingredients.py", label="🥕 Recherche par ingrédients")
with col2:
    st.page_link("pages/0_HOMMAGE.py", label="💐 Page Hommage")
    st.page_link("pages/5_preface.py", label="📖 Préface")
    st.page_link("pages/6_souvenirs.py", label="📚 Souvenirs de famille")

st.markdown("---")

st.markdown("Pour partager un souvenir lié à Maman ou à sa cuisine :")
if st.button("💬 Partager un souvenir"):
    st.markdown(
        "[Si aucun courriel ne s'ouvre, cliquez ici]"
        "(mailto:livrerecetteadrienne@gmail.com"
        "?subject=Souvenir%20pour%20le%20Livre%20d%27Adrienne)",
        unsafe_allow_html=True,
    )

st.markdown("Pour commentaires, suggestions ou même une recette que vous voulez partager :")
if st.button("✉️ Envoyer un commentaire / une suggestion"):
    st.markdown(
        "[Si aucun courriel ne s'ouvre, cliquez ici]"
        "(mailto:livrerecetteadrienne@gmail.com"
        "?subject=Commentaires%20sur%20le%20Livre%20de%20Recettes)",
        unsafe_allow_html=True,
    )

























