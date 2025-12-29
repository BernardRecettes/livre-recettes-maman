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
st.markdown("---")

st.markdown(
    """
J'aimerais que vous preniez le temps de jeter un coup d'oeil à la recette P159-2. Vous reconnaitrez peut-être mon écriture mais, essayer de trouvez quelques chose de bizarre. Si vous le trouvez, mettez le dans les commentaires.

Bonne chance.

Bernard.   
""")
st.markdown("---")

st.markdown(
    """
  Je me souviens du temps où maman, le cœur grand ouvert,  
préparait ses fameuses galettes au Quick, celles qu’on aimait tant.  
Elle y versait tout son amour, et moi, du haut de mon enfance,  
je l’aidais dans ce grand rituel qui annonçait la fête.  

Un mois avant le jour J, déjà, la maison embaumait la vanille et la joie.  
Maman rangeait soigneusement ses trésors gourmands,  
les dissimulant aux goélands affamés que nous étions.  
Parfois même, elle montait jusqu’au grenier du garage,  
les scellant dans des sacs verts pour tromper nos regards.  

Mais nos nez curieux trahissaient sa ruse bienveillante.  
Et, bien malgré elle, nous finissions toujours par trouver le butin.  
Ravis de notre chapardage, nous croquions les galettes encore glacées,  
comme si chaque bouchée volée portait le goût du bonheur défendu.   
  
Bernard.   
""")
st.markdown("---")

st.markdown(
    """
    Salut Bernard,
J'ai pris quelques minutes pour regarder ton travail, car on parle réellement ici d'un travail exceptionnel, le travail de Moine qu'Isabelle a fait pour nous fournir une copie papier de ce livre, ne sera jamais oublié, le mien est dans ma cuisine toujours à porter de main et m'en sert très souvent, ma copie fait déjà partie des choses que Ma Fille héritera, non, tu portes cet héritage à un autre niveau, Maman en serait sûrement fière, Papa aussi car il disait a qui voulait l'entendre qu'Adrienne faisait la meilleure cuisine, surtout la tourtière, il faut pas oublier que Papa qui ne faisait que des œufs, une fois Maman partie il s'est servi de ce livre pour faire ses premières "beans" et elles étaient très bonnes, et maintenant qu'il devient numérique, un jour peut-être, quelqu'un, étranger à notre Famille tombera dessus, par accident, et nourrira sa Famille avec les recettes de Maman... Ce serait une belle continuité, merci 
André.
""")
st.markdown("---")

