#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 10:21:17 2018

@author: marin
On effectue la partie machine learning ici.
"""

# Test de la prédiction d'une probabilité

from pygame.locals import *
from sklearn.cross_validation import train_test_split
from sklearn.metrics import roc_auc_score  # Métrique pour unbalanced data set
from sklearn.metrics import classification_report

# On utilise l'algorithme des K-means
from sklearn.neighbors import KNeighborsClassifier
from sklearn.utils import resample
from src.fonctions import *  # importe les diverses fonctions

# import os
# os.chdir("/home/marin/Bureau/Generation Machine Learning/Debut Projet/Pygame")


# On charge le profil de l'utilisateur.
df_user = pd.read_excel(profil_user, header=None)
user_taste = list(df_user.values)[
    0
]  # On charge le array contenant le profil de l'utilisateur

# Ajout de la colonne 0 pour les faux profils
fake = pd.read_csv("../base_de_donnees/fake_simulation_profil.csv", sep=",", header=0)
type = [0] * fake.shape[0]
fake["Type"] = type

# Ajout de la colonne 1 pour les vrais profils
true = pd.read_csv(
    "../base_de_donnees/simulation_profil_coherent.csv", sep=",", header=0
)
type = [1] * true.shape[0]
true["Type"] = type

# Fusion des deux data frames
frames = [fake, true]
df = pd.concat(frames)

# remplacement des valeurs
df["Couleur"].replace(
    to_replace=["Rouge", "Vert", "Violet", "Bleu", "Noir"],
    value=[1, 2, 3, 4, 5],
    inplace=True,
)
df["Film"].replace(
    to_replace=[
        "Actions",
        "Classiques",
        "Horreur",
        "Dessins Animes",
        "Navets",
        "Classiques Ancien",
    ],
    value=[1, 2, 3, 4, 5, 6],
    inplace=True,
)
df["People"].replace(
    to_replace=["People Jeunes", "People Anciens", "Inconnus"],
    value=[1, 2, 3],
    inplace=True,
)
df["Age"].replace(
    to_replace=["Adulte", "Senior", "Jeune"], value=[1, 2, 3], inplace=True
)

# Enlever la colonne du sexe et de l'âge qui ne sert pas vraiment ici.
df = df.drop("Sexe", 1)
df = df.drop("Age", 1)


# On va augmenter la proportion de la classe minoritaire

# On sépare les classes minoritaires et majoritaires
df_majority = df[df.Type == 1]
df_minority = df[df.Type == 0]

# On va upsampler la classe minoritaire de manière à obtenir le même
# nombre que dans la classe majoritaire

df_minority_upsampled = df_minority

for i in range(4):
    df_intermed = resample(
        df_minority,
        replace=True,  # sample with replacement
        n_samples=100,  # to match majority class
        random_state=123,
    )  # reproducible results
    df_minority_upsampled = pd.concat([df_minority_upsampled, df_intermed])

# Combine majority class with upsampled minority class
df = pd.concat([df_majority, df_minority_upsampled])

# Gestion de l'aléatoire du modèle
np.random.seed(0)

# On mélange le Dataframe
df = df.sample(frac=1).reset_index(drop=True)

# On divise en un train et un test set:

X = df.iloc[:, 0:3].values  # Liste des X
y = df.iloc[:, 3].values  # Liste Y
# train test split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)


classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)

# On effectue alors la prédiction sur le jeu de données test
y_pred = classifier.predict(X_test)
y_proba = classifier.predict_proba(X_test)
# On évalue l'algorithme

# Matrice de Confusion
print(
    pd.crosstab(y_test, y_pred, rownames=["True"], colnames=["Predicted"], margins=True)
)

# Donne des indicateurs de précision.
# On cherche à ce que la précision de la prédiction des 0 soit la plus élevée
print(classification_report(y_test, y_pred))

print(roc_auc_score(y_test, y_pred))

# On crée également un modèle avec des random forest pour comparer:
"""
# Import the model we are using
from sklearn.ensemble import RandomForestRegressor
# Instantiate model with 1000 decision trees
rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
# Train the model on training data
rf.fit(X_train, y_train)

# Use the forest's predict method on the test data
y_predictions = np.round(rf.predict(X_test))

#Matrice de Confusion
print(pd.crosstab(y_test, y_predictions, rownames=['True'],
                  colnames=['Predicted'], margins=True))

#Donne des indicateurs de précision. 
#On cherche à ce que la précision de la prédiction des 0 soit la plus élevée
print(classification_report(y_test, y_predictions))

print( roc_auc_score(y_test, y_predictions))
"""
# Le modèle des KNN donne de meilleurs résultats, c'est celui là
# qu'on conserve

# On sauvegarde le modèle

filename = "model_ml/KNN-model.sav"
pickle.dump(classifier, open(filename, "wb"))

print(classifier.predict(np.array([list(X_test[12, :])])))
a = classifier.predict_proba(np.array([list(X_test[12, :])]))
