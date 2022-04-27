#This project was realised by Bilal-Rayane MAJJAD
#N.B. : be sure to run under Linux or Python IDE such as pycharm (tested) to avoid display problems with colors : bicolors 

N = 10
COLUMNS = [str(i) for i in range(N)]
LINES = [' '] + list(map(chr, range(97, 107)))
DICT_LINES_INT = {LINES[i]: i - 1 for i in range(len(LINES))}
EMPTY = '.'
WATER = 'o'
HIT = 'x'
SHIP = '#'
DESTROYED = '@'
NAMES = ['Carrier', 'Dreadnought', 'Cruiser', 'Submarine', 'Destroyer']
SIZES = [5, 4, 3, 3, 2]


# 1 CARTE ET TIR
# 1 MAP AND SHOOTING

# Question 1

def create_grid():
    L = []
    for i in range(N + 1):
        l = []
        for j in range(N + 1):
            l.append(EMPTY)
        L.append(l)
    return L


# Question 2

def plot_grid1(L): #initial version w/o colors
    for i in range(10):
        print(" " + COLUMNS[i], end="")
    print()
    for k in range(1, N + 1):
        c = LINES[k]
        for j in range(N):
            c += " " + L[k - 1][j]
        print(c)


class bcolors: #for question 5 with colors
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    OKBLUE = '\033[94m'

def plot_grid(L):
    for i in range(10):
        print(" " , end="")
        print(bcolors.WARNING + COLUMNS[i] + bcolors.ENDC , end="")
    print()
    for k in range(1, N + 1):
        print(bcolors.WARNING + LINES[k] + bcolors.ENDC , end="")
        for j in range(N):
            print(" ", end="")
            if L[k - 1][j] == EMPTY:
                print(L[k - 1][j], end="")
            elif L[k - 1][j] == WATER:
                print(bcolors.OKGREEN + WATER + bcolors.ENDC , end="")
            elif L[k - 1][j] == HIT:
                print(bcolors.OKCYAN + HIT + bcolors.ENDC , end="")
            elif L[k - 1][j] ==SHIP:
                print(bcolors.OKBLUE + SHIP + bcolors.ENDC , end="")
            else :
                print(bcolors.FAIL + DESTROYED + bcolors.ENDC , end="")
        print()

# Question 3

def tir1(m, pos):
    m[pos[0]][pos[1]] = WATER


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
        print("You must respect the following format, line between a and j followed by a space then a number representing the column between 0 and 9")
        S = input("Please enter a correct position \n")
    else:
        return (ord(S[0]) - 97, int(S[2]))


# Question 8

def pos2_from_string(S,L): #finalement, cas traité lors du tir et donc non besoin de vérifier ici, il vérifier si la case dans la matrice n'était pas à "EMPTY"
    while len(S) != 3 or ord(S[0]) < 97 or ord(S[0]) > 106 or S[1] != ' ' or ord(S[2]) < 48 or ord(S[2]) > 57 or (
            L[ord(S[0]) - 97][int(S[2])] != EMPTY):
        print("You must respect the following format, line between a and j followed by a space then a number representing the column between 0 and 9")
        S = input("Please enter a correct position \n" )
    else:
        return (ord(S[0]) - 97, int(S[2]))


# 2 La fleet

# Question 1

def new_ship1(fleet, name, size, pos, orientation):
    (a, b) = pos
    if orientation == "h":
        posi = []
        for i in range(size):
            posi.append((a, b + i))
        fleet.append({"name": name, "size": size, "cells hit":
            0, "positions": posi})
    else:
        posi = []
        for i in range(size):
            posi.append((a + i, b))
        fleet.append({"name": name, "size": size, "cells hit":
            0, "positions": posi})


# Question 2

def presence_SHIP(pos, fleet):
    trouver = False
    i = 0
    nb_SHIP = len(fleet)
    while i < nb_SHIP and not trouver:
        j = 0
        while j < fleet[i]["size"] and not trouver:
            trouver = pos == fleet[i]["positions"][j]
            j += 1
        i += 1
    return trouver


# Question 3

def plot_fleet_grid(m, fleet):
    for i in range(len(fleet)):
        k = fleet[i]["size"]
        for j in range(k):
            (a, b) = fleet[i]["positions"][j]
            m[a][b] = SHIP
    plot_grid(m)


# Question 4 et 5 et 7

def input_ajout_SHIP(fleet, name, size):
    pos = input("Please enter a position \n")
    pos = pos_from_string(pos)
    while presence_SHIP(pos, fleet):
        print("a ship is already here")
        pos = pos_from_string(pos)
    orientation = input("Please enter en orientation \n")
    while orientation != "h" and orientation != "v":
        orientation = input("Please enter en orientation \n")
    return new_ship(fleet, name, size, pos, orientation)


