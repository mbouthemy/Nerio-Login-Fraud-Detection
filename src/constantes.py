#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 10:00:38 2018

@author: marin

Ce fichier va contenir toutes les constantes de l'application.
"""

# Paramètres de la fenêtre

largeur_fenetre = 1020
hauteur_fenetre = 720

# Paramètres position des images
BORD_GAUCHE = 134


# Personnalisation de la fenêtre
titre_fenetre = "Hacking Detection"
image_logo = "icones/logo.png"

# Position Logo
COTE_GAUCHE = largeur_fenetre - (110)
COTE_HAUT = 5

# Police écriture
police = "font/FreeSansBold.ttf"

# Fichier Excel avec la liste des vignettes
fichier_film_path = "../assets/fichiers/details_films.xls"
fichier_people_path = "../assets/fichiers/details_people.xls"

# Fond visuel
fond_visuel = "icones/fond_gris.jpeg"
fond_blanc = "icones/fond_blanc_uni.jpeg"

# Bouton continuer
BOUTON_SUIVANT = "icones/bouton_suivant.jpeg"

# Image du cercle des couleurs
cercle_1_path = "../assets/images/cercle_couleur/cercle_couleur_1.jpeg"
cercle_2_path = "../assets/images/cercle_couleur/cercle_couleur_2.jpeg"

# Image des feux tricolores
feu_rouge_path = "../assets/icones/feu_rouge.jpeg"
feu_vert_path = "../assets/icones/feu_vert.jpeg"
feu_orange_path = "../assets/icones/feu_orange.jpeg"

# Profil de l'utilisateur enregistré
profil_user = "profil_user/profil_user.xls"

# Equivalence categories - valeurs (on crée un dictionnaire)
LISTE_CATEGORIES = [
    "rouge",
    "vert",
    "violet",
    "bleu",
    "noir",
    "Action",
    "Classiques Anciens",
    "Horreur",
    "Dessins Animes",
    "Navets",
    "Classiques Ancien",
    "People Jeunes",
    "People Anciens",
    "Inconnus",
]
LISTE_VALEURS_ASSOCIEES = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3]
DICTIONNAIRE = dict(zip(LISTE_CATEGORIES, LISTE_VALEURS_ASSOCIEES))

# Charge le modèle de machine learning.
MODELE_ML_PATH = "model_ml/KNN-model.sav"

# Taille des vignettes
mulan = "images/film/mulan.jpeg"
from PIL import Image

vignette = Image.open(mulan)
taille_vignette = vignette.size
