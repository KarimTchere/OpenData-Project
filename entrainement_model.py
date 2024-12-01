import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

# Charger les données à partir de data2022.csv
df = pd.read_csv('data/data2022.csv')

# Afficher les premières lignes pour voir la structure du fichier
print(df.head())

# Suppose que les colonnes pertinentes sont : 'Fonction Alternance', 'Secteur_Activite_Alternance', 'Type_Contrat_Alternance', 'Type_Structure_Alternance', et 'Fonction Actuelle'

# Créer un LabelEncoder pour chaque colonne catégorielle
label_encoder_fonction = LabelEncoder()
label_encoder_secteur = LabelEncoder()
label_encoder_contrat = LabelEncoder()
label_encoder_structure = LabelEncoder()

# Encoder les variables d'entrée
df['Fonction_Alternance'] = label_encoder_fonction.fit_transform(df['Fonction_Alternance'])
df['Secteur_Activite_Alternance'] = label_encoder_secteur.fit_transform(df['Secteur_Activite_Alternance'])
df['Type_Contrat_Alternance'] = label_encoder_contrat.fit_transform(df['Type_Contrat_Alternance'])
df['Type_Structure_Alternance'] = label_encoder_structure.fit_transform(df['Type_Structure_Alternance'])
df['Fonction_Actuelle'] = label_encoder_fonction.fit_transform(df['Fonction_Actuelle'])

# Séparer les variables explicatives (X) et la variable cible (y)
X = df[['Fonction_Alternance', 'Secteur_Activite_Alternance', 'Type_Contrat_Alternance', 'Type_Structure_Alternance']]
y = df['Fonction_Actuelle']

# Entraîner un modèle (RandomForestClassifier ici)
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# Sauvegarder le modèle et les encodeurs
with open('modele.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('encodeur_fonction.pkl', 'wb') as encoder_file:
    pickle.dump(label_encoder_fonction, encoder_file)

with open('encodeur_secteur.pkl', 'wb') as encoder_file:
    pickle.dump(label_encoder_secteur, encoder_file)

with open('encodeur_contrat.pkl', 'wb') as encoder_file:
    pickle.dump(label_encoder_contrat, encoder_file)

with open('encodeur_structure.pkl', 'wb') as encoder_file:
    pickle.dump(label_encoder_structure, encoder_file)

print("Entraînement terminé et modèles sauvegardés.")
