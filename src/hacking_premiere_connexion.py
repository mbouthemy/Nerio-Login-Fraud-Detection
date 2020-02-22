#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 13:41:36 2018

@author: marin
"""

from src.ecran_utilisateur import *  # importe les fonctions affichage écran
from src.fonctions import *  # importe les diverses fonctions


def main():
    # Initialisation de la bibliothèque Pygame
    pygame.init()

    # On affiche la fenêtre ici, les dimensions sont dans le tuple
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre), RESIZABLE)
    # Initialise les icones
    initialiser_fenetre()

    # Charge le fond ainsi que le logo
    fond = pygame.image.load(fond_visuel).convert()
    fenetre.blit(fond, (0, 0))

    # Variable qui continue la boucle si = 1, stoppe si = 0
    continuer = 1

    # Variable qui stocke le titre du film
    titre_film = ""
    # Choix couleur
    choix_couleur = ""
    # Variable qui stocke la célébrité préférée
    people_prefere = ""

    # Obtient la liste des 8 vignettes de films
    liste_film = selection_aleatoire_vignettes_1(fichier_film_path)

    # Obtient la liste des 8 people à afficher (il s'agit ici de la première connexion)
    liste_people = selection_aleatoire_vignettes_1(fichier_people_path)

    # BOUCLE INFINIE
    niveau = -1  # indique le niveau de sélection à afficher
    continuer = 1
    while continuer:

        # Limitation de vitesse de la boucle
        pygame.time.Clock().tick(20)

        ###Accueil de l'utilisateur pour sa première connexion
        if niveau == -1:
            # On crée le niveau accueil première connexion
            niveau_accueil_connexion_1(fenetre)
            # Rafraichissement
            pygame.display.flip()
            for event in pygame.event.get():  # Boucle des événements Pygame
                if event.type == QUIT:
                    continuer = 0

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if clic_bouton(event.pos[0], event.pos[1], 300, 342, 336, 139):
                        # Si l'on a cliqué sur le bouton suivant,
                        niveau += 1  # alors on passe au niveau suivant

        if niveau == 0:
            # Introduit creation film
            niveau_choix_vignettes(fenetre, liste_film, film=True)
            # Rafraichissement
            pygame.display.flip()
            for event in pygame.event.get():

                if event.type == QUIT:
                    continuer = 0

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    # Si l'on effectue un clic de souris sur une des images
                    (clic_rectangle, position) = souris_dans_rectangles(
                        event.pos[0], event.pos[1]
                    )
                    if clic_rectangle == 0:
                        # Si l'utilisateur a cliqué dans le rectangle
                        niveau += 1
                        titre_film = liste_film[position]  # Et on récupère le titre du film

        """
        On passe alors au niveau de génération du cercle de couleur.
        """

        if niveau == 1:
            rayon_cercle = 0  # On le définit à 0
            # Crée le niveau correspondant, et obtient le rayon du cercle
            rayon_cercle = niveau_choix_couleur(fenetre, premiere_connexion=True)
            # Rafraichissement
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer = 0

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    # Si l'on clique sur le cercle
                    # On définit qu'on a bien cliqué à l'intérieur du cercle
                    if (event.pos[0] - largeur_fenetre / 2) ** 2 + (
                        event.pos[1] - hauteur_fenetre / 2
                    ) ** 2 <= rayon_cercle ** 2:
                        niveau += 1
                        # On récupère la couleur du pixel cliqué ainsi que sa position associée
                        couleur_pixel = fenetre.get_at((event.pos[0], event.pos[1]))
                        choix_couleur = associe_couleur_pixel(couleur_pixel)

        ###Niveau de sélection des people
        if niveau == 2:
            # Introduit creation people quizz
            niveau_choix_vignettes(fenetre, liste_people, film=False)
            # Rafraichissement
            pygame.display.flip()
            for event in pygame.event.get():

                if event.type == QUIT:
                    continuer = 0

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    # Si l'on effectue un clic de souris sur une des images
                    (clic_rectangle, position) = souris_dans_rectangles(
                        event.pos[0], event.pos[1]
                    )
                    if clic_rectangle == 0:
                        # Si l'utilisateur a cliqué dans le rectangle
                        niveau += 1
                        people_prefere = liste_people[
                            position
                        ]  # Et on récupère le titre du film

        ### On arrive à l'écran de fin ###
        if niveau == 3:
            # On affiche le message à l'utilisateur
            niveau_final_1(fenetre)
            # Rafraichissement
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer = 0  # On quitte la boucle
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if clic_bouton(event.pos[0], event.pos[1], 300, 342, 336, 139):
                        # Si l'on a cliqué sur le bouton suivant,
                        continuer = 0  # alors on quitte la banque (et la boucle)

    # Quitte PyGame
    pygame.quit()

    print(titre_film)
    print(choix_couleur)
    print(people_prefere)

    # On écrit alors dans le fichier excel, le choix de la personne.
    df = pd.DataFrame(columns=["Adulte", titre_film, choix_couleur, people_prefere])
    df.to_excel("profil_user/profil_user.xls", index=False)


if __name__ == '__main__':
    main()
