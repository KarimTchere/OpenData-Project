import streamlit as st
import pickle
import pandas as pd


# Charger le modèle et les encodeurs sauvegardés
with open('modele.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('encodeur_fonction.pkl', 'rb') as encoder_file:
    label_encoder_fonction = pickle.load(encoder_file)

with open('encodeur_secteur.pkl', 'rb') as encoder_file:
    label_encoder_secteur = pickle.load(encoder_file)

with open('encodeur_contrat.pkl', 'rb') as encoder_file:
    label_encoder_contrat = pickle.load(encoder_file)

with open('encodeur_structure.pkl', 'rb') as encoder_file:
    label_encoder_structure = pickle.load(encoder_file)

# Charger les données pour obtenir les valeurs uniques
data_path = 'data/data2022.csv'  # Chemin vers fichier de données
data = pd.read_csv(data_path)

# Extraire les valeurs uniques des colonnes d'alternance
unique_fonctions = data['Fonction_Alternance'].dropna().unique().tolist()
unique_secteurs = data['Secteur_Activite_Alternance'].dropna().unique().tolist()
unique_contrats = data['Type_Contrat_Alternance'].dropna().unique().tolist()
unique_structures = data['Type_Structure_Alternance'].dropna().unique().tolist()

# Fonction pour réaliser la prédiction
def predict_function(fonction_alternance, secteur_activite, type_contrat, type_structure):
    # Créer un DataFrame avec les entrées de l'utilisateur
    data = {
        'Fonction_Alternance': [fonction_alternance],
        'Secteur_Activite_Alternance': [secteur_activite],
        'Type_Contrat_Alternance': [type_contrat],
        'Type_Structure_Alternance': [type_structure]
    }
    df_input = pd.DataFrame(data)

    # Encoder les variables d'entrée
    try:
        df_input['Fonction_Alternance'] = label_encoder_fonction.transform(df_input['Fonction_Alternance'])
    except ValueError:
        df_input['Fonction_Alternance'] = -1  
    try:
        df_input['Secteur_Activite_Alternance'] = label_encoder_secteur.transform(df_input['Secteur_Activite_Alternance'])
    except ValueError:
        df_input['Secteur_Activite_Alternance'] = -1

    try:
        df_input['Type_Contrat_Alternance'] = label_encoder_contrat.transform(df_input['Type_Contrat_Alternance'])
    except ValueError:
        df_input['Type_Contrat_Alternance'] = -1

    try:
        df_input['Type_Structure_Alternance'] = label_encoder_structure.transform(df_input['Type_Structure_Alternance'])
    except ValueError:
        df_input['Type_Structure_Alternance'] = -1

    # Prédire la fonction actuelle
    prediction = model.predict(df_input)

    # Décoder la prédiction
    decoded_prediction = label_encoder_fonction.inverse_transform(prediction)
    return decoded_prediction[0]

# Page Streamlit
def display():
    # En-tête de la page

    st.markdown(
    f"""
    <div style='text-align: center; 
                background-image: url("https://www.studycdn.space/sites/default/files/styles/hero_article_big/public/2023-11/universite-paul-valery-montpellier-3.jpg.webp?itok=QBtMZBmZ");
                background-size: cover; 
                padding: 30px; 
                border-radius: 10px;'>
        <div style='background-color: rgba(0, 0, 0, 0.5); padding: 20px; border-radius: 10px;'>
            <h1 style='color: white;'>🔮 Prédiction de Fonction Actuelle</h1>
            <p style='font-size: 18px; color: #EDEDED;'>Ce modèle prédit la fonction future d'un étudiant en fonction de sa situation d'alternance.</p>
        </div>
    </div>
    """, unsafe_allow_html=True
)

    st.markdown("---")


    # Séparer les entrées utilisateur dans deux colonnes
    st.markdown("### 🧑‍💼 Renseignez votre situation en alternance :")
    col1, col2 = st.columns(2)

    with col1:
        fonction_alternance = st.selectbox("**Fonction en Alternance :**", unique_fonctions)
        secteur_activite = st.selectbox("**Secteur d'Activité :**", unique_secteurs)

    with col2:
        type_contrat = st.selectbox("**Type de Contrat :**", unique_contrats)
        type_structure = st.selectbox("**Type de Structure :**", unique_structures)

    # Section prédiction
    st.markdown("---")
    st.markdown("### 🎯 **Résultat de la Prédiction :**")

    # Bouton pour faire la prédiction
    if st.button("✨ Prédire la Fonction Actuelle"):
        result = predict_function(fonction_alternance, secteur_activite, type_contrat, type_structure)
        st.success(f"**La fonction actuelle prédite est : {result}**")
        st.balloons()

    # Pied de page
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<small style='text-align: center; display: block;'>© 2024 - Application de Prédiction</small>", unsafe_allow_html=True)

if __name__ == '__main__':
    display()
