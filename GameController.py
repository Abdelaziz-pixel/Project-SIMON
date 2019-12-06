"""imports of libraries, classes and methods"""
from Player import Player
from Sequence import Sequence 
import time
import os 

"""class"""
class GameController:

    """Constructive method containing two attributes"""
    def __init__(self): 
        self.player = Player()
        self.sequence = Sequence()

    """call methods of the Player object"""
    def Init_Player(self):
        self.player.PlayerName()
        self.dificulty()

    """methods that allow the user to choose the level of difficulty"""
    def dificulty(self):
        level = int(input("niveau facile taper: 1\nniveau moyen taper: 2\nniveau dificile taper: 3\nVotre choix ? "))
        if level == 1:
            self.sequence.sleep = 3
            self.sequence.randrange = 10 
        elif level == 2:
            self.sequence.sleep = 2
            self.sequence.randrange = 20
        elif level == 3:
            self.sequence.sleep = 3
            self.sequence.randrange = 100
        else:
            print("Choisissez entre 1, 2 et 3 !")

    def display_sequence(self):
        self.sequence.add_random_number()
        for element in self.sequence.numbers:
            print(element)
            time.sleep(2)
            os.system("clear")
    """methods allowing a random choice to be displayed to the user according to the level"""
    def computer_play(self):
        self.sequence.add_random_number()

    """methods to request the player's response"""
    def user_play(self):
        for element in self.sequence.numbers :
            chose_player = int(input("Veuillez entrer votre réponse !"))
            while control_play(chose_player) is False:
                print("Entrez seulement un ou des chiffres ! ")
                chose_player = int(input("Votre réponse ? "))
            if chose_player != element:
                return False 
    """methods to check the user's response"""
    def control_play(self, chose_player):
        while True:
            try:
                chose_player = int(input("votre nombre ? ")
                break
            except:
                print("ce n'est pas un nombre")
                continue
        return chose_player
    """methods to restart the game if the player asks for it or stops it"""   
    def replay(self):
        print("Vous avez perdu !")
        while True:
            replay = input("Souhaitez-vous rejouer ? oui/non ? ").lower()
            if replay == "oui":
                self.sequence.numbers = []
                break 
            elif replay == "non":
                exit()
            else:
                print("Choisissez entre oui et non ! ") 
                
    