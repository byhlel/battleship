#Ce projet a été réalisé par Bilal-Rayane MAJJAD
#N.B. : veillez à excétuer sous Linux ou IDE Python tel que pycharm (testé) pour ne pas avoir de problèmes d'affichage avec les couleurs : bicolors 

N = 10
COLONNES = [str(i) for i in range(N)]
LIGNES = [' '] + list(map(chr, range(97, 107)))
DICT_LIGNES_INT = {LIGNES[i]: i - 1 for i in range(len(LIGNES))}
VIDE = '.'
EAU = 'o'
TOUCHE = 'x'
BATEAU = '#'
DETRUIT = '@'
NOMS = ['Transporteur', 'Cuirasse', 'Croiseur', 'Sous-marin', 'Destructeur']
TAILLES = [5, 4, 3, 3, 2]


# 1 CARTE ET TIR

# Question 1

def create_grid():
    L = []
    for i in range(N + 1):
        l = []
        for j in range(N + 1):
            l.append(VIDE)
        L.append(l)
    return L


# Question 2

def plot_grid1(L): #version de base sans couleur
    for i in range(10):
        print(" " + COLONNES[i], end="")
    print()
    for k in range(1, N + 1):
        c = LIGNES[k]
        for j in range(N):
            c += " " + L[k - 1][j]
        print(c)


class bcolors: #pour la question 5 avec les couleurs
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    OKBLUE = '\033[94m'

def plot_grid(L):
    for i in range(10):
        print(" " , end="")
        print(bcolors.WARNING + COLONNES[i] + bcolors.ENDC , end="")
    print()
    for k in range(1, N + 1):
        print(bcolors.WARNING + LIGNES[k] + bcolors.ENDC , end="")
        for j in range(N):
            print(" ", end="")
            if L[k - 1][j] == VIDE:
                print(L[k - 1][j], end="")
            elif L[k - 1][j] == EAU:
                print(bcolors.OKGREEN + EAU + bcolors.ENDC , end="")
            elif L[k - 1][j] == TOUCHE:
                print(bcolors.OKCYAN + TOUCHE + bcolors.ENDC , end="")
            elif L[k - 1][j] ==BATEAU:
                print(bcolors.OKBLUE + BATEAU + bcolors.ENDC , end="")
            else :
                print(bcolors.FAIL + DETRUIT + bcolors.ENDC , end="")
        print()

# Question 3

def tir1(m, pos):
    m[pos[0]][pos[1]] = EAU


# Question 4

from random import randint

def random_position():
    return (randint(0, N - 1), randint(0, N - 1))

# Question 5

# map= create_grid()
# tirer = "True"
# while tirer == "True":
#     plot_grid(map)
#     pos = random_position()
#     tir(map,pos)
#     tirer=input("Shoot again?")

# Question 6
def pos1_from_string(S):
    return (ord(S[0]) - 97, int(S[2]))

# Question 7

def pos_from_string(S):
    while len(S) != 3 or ord(S[0]) < 97 or ord(S[0]) > 106 or S[1] != ' ' or ord(S[2]) < 48 or ord(S[2]) > 57:
        print("Vous devez respecter le format suivant, ligne entre a et j suivi d'un espace puis d'un chiffre représentant la colonne entre 0 et 9")
        S = input("Veuillez entrer une position correcte \n")
    else:
        return (ord(S[0]) - 97, int(S[2]))


# Question 8

def pos2_from_string(S,L): #finalement, cas traité lors du tir et donc non besoin de vérifier ici, il vérifier si la case dans la matrice n'était pas à "VIDE"
    while len(S) != 3 or ord(S[0]) < 97 or ord(S[0]) > 106 or S[1] != ' ' or ord(S[2]) < 48 or ord(S[2]) > 57 or (
            L[ord(S[0]) - 97][int(S[2])] != VIDE):
        print("Vous devez respecter le format suivant, ligne entre a et j suivi d'un espace puis d'un chiffre représentant la colonne entre 0 et 9")
        S = input("Veuillez entrer une position correcte \n" )
    else:
        return (ord(S[0]) - 97, int(S[2]))


# 2 La Flotte

# Question 1

