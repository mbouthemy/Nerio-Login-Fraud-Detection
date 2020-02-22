#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 11:34:18 2018

@author: marin

Ce code contient toutes les fonctions nécesssaires à l'execution.
"""
import pickle
import random

import numpy as np
import pandas as pd

import pygame
from pygame.locals import *
from src.constantes import *  # importe les constantes


def initialiser_fenetre():
    # Affiche l'Icone de l'app
    icone = pygame.image.load(image_logo)
    pygame.display.set_icon(icone)
    # Titre
    pygame.display.set_caption(titre_fenetre)
    return 0


def details_graphiques(fenetre, fond_visuel):
    """
        Définit les détails graphiques comme la position du logo,
        la couleur de fond, le rectangle, etc...
    """
    # Charge le fond ainsi que le logo
    fond = pygame.image.load(fond_visuel).convert()
    fenetre.blit(fond, (0, 0))
    logo = pygame.image.load(image_logo).convert_alpha()
    fenetre.blit(logo, (COTE_GAUCHE, COTE_HAUT))
    # On dessine un rectangle
    pygame.draw.rect(fenetre, (250, 250, 250), (BORD_GAUCHE - 20, 80, 791, 567), 2)
    return 0


def ecriture_texte_ecran(fenetre, texte_a_afficher, hauteur_texte, taille_police):
    """
        Ecrit le texte pour l'utilisateur à l'écran.
    """
    # Charge la police
    california_font = pygame.font.SysFont("Sans", taille_police)

    message_surface = california_font.render(texte_a_afficher, True, (0, 0, 0))
    position_message = message_surface.get_rect()
    # Pose le texte au milieu
    position_message.center = (largeur_fenetre / 2, hauteur_texte)
    fenetre.blit(message_surface, position_message)
    return 0


def associe_couleur_pixel(couleur_pixel):
    """
    Prend en argument le tuple de couleur et associe
    la couleur correspondante.
    """
    if couleur_pixel[0] >= 100 and couleur_pixel[2] >= 100:
        return "violet"
    elif couleur_pixel[2] >= 200:
        return "bleu"
    elif couleur_pixel[0] >= 200:
        return "rouge"
    elif couleur_pixel[1] >= 200:
        return "vert"
    else:
        return "noir"


def categorie_associee(fichier_excel, element):
    """
    On donne en entrée le film ou le people.
    Et elle nous renvoie la catégorie qui lui est associé.
    """
    # On charge le dataframe
    df = pd.read_excel(fichier_excel, index_col="Categorie")

    # On trouve la catégorie associée en fonction du nom de la vignette
    categorie = df.loc[df["Chemin Image"] == element]
    return categorie.index.values[0]


def clic_bouton(pos_x, pos_y, x_rectangle, y_rectangle, largeur, longueur):
    """
        Vérifie si  l'on a bien cliqué dans le rectangle.
    """
    if x_rectangle <= pos_x and pos_x <= x_rectangle + largeur:
        # Si l'on a cliqué dans la zone d'abscisse correcte
        if y_rectangle <= pos_y and pos_y <= y_rectangle + longueur:
            # Et qu'il en est de même pour les ordonnées
            return True
    else:
        return False


def souris_dans_rectangles(pos_x, pos_y):
    """
    Vérifie si la position de la souris est bien dans une zone
    qui correspond à des vignettes.
    """
    # 60
    liste_position_rectangles = [
        [BORD_GAUCHE, 100],
        [200 + BORD_GAUCHE, 100],
        [400 + BORD_GAUCHE, 100],
        [600 + BORD_GAUCHE, 100],
        [BORD_GAUCHE, 400],
        [200 + BORD_GAUCHE, 400],
        [400 + BORD_GAUCHE, 400],
        [600 + BORD_GAUCHE, 400],
    ]
    index_position = 0
    dans_rectangle = 1
    for rect in liste_position_rectangles:
        if clic_bouton(
            pos_x, pos_y, rect[0], rect[1], taille_vignette[0], taille_vignette[1]
        ):
            # Si l'utilisateur clique dans la zone de la vignette
            dans_rectangle = 0
            index_position = liste_position_rectangles.index(rect)
    return (dans_rectangle, index_position)


def selection_aleatoire_vignettes_1(fichier_excel):
    """
        Ouvre le fichier excel et sélectionne 8 films
        parmi une sélection de plusieurs.
        Il s'agit de la première connexion, il n'y a pas de vignettes fausses.
    """
    # On importe le fichier excel
    df = pd.read_excel(fichier_excel, index_col="Categorie")

    if fichier_excel == fichier_film_path:
        # S'il s'agit du fichier avec les films
        # On groupe selon la catégorie de films,et on prend 2 film aléatoires de chaque
        group_df = df.groupby("Categorie").apply(lambda x: x.sample(2))

    else:
        # Sinon, il s'agit du fichier avec les people
        # On ne fait alors pas de mélange dans les catégories
        group_df = df

    # On enlève les films et people inconnus car il s'agit de la première connexion
    group_df = group_df.head(8)  # On prend les 8 premiers
    liste = group_df["Chemin Image"].tolist()  # On met sous forme de liste
    # On mélange alors la liste
    random.shuffle(liste)

    return liste


def selection_aleatoire_vignettes_2(fichier_excel):
    """
        Ouvre le fichier excel et sélectionne 8 vignettes
        parmi une sélection de plusieurs.
        Il s'agit de la seconde connexion, le pourcentage d'intrus est
        plus élevé.
    """
    # On importe le fichier excel
    df = pd.read_excel(fichier_excel, index_col="Categorie")
    df_user = pd.read_excel(profil_user, header=None)
    user = list(df_user.values)[
        0
    ]  # On charge le array contenant le profil de l'utilisateur

    if fichier_excel == fichier_film_path:
        # S'il s'agit du fichier avec les films

        film_user = user[1]  # on récupère le film de base
        # On prend la catégorie qui lui est associée
        categorie = categorie_associee(fichier_excel, film_user)

        # On crée la liste qui va recevoir les films
        liste = [film_user]

        # On ajoute alors un film différent de la même catégorie
        a = df.loc[categorie]
        a = a.loc[a["Chemin Image"] != film_user]
        liste.append(
            random.sample(a["Chemin Image"].tolist(), 1)[0]
        )  # il est choisit aléatoirement

        # On ajoute ensuite un film issu d'une autre catégorie
        v = df.loc[(df.index != categorie) & (df.index != "Navets")]
        liste.append(random.sample(v["Chemin Image"].tolist(), 1)[0])

        # on prend ensuite les navets
        liste_navets = df.loc["Navets"]["Chemin Image"].tolist()

        liste = liste + liste_navets  # on concatène alors

    else:
        # Sinon, il s'agit du fichier avec les people
        people_user = user[3]  # On récupère le people de base
        # On prend la catégorie associée
        categorie = categorie_associee(fichier_excel, people_user)

        # On crée la liste qui reçoit les people
        liste = [people_user]

        # On ajoute alors un people différent de la même catégorie
        a = df.loc[categorie]
        a = a.loc[a["Chemin Image"] != people_user]
        liste.append(
            random.sample(a["Chemin Image"].tolist(), 1)[0]
        )  # il est choisit aléatoirement

        # On ajoute ensuite un people issu de l'autre catégorie
        v = df.loc[(df.index != categorie) & (df.index != "Inconnus")]
        liste.append(random.sample(v["Chemin Image"].tolist(), 1)[0])

        # on prend ensuite les inconnus restants
        liste_inconnus = df.loc["Inconnus"]["Chemin Image"].tolist()
        liste_inconnus = random.sample(liste_inconnus, 5)  # On en prend 5

        # On concatène alors
        liste = liste + liste_inconnus

    # On mélange alors la liste
    random.shuffle(liste)

    return liste


def niveau_choix_couleur(fenetre, premiere_connexion=True):
    """
        Cette fonction initialise le niveau où on choisit les couleurs.
        Elle renvoie ensuite le rayon du cercle des couleurs.
    """
    # Charge l'image de fond et le logo
    fond = pygame.image.load(fond_blanc).convert()
    logo = pygame.image.load(image_logo).convert_alpha()
    fenetre.blit(fond, (0, 0))
    fenetre.blit(logo, (COTE_GAUCHE, COTE_HAUT))

    # On Affiche aussi un rectangle
    pygame.draw.rect(fenetre, (0, 0, 0), (BORD_GAUCHE - 20, 80, 791, 567), 2)

    # Ecriture message utilisateur:
    texte_a_afficher = "Pouvez-vous cliquer sur votre couleur préférée ?"
    ecriture_texte_ecran(fenetre, texte_a_afficher, 40, 24)

    # Chargement et collage du cercle de couleurs au centre de l'écran
    if premiere_connexion:
        cercle = pygame.image.load(cercle_1_path).convert()

    else:  # S'il s'agit de la seconde connexion
        cercle = pygame.image.load(cercle_2_path).convert()
    position_cercle = cercle.get_rect()
    position_cercle.center = (largeur_fenetre / 2, hauteur_fenetre / 2)
    # On affiche le cercle au milieu de la fenêtre
    fenetre.blit(cercle, position_cercle)

    rayon_cercle = position_cercle.size[0] / 2  # On obtient le rayon du cercle
    return rayon_cercle


def niveau_choix_vignettes(fenetre, liste_vignettes, film):
    """
        Crée le niveau correspondant au choix des vignettes.
        film == 1 signifie qu'on est dans le niveau des films, 
        autrement on est dans celui des people
    """
    # Charge le fond, rectangle et logo
    details_graphiques(fenetre, fond_visuel)

    # Ecriture message utilisateur:
    if film:
        texte_a_afficher = "Parmi ces films, lequel préférez-vous ?"

    else:
        texte_a_afficher = "Parmi ces célébrités, laquelle préférez-vous ?"
    ecriture_texte_ecran(fenetre, texte_a_afficher, 40, 24)

    """
    La boucle va parcourir la liste des 8 vignettes
    afin de les coller sur le fond de l'application.
    """

    vignettes = dict()  # Le dictionnaire qui stocke les vignettes
    for k in range(len(liste_vignettes)):
        vignette = liste_vignettes[k]  # prend la vignette
        # Charge l'image
        if film:  # S'il s'agit d'un film
            vignettes[k] = pygame.image.load(
                "images/film/" + vignette + ".jpeg"
            ).convert()
        else:
            vignettes[k] = pygame.image.load(
                "images/people/" + vignette + ".jpeg"
            ).convert()

        # La colle alors sur la position
        if k < 4:
            # On colle les 4 premières sur la ligne du haut
            fenetre.blit(vignettes[k], (200 * k + BORD_GAUCHE, 100))
        else:
            # Et les 4 suivantes sur la ligne du bas
            fenetre.blit(vignettes[k], (200 * (k - 4) + BORD_GAUCHE, 400))

    # Rafraîchissement de l'écran
    pygame.display.flip()

    return 0


def calcul_machine_learning(choix_individu_2):
    """
        On va calculer la probabilité à l'aide de notre modèle de machine learning
        préalablement entraîné. On lui passe les choix que l'individu a renseigné.
        Il s'agit d'un array = [film, couleur, people].
    """
    # On récupère la catégorie du film ainsi que celle du people.
    categorie_film = categorie_associee(fichier_film_path, choix_individu_2[0])
    categorie_people = categorie_associee(fichier_people_path, choix_individu_2[2])

    # Couleur, Film, People
    vecteur_choix_2 = [choix_individu_2[1], categorie_film, categorie_people]

    # On récupère également les choix rentrés par l'individu lors de la première connexion
    df_user = pd.read_excel(profil_user, header=None)
    vecteur_choix_1 = list(df_user.values)[
        0
    ]  # On charge le array contenant le profil de l'utilisateur

    # On transforme alors les categories en valeurs afin d'utiliser le machine learning
    vecteur_choix_num_2 = [DICTIONNAIRE.get(e, e) for e in vecteur_choix_2]
    vecteur_choix_num_1 = [DICTIONNAIRE.get(e, e) for e in vecteur_choix_1]

    # Si la couleur de première connexion est la même que lors de la deuxième
    # connexion, on augmente la probabilité que l'individu soit vrai
    if vecteur_choix_num_2[0] == vecteur_choix_num_1[1]:
        vecteur_choix_num_2[0] = 4

    # On charge le modèle de Machine Learning
    modele = pickle.load(open(MODELE_ML_PATH, "rb"))

    # Il calcule ensuite la probabilité d'être la bonne personne.
    probabilite_vrai_vecteur = modele.predict_proba(
        np.array([list(vecteur_choix_num_2)])
    )
    probabilite_vrai = probabilite_vrai_vecteur[0][1]
    print(probabilite_vrai)

    return probabilite_vrai
