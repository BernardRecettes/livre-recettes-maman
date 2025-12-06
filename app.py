import streamlit as st

st.markdown(
    """
    <style>
    .hero-wrapper {
        position: relative;
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 0 18px rgba(0, 0, 0, 0.25);
        margin-bottom: 20px;
    }
    .hero-title {
        position: absolute;
        top: 15px;
        left: 0;
        right: 0;
        text-align: center;
        color: white;
        font-size: 30px;
        font-weight: bold;
        text-shadow: 0 0 10px rgba(0,0,0,0.7);
    }
    .menu-bar {
        background: #fff7ec;
        border-radius: 20px;
        padding: 10px 20px;
        box-shadow: 0 0 12px rgba(0,0,0,0.15);
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Image + titre dans l'image
st.markdown('<div class="hero-wrapper">', unsafe_allow_html=True)
st.image("grand_mere.png", use_container_width=True)
st.markdown(
    "<div class='hero-title'>Livre de Recettes d'Adrienne Tremblay</div>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# Bandeau avec les boutons SOUS l'image
st.markdown('<div class="menu-bar">Choisissez une façon de découvrir les recettes de Maman :</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/1_Recherche_par_nom.py", label="🔍 Recherche par titre", icon="🔎")
    st.page_link("pages/2_Recherche_par_categorie.py", label="📂 Recherche par catégorie")

with col2:
    st.page_link("pages/3_Recherche_par_ingredients.py", label="🥕 Recherche par ingrédients")
    st.page_link("pages/0_HOMMAGE.py", label="💐 Page Hommage / Préface")
