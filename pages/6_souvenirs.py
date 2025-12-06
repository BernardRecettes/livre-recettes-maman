import streamlit as st

if st.button("🏠 Retour à l'accueil"):
    st.switch_page("app.py")

st.title("Souvenirs et anecdotes")

st.markdown(
    """
Ici, vous pourrez lire les souvenirs, anecdotes et histoires que la famille a partagés par courriel à propos d’Adrienne et de sa cuisine.

N’hésitez pas à nous en envoyer pour les partager avec tout le monde. !!!
"""
)