def nouveau_bateau1(flotte, nom, taille, pos, orientation):
    (a, b) = pos
    if orientation == "h":
        posi = []
        for i in range(taille):
            posi.append((a, b + i))
        flotte.append({"nom": nom, "taille": taille, "cases touchés":
            0, "positions": posi})
    else:
        posi = []
        for i in range(taille):
            posi.append((a + i, b))
        flotte.append({"nom": nom, "taille": taille, "cases touchés":
            0, "positions": posi})


# Question 2

def presence_bateau(pos, flotte):
    trouver = False
    i = 0
    nb_bateaux = len(flotte)
    while i < nb_bateaux and not trouver:
        j = 0
        while j < flotte[i]["taille"] and not trouver:
            trouver = pos == flotte[i]["positions"][j]
            j += 1
        i += 1
    return trouver


# Question 3

def plot_flotte_grid(m, flotte):
    for i in range(len(flotte)):
        k = flotte[i]["taille"]
        for j in range(k):
            (a, b) = flotte[i]["positions"][j]
            m[a][b] = BATEAU
    plot_grid(m)


# Question 4 et 5 et 7

def input_ajout_bateau(flotte, nom, taille):
    pos = input("Veuillez entre une position \n")
    pos = pos_from_string(pos)
    while presence_bateau(pos, flotte):
        print("un bateau est présent ici")
        pos = pos_from_string(pos)
    orientation = input("Veuillez entrer une orientation \n")
    while orientation != "h" and orientation != "v":
        orientation = input("Veuillez entrer une orientation \n")
    return nouveau_bateau(flotte, nom, taille, pos, orientation)


# Question 6

def nouveau_bateau(flotte, nom, taille, pos, orientation):  # on appelle ajout bateau dans input ajout bateau qui lui nous informe de l'eventuelle erreur
    (a, b) = pos
    if orientation == "h":
        if 10 - b < taille:
            print("Le bateau ne peut pas etre placé ici car il sort du tableau")
            return False
        else:
            posi = []
            for i in range(taille):
                posi.append((a, b + i))
            used_spot = False
            c = 0
            while not used_spot and c < taille:
                k = 0
                l = len(flotte)
                while not used_spot and k < l:
                    n = 0
                    m = flotte[k]["taille"]
                    while not used_spot and n < m:
                        used_spot = (flotte[k]["positions"][n] == posi[c])
                        n += 1
                    k += 1
                c += 1
            if not used_spot:
                flotte.append({"nom": nom, "taille": taille, "cases touchés": 0, "positions": posi})
                return True
            else:
                return False
    else:
        if 10 - a < taille:
            print("Le bateau ne peut pas etre placé ici car il sort du tableau")
            return False
        else:
            posi = []
            for i in range(taille):
                posi.append((a + i, b))
            used_spot = False
            c = 0
            while not used_spot and c < taille:
                k = 0
                l = len(flotte)
                while not used_spot and k < l:
                    n = 0
                    m = flotte[k]["taille"]
                    while not used_spot and n < m:
                        used_spot = (flotte[k]["positions"][n] == posi[c])
                        n += 1
                    k += 1
                c += 1
            if not used_spot:
                flotte.append({"nom": nom, "taille": taille, "cases touchés": 0, "positions": posi})
                return True
            else:
                return False


# Question 8

def init_joueur():
    flotte = []
    for i in range(len(NOMS)):
        continuer = input_ajout_bateau(flotte, NOMS[i], TAILLES[i])
        while not continuer:
            continuer = input_ajout_bateau(flotte, NOMS[i], TAILLES[i])
    m = create_grid()
    return (m, flotte)


# Question 9

def nouveau_bateau_ia(flotte, nom, taille, pos, orientation):  # même fonction qu'avant sans le print d'erreur car il s'agit de l'IA
    (a, b) = pos
    if orientation == "h":
        if 10 - b < taille:
            return False
        else:
            posi = []
            for i in range(taille):
                posi.append((a, b + i))
            used_spot = False
            c = 0
            while not used_spot and c < taille:
                k = 0
                l = len(flotte)
                while not used_spot and k < l:
                    n = 0
                    m = flotte[k]["taille"]
                    while not used_spot and n < m:
                        used_spot = (flotte[k]["positions"][n] == posi[c])
                        n += 1
                    k += 1
                c += 1
            if not used_spot:
                flotte.append({"nom": nom, "taille": taille, "cases touchés": 0, "positions": posi})
                return True
            else:
                return False
    else:
        if 10 - a < taille:
            return False
        else:
            posi = []
            for i in range(taille):
                posi.append((a + i, b))
            used_spot = False
            c = 0
            while not used_spot and c < taille:
                k = 0
                l = len(flotte)
                while not used_spot and k < l:
                    n = 0
                    m = flotte[k]["taille"]
                    while not used_spot and n < m:
                        used_spot = (flotte[k]["positions"][n] == posi[c])
                        n += 1
                    k += 1
                c += 1
            if not used_spot:
                flotte.append({"nom": nom, "taille": taille, "cases touchés": 0, "positions": posi})
                return True
            else:
                return False

