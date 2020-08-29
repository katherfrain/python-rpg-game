import random
import pygame

class Librarian:
    def __init__(self, levelinput, health, power):
        self.levelinput = levelinput
        self.health = health
        self.power = power
        self.name = input("You are a Librarian! What is your name? ")

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False    
        
class Janitor:
    def __init__(self, levelinput, health, power):
        self.levelinput = levelinput
        self.health = health
        self.power = power
        self.name = input("You are a Janitor! What is your name?" )
    
    def is_alive(self):
        return self.health > 0

class Gremlin:
    def __init__(self, levelinput, health, power):
        self.levelinput = levelinput
        self.health = health
        self.power = power
        self.name = input("You are a Gremlin! What is your name? ")

    def is_alive(self):
        return self.health > 0

def startercode():
    levelinput = int(input("What level (1-10) would you like to start out as? "))
    health = 25 - levelinput
    power = 13 - levelinput
    print("Let's figure out what kind of character you are.")
    
    with open('/home/katherine/DigitalCrafts/python-rpg-game2/classquiz.txt', 'r') as classq:
            classquestionnaire = classq.read().split("\n")
            janitor_count = 0
            gremlin_count = 0
            librarian_count = 0 
            
            for question in classquestionnaire:
                try:
                    if not question:
                        break
                    elif question[0] == "~":
                        answer = input(" >") 
                        if answer == "1":
                            janitor_count =+ 1            
                        elif answer == "2":
                            librarian_count =+ 1
                        elif answer == "3":
                            gremlin_count =+ 1
                    else:
                        print(question)
                except IndexError:
                    print("WHY")
                
                #totals up answer scores, casts character as answer
                #9 score possibilities?
                
            if gremlin_count > janitor_count: # G > J, possibilities therefrom either G < L, G > L, or G == L
                if gremlin_count > librarian_count: #G > L
                    return Gremlin(levelinput, health, power)
                elif gremlin_count == librarian_count: #G = L
                    print("Smart little chaos demon, are you? We can handle that.")
                    return Gremlin(levelinput, health -2, power + 3)
                elif gremlin_count < librarian_count:  # G < L
                    return Librarian(levelinput, health, power)

            elif gremlin_count == janitor_count: #G = J, possibilites therefrom G > L, G < L, or G == L
                if gremlin_count > librarian_count:  #G > L
                    print("An odd one. We can handle that.")
                    return Gremlin(levelinput - 1, health + 2, power +1)
                elif gremlin_count < librarian_count: #G < L
                    print("A classic librarian!")
                    return Librarian(levelinput, health, power)
                elif gremlin_count == librarian_count:
                    print("THIS IS NOT WHAT I WANT TO HAPPEN")
                    Librarian(levelinput, health, power)

            elif janitor_count > gremlin_count:
                if janitor_count > librarian_count:
                    return Janitor(levelinput, health, power)
                elif janitor_count == librarian_count:
                    print("A smart one, but still practical. Hmm.")
                    return Janitor(levelinput + 2, health - 1, power)

            elif librarian_count > gremlin_count:
                if librarian_count > janitor_count:
                    return Librarian(levelinput, health, power)
                elif librarian_count == janitor_count:
                    print("Smart and well-rounded. I know what to do.")
                    return Janitor(levelinput + 2, health, power)


def main():
    player = startercode()
    while player.is_alive(): 
        print(f"You have started out as {player.name}")
        break

main()
# player.doThingToIt(targetofaction)              
                
