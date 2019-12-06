"""importing classes and methods"""
from Player import Player
from Sequence import Sequence
from GameController import GameController   

"""Welcome message display and reminder of rules and level of difficulty"""

print("############## BIENVENUE AUX JEUX DU SIMON ###############")
print("################ RAPPEL DES RÉGLES #######################")
print("Une série de nombre vont s'afficher avec un intervalle différent") 
print("selon le niveau de dificultés choisit et vous devrez retapez dans")
print("le terminal les nombres visualisé !")
print("################ NIVEAU DE DIFFICULTÉS ###################")
print("Voici les niveaux d'intervalles entre les nombres selon le niveau")
print("Niveau1: 3 secondes / Niveau2: 2 secondes / Niveau3: 1 seconde")


if __name__ == "__main__":

    gamecontroller = GameController()
    gamecontroller.Init_Player()

"""loop allowing to call the methods of the objects"""
    while True:
        gamecontroller.display_sequence()
        answer = gamecontroller.user_play()
        if answer == False:
            gamecontroller.replay()