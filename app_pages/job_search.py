# app_pages/job_search.py

import streamlit as st
import requests

# Fonction pour récupérer les offres d'emploi via l'API Jooble
def get_jobs_by_criteria(keywords, location, limit=10):
    """
    Fonction pour récupérer les offres d'emploi à partir des critères donnés.
    """
    url = "https://jooble.org/api/e84bff5a-4b19-4930-b76a-1c0b791a3e7a"
    headers = {'Content-Type': 'application/json'}
    params = {
        "keywords": keywords,
        "location": location,
        "limit": limit
    }

    try:
        response = requests.post(url, json=params, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur lors de la récupération des données : {e}")
        return None

# Initialisation de l'état pour la pagination et les résultats
def initialize_session_state():
    if "results" not in st.session_state:
        st.session_state.results = []
    if "current_page" not in st.session_state:
        st.session_state.current_page = 1
    if "total_jobs" not in st.session_state:
        st.session_state.total_jobs = 0
    if "search_in_progress" not in st.session_state:
        st.session_state.search_in_progress = False

# Fonction pour afficher résultats
def display_results(jobs, start_index):
    for idx, job in enumerate(jobs, start=start_index):
        company = job.get("company", "Inconnu")
        card = f"""
            <div style="border: 2px solid #E6E6E6; padding: 20px; margin-bottom: 20px; border-radius: 12px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1); background-color: #ffffff; min-height: 220px;">
                <h3 style="color: #333; font-size: 1.2em; font-weight: bold;">{job['title']}</h3>
                <p style="color: #666; font-size: 1em;"><strong>Entreprise:</strong> {company}</p>
                <p style="color: #777; font-size: 0.9em;"><strong>Lieu:</strong> {job['location']}</p>
                <div style="margin-top: 10px; text-align: right;">
                    <a href="{job['link']}" target="_blank" style="background-color: #0073e6; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none; font-weight: bold;">Voir l'offre</a>
                </div>
            </div>
        """
        st.markdown(card, unsafe_allow_html=True)

# Fonction principale pour afficher la page de recherche d'emploi
def display_job_search_page():
    st.markdown(
    f"""
    <div style='text-align: center; 
                background-image: url("https://www.studycdn.space/sites/default/files/styles/hero_article_big/public/2023-11/universite-paul-valery-montpellier-3.jpg.webp?itok=QBtMZBmZ");
                background-size: cover; 
                padding: 30px; 
                border-radius: 10px;'>
        <div style='background-color: rgba(0, 0, 0, 0.5); padding: 20px; border-radius: 10px;'>
            <h1 style='color: white;'>🔍 Recherche d'Emploi</h1>
            <p style='font-size: 18px; color: #EDEDED;'>Simplifiez votre parcours vers votre prochaine opportunité professionnelle</p>
        </div>
    </div>
    """, unsafe_allow_html=True
)


    st.markdown("---")
    st.markdown("Faite votre recherche...")
    # Initialiser les variables de session
    initialize_session_state()

    # Disposition avec deux colonnes : une pour la recherche, l'autre pour les résultats
    col1, col2 = st.columns([1, 2])  


    # Colonne pour la recherche
    with col1:
        with st.form(key='search_form'):
            # Design de la recherche avec icônes
            job_type = st.text_input("Type de poste recherché", value=st.session_state.get('job_type', ''), placeholder="Ex : Data Scientist, Analyste, etc.", max_chars=50, label_visibility="collapsed")
            location = st.text_input("Localisation souhaitée", value=st.session_state.get('location', ''), placeholder="Ex : Paris, France", max_chars=50, label_visibility="collapsed")
            submit_button = st.form_submit_button(label="Rechercher", use_container_width=True)

        # Si l'utilisateur soumet le formulaire
        if submit_button:
            if not job_type or not location:
                st.error("Veuillez remplir les deux champs pour lancer la recherche.")
            else:
                # Mémoriser les valeurs dans la session pour les garder
                st.session_state.job_type = job_type
                st.session_state.location = location

                st.session_state.search_in_progress = True
                st.info("Recherche en cours, veuillez patienter...")

                # Appeler l'API et récupérer les résultats
                results = get_jobs_by_criteria(job_type, location, limit=50)
                if results and "jobs" in results:
                    st.session_state.results = results["jobs"]
                    st.session_state.total_jobs = len(st.session_state.results)
                    st.session_state.current_page = 1  # Réinitialiser la page
                    st.session_state.search_in_progress = False
                    # Affichage du message "Résultats trouvés"
                    st.success(f"Résultat trouvé : {st.session_state.total_jobs} offres.")
                else:
                    st.error("Aucune offre trouvée ou problème de connexion à l'API.")
                    st.session_state.results = []
                    st.session_state.total_jobs = 0
                    st.session_state.search_in_progress = False

    # Colonne pour afficher les résultats
    with col2:
        if st.session_state.results:
            # Affichage des résultats sous forme de cartes
            jobs_per_page = 9  # Affichage de 9 offres par page
            start_idx = (st.session_state.current_page - 1) * jobs_per_page
            end_idx = start_idx + jobs_per_page
            jobs_to_display = st.session_state.results[start_idx:end_idx]

            display_results(jobs_to_display, start_index=start_idx)

            # Pagination
            col3, col4 = st.columns([1, 1])
            with col3:
                if st.button("◀️ Page précédente") and st.session_state.current_page > 1:
                    st.session_state.current_page -= 1
            with col4:
                if st.button("Page suivante ▶️") and end_idx < st.session_state.total_jobs:
                    st.session_state.current_page += 1

# Fonction pour afficher les résultats sous forme de cartes (avec une taille réduite des cartes)
def display_results(jobs, start_index):
    for idx, job in enumerate(jobs, start=start_index):
        company = job.get("company", "Inconnu")
        card = f"""
            <div style="border: 1px solid #E6E6E6; padding: 15px; margin-bottom: 15px; border-radius: 10px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); background-color: #ffffff; min-height: 180px;">
                <h3 style="color: #333; font-size: 1.1em; font-weight: bold;">{job['title']}</h3>
                <p style="color: #666; font-size: 0.9em;"><strong>Entreprise:</strong> {company}</p>
                <p style="color: #777; font-size: 0.85em;"><strong>Lieu:</strong> {job['location']}</p>
                <div style="margin-top: 10px; text-align: right;">
                    <a href="{job['link']}" target="_blank" style="background-color: #0073e6; color: white; padding: 8px 18px; border-radius: 5px; text-decoration: none; font-weight: bold;">Voir l'offre</a>
                </div>
            </div>
        """
        st.markdown(card, unsafe_allow_html=True)


def display():
    display_job_search_page()