# Question 6

def new_ship(fleet, name, size, pos, orientation):  # on appelle ajout SHIP dans input ajout SHIP qui lui nous informe de l'eventuelle erreur
    (a, b) = pos
    if orientation == "h":
        if 10 - b < size:
            print("The ship can not be placed here as it goes out of the grid")
            return False
        else:
            posi = []
            for i in range(size):
                posi.append((a, b + i))
            used_spot = False
            c = 0
            while not used_spot and c < size:
                k = 0
                l = len(fleet)
                while not used_spot and k < l:
                    n = 0
                    m = fleet[k]["size"]
                    while not used_spot and n < m:
                        used_spot = (fleet[k]["positions"][n] == posi[c])
                        n += 1
                    k += 1
                c += 1
            if not used_spot:
                fleet.append({"name": name, "size": size, "cells hit": 0, "positions": posi})
                return True
            else:
                return False
    else:
        if 10 - a < size:
            print("The ship can not be placed here as it goes out of the grid")
            return False
        else:
            posi = []
            for i in range(size):
                posi.append((a + i, b))
            used_spot = False
            c = 0
            while not used_spot and c < size:
                k = 0
                l = len(fleet)
                while not used_spot and k < l:
                    n = 0
                    m = fleet[k]["size"]
                    while not used_spot and n < m:
                        used_spot = (fleet[k]["positions"][n] == posi[c])
                        n += 1
                    k += 1
                c += 1
            if not used_spot:
                fleet.append({"name": name, "size": size, "cells hit": 0, "positions": posi})
                return True
            else:
                return False


# Question 8

def init_player():
    fleet = []
    for i in range(len(NAMES)):
        continuer = input_ajout_SHIP(fleet, NAMES[i], SIZES[i])
        while not continuer:
            continuer = input_ajout_SHIP(fleet, NAMES[i], SIZES[i])
    m = create_grid()
    return (m, fleet)


# Question 9

def new_ship_ia(fleet, name, size, pos, orientation):  # same function than before w/o error print since it's used for the AI
    (a, b) = pos
    if orientation == "h":
        if 10 - b < size:
            return False
        else:
            posi = []
            for i in range(size):
                posi.append((a, b + i))
            used_spot = False
            c = 0
            while not used_spot and c < size:
                k = 0
                l = len(fleet)
                while not used_spot and k < l:
                    n = 0
                    m = fleet[k]["size"]
                    while not used_spot and n < m:
                        used_spot = (fleet[k]["positions"][n] == posi[c])
                        n += 1
                    k += 1
                c += 1
            if not used_spot:
                fleet.append({"name": name, "size": size, "cells hit": 0, "positions": posi})
                return True
            else:
                return False
    else:
        if 10 - a < size:
            return False
        else:
            posi = []
            for i in range(size):
                posi.append((a + i, b))
            used_spot = False
            c = 0
            while not used_spot and c < size:
                k = 0
                l = len(fleet)
                while not used_spot and k < l:
                    n = 0
                    m = fleet[k]["size"]
                    while not used_spot and n < m:
                        used_spot = (fleet[k]["positions"][n] == posi[c])
                        n += 1
                    k += 1
                c += 1
            if not used_spot:
                fleet.append({"name": name, "size": size, "cells hit": 0, "positions": posi})
                return True
            else:
                return False

from random import choice


def init_ai():
    fleet_ia = []
    for i in range(len(NAMES)):
        pos = random_position()
        lettre = choice([0, 14])
        ajout = new_ship_ia(fleet_ia, NAMES[i], SIZES[i], pos, chr(104 + lettre))
        while not ajout:
            pos = random_position()
            ajout = new_ship_ia(fleet_ia, NAMES[i], SIZES[i], pos, chr(104 + lettre))  
    m = create_grid()
    return (m, fleet_ia)


# 3 Touché coulé

# Question 1 et 2

def tir1(pos, m, fleet):
    if m[pos[0]][pos[1]] == EMPTY:
        m[pos[0]][pos[1]] = WATER
        print("MISSED")
        return True
    elif m[pos[0]][pos[1]] == SHIP:
        m[pos[0]][pos[1]] = HIT
        print("HIT")
        return True
    else:
        return False


# Question 3

def id_SHIP_at_pos(pos, fleet):
    trouver = False
    i = 0
    nb_SHIPx = len(fleet)
    while i < nb_SHIPx and not trouver:
        j = 0
        while j < fleet[i]["size"] and not trouver:
            trouver = pos == fleet[i]["positions"][j]
            j += 1
        i += 1
    return i - 1 if trouver else None


# Question 4

