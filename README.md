# Dashboard Open Data - Analyse des parcours des Diplômés MIASHS de l'Université Paul Valery Montpellier 3

Ce projet permet de visualiser et d'analyser les données des diplômés de la filière MIASHS à l'aide de **Streamlit**. Le dashboard est conçu pour fournir des informations sur les parcours des diplômés, y compris leurs secteurs d'activité, types de structures, et d'autres indicateurs clés tels que la satisfaction par rapport aux salaires, et les premiers emplois après l'alternance.

### Fonctionnalités

- **Visualisation des données démographiques** : Répartition par genre et par année de diplôme.
- **Parcours des diplômés** : Visualisation des secteurs d'activité, types de structures actuelles, fonctions des diplômés, et satisfaction par rapport au salaire.
- **Filtres interactifs** : Filtrer les données par genre, année de diplôme et secteur d'activité.
- **Diagrammes interactifs** : Diagrammes à barres, camemberts, et diagrammes Sankey pour explorer les données de manière interactive.
- **Prédiction de futur métier** : Utilisation de modèle de prédiction (Random Forest) pour estimer les métiers futurs des diplômés en fonction de leurs parcours et de leurs compétences.
- **Recherche de jobs** : Intégration avec l'API Jobless pour permettre la recherche d'offres d'emploi adaptées aux profils des diplômés.

## Prérequis

Avant d'exécuter le projet, assurez-vous que vous avez installé les dépendances suivantes :

- Python 3.7 ou supérieur
- Streamlit
- Pandas
- Plotly
- Jobless API client
- Autres dépendances pour la prédiction (scikit-learn, TensorFlow).

Vous pouvez installer les dépendances en exécutant la commande suivante :

```bash
pip install streamlit pandas plotly jobless-api-client scikit-learn
