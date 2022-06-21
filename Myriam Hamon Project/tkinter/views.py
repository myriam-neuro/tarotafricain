import tkinter as Tk
from doctest import master
from pydoc import text
from tkinter import X, LEFT, W, DISABLED, NORMAL
from tkinter.ttk import Radiobutton
from turtle import mode

import controller
import utils


class View:
    def __init__(self, controller):

        self.frame = Tk.Frame(controller.root)
        self.controller = controller
        self.var_paris = Tk.IntVar()
        self.var_niveau = Tk.IntVar()

        self.title = controller.root.title("Tarot Africain")
        self.geometry = controller.root.geometry('600x500')

        self.frameNouvellePartie = Tk.Frame(self.controller.root)
        self.frameTour = Tk.Frame(self.controller.root)
        self.frameNiveau = Tk.Frame(self.controller.root)
        self.frameParis = Tk.Frame(self.controller.root)
        self.framePlis = Tk.Frame(self.controller.root)
        self.frameMesCartes = Tk.Frame(self.controller.root)
        self.frameBoutonJouer = Tk.Frame(self.controller.root)
        self.frameMesCartesJouer = Tk.Frame(self.controller.root)
        self.frameCartesJouees = Tk.Frame(self.controller.root)
        self.framePlisGagnes = Tk.Frame(self.controller.root)
        self.frameScoresTour = Tk.Frame(self.controller.root)
        self.frameScoresPartie = Tk.Frame(self.controller.root)
        self.frameTourSuivant = Tk.Frame(self.controller.root)
        self.frameGagnant = Tk.Frame(self.controller.root)

        self.frameNiveaux()
        self.boutonNouvellePartie()

    def boutonNouvellePartie(self):

        # utils.supprimerWidgetsFrame(self.frameNouvellePartie)

        self.bt_nouvellePartie = Tk.Button(self.frameNouvellePartie, text=str("Nouvelle Partie"), justify=Tk.LEFT,
                                           state=DISABLED)
        self.bt_nouvellePartie.unbind('<Key-Up>')
        self.bt_nouvellePartie.pack(side=Tk.LEFT)

        self.frameNouvellePartie.pack(fill=X, padx=5, pady=5)

    def afficherTour(self, partie):
        # utils.supprimerWidgetsFrame(self.frameTour)

        self.lbl_tour = Tk.Label(self.frameTour, text="Tour : " + str(partie.num_tour) + "/" + str(partie.nb_tour),
                                 width=6)
        self.lbl_tour.pack(side=LEFT, padx=5, pady=5)

        self.bt_tourSuivant = Tk.Button(self.frameTour, text=str("Tour " + str(partie.num_tour + 1) + ">>>"),
                                        justify=Tk.LEFT,
                                        state=DISABLED)
        self.bt_tourSuivant.unbind('<Key-Up>')
        self.bt_tourSuivant.pack(side=Tk.LEFT)

        self.frameTour.pack(fill=X, padx=5, pady=5)

    def activer_btn_tour_suivant(self, controller, partie):
        self.bt_tourSuivant['state'] = NORMAL
        self.bt_tourSuivant.bind("<Button>", controller.tourSuivant)

    def activer_btn_nouvelle_partie(self, controller):
        self.bt_nouvellePartie['state'] = NORMAL
        self.bt_nouvellePartie.bind("<Button>", controller.nouvellePartie)

    def frameNiveaux(self):

        self.lbl = Tk.Label(self.frameNiveau, text="Niveau : ", width=6)
        self.lbl.pack(side=LEFT, padx=5, pady=5)

        self.radioNiveau(self.frameNiveau)

        self.frameNiveau.pack(fill=X, padx=5, pady=5);

    def radioNiveau(self, frame):

        for i in range(self.controller.jeu.nb_niveaux):
            num = i + 1
            self.radioNiveaux = Radiobutton(frame, text=str(num), variable=self.var_niveau, value=num,
                                            command=self.controller.selectionNiveau)
            self.radioNiveaux.pack(anchor=W, side=LEFT, ipadx=5)

    def frameMesPlis(self, partie):

        # utils.supprimerWidgetsFrame(self.framePlis)

        self.framePlis.pack(fill=X, padx=5, pady=5)

        self.lbl = Tk.Label(self.framePlis, text="Mes plis envisagés: ", justify=Tk.LEFT)
        self.lbl.pack(side=Tk.LEFT)

        self.radioParis(self.framePlis, partie)

        self.bt_afficherParis = Tk.Button(self.framePlis, text=str("afficher les paris"), justify=Tk.LEFT,
                                          state=DISABLED)
        self.bt_afficherParis.pack(side=Tk.LEFT)

        self.framePlis.pack(padx=5, pady=5)

    def activer_btn_afficher_paris(self, controller):
        self.bt_afficherParis['state'] = NORMAL
        self.bt_afficherParis.bind("<Button>", controller.selectionPari)

    def radioParis(self, frame, partie):
        self.radioPari = dict()
        for i in range(partie.liste_tour[partie.num_tour - 1].nb_carte_joueur + 1):
            self.radioPari[i] = Radiobutton(frame, text=str(i), variable=self.var_paris, value=i,
                                            command=self.controller.activer_btn_afficher_paris)
            self.radioPari[i].pack(anchor=W, side=LEFT, ipadx=5)

    def afficherCartesAutresJoueurs(self, libelle, status, frame):

        frame.pack(fill=X)

        self.lbl = Tk.Label(frame, text=libelle + " : ", justify=Tk.LEFT)
        self.lbl.pack(side=Tk.LEFT)

        self.afficherLesCartes(status, frame)

        frame.pack(padx=5, pady=5)

    def afficherLesCartes(self, status, frame):

        joeurs = self.controller.jeu.listeJoueurs

        colonne = 0
        for joueur in joeurs:
            if not joueur.isJoueurPrincipal:
                self.lbl = Tk.Label(frame, text=joueur.name + " : ", justify=Tk.LEFT)
                self.lbl.pack(side=Tk.LEFT)

                carte = joueur.listeCartes[0].nom
                self.btn = Tk.Button(frame, text=carte, justify=Tk.LEFT, state=status)
                self.btn.pack(side=Tk.LEFT)

                frame.pack(padx=1, pady=1)

                colonne = colonne + 1

    def afficherMesCartes(self, libelle, status, frame):

        # utils.supprimerWidgetsFrame(frame)

        frame.pack(fill=X)

        self.lbl = Tk.Label(frame, text=libelle + " : ", justify=Tk.LEFT)
        self.lbl.pack(side=Tk.LEFT)

        self.afficherCartes(status, frame)

        frame.pack(padx=5, pady=5)

    def afficherCartes(self, status, frame):

        controller = self.controller

        mesCartes = controller.jeu.listeJoueurs[controller.jeu.joueurPrincipal].listeCartes

        colonne = 0
        for cartes in mesCartes:
            nom = cartes.nom
            self.btn = Tk.Button(frame, text=nom, justify=Tk.LEFT, state=status)
            self.btn['command'] = lambda idx=colonne, binst=self.btn: self.click(idx, binst, controller, mesCartes)
            self.btn.pack(side=Tk.LEFT)

            frame.pack(padx=1, pady=1)

            colonne = colonne + 1

    def click(self, idx, binst, controller, mesCartes):
        binst.destroy()
        carteLib = mesCartes[idx].nom
        controller.jouerCarte(carteLib)

    def afficherLesParis(self):

        # utils.supprimerWidgetsFrame(self.frameParis)

        self.lbl = Tk.Label(self.frameParis, text="Les paris : ", justify=Tk.LEFT)
        self.lbl.pack(side=Tk.LEFT)

        for joueur in self.controller.jeu.listeJoueurs:
            nom = joueur.name
            pari = joueur.nbPlisAnnonces

            self.lbl = Tk.Label(self.frameParis, text=nom + " : " + str(pari), width=6)
            self.lbl.pack(side=LEFT, padx=5, pady=5)

        self.frameParis.pack(fill=X, padx=5, pady=5)

    def frameBoutonJouer(self):

        # utils.supprimerWidgetsFrame(self.frameBoutonJouer)

        self.btn = Tk.Button(self.frameBoutonJouer, text=str("Jouer"), justify=Tk.LEFT, state=DISABLED)
        self.btn.bind("<Button>", controller.jouerCarte)
        self.btn.pack(side=Tk.LEFT)

        self.frameBoutonJouer.pack(fill=X, padx=5, pady=5)

    def afficherCartesJouees(self, plis):
        utils.supprimerWidgetsFrame(self.frameCartesJouees)

        self.lbl = Tk.Label(self.frameCartesJouees, text="Cartes Jouées: ", justify=Tk.LEFT)
        self.lbl.pack(side=Tk.LEFT)

        p = 0
        for pli in plis.cartesJouees:
            nomJoueur = self.controller.jeu.listeJoueurs[p].name
            self.lbl = Tk.Label(self.frameCartesJouees, text=nomJoueur + " : " + str(pli), width=6)
            self.lbl.pack(side=LEFT, padx=5, pady=5)
            p = p + 1

        self.frameCartesJouees.pack(fill=X, padx=5, pady=5)

    def plisGagnes(self, joueurs):
        utils.supprimerWidgetsFrame(self.framePlisGagnes)

        self.lbl = Tk.Label(self.framePlisGagnes, text="Plis gagnés: ", justify=Tk.LEFT)
        self.lbl.pack(side=Tk.LEFT)

        for joueur in joueurs:
            self.lbl = Tk.Label(self.framePlisGagnes, text=joueur.name + " : " + str(joueur.nbPlisGagnes), width=6)
            self.lbl.pack(side=LEFT, padx=5, pady=5)

        self.framePlisGagnes.pack(fill=X, padx=5, pady=5)

    def scoresTour(self, joueurs):
        utils.supprimerWidgetsFrame(self.frameScoresTour)

        self.lbl = Tk.Label(self.frameScoresTour, text="Scores Tour: ", justify=Tk.LEFT)
        self.lbl.pack(side=Tk.LEFT)

        for joueur in joueurs:
            self.lbl = Tk.Label(self.frameScoresTour, text=joueur.name + " : " + str(joueur.scoreTour), width=6)
            self.lbl.pack(side=LEFT, padx=5, pady=5)

        self.frameScoresTour.pack(fill=X, padx=5, pady=5)

    def scoresPartie(self, joueurs):
        utils.supprimerWidgetsFrame(self.frameScoresPartie)

        self.lbl = Tk.Label(self.frameScoresPartie, text="Scores Partie: ", justify=Tk.LEFT)
        self.lbl.pack(side=Tk.LEFT)

        for joueur in joueurs:
            self.lbl = Tk.Label(self.frameScoresPartie, text=joueur.name + " : " + str(joueur.scorePartie), width=6)
            self.lbl.pack(side=LEFT, padx=5, pady=5)

        self.frameScoresPartie.pack(fill=X, padx=5, pady=5)

    def afficherBoutonTourSuivant(self, partie):

        numTour = partie.num_tour + 1 if partie.num_tour < partie.nb_tour else partie.num_tour

        self.bt_tourSuivant["text"] = "Tour " + str(numTour) + ">>>"
        self.bt_tourSuivant['state'] = DISABLED
        self.bt_tourSuivant.unbind("<Button>")

        self.lbl_tour["text"] = "Tour : " + str(partie.num_tour) + "/" + str(partie.nb_tour)

    def intitFramesTourSuivant(self):
        utils.supprimerWidgetsFrame(self.frameMesCartes)
        utils.supprimerWidgetsFrame(self.framePlis)
        utils.supprimerWidgetsFrame(self.frameParis)
        utils.supprimerWidgetsFrame(self.frameMesCartesJouer)
        utils.supprimerWidgetsFrame(self.frameCartesJouees)
        utils.supprimerWidgetsFrame(self.framePlisGagnes)
        utils.supprimerWidgetsFrame(self.frameScoresTour)

    def gagnant(self, partie):
        utils.supprimerWidgetsFrame(self.frameGagnant)

        self.lblGagnant = Tk.Label(self.frameGagnant, text="joueur gagnant: " + partie.partie_joueur_gagnant +
                                                           " score :" + str(partie.partie_joueur_gagnant_score),
                                   justify=Tk.LEFT)
        self.lblGagnant.pack(side=Tk.LEFT)

        self.frameGagnant.pack(fill=X, padx=5, pady=5)

    def supprimerWidgetsNouvellePartie(self):
        utils.supprimerWidgetsFrame(self.frameTour)
        utils.supprimerWidgetsFrame(self.frameMesCartes)
        utils.supprimerWidgetsFrame(self.framePlis)

        utils.supprimerWidgetsFrame(self.frameParis)
        utils.supprimerWidgetsFrame(self.frameMesCartesJouer)
        utils.supprimerWidgetsFrame(self.frameCartesJouees)
        utils.supprimerWidgetsFrame(self.framePlisGagnes)
        utils.supprimerWidgetsFrame(self.frameScoresTour)
        utils.supprimerWidgetsFrame(self.frameScoresPartie)
        utils.supprimerWidgetsFrame(self.frameGagnant)


    def afficherNouvellePartie(self, partie):
        self.supprimerWidgetsNouvellePartie()

        self.afficherTour(partie)
        self.afficherMesCartes("Mes cartes", DISABLED, self.frameMesCartes)
        self.frameMesPlis(partie)

    def supprimerFrameSelectionPari(self):
        utils.supprimerWidgetsFrame(self.frameParis)
        utils.supprimerWidgetsFrame(self.frameMesCartesJouer)

    def desactiverWidgetsSelectionPari(self):
        utils.desactiverBouton(self.bt_afficherParis, 'disabled')
        utils.desactiverRaddioBouton(self.radioPari, 'disabled')

    def afficherScores(self, controller):
        self.plisGagnes(controller.jeu.listeJoueurs)
        self.scoresTour(controller.jeu.listeJoueurs)
        self.scoresPartie(controller.jeu.listeJoueurs)

    def afficherBtTourSuivant(self, controller, partie):
        self.activer_btn_tour_suivant(controller, partie)
