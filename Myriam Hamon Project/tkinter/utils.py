# fonctions-------------------------------------------------
from random import randint


def pioche():
    return ([k for k in range(1, 23)])


def depart(p, nbpartie):
    jeu = [[], [], []]
    for k in range(3):
        for i in range(7 - nbpartie):
            jeu[k] += [p.pop(randint(0, len(p) - 1))]
    return jeu


def tour(jeu, ordre, point):
    Plateau = []
    Vq = []
    for i in range(3):
        if ordre == 0:
            a = int(input("Que voulez -vous jouer?"))
            Plateau += [jeu[0].pop(jeu[0].index(a))]
            Vq += [0]
        else:
            b = jeu[ordre].pop(randint(0, len(jeu[ordre]) - 1))
            Plateau += [b]
            Vq += [ordre]
            print(Plateau)
        ordre = (ordre + 1) % 3
    m = max(Plateau)
    print('Le plateau est :', Plateau)
    for k in range(3):
        if Plateau[k] == m:
            point[Vq[k]] = point[Vq[k]] + 1
    print('le nombre de score remportés sont :', point, '\n Votre jeu est :', jeu[0])
    return point, jeu


def partie(nbtour, point, jeu, a, Pari, Plateau):
    ordre = 0
    for i in range(7 - nbtour):
        if a == 2:
            niveau2(nbtour, jeu, Pari, ordre, point, Plateau)
        if a == 1:
            tour(jeu, ordre, point)
        if a == 3:
            niveau3(nbtour, jeu, Pari, ordre, point, Plateau)
        ordre = (ordre + 1) % 3
    return (point)


def niveau3(nbtour, jeu, Pari, ordre, point, Plateau, m):
    Plateau = []
    if ordre % 3 == 1:
        if pari[1] > point[1]:
            Plateau += [jeu[1].pop(jeu[1]).index(max(jeu[1]))]
        else:
            Plateau += [jeu[1].pop(jeu[1]).index(min(jeu[1]))]
        if Pari[2] > point[2]:
            if max(jeu[2]) >= 20:
                Plateau += [jeu[2].pop(jeu[2]).index(max(jeu[2]))]
        else:
            Plateau += [jeu[2].pop(min(jeu[2]))]
        print('Le plateau est :', Plateau)
        a = int(input("Que voulez -vous jouer?"))
        Plateau += [jeu[0].pop(jeu[0].index(a))]
    if ordre % 3 == 0:
        a = int(input("Que voulez -vous jouer?"))
        Plateau += [jeu[0].pop(jeu[0].index(a))]
        if Pari[1] > point[1]:
            if max(jeu[1]) >= 20:
                Plateau += [jeu[1].pop(jeu[1]).index(max(jeu[1]))]
        else:
            Plateau += [jeu[1].pop(jeu[1]).index(min(jeu[1]))]
        if Pari[2] > point[2]:
            if max(jeu[2]) > max(Plateau):
                Plateau += [jeu[2].pop((jeu[2]).index(max(jeu[2])))]
            else:
                Plateau += [jeu[2].pop((jeu[2]).index(min(jeu[2])))]
        else:
            k = compareliste(jeu, Plateau)
            Plateau += [jeu[2].pop(jeu[2].index(k))]
    if ordre % 3 == 2:
        if Pari[1] > point[1]:
            Plateau += [jeu[1].pop(jeu[1]).index(max(jeu[1]))]
        else:
            Plateau += [jeu[1].pop(jeu[1]).index(min(jeu[1]))]
        print('Le plateau est :', Plateau)
        a = int(input("Que voulez -vous jouer?"))
        Plateau += [jeu[0].pop(jeu[0].index(a))]
        if Pari[2] > point[2]:
            if max(jeu[2]) > max(Plateau):
                Plateau += [jeu[2].pop(jeu[2]).index(max(jeu[2]))]
            else:
                Plateau += [jeu[2].pop(jeu[2]).index(min(jeu[2]))]
        else:
            k = compareliste(jeu, Plateau)
            Plateau += [jeu[2].pop(jeu[2].index(k))]
    for k in range(3):
        if Plateau[k] == m:
            point[k] = point[k] + 1
    print('le nombre de score remportés sont :', point, ' \nVotre jeu est :', jeu[0])
    return (point)


