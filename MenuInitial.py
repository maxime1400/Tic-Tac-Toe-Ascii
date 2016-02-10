'''
Created on 2014-12-19

@author: Maxime
'''

from Effacer import *
from Jouer import *


def MenuInitial():

    print("")
    print(" █████  █   ████         █████    █     ████         █████   ███   ████")
    print("   █    █  █       ███     █     █ █   █               █    █   █  █")
    print("   █    █  █               █    █████  █       ███     █    █   █  ███")
    print("   █    █  █               █    █   █  █               █    █   █  █")
    print("   █    █   ████           █    █   █   ████           █     ███   ████")
    print("")
    print(" 1- JOUER")
    print(" 0- QUITTER")
    
    rep = input(" Que voulez-vous faire: ")
    
    if rep == "1":
        cls()
        Tableau()
    elif rep == "0":
        input("\n Fin de l'application")