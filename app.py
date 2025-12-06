import streamlit as st

st.markdown(
    """
    <style>
    .hero-wrapper {
        position: relative;
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 0 18px rgba(0, 0, 0, 0.25);
        margin-bottom: 25px;
    }
    .hero-wrapper img {
        width: 100%;
        object-fit: cover;
    }
    .hero-title {
        position: absolute;
        top: 20px;
        left: 30px;
        right: 30px;
        text-align: center;
        color: white;
        font-size: 30px;
        font-weight: bold;
        text-shadow: 0 0 10px rgba(0,0,0,0.7);
    }
    .hero-menu {
        position: absolute;
        bottom: 10px;
        left: 50%;
        transform: translateX(-50%);
        background: rgba(255, 247, 236, 0.92);
        border-radius: 20px;
        padding: 10px 25px;
        display: flex;
        gap: 25px;
        flex-wrap: wrap;
        justify-content: center;
    }
    .hero-menu-item {
        font-size: 15px;
        color: #5e3b1f;
        font-weight: 500;
    }
    .hero-menu-item button {
        all: unset;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Bloc image + titre + options
st.markdown('<div class="hero-wrapper">', unsafe_allow_html=True)
st.image("grand_mere.png", use_container_width=True)
st.markdown(
    "<div class=\"hero-title\">Livre de Recettes d'Adrienne Tremblay</div>",
    unsafe_allow_html=True,
)

st.markdown('<div class="hero-menu">', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🔍 Recherche par titre", key="menu_titre"):
        st.switch_page("pages/1_Recherche_par_nom.py")

with col2:
    if st.button("📂 Par catégorie", key="menu_cat"):
        st.switch_page("pages/2_Recherche_par_categorie.py")

with col3:
    if st.button("🥕 Par ingrédients", key="menu_ing"):
        st.switch_page("pages/3_Recherche_par_ingredients.py")

with col4:
    if st.button("💐 Hommage / préface", key="menu_hommage"):
        st.switch_page("pages/0_HOMMAGE.py")

st.markdown("</div>", unsafe_allow_html=True)  # fin hero-menu
st.markdown("</div>", unsafe_allow_html=True)  # fin hero-wrapper