def compareliste(jeu, Plateau):
    a = []
    for k in (len(jeu[2]) - 1):
        if jeu[2][k] < max(Plateau):
            a += jeu[2][k]
    return max(a)


def lastpartie(p, jeu, nbtour, score, point):
    print('Vous devez parier sans votre carte, mais vous ne pouvez pas voir les autres cartes')
    jeu = depart(p, 6)
    print("jeu du jour 1 :", jeu[1], " jeu du jour 2:", jeu[2])
    pari0 = int(input("Combien de tour pensez-vous gagner ?"))
    pari1 = randint(0, 7)
    pari2 = pari(pari0, pari1, nbtour)
    Pari = [pari0, pari1, pari2]
    print('Le plateau est ', jeu)
    for k in range(3):
        if Pari[k] == point[k]:
            print('Le joueur', k, 'n a pas perdu de point dans cette partie')

        else:
            print('Le joueur', k, 'a perdu', abs(Pari[k] - point[k]), 'points')
            score[k] = scorecalc(point, score, Pari, k)
        print('Le score du joueur', k, 'est', score[k])
    return


def lastpartie(Plateau, point, score):
    # derniere partie differente
    print('Vous devez parier sans votre carte, mais vous pouvez voir les quatres cartes')
    pio = pioche()
    jeu = depart(pio, 6)

    print("jeu du jour 1 :", jeu[1], " jeu du jour 2:", jeu[2])
    pari0 = int(input("Combien de plis pensez-vous gagner ?"))
    pari1 = randint(0, 2)
    pari2 = pari(pari0, pari1, 6)
    Pari = [pari0, pari1, pari2]
    print('Le plateau est ', Plateau)
    for k in range(3):
        if Pari[k] == point[k]:
            print('Le joueur', k, 'n a pas perdu de point dans cette partie')

        else:
            print('Le joueur', k, 'a perdu', abs(Pari[k] - point[k]), 'points')
            score[k] = scorecalc(point, score, Pari, k)
        print('Le score du joueur', k, 'est', score[k])
    return


def pari(nbtour, jeu, a):
    pari0 = int(input("Combien de tour pensez-vous gagner ?"))
    if a == 1:
        pari1 = randint(0, 8 - nbtour)
        m = pari0 + pari1
        p = m
        while p == m:
            p = randint(0, 8 - nbtour)
        pari2 = p
    if a == 2 or a == 3:
        pari1 = 0
        for k in range(len(jeu[1]) - 1):
            if jeu[1][k] > 15:
                pari1 = pari1 + 1
        m = pari0 + pari1
        pari2 = 0
        for k in range(len(jeu[2]) - 1):
            if jeu[2][k] > 15:
                pari2 = pari2 + 1
        if pari2 == m:
            pari2 = pari2 - 1
    Pari = [pari0, pari1, pari2]
    print(pari0, pari1, pari2)
    return Pari


def niveau2(nbtour, jeu, pari, ordre, point, Plateau):
    Plateau = []
    print(jeu)  # juste pour vérifier
    a = int(input("Que voulez -vous jouer?"))
    Plateau += [jeu[0].pop(jeu[0].index(a))]
    b = jeu[1].pop(jeu[1].index(max(jeu[1])))
    Plateau += [b]
    c = jeu[2].pop(jeu[2].index(min(jeu[2])))
    Plateau += [c]
    m = max(Plateau)
    print('Le plateau est :', Plateau)
    for k in range(3):
        if Plateau[k] == m:
            point[k] = point[k] + 1
    print('le nombre de score remportés sont :', point, ' \nVotre jeu est :', jeu[0])
    return (point)


def scorecalc(point, score, Pari, k):
    score[k] = score[k] - abs(Pari[k] - point[k])
    return score[k]


def supprimerWidgetsFrame(frame):
    if len(frame.winfo_children()) == 0:
        return
    for widget in frame.winfo_children():
        #       widget.pack_forget()
        widget.destroy()

def click(self, idx, binst):
    binst.destroy()

def desactiverBouton(bouton, state):
    bouton['state'] = state
    bouton.unbind("<Button>")

def desactiverRaddioBouton(bouton, state):
    for key in bouton:
        bouton[key]['state'] = state