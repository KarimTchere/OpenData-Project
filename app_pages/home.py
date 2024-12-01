import streamlit as st

def display():

    st.markdown(
    f"""
    <div style='text-align: center; 
                background-image: url("https://www.studycdn.space/sites/default/files/styles/hero_article_big/public/2023-11/universite-paul-valery-montpellier-3.jpg.webp?itok=QBtMZBmZ");
                background-size: cover; 
                padding: 30px; 
                border-radius: 10px;'>
        <div style='background-color: rgba(0, 0, 0, 0.5); padding: 20px; border-radius: 10px;'>
            <h1 style='color: white;'>🎓 MIASHS - Explorez, Analysez, Prévoyez</h1>
            <p style='font-size: 18px; color: #EDEDED;'>Statistiques sur les diplômés | Modèle de prédiction | Recherche d'emploi simplifiée</p>
        </div>
    </div>
    """, unsafe_allow_html=True
)



    st.markdown("---")

    # Objectifs de l'application
    st.markdown("""## <h3 style="color: #4C72B0; margin-top: -60px; margin-bottom: 20px;">🎯 Objectifs de l'Application</h3>""", unsafe_allow_html=True)
    st.markdown(
        """
        Cette application vise à offrir une expérience interactive dans l'exploration des parcours professionnels des anciens diplômés de la filière Miashs de l'Université Paul Valery Montpellier 3.       """, unsafe_allow_html=True
    )

    st.markdown("---")

    # Présentation des fonctionnalités principales
    st.markdown("""### <h3 style="color: #4C72B0; margin-bottom: 20px;">🛠️ Fonctionnalités Principales</h3>""", unsafe_allow_html=True)

    # Structure en colonnes
    col1, col2, col3 = st.columns(3)

    # Première fonctionnalité : Dashboard
    with col1:
        st.markdown(
            """
            <div style="background-color: #f5f5f5; padding: 20px; border-radius: 8px; 
                        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); margin-bottom: 20px;">
                <h4 style="text-align: center; color: #4C72B0;">📊 Dashboard</h4>
                <p style="text-align: center;">Explorez les parcours des diplômés avec des graphiques et des statistiques clés.</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Deuxième fonctionnalité : Prédictions
    with col2:
        st.markdown(
            """
            <div style="background-color: #f5f5f5; padding: 20px; border-radius: 8px; 
                        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); margin-bottom: 20px;">
                <h4 style="text-align: center; color: #4C72B0;">🔮 Prédictions</h4>
                <p style="text-align: center;">Obtenez des prévisions sur le métier futur d'un étudiant sur la base des informations sur son parcours d'alternance.</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Troisième fonctionnalité : Recherche d'emploi
    with col3:
        st.markdown(
            """
            <div style="background-color: #f5f5f5; padding: 20px; border-radius: 8px; 
                        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); margin-bottom: 20px;">
                <h4 style="text-align: center; color: #4C72B0;">🔍 Recherche d'emploi</h4>
                <p style="text-align: center;">Trouvez des opportunités d'emploi adaptées à votre profil grâce à l'API Jobless.</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    # Call-to-Action
    st.markdown("""### <h3 style="color: #4C72B0;">🚀 Prêt à explorer ?</h3>""", unsafe_allow_html=True)
    st.markdown(
        """
        Cliquez sur les boutons ci-contre pour commencer à explorer les fonctionnalités de l'application.
        """, unsafe_allow_html=True
    )


    st.markdown("---")
    st.markdown(
        """
        <footer style="text-align: center; font-size: small; color: #5D6D7E;">
        © 2024 Université Paul Valéry - MIASHS. Développé pour simplifier l'accès aux opportunités professionnelles.
        </footer>
        """, unsafe_allow_html=True
    )
