import streamlit as st

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

col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/1_Recherche_par_nom.py", label="🔍 Recherche par titre", icon="🔎")
    st.page_link("pages/2_Recherche_par_categorie.py", label="📂 Recherche par catégorie")
    st.page_link("pages/3_Recherche_par_ingredients.py", label="🥕 Recherche par ingrédients")
with col2:
    
    st.page_link("pages/0_HOMMAGE.py", label="💐 Page Hommage")
    st.page_link("pages/5_preface.py", label="📖 Préface")
    st.markdown("---")
    st.markdown("Pour commentaires ou suggestions :")

if st.button("✉️ Envoyer un commentaire / une suggestion"):
    st.markdown(
        "[Si aucun courriel ne s'ouvre, cliquez ici]"
        "(mailto:livrerecetteadrienne@gmail.com"
        "?subject=Commentaires%20sur%20le%20Livre%20de%20Recettes)",
        unsafe_allow_html=True,
    )

st.markdown("Pour partager un souvenir lié à Maman ou à sa cuisine :")

if st.button("💬 Partager un souvenir"):
    st.markdown(
        "[Si aucun courriel ne s'ouvre, cliquez ici]"
        "(mailto:livrerecetteadrienne@gmail.com"
        "?subject=Souvenir%20pour%20le%20Livre%20d%27Adrienne)",
        unsafe_allow_html=True,
    )