def tir1(pos, m, fleet):
    if m[pos[0]][pos[1]] == EMPTY:
        m[pos[0]][pos[1]] = WATER
        print("MANQUE")
        return True
    elif m[pos[0]][pos[1]] == SHIP:
        fleet[id_SHIP_at_pos(pos, fleet)]["cells hit"] += 1
        m[pos[0]][pos[1]] = HIT
        print("HIT")
        return True
    else:
        return False


# Question 5

def tir(pos, m, fleet):
    if m[pos[0]][pos[1]] == EMPTY:
        i = id_SHIP_at_pos(pos, fleet)
        if i != None:
            fleet[i]["cells hit"] += 1
            if fleet[i]["cells hit"] == fleet[i]["size"]:
                for j in range(fleet[i]["size"]):
                    m[fleet[i]["positions"][j][0]][fleet[i]["positions"][j][1]] = DESTROYED
                print(fleet[i]["name"])
                print(bcolors.FAIL + "HIT AND SUNK" + bcolors.ENDC)
                fleet.pop(i)
                return True
            else:
                m[pos[0]][pos[1]] = HIT
                print(bcolors.OKCYAN + "HIT" + bcolors.ENDC)
            return True
        else:
            m[pos[0]][pos[1]] = WATER
            print(bcolors.OKGREEN + "MANQUE" + bcolors.ENDC)
            return True
    else:
        return False


# partie 4

# Question 1

def turn_ia_random(m, fleet):
    tirer = tir(random_position(), m, fleet)
    while not tirer:
        tirer = tir(random_position(), m, fleet)


# Question 2

def turn_joueur(name, m, fleet):
    pos = input()
    pos = pos_from_string(pos)
    tirer = tir(pos, m, fleet)
    while not tirer:
        pos = pos_from_string(pos)
        tirer = tir(pos, m, fleet)


# Question 3
#sub-function for the AI to browse the matrix when you have drawn on 4 squares around the hit square to know if you have hit another one

def hit_cells(m,i,j,new):
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
            trouver = (m[i][j] == HIT)
            if not trouver:
                j += 1
        if not trouver:
            j =0
            i += 1
    return (trouver,i,j)


 # made this way to explicit all the cases
 #some cases can be merged
def turn_ia_better_random(m,fleet):
    (trouver, i, j)=hit_cells(m,0,0,True)
    tire = True
    while tire and trouver and i != 9 and j !=9 :
        if i < 1:
            if j < 1:
                if tir((i, j + 1), m, fleet):
                    tire = False
                elif tir((i + 1, j), m, fleet):
                    tire = False
                else:
                    (trouver, i, j) = hit_cells(m,i,j, False)
            elif j > 8:
                if tir((i, j - 1), m, fleet):
                    tire = False
                elif tir((i + 1, j), m, fleet):
                    tire = False
                else:
                    (trouver, i, j) = hit_cells(m,i,j, False)
            else:
                if tir((i + 1, j), m, fleet):
                    tire = False
                elif tir((i, j - 1), m, fleet):
                    tire = False
                elif  tir((i, j + 1), m, fleet):
                    tire = False
                else:
                    (trouver, i, j) = hit_cells(m,i,j, False)
        elif i > 8:
            if j < 1:
                if tir((i - 1, j), m, fleet):
                    tire = False
                elif tir((i, j + 1), m, fleet):
                    tire = False
                else:
                    (trouver, i, j) = hit_cells(m,i,j, False)
            elif j > 8:
                if tir((i - 1, j), m, fleet):
                    tire = False
                elif tir((i, j - 1), m, fleet):
                    tire = False
                else:
                    (trouver, i, j) = hit_cells(m,i,j, False)
            else:
                if tir((i - 1, j), m, fleet):
                    tire = False
                elif tir((i, j + 1), m, fleet):
                    tire = False
                elif tir((i, j - 1), m, fleet):
                    tire = False
                else:
                    (trouver, i, j) = hit_cells(m,i,j, False)
        else:
            if j < 1:
                if tir((i - 1, j), m, fleet):
                    tire = False
                elif tir((i + 1, j), m, fleet):
                    tire = False
                elif tir((i, j + 1), m, fleet):
                    tire = False
                else:
                    (trouver, i, j) = hit_cells(m,i,j, False)
            elif j > 8:
                if tir((i - 1, j), m, fleet):
                    tire = False
                elif tir((i + 1, j), m, fleet):
                    tire = False
                elif tir((i, j - 1), m, fleet):
                    tire = False
                else:
                    (trouver, i, j) = hit_cells(m,i,j, False)
            else:
                if tir((i - 1, j), m, fleet):
                    tire = False
                elif tir((i + 1, j), m, fleet):
                    tire = False
                elif tir((i, j - 1), m, fleet):
                    tire = False
                elif tir((i, j + 1), m, fleet):
                    tire = False
                else:
                    (trouver, i, j) = hit_cells(m,i,j, False)
    if not trouver:
        turn_ia_random(m, fleet)


