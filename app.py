import streamlit as st
from app_pages.home import display as home_display
from app_pages.dashboard import display as dashboard_display
from app_pages.prediction import display as prediction_display
from app_pages.job_search import display as job_search_display

# Configuration de la page
st.set_page_config(
    page_title="Mon Site Streamlit",
    page_icon="🌟",
    layout="wide"
)

st.markdown(
    """
    <style>
    header {visibility: hidden;}
        /* Réduire l'espace au-dessus des onglets */
        .stTabs {
            margin-top: -100px !important; /* Décaler les onglets vers le haut */
        }
        /* Réduire l'espace général en haut de la page */
        .css-18e3th9 {
            padding-top: 0px !important; /* Enlèver l'espace en haut */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Création des onglets pour la navigation
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Accueil", "📊 Dashboard", "🔮 Prediction", "💼 JobSearch"])

with tab1:
    home_display()
with tab2:
    dashboard_display()
with tab3:
    prediction_display()
with tab4:
    job_search_display()
