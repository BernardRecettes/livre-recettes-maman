import streamlit as st

st.title("Livre de Recettes d'Adrienne Tremblay")

st.markdown("Bienvenue dans le livre de recettes de Maman. Choisissez une option :")

col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/1_Recherche_par_nom.py", label="🔍 Recherche par titre", icon="🔎")
    st.page_link("pages/2_Recherche_par_categorie.py", label="📂 Recherche par catégorie")
    st.page_link("pages/3_Recherche_par_ingredients.py", label="🥕 Recherche par ingrédients")

#with col2:
    #st.page_link("pages/0_HOMMAGE.py", label="💐 Page Hommage")
    #st.page_link("pages/5_Preface.py", label="📖 Préface")