from random import choice


def init_ia():
    flotte_ia = []
    for i in range(len(NOMS)):
        pos = random_position()
        lettre = choice([0, 14])
        ajout = nouveau_bateau_ia(flotte_ia, NOMS[i], TAILLES[i], pos, chr(104 + lettre))
        while not ajout:
            pos = random_position()
            ajout = nouveau_bateau_ia(flotte_ia, NOMS[i], TAILLES[i], pos, chr(104 + lettre))  # remplacer
    m = create_grid()
    return (m, flotte_ia)


# 3 Touché coulé

# Question 1 et 2

def tir1(pos, m, flotte):
    if m[pos[0]][pos[1]] == VIDE:
        m[pos[0]][pos[1]] = EAU
        print("MANQUE")
        return True
    elif m[pos[0]][pos[1]] == BATEAU:
        m[pos[0]][pos[1]] = TOUCHE
        print("TOUCHE")
        return True
    else:
        return False


# Question 3

def id_bateau_at_pos(pos, flotte):
    trouver = False
    i = 0
    nb_bateaux = len(flotte)
    while i < nb_bateaux and not trouver:
        j = 0
        while j < flotte[i]["taille"] and not trouver:
            trouver = pos == flotte[i]["positions"][j]
            j += 1
        i += 1
    return i - 1 if trouver else None


# Question 4

def tir1(pos, m, flotte):
    if m[pos[0]][pos[1]] == VIDE:
        m[pos[0]][pos[1]] = EAU
        print("MANQUE")
        return True
    elif m[pos[0]][pos[1]] == BATEAU:
        flotte[id_bateau_at_pos(pos, flotte)]["cases touchés"] += 1
        m[pos[0]][pos[1]] = TOUCHE
        print("TOUCHE")
        return True
    else:
        return False


# Question 5

def tir(pos, m, flotte):
    if m[pos[0]][pos[1]] == VIDE:
        i = id_bateau_at_pos(pos, flotte)
        if i != None:
            flotte[i]["cases touchés"] += 1
            if flotte[i]["cases touchés"] == flotte[i]["taille"]:
                for j in range(flotte[i]["taille"]):
                    m[flotte[i]["positions"][j][0]][flotte[i]["positions"][j][1]] = DETRUIT
                print(flotte[i]["nom"])
                print(bcolors.FAIL + "TOUCHE COULE" + bcolors.ENDC)
                flotte.pop(i)
                return True
            else:
                m[pos[0]][pos[1]] = TOUCHE
                print(bcolors.OKCYAN + "TOUCHE" + bcolors.ENDC)
            return True
        else:
            m[pos[0]][pos[1]] = EAU
            print(bcolors.OKGREEN + "MANQUE" + bcolors.ENDC)
            return True
    else:
        return False


# partie 4

# Question 1

def tour_ia_random(m, flotte):
    tirer = tir(random_position(), m, flotte)
    while not tirer:
        tirer = tir(random_position(), m, flotte)


# Question 2

def tour_joueur(nom, m, flotte):
    pos = input()
    pos = pos_from_string(pos)
    tirer = tir(pos, m, flotte)
    while not tirer:
        pos = pos_from_string(pos)
        tirer = tir(pos, m, flotte)


# Question 3
#sous fonction pour l'IA afin de parcourir la matrice lorsque l'on a tiré sur 4 cases autour de la case touchée pour savoir si on en a touché une autre

def cases_touchees(m,i,j,new):
    trouver = False
    l = len(m)
    if not new:
        if j< 8:
            j+=1
        else:
            i+=1
            j=0
    while not trouver and i < l:
        while not trouver and j < l:
            trouver = (m[i][j] == TOUCHE)
            if not trouver:
                j += 1
        if not trouver:
            j =0
            i += 1
    return (trouver,i,j)


 # faites ainsi pour expliciter tous les cas
