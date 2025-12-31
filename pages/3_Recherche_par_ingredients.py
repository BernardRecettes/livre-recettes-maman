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

st.title("Recherche de Recettes par Ingrédient")

# --- RECHERCHE PAR INGREDIENT ---
recherche_ing = st.text_input("Rechercher un ingrédient :")
df_filtre = df_recettes.copy()

if recherche_ing:
    terme = sans_accents(recherche_ing)
    # normalisation texte des ingrédients
    df_ing_work = df_ingredients.copy()
    df_ing_work["ingredients_norm"] = df_ing_work["ingredients"].astype(str).apply(sans_accents)
    masque_ing = df_ing_work["ingredients_norm"].str.contains(terme, na=False)
    ids_trouves = df_ing_work.loc[masque_ing, "id_recette"].unique()
    # filtrage des recettes correspondant aux id_recette trouvés
    df_filtre = df_filtre[df_filtre["Clé"].isin(ids_trouves)]

# --- TABLEAU RESUME ---
colonnes_resume = ["Clé", "id_recette", "titre", "origine", "id_categorie"]
df_resume = df_filtre[colonnes_resume].copy()

st.write("Résultats trouvés :", df_resume.shape[0])

# **TABLEAU CLIQUABLE**
colonnes_affichees = ["id_recette","titre", "origine", "id_categorie"]
table_event = st.dataframe(
    df_resume[colonnes_affichees],
    use_container_width=True,
    selection_mode="single-row",
    on_select="rerun",
    key="table_recettes_ingredients"
)

# --- RECETTE SÉLECTIONNÉE ---
id_choisi = None
if 'table_recettes_ingredients' in st.session_state:
    selected_rows = st.session_state['table_recettes_ingredients']['selection']['rows']
    if selected_rows:
        selected_idx = list(selected_rows)[0]
        id_choisi = df_resume.iloc[selected_idx]['id_recette']

if df_resume.shape[0] > 0 and id_choisi:
    df_test = df_recettes[df_recettes["id_recette"].astype(str) == id_choisi]
    if df_test.shape[0] == 0:
        st.error("Aucune recette trouvée dans df_recettes pour cet id_recette.")
    else:
        rec = df_test.iloc[0]

        col_g, c
