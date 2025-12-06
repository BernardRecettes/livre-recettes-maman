import streamlit as st
import pandas as pd
import unicodedata


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

nom_feuille_ingredients = "ingredients"  # nom exact de l'onglet

df_ing_brut = pd.read_excel(
    fichier_excel,
    sheet_name=nom_feuille_ingredients,
    header=0  # id_cle, id_recette, ingredients
)

df_ingredients = df_ing_brut[["id_recette", "ingredients"]].copy()
df_ingredients["id_recette"] = df_ingredients["id_recette"].astype(int)


# id_recette en texte pour la sélection
df_recettes["id_recette"] = df_recettes["id_recette"].astype(str)

st.title("Livre de Recettes de Maman")

# --- RECHERCHE ---
recherche_titre = st.text_input("Rechercher une recette par titre :")

df_filtre = df_recettes.copy()
if recherche_titre:
    recherche_norm = sans_accents(recherche_titre)
    masque = (
        df_filtre["TitreSansAccents"]
        .astype(str)
        .apply(sans_accents)
        .str.contains(recherche_norm, na=False)
    )
    df_filtre = df_filtre[masque]

# --- TABLEAU RESUME ---
# Colonnes utilisées en interne
colonnes_resume = ["Clé", "id_recette", "titre", "origine", "id_categorie"]
df_resume = df_filtre[colonnes_resume].copy()

st.write("Résultats trouvés :", df_resume.shape[0])

# Tableau affiché à l'utilisateur (sans Clé)
colonnes_affichees = ["id_recette","titre", "origine", "id_categorie"]
st.dataframe(df_resume[colonnes_affichees], use_container_width=True)


# --- SÉLECTION RECETTE ---
liste_ids = df_resume["id_recette"].astype(str).dropna().unique()
id_choisi = st.selectbox("Choisir une recette à afficher (id_recette) :", liste_ids)

if id_choisi:
    df_test = df_recettes[df_recettes["id_recette"].astype(str) == id_choisi]

    if df_test.shape[0] == 0:
        st.error("Aucune recette trouvée dans df_recettes pour cet id_recette.")
    else:
        rec = df_test.iloc[0]

        col_g, col_d = st.columns([3, 1])

with col_g:
    st.subheader(str(rec["titre"]))
    st.write("Origine :", rec["origine"])
    st.write("Catégorie :", rec["id_categorie"])

with col_d:
    st.markdown("**Temperature**")
    st.write(rec["temperature"])
    st.markdown("temps_cuisson")
    st.write(rec["temps_cuisson"])

# Clé numérique de la recette choisie
cle_num = int(rec["Clé"])

# Ingrédients correspondant à cette clé
ing_recette = df_ingredients[df_ingredients["id_recette"] == cle_num]

#st.markdown("### Ingrédients")
#st.dataframe(
#    ing_recette[["ingredients"]],
#    use_container_width=True,
#    hide_index=True
#)

st.markdown("### Ingrédients")
for i, ligne in ing_recette.iterrows():
    checked = st.checkbox(ligne["ingredients"], key=f"ing_{cle_num}_{i}")
    # Optionnel : faire quelque chose avec 'checked'

st.markdown("### Instructions")
st.write(rec["instructions"])
if pd.notna(rec["note"]) and str(rec["note"]).strip() != "":
    st.markdown("### Note")
    st.write(rec["note"])
import os  # si ce n'est pas déjà en haut du fichier
    # --- Recette manuscrite ---
    #import os  # à mettre en haut du fichier si tu préfères

st.markdown("---")
st.subheader("Recette originale manuscrite")

id_recette_str = str(rec["id_recette"])
image_path = os.path.join("images", f"{id_recette_str}.jpg")  # ou .png

if os.path.exists(image_path):
    if st.button("📜 Voir la recette manuscrite"):
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


st.markdown("---")

#id_recette_str = str(rec["id_recette"])
#image_path = os.path.join("images", f"{id_recette_str}.jpg")  # ou .png selon tes fichiers