def tour_ia_better_random(m,flotte):
    (trouver, i, j)=cases_touchees(m,0,0,True)
    tire = True
    while tire and trouver and i != 9 and j !=9 :
        if i < 1:
            if j < 1:
                if tir((i, j + 1), m, flotte):
                    tire = False
                elif tir((i + 1, j), m, flotte):
                    tire = False
                else:
                    (trouver, i, j) = cases_touchees(m,i,j, False)
            elif j > 8:
                if tir((i, j - 1), m, flotte):
                    tire = False
                elif tir((i + 1, j), m, flotte):
                    tire = False
                else:
                    (trouver, i, j) = cases_touchees(m,i,j, False)
            else:
                if tir((i + 1, j), m, flotte):
                    tire = False
                elif tir((i, j - 1), m, flotte):
                    tire = False
                elif  tir((i, j + 1), m, flotte):
                    tire = False
                else:
                    (trouver, i, j) = cases_touchees(m,i,j, False)
        elif i > 8:
            if j < 1:
                if tir((i - 1, j), m, flotte):
                    tire = False
                elif tir((i, j + 1), m, flotte):
                    tire = False
                else:
                    (trouver, i, j) = cases_touchees(m,i,j, False)
            elif j > 8:
                if tir((i - 1, j), m, flotte):
                    tire = False
                elif tir((i, j - 1), m, flotte):
                    tire = False
                else:
                    (trouver, i, j) = cases_touchees(m,i,j, False)
            else:
                if tir((i - 1, j), m, flotte):
                    tire = False
                elif tir((i, j + 1), m, flotte):
                    tire = False
                elif tir((i, j - 1), m, flotte):
                    tire = False
                else:
                    (trouver, i, j) = cases_touchees(m,i,j, False)
        else:
            if j < 1:
                if tir((i - 1, j), m, flotte):
                    tire = False
                elif tir((i + 1, j), m, flotte):
                    tire = False
                elif tir((i, j + 1), m, flotte):
                    tire = False
                else:
                    (trouver, i, j) = cases_touchees(m,i,j, False)
            elif j > 8:
                if tir((i - 1, j), m, flotte):
                    tire = False
                elif tir((i + 1, j), m, flotte):
                    tire = False
                elif tir((i, j - 1), m, flotte):
                    tire = False
                else:
                    (trouver, i, j) = cases_touchees(m,i,j, False)
            else:
                if tir((i - 1, j), m, flotte):
                    tire = False
                elif tir((i + 1, j), m, flotte):
                    tire = False
                elif tir((i, j - 1), m, flotte):
                    tire = False
                elif tir((i, j + 1), m, flotte):
                    tire = False
                else:
                    (trouver, i, j) = cases_touchees(m,i,j, False)
    if not trouver:
        tour_ia_random(m, flotte)


# Question 4

def test_fin_partie(nom, m, flotte, nb_tour):
    if len(flotte) == 0:
        print()
        print(nom + " a gagné en " + str(nb_tour) + " tours.")
        exit()
        return True
    else:
        return False


# Question 5

def joueur_vs_ia(name):
    (m_ia, flotte_ia) = init_ia()
    (m_joueur, flotte_joueur) = init_joueur()
    finie = False
    joueur = 1
    nb_tour = 0
    while not finie:
        nb_tour += 1
        if joueur == 1:
            tour_joueur(name, m_joueur, flotte_ia)
            plot_grid(m_joueur)
            joueur -= 1
            finie = test_fin_partie(name, m_joueur, flotte_ia, nb_tour)
        else:
            tour_ia_better_random(m_ia, flotte_joueur)
            plot_grid(m_ia)
            joueur += 1
            finie = test_fin_partie("IA", m_ia, flotte_joueur, nb_tour)



# Question 6

def hide():
    for i in range(100): #pris aussi large pour prendre en charge toute taille d'écran
        print()

import time

