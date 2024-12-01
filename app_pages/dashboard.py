import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def display():
    # Bannière principale
    st.markdown(
    f"""
    <div style='text-align: center; 
                background-image: url("https://www.studycdn.space/sites/default/files/styles/hero_article_big/public/2023-11/universite-paul-valery-montpellier-3.jpg.webp?itok=QBtMZBmZ");
                background-size: cover; 
                padding: 30px; 
                border-radius: 10px;'>
        <div style='background-color: rgba(0, 0, 0, 0.5); padding: 20px; border-radius: 10px;'>
            <h1 style='color: white;'>🎓 Tableau de Bord MIASHS 🎓</h1>
            <p style='font-size: 18px; color: #EDEDED;'>Analyse complète des diplômés : parcours, insertion et compétences.</p>
        </div>
    </div>
    """, unsafe_allow_html=True
    )
    st.markdown("---")
    # Introduction
    st.markdown(
        """
        <p style='font-size: 16px;'>
            Ce tableau de bord vous permet d'explorer les données issues de l'enquête menée auprès des anciens diplômés
            de la filière MIASHS. Utilisez les filtres interactifs pour personnaliser votre exploration des résultats.
        </p>
        """, unsafe_allow_html=True
    )

    # Chargement des données
    st.markdown("### 🔄 Charger les données")
    uploaded_file = st.file_uploader("Chargez votre fichier CSV contenant les données des diplômés", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("✅ Fichier chargé avec succès!")
        st.write("### Aperçu des données")
        st.dataframe(df.head())
        build_dashboard(df)

def build_dashboard(df):
    # ---- Configuration des filtres ----
    st.sidebar.header("Filtres interactifs")
    genre_filter = st.sidebar.multiselect("Filtrer par genre :", options=df['Genre'].unique(), default=df['Genre'].unique())
    annee_filter = st.sidebar.multiselect("Filtrer par année de diplôme :", options=df['Annee_Diplome_MIASHS'].unique(), default=df['Annee_Diplome_MIASHS'].unique())
    secteur_filter = st.sidebar.multiselect("Filtrer par secteur d'activité actuel :", options=df['Secteur_Activite_Actuelle'].unique(), default=df['Secteur_Activite_Actuelle'].unique())

    filtered_data = df[(
        df['Genre'].isin(genre_filter)) &
        (df['Annee_Diplome_MIASHS'].isin(annee_filter)) &
        (df['Secteur_Activite_Actuelle'].isin(secteur_filter))
    ]

    st.write(f"### Données filtrées ({filtered_data.shape[0]} répondants)")
    st.dataframe(filtered_data)

    # ---- Structure du Dashboard ----

    # 1. Répartition démographique
    st.write("---")
    col1, col2 = st.columns(2)
    
    with col1:
        # Graphique en anneau pour la répartition des genres
        fig_genre = px.pie(
            filtered_data, 
            names='Genre', 
            title="Répartition des genres",
            color='Genre',
            color_discrete_sequence=px.colors.qualitative.Set2,
            hole=0.4 
        )
        st.plotly_chart(fig_genre)

    with col2:

    # 2. Répartition des diplômés par année - Diagramme en camembert
        fig_annee_camembert = px.pie(
            filtered_data, 
            names='Annee_Diplome_MIASHS', 
            title="Répartition des diplômés par année de diplôme",
            color='Annee_Diplome_MIASHS', 
            color_discrete_sequence=px.colors.qualitative.Set1,  
            hole=0.3  
        )
        st.plotly_chart(fig_annee_camembert)


    # 3. Premiers emplois après l'alternance
    st.write("## Premiers emplois après l'alternance")
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        fig_fonction_premier = px.bar(
            filtered_data,
            x='Fonction_Premier_Emploi',
            color='Genre',
            title="Premières fonctions",
            labels={'Fonction_Premier_Emploi': 'Fonction'},
            color_discrete_sequence=px.colors.qualitative.Set2,
            barmode='group',
            text_auto=True
        )
        st.plotly_chart(fig_fonction_premier)

    with col2:
        fig_salaire_premier = px.box(
            filtered_data,
            y='Satisfaction_Salaire_1er_Emploi',
            title="Satisfaction du salaire (premier emploi)",
            points="all",
            color='Genre',
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        st.plotly_chart(fig_salaire_premier)

    # 4. Situation actuelle des diplômés
    st.write("## Situation actuelle")
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        fig_secteur_actuel = px.bar(
            filtered_data,
            x='Secteur_Activite_Actuelle',
            color='Genre',
            title="Secteurs d'activité actuels",
            color_discrete_sequence=px.colors.qualitative.Set1,
            barmode='group',
            text_auto=True
        )
        st.plotly_chart(fig_secteur_actuel)

    with col2:
        fig_structure_actuelle = px.bar(
            filtered_data,
            x='Type_Structure_Actuelle',
            color='Genre',
            title="Types de structures actuelles",
            color_discrete_sequence=px.colors.qualitative.Set1,
            barmode='group',
            text_auto=True
        )
        st.plotly_chart(fig_structure_actuelle)

    # --- Création du Diagramme Sankey ---
    st.write("## Parcours des diplômés")
    st.write("---")

    # Agrégations par secteurs, entreprises, fonctions et types de contrat
    df_counts = filtered_data.groupby(
        ['Secteur_Activite_Actuelle', 'Nom_Entreprise_Actuelle', 'Fonction_Actuelle', 'Type_Contrat_Actuel']
    ).size().reset_index(name='Nombre_Diplomes')

    # Créer les labels et mappage des indices
    labels = pd.concat([df_counts['Secteur_Activite_Actuelle'], 
                        df_counts['Nom_Entreprise_Actuelle'], 
                        df_counts['Fonction_Actuelle'], 
                        df_counts['Type_Contrat_Actuel']]).unique()

    label_to_index = {label: i for i, label in enumerate(labels)}

    # Créer les sources, cibles, valeurs et hover_texts
    sources = []
    targets = []
    values = []
    hover_texts = []

    total_diplomes = df_counts['Nombre_Diplomes'].sum()

    # Construire les liens entre secteurs, entreprises, fonctions et types de contrat
    for _, row in df_counts.iterrows():
        secteur_idx = label_to_index[row['Secteur_Activite_Actuelle']]
        entreprise_idx = label_to_index[row['Nom_Entreprise_Actuelle']]
        fonction_idx = label_to_index[row['Fonction_Actuelle']]
        contrat_idx = label_to_index[row['Type_Contrat_Actuel']]

        # Calcul des pourcentages
        percentage = (row['Nombre_Diplomes'] / total_diplomes) * 100
        percentage_text = f"{percentage:.2f}%"

        # Ajouter les liens Secteur -> Entreprise
        sources.append(secteur_idx)
        targets.append(entreprise_idx)
        values.append(row['Nombre_Diplomes'])
        hover_texts.append(f"{row['Nombre_Diplomes']} diplômés ({percentage_text})")

        # Ajouter les liens Entreprise -> Fonction
        sources.append(entreprise_idx)
        targets.append(fonction_idx)
        values.append(row['Nombre_Diplomes'])
        hover_texts.append(f"{row['Nombre_Diplomes']} diplômés ({percentage_text})")

        # Ajouter les liens Fonction -> Type de Contrat
        sources.append(fonction_idx)
        targets.append(contrat_idx)
        values.append(row['Nombre_Diplomes'])
        hover_texts.append(f"{row['Nombre_Diplomes']} diplômés ({percentage_text})")

    # Créer le graphique Sankey
    fig_sankey = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,  
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels,
        color=['#2c7bb6' if 'Fonction' in label else '#abd9e9' if 'Secteur' in label else '#fdae61' if 'Type_Contrat' in label else '#e31a1c' for label in labels],
        x=[0.1 if 'Secteur' in label else 0.3 if 'Entreprise' in label else 0.5 if 'Fonction' in label else 0.7 for label in labels],  # Position des nœuds
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values,
        color="rgba(0, 100, 200, 0.4)",
        hovertemplate="%{source} → %{target}: %{value} diplômés <br> (%{customdata})",  
        customdata=hover_texts,
    )
    )])

    fig_sankey.update_layout(
    font=dict(family='Verdana, sans-serif', size=12, color='white'),
    plot_bgcolor='black',  
    paper_bgcolor='black',
    margin=dict(l=10, r=10, t=10, b=10),
    height=700,  
    hovermode="closest",  
    showlegend=False 
    )


    # Affichage du graphique
    st.plotly_chart(fig_sankey)