# Question 4

def test_endgame(name, m, fleet, nb_turn):
    if len(fleet) == 0:
        print()
        print(name + " won in" + str(nb_turn) + " turns.")
        exit()
        return True
    else:
        return False


# Question 5

def joueur_vs_ia(name):
    (m_ia, fleet_ia) = init_ai()
    (m_joueur, fleet_joueur) = init_player()
    finie = False
    joueur = 1
    nb_turn = 0
    while not finie:
        nb_turn += 1
        if joueur == 1:
            turn_joueur(name, m_joueur, fleet_ia)
            plot_grid(m_joueur)
            joueur -= 1
            finie = test_endgame(name, m_joueur, fleet_ia, nb_turn)
        else:
            turn_ia_better_random(m_ia, fleet_joueur)
            plot_grid(m_ia)
            joueur += 1
            finie = test_endgame("IA", m_ia, fleet_joueur, nb_turn)



# Question 6

def hide():
    for i in range(100): #pris aussi large pour prendre en charge toute size d'écran
        print()

import time

def two_players(name1,name2):
    (m_j1, fleet_j1) = init_player()
    hide()
    (m_j2, fleet_j2) = init_player()
    finie = False
    joueur = 1
    nb_turn = 0
    while not finie:
        hide()
        nb_turn += 1
        if joueur == 1:
            turn_joueur(name1, m_j2, fleet_j2)
            plot_grid(m_j2)
            joueur -= 1
            finie = test_endgame(name1, m_j1, fleet_j2, nb_turn)
            time.sleep(10)
        else:
            turn_joueur(name2, m_j1, fleet_j1)
            plot_grid(m_j1)
            joueur += 1
            finie = test_endgame(name2, m_j2, fleet_j1, nb_turn)
            time.sleep(10)


# Question 7

#Règles
def regless():
    print("Battleship is a 2 player game and is therefore always played with 2 players or alone against a bot.")
    print("Each player has:")
    print("- 1 board of 10 lines numbered from a to j and 10 columns numbered from 0 to 9")
    print("- a fleet is made of :")
    print("     - 1 Carrier (ship of 5 cells)")
    print("     - 1 Dreadnought  (ship of 4 cells)")
    print("     - 1 Cruiser (ship of 3 cells)")
    print("     - 1 Submarine (ship of 3 cells)")
    print("     - 1 Destroyer (ship of 2 cells)")
    print("First, each player places his fleet on his board.)")
    print("Then, each player in turn names a square on the opponent's board, which constitutes an attack, while respecting the following syntax (letter then a space then the number, e.g. :h 5).")
    print("If the shot does not hit a boat then it is a miss,")
    print("If the boat is hit but is still standing it is hit,")
    print("If the shot hits the last square of the same boat, it is a hit and the boat in question is eliminated.")
    print("The goal is simple, the first to sink all the opposing boats wins. ")
    print("")
    print("")


def game(): #fonction principale du jeu
    print("Welcome to the Battleship Project developed by Bilal MAJJAD")
    print("Do you want to know the rules before playing?")
    print("Press enter if yes,otherwise type anything else ")
    regles= input()
    if regles ==  "" :
        regless()
    print("Do you want to play with 1 or 2 people?")
    print("Please answer 1 or 2")
    number_of_player= input()
    while  number_of_player != "1" and number_of_player != "2":
        print("Do you want to play with 1 or 2 people?")
        print("Please answer 1 or 2")
        number_of_player = input()
    if number_of_player == "1":
        print("Enter your name : ")
        name = input()
        print("Confirm that your name is the following: " + name  )
        print("Press enter if yes,otherwise type anything else ")
        confirm = input()
        while confirm != "":
            print("Enter your name : ")
            name = input()
            print("Confirm that your name is the following: " + name  )
            print("Press enter if yes,otherwise type anything else ")
            confirm = input()
            print("Bonne partie à vous!")
        joueur_vs_ia(name)
    else:
        print("Player 1, enter your name : ")
        name1 = input()
        print("Confirm that your name is the following: " + name1  )
        print("Press enter if yes,otherwise type anything else ")
        confirm = input()
        while confirm != "":
            print("Enter your name :")
            name1 = input()
            print("Confirm that your name is the following: " + name1  )
            print("Press enter if yes,otherwise type anything else ")
            confirm = input()
        print("Have a good game!")
        print("Player 2, enter your name :")
        name2 = input()
        print("Confirm that your name is the following: " + name2  )
        print("Press enter if yes,otherwise type anything else ")
        confirm = input()
        while confirm != "":
            print("Entrez votre name :")
            name2 = input()
            print("Confirm that your name is the following: " + name2  )
            print("Press enter if yes,otherwise type anything else ")
            confirm = input()
        print("Have a good game!")
        two_players(name1,name2)

game()