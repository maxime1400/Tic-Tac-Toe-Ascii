'''
Created on 2014-12-16

@author: Maxime
'''

from Effacer import *

def Tableau():
    
    a1 = " "
    a2 = " "
    a3 = " "
    b1 = " "
    b2 = " "
    b3 = " "
    c1 = " "
    c2 = " "
    c3 = " "
    pos = ""
    rejouer = 0
    victoire = 0
    joueur = "X"
    ressaye = " "
    
    while victoire != 1 or pos != "0":
        
        #cls()
        print("\n Joueur", joueur ,"\n Appuyer sur entrée")
        input()
        pos = ""
        cls()
        
        while pos != "1" and pos != "2" and pos != "3" and pos != "4" and pos != "5" and pos != "6" and pos != "7" and pos != "8" and pos != "9" or rejouer != 0:
            
            cls()
            rejouer = 0
            ressaye = "0"
            print("\n\n Joueur",joueur,"\n")
        
            print("    JEU          POSITION")
            print("  ╔═╦═╦═╗        ┌─┬─┬─┐")
            print("  ║"+a1+"║"+a2+"║"+a3+"║        │7│8│9│")
            print("  ╠═╬═╬═╣        ├─┼─┼─┤")
            print("  ║"+b1+"║"+b2+"║"+b3+"║        │4│5│6│")
            print("  ╠═╬═╬═╣        ├─┼─┼─┤")
            print("  ║"+c1+"║"+c2+"║"+c3+"║        │1│2│3│")
            print("  ╚═╩═╩═╝        └─┴─┴─┘")
    
        
            print("\n À quelle position voulez-vous placer votre",'"'+joueur+'"'," \n 0 = Quitter")
            pos = input("")
        
            if pos != "1" and pos != "2" and pos != "3" and pos != "4" and pos != "5" and pos != "6" and pos != "7" and pos != "8" and pos != "9" and pos != "0":
                print("\n\n Position erronée:\n\n Assurez-vous d'avoir écrit un chiffre\n pas un nombre.")
                input(" Appuyez sur entrée pour rejouer")
                
            elif pos == "7":
                if a1 != " ":
                    print("\n\n Position erronée:\n\n Assurez-vous que la position n'est pas utilisée.")
                    rejouer = 1
                    input("\n Appuyez sur entrée pour rejouer")
                else:
                    cls()
                    a1 = joueur
                    print("\n\n\n")
                    print("  ╔═╦═╦═╗")
                    print("  ║"+a1+"║"+a2+"║"+a3+"║")
                    print("  ╠═╬═╬═╣")
                    print("  ║"+b1+"║"+b2+"║"+b3+"║")
                    print("  ╠═╬═╬═╣")
                    print("  ║"+c1+"║"+c2+"║"+c3+"║")
                    print("  ╚═╩═╩═╝")
                    if joueur == "X":
                        joueur = "O"
                    elif joueur == "O":
                        joueur = "X"
                        
                        
            elif pos == "8":
                if a2 != " ":
                    print("\n\n Position erronée:\n\n Assurez-vous que la position n'est pas utilisée.")
                    rejouer = 1
                    input("\n Appuyez sur entrée pour rejouer")
                else:
                    cls()
                    a2 = joueur
                    print("\n\n\n")
                    print("  ╔═╦═╦═╗")
                    print("  ║"+a1+"║"+a2+"║"+a3+"║")
                    print("  ╠═╬═╬═╣")
                    print("  ║"+b1+"║"+b2+"║"+b3+"║")
                    print("  ╠═╬═╬═╣")
                    print("  ║"+c1+"║"+c2+"║"+c3+"║")
                    print("  ╚═╩═╩═╝")
                    if joueur == "X":
                        joueur = "O"
                    elif joueur == "O":
                        joueur = "X"
                        
    
            elif pos == "9":
                if a3 != " ":
                    print("\n\n Position erronée:\n\n Assurez-vous que la position n'est pas utilisée.")
                    rejouer = 1
                    input("\n Appuyez sur entrée pour rejouer")
                else:
                    cls()
                    a3 = joueur
                    print("\n\n\n")
                    print("  ╔═╦═╦═╗")
                    print("  ║"+a1+"║"+a2+"║"+a3+"║")
                    print("  ╠═╬═╬═╣")
                    print("  ║"+b1+"║"+b2+"║"+b3+"║")
                    print("  ╠═╬═╬═╣")
                    print("  ║"+c1+"║"+c2+"║"+c3+"║")
                    print("  ╚═╩═╩═╝")
                    if joueur == "X":
                        joueur = "O"
                    elif joueur == "O":
                        joueur = "X"
                        

            elif pos == "4":
                if b1 != " ":
                    print("\n\n Position erronée:\n\n Assurez-vous que la position n'est pas utilisée.")
                    rejouer = 1
                    input("\n Appuyez sur entrée pour rejouer")
                else:
                    cls()
                    b1 = joueur
                    print("\n\n\n")
                    print("  ╔═╦═╦═╗")
                    print("  ║"+a1+"║"+a2+"║"+a3+"║")
                    print("  ╠═╬═╬═╣")
                    print("  ║"+b1+"║"+b2+"║"+b3+"║")
                    print("  ╠═╬═╬═╣")
                    print("  ║"+c1+"║"+c2+"║"+c3+"║")
                    print("  ╚═╩═╩═╝")
                    if joueur == "X":
                        joueur = "O"
                    elif joueur == "O":
                        joueur = "X"
                        
    
            elif pos == "5":
                if b2 != " ":
                    print("\n\n Position erronée:\n\n Assurez-vous que la position n'est pas utilisée.")
                    rejouer = 1
                    input("\n Appuyez sur entrée pour rejouer")
                else:
                    cls()
                    b2 = joueur
                    print("\n\n\n")
                    print("  ╔═╦═╦═╗")
                    print("  ║"+a1+"║"+a2+"║"+a3+"║")
                    print("  ╠═╬═╬═╣")
                    print("  ║"+b1+"║"+b2+"║"+b3+"║")
                    print("  ╠═╬═╬═╣")
                    print("  ║"+c1+"║"+c2+"║"+c3+"║")
                    print("  ╚═╩═╩═╝")
                    if joueur == "X":
                        joueur = "O"
                    elif joueur == "O":
                        joueur = "X"
                        
    
            elif pos == "6":
                if b3 != " ":
                    print("\n\n Position erronée:\n\n Assurez-vous que la position n'est pas utilisée.")
                    rejouer = 1
                    input("\n Appuyez sur entrée pour rejouer")
                else:
                    cls()
                    b3 = joueur
                    print("\n\n\n")
                    print("  ╔═╦═╦═╗")
                    print("  ║"+a1+"║"+a2+"║"+a3+"║")
                    print("  ╠═╬═╬═╣")
                    print("  ║"+b1+"║"+b2+"║"+b3+"║")
                    print("  ╠═╬═╬═╣")
                    print("  ║"+c1+"║"+c2+"║"+c3+"║")
                    print("  ╚═╩═╩═╝")
                    if joueur == "X":
                        joueur = "O"
                    elif joueur == "O":
                        joueur = "X"
                        

            elif pos == "1":
                if c1 != " ":
                    print("\n\n Position erronée:\n\n Assurez-vous que la position n'est pas utilisée.")
                    rejouer = 1
                    input("\n Appuyez sur entrée pour rejouer")
                else:
                    cls()
                    c1 = joueur
                    print("\n\n\n")
                    print("  ╔═╦═╦═╗")
                    print("  ║"+a1+"║"+a2+"║"+a3+"║")
                    print("  ╠═╬═╬═╣")
                    print("  ║"+b1+"║"+b2+"║"+b3+"║")
                    print("  ╠═╬═╬═╣")
                    print("  ║"+c1+"║"+c2+"║"+c3+"║")
                    print("  ╚═╩═╩═╝")
                    if joueur == "X":
                        joueur = "O"
                    elif joueur == "O":
                        joueur = "X"
                        

            elif pos == "2":
                if c2 != " ":
                    print("\n\n Position erronée:\n\n Assurez-vous que la position n'est pas utilisée.")
                    rejouer = 1
                    input("\n Appuyez sur entrée pour rejouer")
                else:
                    cls()
                    c2 = joueur
                    print("\n\n\n")
                    print("  ╔═╦═╦═╗")
                    print("  ║"+a1+"║"+a2+"║"+a3+"║")
                    print("  ╠═╬═╬═╣")
                    print("  ║"+b1+"║"+b2+"║"+b3+"║")
                    print("  ╠═╬═╬═╣")
                    print("  ║"+c1+"║"+c2+"║"+c3+"║")
                    print("  ╚═╩═╩═╝")
                    if joueur == "X":
                        joueur = "O"
                    elif joueur == "O":
                        joueur = "X"
                        

            elif pos == "3":
                if c3 != " ":
                    print("\n\n Position erronée:\n\n Assurez-vous que la position n'est pas utilisée.")
                    rejouer = 1
                    input("\n Appuyez sur entrée pour rejouer")
                else:
                    cls()
                    c3 = joueur
                    print("\n\n\n")
                    print("  ╔═╦═╦═╗")
                    print("  ║"+a1+"║"+a2+"║"+a3+"║")
                    print("  ╠═╬═╬═╣")
                    print("  ║"+b1+"║"+b2+"║"+b3+"║")
                    print("  ╠═╬═╬═╣")
                    print("  ║"+c1+"║"+c2+"║"+c3+"║")
                    print("  ╚═╩═╩═╝")
                    if joueur == "X":
                        joueur = "O"
                    elif joueur == "O":
                        joueur = "X"
                        
                    
            if a1 != " " and a2 != " " and a3 != " " and b1 != " " and b2 != " " and b3 != " " and c1 != " " and c2 != " " and c3 != " ":
                cls()
                print("\n Partie nul!\n")
                print("")
                print("  ╔═╦═╦═╗")
                print("  ║"+a1+"║"+a2+"║"+a3+"║")
                print("  ╠═╬═╬═╣")
                print("  ║"+b1+"║"+b2+"║"+b3+"║")
                print("  ╠═╬═╬═╣")
                print("  ║"+c1+"║"+c2+"║"+c3+"║")
                print("  ╚═╩═╩═╝")
                
                while ressaye != "1" and ressaye != "2":
                
                    print("\n Réessayer?")
                    print(" 1- Oui")
                    print(" 2- Non\n")
                    ressaye = input()
                    cls()

                    if ressaye != "1" and ressaye != "2":
                        print("\n\n RÉPONSE INVALIDE")
                    elif ressaye == "1":
                        a1 = " "
                        a2 = " "
                        a3 = " "
                        b1 = " "
                        b2 = " "
                        b3 = " "
                        c1 = " "
                        c2 = " "
                        c3 = " "
                        pos = ""
                        victoire = 0
                        joueur = "X"
                    elif ressaye == "2":
                        print("\n Fin de l'application")
                        input()
                        return()
                
            
            if pos == "0":
                input(" Fin de l'application")
                return()
            
                
            if a1==a2==a3!=" " or b1==b2==b3!=" " or c1==c2==c3!=" " or a1==b1==c1!=" " or a2==b2==c2!=" " or a3==b3==c3!=" " or a1==b2==c3!=" " or a3==b2==c1!=" ":
                cls()
                if joueur == "X":
                        joueur = "O"
                elif joueur == "O":
                        joueur = "X"
                print("\n FÉLICITATION\n\n\n Joueur "+joueur+", vous avez gagné")
                pos = "0"
                    
                print("  ╔═╦═╦═╗")
                print("  ║"+a1+"║"+a2+"║"+a3+"║")
                print("  ╠═╬═╬═╣")
                print("  ║"+b1+"║"+b2+"║"+b3+"║")
                print("  ╠═╬═╬═╣")
                print("  ║"+c1+"║"+c2+"║"+c3+"║")
                print("  ╚═╩═╩═╝")

                while ressaye != "1" and ressaye != "2":
                    print("\n Rejouer?")
                    print(" 1- Oui")
                    print(" 2- Non\n")
                    ressaye = input()
                    
                    if ressaye != "1" and ressaye != "2":
                        cls()
                        print("\n\n RÉPONSE INVALIDE")
                    elif ressaye == "1":
                        a1 = " "
                        a2 = " "
                        a3 = " "
                        b1 = " "
                        b2 = " "
                        b3 = " "
                        c1 = " "
                        c2 = " "
                        c3 = " "
                        pos = ""
                        victoire = 0
                        joueur = "X"
                    elif ressaye == "2":
                        victoire = 1
                        print(" Fin de l'application")
                        input()
                        return()