def deux_joueurs(name1,name2):
    (m_j1, flotte_j1) = init_joueur()
    hide()
    (m_j2, flotte_j2) = init_joueur()
    finie = False
    joueur = 1
    nb_tour = 0
    while not finie:
        hide()
        nb_tour += 1
        if joueur == 1:
            tour_joueur(name1, m_j2, flotte_j2)
            plot_grid(m_j2)
            joueur -= 1
            finie = test_fin_partie(name1, m_j1, flotte_j2, nb_tour)
            time.sleep(10)
        else:
            tour_joueur(name2, m_j1, flotte_j1)
            plot_grid(m_j1)
            joueur += 1
            finie = test_fin_partie(name2, m_j2, flotte_j1, nb_tour)
            time.sleep(10)


# Question 7

#Règles
def regless():
    print("La bataille navale est un jeu qui oppose 2 joueurs et se joue par conséquent obliagtoirement à 2 ou bien seul contre un bot.")
    print("Chaque joueur possède :")
    print("- 1 plateau de 10 lignes numérotées de a à j et 10 colones numérotées de 0 à 9")
    print("- une flotte composée de :")
    print("     - 1 Transporteur (bateau de 5 cases)")
    print("     - 1 Cuirassé (bateau de 4 cases)")
    print("     - 1 Croiseur (bateau de 3 cases)")
    print("     - 1 Sous-marin (bateau de 3 cases)")
    print("     - 1 Destructeur (bateau de 2 cases)")
    print("Tout d'abord chaque joueur place sa flotte sur son plateau de jeu.")
    print("Ensuite, chaque joueur chacun leur tour cite une case du plateau adverse ce qui constitue une attaque tout en respectant bien la syntaxe proposée (lettre puis un espace puis le chiffre, exemple :h 5).")
    print("Si le tir ne touche pas de bateau alors c'est manqué!")
    print("Si le bateau est touché mais est encore debout c'est touché!")
    print("Si le tir touche la dernière case d'un même bateau alors c'est touché-coulé et le bateau en question est éliminé.")
    print("Le but est simple, le premier à faire couler tous les bateaux adverses gagne.")
    print("")
    print("")


def game(): #fonction principale du jeu
    print("Bienvenue au projet bataille navale développée par Bilal-Rayane MAJJAD")
    print("Voulez vous connaitre les règles avant de jouer?")
    print("Appuyez sur entrée si oui, taper quelquechose sinon ")
    regles= input()
    if regles ==  "" :
        regless()
    print("Voulez-vous jouer a 1 ou 2 personnes? ")
    print("Veuillez répondre 1 ou 2 s'il vous plait! ")
    number_of_player= input()
    while  number_of_player != "1" and number_of_player != "2":
        print("Voulez-vous jouer a 1 ou 2 personnes?"  "Veuillez répondre 1 ou 2 s'il vous plait")
        print("Veuillez répondre 1 ou 2 s'il vous plait ")
        number_of_player = input()
    if number_of_player == "1":
        print("Entrez votre nom : ")
        name = input()
        print("Confirmez vous que votre nom est le suivant : " + name  )
        print("Appuyez sur entrée pour confirmer taper quelquechose sinon ")
        confirm = input()
        while confirm != "":
            print("Entrez votre nom : ")
            name = input()
            print("Confirmez vous que votre nom est le suivant : " + name)
            print("Appuyez sur entrée pour confirmer taper quelquechose sinon ")
            confirm = input()
        print("Bonne partie à vous!")
        joueur_vs_ia(name)
    else:
        print("Joueur 1, entrez votre nom : ")
        name1 = input()
        print("Confirmez vous que votre nom est le suivant : " + name1)
        print("Appuyez sur entrée pour confirmer taper quelquechose sinon ")
        confirm = input()
        while confirm != "":
            print("Entrez votre nom :")
            name1 = input()
            print("Confirmez vous que votre nom est le suivant : " + name1)
            print("Appuyez sur entrée pour confirmer taper quelquechose sinon ")
            confirm = input()
        print("Bonne partie à vous!")
        print("Joueur 2, entrez votre nom :")
        name2 = input()
        print("Confirmez vous que votre nom est le suivant : " + name2)
        print("Appuyez sur entrée pour confirmer taper quelquechose sinon ")
        confirm = input()
        while confirm != "":
            print("Entrez votre nom :")
            name2 = input()
            print("Confirmez vous que votre nom est le suivant : " + name2)
            print("Appuyez sur entrée pour confirmer taper quelquechose sinon ")
            confirm = input()
        print("Bonne partie à vous!")
        deux_joueurs(name1,name2)

game()