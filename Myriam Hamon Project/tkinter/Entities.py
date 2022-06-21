class Carte:
    def __init__(self):
        self.nom = ""
        self.valeur = ""


class Joueur:
    def __init__(self):
        self.name = ""
        self.listeCartes = []
        self.carteJouee = ""
        self.isJoueurPrincipal = False
        self.isCarteSuperieur = False
        self.isExcuseMax = False
        self.isExcuseLess = False
        self.nbPlisAnnonces = 0
        self.nbPlisGagnes = 0
        self.position = 0
        self.isDistributeur = False
        self.pointPlis = 0
        self.scoreTour = 0
        self.scorePartie = 0

    def add_carte(self, carte):
        self.listeCartes.append(carte)


class Jeu:
    def __init__(self):
        self.niveau = 0
        self.nb_niveau = 0
        self.nbJoueurs = 0
        self.partie_current = 0
        self.tour_current = 0
        self.pli_current = 0
        self.liste_parties = []
        self.listeJoueurs = []
        self.joueurPrinipal = ""
        self.listeCartes = []
        self.isAllDistributeur = False
        self.isJeuTermine = False
        self.jeu_joueur_gagnant = ""
        self.is_dernier_tour = False

    def add_partie(self, parti):
        self.liste_parties.append(parti)

    def add_joueur(self, joueur):
        self.listeJoueurs.append(joueur)

    def add_carte(self, carte):
        self.listeCartes.append(carte)


class Partie:
    def __init__(self):
        self.distributeur = ""
        self.nb_tour = 0
        self.num_tour = 0
        self.liste_tour = []
        self.partie_joueur_gagnant = ""
        self.partie_joueur_gagnant_score = 0
        self.is_partie_ternminee = False

    def add_tour(self, tour):
        self.liste_tour.append(tour)


class Tour:
    def __init__(self):
        self.num_tour = 0
        self.nb_carte_joueur = 0
        self.cartesRestantes = ""
        self.parisPossibles = []
        self.liste_plis = []
        self.is_dernier_tour = False
        self.tour_joueur_gagnant = ""

    def add_paris_possible(self, paris):
        self.parisPossibles.append(paris)

    def add_plis(self, pli):
        self.liste_plis.append(pli)


class Pli:
    def __init__(self):
        self.num_plis = 0
        self.cartesJouees = []
        self.carteHaute = ""
        self.joueurGagnant = 0

    def add_cartesJouees(self, carteJouee):
        self.cartesJouees.append(carteJouee)
