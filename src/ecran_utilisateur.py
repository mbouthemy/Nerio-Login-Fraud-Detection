#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 21:01:43 2018

@author: marin

Contient les différentes fonctions d'accueil du message utilisateur.
"""

import pygame
from pygame.locals import *
from src.fonctions import *


def niveau_accueil_connexion_1(fenetre):
    """
        Crée le niveau d'accueil du client. (première connexion)
    """
    # Charge le fond, rectangle et logo
    details_graphiques(fenetre, fond_visuel)

    # On Affiche aussi un rectangle (de bord noir)
    pygame.draw.rect(fenetre, (0, 0, 0), (BORD_GAUCHE - 20, 80, 791, 567), 2)
    # Affiche les messages pour l'accueil du client.
    texte_1 = "Bonjour, M. Dupont, bienvenue sur le site de votre banque en ligne."
    texte_2 = "Il s'agit de votre première connexion, par mesure de sécurité,"
    texte_3 = "nous allons vous poser quelques questions."
    texte_4 = "Ce ne sera pas bien long, pour commencer, merci de cliquer sur le bouton suivant:"
    ecriture_texte_ecran(fenetre, texte_1, 200, 18)
    ecriture_texte_ecran(fenetre, texte_2, 230, 18)
    ecriture_texte_ecran(fenetre, texte_3, 250, 18)
    ecriture_texte_ecran(fenetre, texte_4, 280, 18)

    # On affiche le bouton continuer, au centre de l'écran
    bouton = pygame.image.load(BOUTON_SUIVANT).convert()
    position_bouton = bouton.get_rect()
    position_bouton.center = (largeur_fenetre / 2, 420)
    # On affiche le cercle au milieu de la fenêtre
    fenetre.blit(bouton, position_bouton)

    return 0


def niveau_final_1(fenetre):
    """
        Cette fonction affiche la dernière page.
        (première connexion)
    """
    # Charge le fond, rectangle et logo
    details_graphiques(fenetre, fond_visuel)

    texte_1 = "Merci beaucoup pour ces informations !"
    texte_2 = "Vous pouvez maintenant accéder à votre banque:"
    ecriture_texte_ecran(fenetre, texte_1, 250, 18)
    ecriture_texte_ecran(fenetre, texte_2, 280, 18)

    # On affiche le bouton continuer, au centre de l'écran
    # Chargement et collage du cercle de couleurs au centre de l'écran
    bouton = pygame.image.load(BOUTON_SUIVANT).convert()
    position_bouton = bouton.get_rect()
    position_bouton.center = (largeur_fenetre / 2, 420)
    # On affiche le cercle au milieu de la fenêtre
    fenetre.blit(bouton, position_bouton)

    return 0


def niveau_accueil_connexion_2(fenetre):
    """
        Crée le niveau d'accueil du client. (première connexion)
    """
    # Charge le fond, rectangle et logo
    details_graphiques(fenetre, fond_visuel)

    # On Affiche aussi un rectangle (de bord noir)
    pygame.draw.rect(fenetre, (0, 0, 0), (BORD_GAUCHE - 20, 80, 791, 567), 2)
    # Affiche les messages pour l'accueil du client.
    texte_1 = "Attention, nous avons détecté une activité suspecte sur votre compte."
    texte_4 = "Par mesure de sécurité, merci de bien vouloir répondre aux questions suivantes:"
    ecriture_texte_ecran(fenetre, texte_1, 200, 18)
    ecriture_texte_ecran(fenetre, texte_4, 280, 18)

    # On affiche le bouton continuer, au centre de l'écran
    bouton = pygame.image.load(BOUTON_SUIVANT).convert()
    position_bouton = bouton.get_rect()
    position_bouton.center = (largeur_fenetre / 2, 420)
    fenetre.blit(bouton, position_bouton)

    return 0


def niveau_final_2(fenetre, pourcentage):
    """
        Il s'agit de la fenêtre qui apparaît lors de la seconde connexion.
        Elle affiche un feu tricolore, qui dépend du pourcentage passé 
        en paramètres.
    """
    # Charge le fond, rectangle et logo
    details_graphiques(fenetre, fond_visuel)
    if pourcentage >= 0.8:
        # Si on est sûr que le client est bien le bon.
        # On affiche l'image du feu vert.
        feu_vert = pygame.image.load(feu_vert_path).convert()
        position_feu = feu_vert.get_rect()
        position_feu.center = (largeur_fenetre / 2, 200)
        fenetre.blit(feu_vert, position_feu)
        texte_1 = "Bonjour M. Dupont, merci pour cette vérification !"
        texte_2 = "Vous pouvez maintenant accéder à votre banque en toute sécurité"
        ecriture_texte_ecran(fenetre, texte_1, 300, 18)
        ecriture_texte_ecran(fenetre, texte_2, 330, 18)

        # On affiche le bouton continuer, au centre de l'écran
        bouton = pygame.image.load(BOUTON_SUIVANT).convert()
        position_bouton = bouton.get_rect()
        position_bouton.center = (largeur_fenetre / 2, 470)
        fenetre.blit(bouton, position_bouton)

    if 0.5 < pourcentage and pourcentage < 0.8:
        # Si on est moyennement sûr. On affiche un feu orange.
        # Et on lui demande de confirmer par mail.
        feu_orange = pygame.image.load(feu_orange_path).convert()
        position_feu = feu_orange.get_rect()
        position_feu.center = (largeur_fenetre / 2, 200)
        fenetre.blit(feu_orange, position_feu)
        texte_1 = "Attention, nous détectons une tentative d'intrusion."
        texte_2 = "Par mesure de sécurité, nous vous avons envoyé un mail."
        ecriture_texte_ecran(fenetre, texte_1, 300, 18)
        ecriture_texte_ecran(fenetre, texte_2, 330, 18)

    if pourcentage <= 0.5:
        # Dans le cas, où on a de grosses suspicions.
        # On affiche un feu rouge et on demandde sms de confirmation.
        feu_rouge = pygame.image.load(feu_rouge_path).convert()
        position_feu = feu_rouge.get_rect()
        position_feu.center = (largeur_fenetre / 2, 200)
        fenetre.blit(feu_rouge, position_feu)
        texte_1 = "Attention, nous détectons une tentative d'intrusion."
        texte_2 = "Par mesure de sécurité, merci de saisir le code qui vous est envoyé par SMS."
        ecriture_texte_ecran(fenetre, texte_1, 300, 18)
        ecriture_texte_ecran(fenetre, texte_2, 330, 18)

    return 0
