import streamlit as st

if st.button("🏠 Retour à l'accueil"):
    st.switch_page("app.py")

st.markdown(
    """
    <style>
    .souvenirs-container {
        background: #fff7ec;
        padding: 30px 40px;
        border-radius: 20px;
        box-shadow: 0 0 15px rgba(0,0,0,0.12);
        margin-top: 20px;
    }
    .souvenirs-title {
        font-size: 28px;
        font-weight: bold;
        color: #5e3b1f;
        margin-bottom: 10px;
    }
    .souvenirs-text {
        font-size: 16px;
        color: #4a3b2a;
        line-height: 1.6;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="souvenirs-container">', unsafe_allow_html=True)
st.markdown('<div class="souvenirs-title">Souvenirs et anecdotes</div>', unsafe_allow_html=True)

st.markdown(
    """
<div class="souvenirs-text">
Ici, vous pourrez lire les souvenirs, anecdotes et histoires que la famille a partagés
par courriel à propos d’Adrienne et de sa cuisine.

N’hésitez pas à nous en envoyer pour les partager avec tout le monde.
</div>
    """,
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)
