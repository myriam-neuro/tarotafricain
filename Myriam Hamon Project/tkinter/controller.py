import tkinter as Tk
from tkinter import X, NORMAL, DISABLED

from pip._vendor.cachecontrol import controller

import utils
from Entities import Partie, Tour, Pli
from models import Model
from views import View


class Controller():
    def __init__(self):

        # Instantiation de Tk
        self.root = Tk.Tk()

        # Instantiation du model
        self.model = Model()

        # Commencer Jeu
        self.jeu = Model.commencerJeu(self.model, self)

        # Pass to view links on root frame and controller object
        self.view = View(self)

        self.root.mainloop()

    def nouvellePartie(self, event):

        partie = self.model.creerPartie(self)

        self.jeu.add_partie(partie)
        self.jeu.partie_current = self.jeu.partie_current + 1
        self.jeu.is_dernier_tour = False

        self.model.initPlisGagnes(self.jeu.listeJoueurs)

        self.view.afficherNouvellePartie(partie)

    def tourSuivant(self, event):

        partieCurrent = self.jeu.partie_current
        partie = self.jeu.liste_parties[partieCurrent - 1]

        # incrémenter num tour
        self.model.incrementerNumTour(partie)

        # affichier bouton tour suivant
        self.view.afficherBoutonTourSuivant(partie)

        # Initialisation des frames
        self.view.intitFramesTourSuivant()

        # nouveau tour
        tour = self.model.nouveauTourPartie(partie)

        # ajouter le tour à la partie
        self.model.ajouterTourPartie(partie, tour)

        self.jeu.is_dernier_tour = tour.is_dernier_tour

        self.model.initScoreTour(self.jeu.listeJoueurs)
        self.model.getCartesJoueurs(self, tour)

        if not tour.is_dernier_tour:
            self.view.afficherMesCartes("Mes cartes", DISABLED, self.view.frameMesCartes)
        else:
            self.view.afficherCartesAutresJoueurs("Les cartes", DISABLED, self.view.frameMesCartes)

        self.view.frameMesPlis(partie)

    def jouerCarte(self, carteJouee):

        partie_current = self.jeu.partie_current
        partie = self.jeu.liste_parties[partie_current - 1]
        tour = partie.liste_tour[self.jeu.tour_current - 1]

        # creation d un nouveau pli
        pli = self.model.creerPli(self, carteJouee, tour)

        # Ajout du nouveau pli pour le tour
        self.model.ajoutPliDansTour(tour)

        # ajout d'un pli gagné pour le gagnant du plis
        self.model.majNbPlisGagnesJoueurGagnant(self, pli.joueurGagnant)

        # on renseigne le num du pli en cour au niveau du jeu
        self.jeu.pli_current = pli.num_plis

        dernierPli = pli.num_plis == tour.nb_carte_joueur
        # Calcul des scores pour le Tour et la Partie
        if dernierPli:
            self.model.calculScores(self.jeu.listeJoueurs, partie)

        # au dernier plis, activation du bouton du tour suivant si on est pas au dernier tour
        if dernierPli and tour.num_tour <= partie.nb_tour:
            self.view.afficherBtTourSuivant(self, partie)

        # Afficher les cartes jouees
        self.view.afficherCartesJouees(pli)

        # Affichier les scores
        self.view.afficherScores(self)

    def selectionNiveau(self):
        self.view.activer_btn_nouvelle_partie(self)

    def selectionPari(self, event):

        # Supprimer les frames à la selection du pari
        self.view.supprimerFrameSelectionPari()

        # Désactiver des radioboutton à la selection du pari
        self.view.desactiverWidgetsSelectionPari()

        # Désigner les plis annoncés
        self.setNbPlisAnnonces(self.view.var_paris.get())

        # Afficher le paris
        self.view.afficherLesParis()

        # Afficher mes cartes (joueur principal) : si on n 'est pas au dernier tour
        if not self.jeu.is_dernier_tour:
            self.view.afficherMesCartes("Jouer les plis ", NORMAL, self.view.frameMesCartesJouer)

        if self.jeu.is_dernier_tour:
            partie = self.jeu.liste_parties[self.jeu.partie_current - 1]
            self.model.calculScores(self.jeu.listeJoueurs, partie)

            # Afficher les cartes jouees
            self.view.cartesJouees(self.model.getPlisEnCour(self))

            # Affichier les scores
            self.view.afficherScores(self)

            # Afficher gagnant
            self.view.gagnant(partie)

    def setNbPlisAnnonces(self, parisJoeurPrincipal):

        partie = self.jeu.liste_parties[self.jeu.partie_current - 1]
        tour = partie.liste_tour[partie.num_tour - 1]

        tour.parisPossibles = self.model.getParisPossible(tour)

        # Boucle sur les joueur pour ajouter les paris des autres joueurs
        for joueur in self.jeu.listeJoueurs:

            # pari du joueur principal
            if joueur.isJoueurPrincipal:
                joueur.nbPlisAnnonces = parisJoeurPrincipal

            # pari des autres joueurs
            if not joueur.isJoueurPrincipal:
                # calcul du pari (random dans les paris possibles)
                pari = self.model.getPariAnnonce(tour.parisPossibles, self.jeu.niveau)

                # set du pari  pour le joueur
                joueur.nbPlisAnnonces = pari

    def activer_btn_afficher_paris(self):
        self.view.activer_btn_afficher_paris(self)


