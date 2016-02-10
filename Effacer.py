'''
Created on 2014-11-16

@author: Maxime
'''

'''Module avec la fonction qui efface l'écran.'''

'''SECTION IMPORTATION'''
import os


'''FONCTION'''
def cls():
    if os.name == 'posix':
        os.system('clear')

    elif os.name in ('ce', 'nt', 'dos'):
        os.system('cls')