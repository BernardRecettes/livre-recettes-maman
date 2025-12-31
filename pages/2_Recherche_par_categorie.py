import streamlit as st
import pandas as pd
import unicodedata
import os

if st.button("🏠 Retour à l'accueil"):
    st.switch_page("app.py")

def sans_accents(texte: str) -> str:
    if texte is None:
        return ""
    return "".join(
        c for c in unicodedata.normalize("NFD", str(texte))
        if unicodedata.category(c) != "Mn"
    ).lower()

fichier_excel = "Livre Blanc 2.06.xlsm"
nom_feuille_recettes = "recettes"
nom_feuille_ingredients = "ingredients"
nom_feuille_categories = "Categories"

# --- CHARGEMENT RECETTES ---
df_rec_brut = pd.read_excel(
    fichier_excel,
    sheet_name=nom_feuille_recettes,
    header=None,
    skiprows=1
)
df_recettes = df_rec_brut[1:].copy()
df_recettes.columns = df_rec_brut.iloc[0]
df_recettes = df_recettes.loc[:, ~df_recettes.columns.isna()]
df_recettes["id_recette"] = df_recettes["id_recette"].astype(str)

# --- CHARGEMENT INGREDIENTS ---
df_ing_brut = pd.read_excel(
    fichier_excel,
    sheet_name=nom_feuille_ingredients,
    header=0
)
df_ingredients = df_ing_brut[["id_recette", "ingredients"]].copy()
df_ingredients["id_recette"] = df_ingredients["id_recette"].astype(int)

# --- CHARGEMENT CATEGORIES ---
df_categories = pd.read_excel(
    fichier_excel,
    sheet_name=nom_feuille_categories,
    header=0
)
liste_categories = sorted(df_categories["Libelle"].dropna().unique())

st.title("Recherche de Recettes par Catégorie")

# --- RECHERCHE PAR CATEGORIE ---
df_filtre = df_recettes.copy()

categorie_choisie = st.selectbox(
    "Choisir une catégorie :",
    ["Toutes les catégories"] + list(liste_categories)
)

if categorie_choisie != "Toutes les catégories":
    df_filtre = df_filtre[
        df_filtre["id_categorie"]
        .astype(str)
        .str.contains(categorie_choisie, na=False)
    ]

# --- TABLEAU RESUME ---
colonnes_resume = ["Clé", "id_recette", "titre", "origine", "id_categorie"]
df_resume = df_filtre[colonnes_resume].copy()

st.write("Résultats trouvés :", df_resume.shape[0])

# **TABLEAU CLIQUABLE**
colonnes_affichees = ["id_recette","titre", "origine", "id_categorie"]
st.dataframe(
    df_resume[colonnes_affichees],
    use_container_width=True,
    selection_mode="single-row",
    on_select="rerun",
    key="table_recettes_categorie"
)

# --- RECETTE SÉLECTIONNÉE ---
id_choisi = None
if 'table_recettes_categorie' in st.session_state:
    selected_rows = st.session_state['table_recettes_categorie']['selection']['rows']
    if selected_rows:
        selected_idx = list(selected_rows)[0]
        id_choisi = df_resume.iloc[selected_idx]['id_recette']

if df_resume.shape[0] > 0 and id_choisi:
    df_test = df_recettes[df_recettes["id_recette"].astype(str) == id_choisi]
    if df_test.shape[0] == 0:
        st.error("Aucune recette trouvée dans df_recettes pour cet id_recette.")
    else:
        rec = df_test.iloc[0]

        col_g, col_d = st.columns([3, 1])
        
        with col_g:
            st.subheader(str(rec["titre"]))
            st.write("Origine :", rec["origine"])
            st.write("Catégorie(s) :", rec["id_categorie"])
        
        with col_d:
            st.markdown("**Temperature**")
            st.write(rec["temperature"])
            st.markdown("temps_cuisson")
            st.write(rec["temps_cuisson"])

        # Clé numérique pour retrouver les ingrédients
        cle_num = int(rec["Clé"])
        ing_recette = df_ingredients[df_ingredients["id_recette"] == cle_num]

        st.markdown("### Ingrédients")
        for i, ligne in ing_recette.iterrows():
            checked = st.checkbox(
                ligne["ingredients"],
                key=f"ing_{cle_num}_{i}"
            )

        st.markdown("### Instructions")
        st.write(rec["instructions"])

        if pd.notna(rec["note"]) and str(rec["note"]).strip() != "":
            st.markdown("### Note")
            st.write(rec["note"])

        # --- Recette manuscrite / Vidéo ✅ AJOUTÉ ---
        st.markdown("---")
        st.subheader("Recette originale manuscrite")

        id_recette_str = str(rec["id_recette"])
        image_path = os.path.join("images", f"{id_recette_str}.jpg")
        youtube_url = rec.get("youtube_url", "")

        # Vidéo Yxxx
        if id_recette_str.startswith("Y") and pd.notna(youtube_url) and str(youtube_url).strip() != "":
            st.markdown("### Vidéo de la recette")
            st.video(youtube_url)
        # Photo P/E
        elif os.path.exists(image_path):
            if st.button("📜 Voir la recette manuscrite", key=f"manuscrit_{id_recette_str}"):
                st.image(image_path, use_container_width=True)
        else:
            st.info("Aucune image manuscrite n'est disponible pour cette recette.")

        # --- Fiche PDF ---
        from utils_pdf import generer_fiche_recette_pdf

        st.markdown("---")
        st.subheader("📥 Télécharger la fiche")

        pdf_bytes = generer_fiche_recette_pdf(
            rec,
            ing_recette,
            id_recette_str,
            image_path if os.path.exists(image_path) else None,
        )

        st.download_button(
            label="📄 Télécharger en PDF",
            data=pdf_bytes,
            file_name=f"Recette_{id_recette_str}_{rec['titre']}.pdf",
            mime="application/pdf",
        )
else:
    if df_resume.shape[0] > 0:
        st.info("👆 **Cliquez sur une ligne du tableau pour voir la recette**")
    else:
        st.info("Aucune recette trouvée pour cette catégorie.")
