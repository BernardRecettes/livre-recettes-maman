import streamlit as st

# --- Photo en haut de la page ---
st.image("grand_mere.png", use_container_width=False, width=350)

# --- Style général de la page d'accueil ---
st.markdown(
    """
    <style>
    .accueil-container {
        background: #fff7ec;
        padding: 30px 40px;
        border-radius: 20px;
        box-shadow: 0 0 18px rgba(0, 0, 0, 0.08);
    }
    .accueil-titre {
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        color: #5e3b1f;
        margin-bottom: 5px;
    }
    .accueil-sous-titre {
        text-align: center;
        font-size: 18px;
        color: #7b5a3a;
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="accueil-container">', unsafe_allow_html=True)
st.markdown('<div class="accueil-titre">Livre de Recettes d\'Adrienne Tremblay</div>', unsafe_allow_html=True)
st.markdown('<div class="accueil-sous-titre">Choisissez une façon de découvrir les recettes de Maman :</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/1_Recherche_par_nom.py", label="🔍 Recherche par titre", icon="🔎")
    st.page_link("pages/2_Recherche_par_categorie.py", label="📂 Recherche par catégorie")
    st.page_link("pages/3_Recherche_par_ingredients.py", label="🥕 Recherche par ingrédients")

with col2:
    st.page_link("pages/0_HOMMAGE.py", label="💐 Page Hommage")
    st.page_link("pages/5_Preface.py", label="📖 Préface")

st.markdown("</div>", unsafe_allow_html=True)
