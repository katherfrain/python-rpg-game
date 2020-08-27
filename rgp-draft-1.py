import random

class Enemy:
    def __init__(self):
        self.health = 6
        self.power = 9


    def startercode(self):
        self.levelinput = int(input("What level (1-10) would you like to start out as? "))
        self.health = 25 - self.levelinput
        self.power = 13 - self.levelinput
        print("What hero would you like to play?")

        self.classchoice = input("You may play Medic, Shadow, Hero, Inventor, or Rogue ").lower()
        allowedclasses = ["medic", "shadow", "hero", "inventor", "rogue"]
        if self.classchoice not in allowedclasses:
            self.classchoice = input("Dude, pick something legal: ")
        
        self.charstats = [self.health, self.power, self.classchoice]
        return self.charstats
        
class Player:    
    def attack(self, target):
        target.health = target.health - self.power
        #if class = Hero, do other thing???

    def __init__(self):
        self.startercode()
        print(self.charstats)


class Hero(Player):

    def attack(self, target):
        originalpower = self.power
        doubledamage = random.random() #should run random generator for number between 0 and 1
        if doubledamage >= 0.5:
            self.power = self.power * 2
        super(Hero, self).attack(target) #this reaches up to the parent and uses its attack function
        self.power = originalpower 
        return target.health

    def restore(self):
        self.health = self.health + (self.levelinput/2)

    def __init__(self):
        print(self.attack(goblin))



Player()