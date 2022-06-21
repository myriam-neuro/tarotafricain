from math import fabs, floor
from random import choice, random

from Entities import Carte, Jeu, Pli, Tour
from Entities import Joueur
from Entities import Partie


class Model():
    def __init__(self):
        pass

    def commencerJeu(self, controller):
        jeu = Jeu()
        jeu.niveau = 1
        jeu.nb_niveaux = 3
        jeu.nbJoueurs = 3
        jeu.partie_current = 0
        self.ajouterJoueursJeu(jeu)
        self.ajouterCartesJeu(jeu)

        return jeu

    def creerPartie(self, controller):
        partie = Partie()
        partie.niveau = controller.view.var_niveau.get()
        partie.nb_tour = floor(len(controller.jeu.listeCartes) / controller.jeu.nbJoueurs)
        partie.num_tour = 1

        partie.add_tour(self.nouveauTour(controller, partie))

        return partie;

    def nouveauTour(self, controller, partie):

        tour = Tour()
        tour.num_tour = tour.num_tour
        tour.nb_carte_joueur = partie.nb_tour

        self.initScoreTour(controller.jeu.listeJoueurs)
        self.getCartesJoueurs(controller, tour)

        return tour

    def ajouterCartesJeu(self, jeu):

        for i in range(22):
            carteCurrent = i + 1
            carte = Carte()
            # carte.nom = str(carteCurrent) if carteCurrent <= 21 else "excuse"
            carte.nom = str(carteCurrent)
            carte.valeur = carteCurrent

            jeu.add_carte(carte)

    def ajouterJoueursJeu(self, jeu):

        for j in range(jeu.nbJoueurs):
            joueur = Joueur()

            joueur.position = j + 1
            joueur.name = "MOI" if (j == 0) else "J" + str(j + 1)

            if j == 0:
                jeu.joueurPrincipal = j
                joueur.isJoueurPrincipal = True

            jeu.add_joueur(joueur)

    def getCartesJoueurs(self, controller, tour):

        jeu = controller.jeu

        # duplication de la liste des cartes, sans pointer sur les mêmes données
        cartesPartieDistribuables = jeu.listeCartes[:]
        # nbCartesJoueur = nb_carte_joueur - num_tour + 1

        for joueur in jeu.listeJoueurs:
            joueur.listeCartes = []
            self.ajouterCartes(tour, joueur, cartesPartieDistribuables)

    def ajouterCartes(self, tour, joueur, cartesPartieDistribuables):

        for i in range(tour.nb_carte_joueur):
            carte = choice(cartesPartieDistribuables)

            joueur.add_carte(carte)

            cartesPartieDistribuables.remove(carte)

    def getParisPossible(self, current_tour):

        liste_paris_possible = []
        for pari in range(current_tour.nb_carte_joueur + 1):
            # current_tour.add_paris_possible(pari)
            liste_paris_possible.append(pari)

        return liste_paris_possible

    def getPariAnnonce(self, current_paris_possibles, niveau):

        def niveau_1():
            # random du pari pour les autres joueurs
            return choice(current_paris_possibles)

        def niveau_2():
            return choice(current_paris_possibles)

        def niveau_3():
            return choice(current_paris_possibles)

        switcher = {
            1: niveau_1(),
            2: niveau_2(),
            3: niveau_3()
        }

        return switcher[niveau]

    def cartesJoueesPli(self, joueurs, pli, carteJoueeJoueurPrincipal):

        dernierTour = carteJoueeJoueurPrincipal == ""

        for joueur in joueurs:

            if joueur.isJoueurPrincipal and not dernierTour:
                # ajout de carte jouée par le joueur principal dans le pli
                pli.add_cartesJouees(int(carteJoueeJoueurPrincipal))

            if not joueur.isJoueurPrincipal or dernierTour:
                # choix aléatoire du choix de la carte parmis les cartes du joueur pour le pli
                carteJouee = choice(joueur.listeCartes)

                # ajout de la carte choisie dans le pli
                pli.add_cartesJouees(carteJouee.valeur)

                # on retire la carte des cartes du joueur pour ce pli
                joueur.listeCartes.remove(carteJouee)

    def initScoreTour(self, joueurs):
        for joueur in joueurs:
            joueur.scoreTour = 0
            joueur.nbPlisGagnes = 0

    def calculScores(self, joueurs, partie):

        scoresJoueurs = []

        for joueur in joueurs:
            if joueur.nbPlisGagnes != joueur.nbPlisAnnonces:
                joueur.scoreTour = joueur.scoreTour - (abs(joueur.nbPlisGagnes - joueur.nbPlisAnnonces))

            joueur.scorePartie = joueur.scorePartie + joueur.scoreTour

            scoresJoueurs.append(joueur.scorePartie)

        joueurGagnatIndex = scoresJoueurs.index(max(scoresJoueurs))
        partie.partie_joueur_gagnant = joueurs[joueurGagnatIndex].name
        partie.partie_joueur_gagnant_score = joueurs[joueurGagnatIndex].scorePartie

    def creerPli(self, controller, carteJoueeJoueurPrincipal, tour):
        pli = Pli()
        pli.num_tour = controller.jeu.tour_current

        # cartes jouees des joueurs
        self.cartesJoueesPli(controller.jeu.listeJoueurs, pli, carteJoueeJoueurPrincipal)

        # joueur gagnant du pli
        pli.joueurGagnant = pli.cartesJouees.index(max(pli.cartesJouees))

        pli.num_plis = len(tour.liste_plis) + 1

        return pli

    def getPlisEnCour(self, controller):

        partie = controller.jeu.liste_parties[controller.jeu.partie_current - 1]
        tour = partie.liste_tour[controller.jeu.tour_current - 1]

        pli = self.creerPli(controller, "", tour)

        joueurGagnant = controller.jeu.listeJoueurs[pli.joueurGagnant]
        joueurGagnant.nbPlisGagnes = joueurGagnant.nbPlisGagnes + 1

        return pli

    def initPlisGagnes(self, joueurs):
        for joueur in joueurs:
            joueur.nbPlisGagnes = 0

    def majNbPlisGagnesJoueurGagnant(self, controller, joueurGagnant):
        joueurGagnant = controller.jeu.listeJoueurs[joueurGagnant]
        joueurGagnant.nbPlisGagnes = joueurGagnant.nbPlisGagnes + 1

    def ajoutPliDansTour(self, tour):
        tour.add_plis(tour)

    def incrementerNumTour(self, partie):
        partie.num_tour = partie.num_tour + 1

    def nouveauTourPartie(self, partie):
        tour = Tour()
        tour.num_tour = len(partie.liste_tour)
        tour.nb_carte_joueur = partie.nb_tour - len(partie.liste_tour)
        tour.is_dernier_tour = tour.num_tour == partie.nb_tour - 1

        return tour

    def ajouterTourPartie(self, partie, tour):
        partie.add_tour(tour)
