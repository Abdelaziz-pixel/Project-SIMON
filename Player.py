"""class"""
class Player:

"""Constructive method containing two attributes"""
    def __init__(self):
        self.name = None
        self.score = 0

"""method to request the player's name"""
    def PlayerName(self):
        name = input("Quel est votre nom ? ")
        while self.ControlName(name) is False:
            print("Votre nom doit contenir au minimum 2 et au maximum 10 caratéres ! ")
            name = input("Votre nom ? ")
        self.name = name
        print("Bonne chance {}".format(name))

"""methods to check the player's name"""
    def ControlName(self, name):
        
        if len(name)>1 and len(name)<10:
            return True
        else:
            return False



    
   


        
