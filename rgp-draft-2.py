import random
import pygame


class Alive:
    def __init__(self, levelinput, health, power):
        self.levelinput = levelinput
        self.health = health
        self.power = power
        self.name = name

    def is_alive(self):
        return self.health > 0 #this passes a boolean based on the statement

    def attack(self, enemy):
        enemy.health = enemy.health - self.power
    
    def print_status(self):
        print(f'{self.name} has {self.health} HP remaining and {self.power} power.')
 
class Janitor(Alive):
    def __init__(self, levelinput, health, power):
        self.levelinput = levelinput
        self.health = health
        self.power = power
        self.has_Vorpal = False
        self.classname = 'Janitor'
        self.name = input("You are a Janitor! What is your name? ")

    def discoverscene(self, scene):
        self.scene = scene 
        if scene == 'EastCorridor':
            with open('/home/katherine/DigitalCrafts/python-rpg-game2/janitorscenes.txt') as scenes:
                scenereader = scenes.read().split('\n')
                for line in scenereader:
                    print(line)
                choice = input(" >")
                
                if choice == "1":
                    return 'RetirementRoom'
                
                elif choice == '2':
                    return 'LibrarianRoom'

                elif choice == '3':
                    return 'FightRoom'
        
        elif scene == 'LibrarianRoom':
            with open('/home/katherine/DigitalCrafts/python-rpg-game2/janitorscene2.txt') as scenes:
                scenereader = scenes.read().split('\n')
                for line in scenereader:
                    print(line)
                choice = input(" >")
                if choice == '1':
                    self.has_Vorpal = True
                return 'FightRoom'
        
        elif scene == 'FightRoom':
            print("You enter the room of the beast.")      
        
class Gremlin(Alive):
    def __init__(self, levelinput, health, power):
        self.levelinput = levelinput
        self.health = health
        self.power = power
        self.has_Vorpal = False
        self.classname = 'Gremlin'
        self.name = input("You are a Gremlin! What is your name? ")

        def discoverscene(self, scene):
            self.scene = scene
            if scene == 'GremlinIntro':
                with open('/home/katherine/DigitalCrafts/python-rpg-game2/gremlinintro.txt') as scenes:
                    scenereader = scenes.read().split('\n')
                    for line in scenereader:
                        print(line)
                choice = input(" >")
                if choice == '1':
                    return 'MirrorRoom'
                elif choice == '2':
                    return 'DoomRoom'
            if scene == 'MirrorRoom':
                print("Something glints under the threshhold of this door.")
                print("Rubies, maybe. Diamonds. But no - as you walk into")
                print("the room, you see mirrors instead. Walls of them.")
                print(f"You're a handsome {self.classname}, {self.name}.")
                print(f"Your power is {self.power}, and your health is {self.health}.")
                print("You make faces in the mirror for a while before choosing to leave.")
                rightorleft = input('Do you go:\n[1] right\n[2] left')
                if rightorleft == '1':
                    return 'TreasureRoom'
                elif rightorleft == '2':
                    return 'DoomRoom'
                else:
                    print("Choose something legal.")
            elif scene == 'TreasureRoom':
                print('Treasure? How much treasure?')
            elif scene == 'DoomRoom':
                print("You enter the East Corridor.")


class Librarian(Alive):
    def __init__(self, levelinput, health, power):
        self.levelinput = levelinput
        self.health = health
        self.power = power
        self.has_Vorpal = False
        self.classname = 'Librarian'
        self.name = input("You are a Librarian! What is your name? ")

        def discoverscene(self, scene):
            self.scene = scene
            if scene == 'LibrarianIntro':
                with open('/home/katherine/DigitalCrafts/python-rpg-game2/librarianintro.txt') as scenes:
                    scenereader = scenes.read().split('\n')
                    for line in scenereader:
                        print(line)
                    choice = input(' >')
                    if choice == "1":
                        return 'RetirementRoom'
                    elif choice == "2":
                        return 'FightMelchior'
                    elif choice == "3":
                        return 'TransformationRoom'
            elif scene == 'FightMelchior':
                print("Unfortunately, this demon won't do your bidding so easily.")


class Dragon(Alive):
    def __init__(self, name, health, power):
        self.health = health
        self.power = power
        self.name = name

class Battle(object):
    def do_battle(self, protagonist, enemy):
        self.protagonist = protagonist
        self.enemy = enemy
        print(f"You, {self.protagonist}, have chosen to face down {self.enemy}.")
        protagonist.print_status()
        enemy.print_status()
        while protagonist.is_alive() and enemy.is_alive(): 
            choices = input("You have three choices:\n[1] attack\n[2] flinch\n[3] flee.\n")
            if choices == "1":
                protagonist.attack(enemy)
                enemy.attack(protagonist)
                print(f'You have done the enemy {protagonist.power} damage - their health is now {enemy.health}.')
                print(f'Unfortunately, they got a shot in too - your health is {protagonist.health}.')
                if protagonist.is_alive() and not enemy.is_alive():
                    print("You win")
                    break
                elif not protagonist.is_alive and enemy.is_alive():
                    print("You died!")
                    break
            elif choices == "2":
                enemy.attack(protagonist)
            elif choices == "3":
                print("You run away!")
                if protagonist.classname == "Gremlin":
                    print("You run back to the caves where you sprouted and stay there.")
                    print("FINISH")
                    break
                elif protagonist.classname == "Librarian":
                    print("This seems like a good time to go into research. Forever.")
                    print("FINISH")
                    break
                elif protagonist.classname == "Janitor":
                    print("You know what? This isn't in your job description.")
                    print("You return to mopping messes by the Help Desk.")
                    print("FINISH")
                    break


#class Vorpal(object):
    

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
                    return Janitor(levelinput - 1, health + 2, power +1)
                elif gremlin_count < librarian_count: #G < L
                    print("A classic librarian!")
                    return Librarian(levelinput, health, power)
                elif gremlin_count == librarian_count:
                    print("A smart trickster, eh?")
                    return Librarian(levelinput, health-1, power+1)

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
    dragon = Dragon('Dragon', 40,10)
    melchior = Dragon('Melchior', 30, 5)
    battle_engage = Battle()
    
    while player.is_alive(): 
        print(f"You have started out as {player.name} the {player.classname}.")
        
        if player.classname == 'Janitor':
            outcome = player.discoverscene('EastCorridor')
            if outcome == 'LibrarianRoom':
                outcome2 = player.discoverscene('LibrarianRoom')
                if outcome2 == 'FightRoom':
                    player.discoverscene('FightRoom')
                    if player.has_Vorpal:
                        player.health = player.health + 20
                        player.power = player.power + 10
                    player.attack(dragon)
                    print(f"Your current health and power are {player.health} and {player.power}")
            elif outcome == 'RetirementRoom':
                print("You decide this has gone far enough.")
                print("The Librarian can mess around with something else magickal and ominous.")
                print("You put up the yellow maintenance sign and start mixing grout out of grave dirt and dragon knuckles.")
                print("Maybe next year you'll take a vacation to Hawai'i after all.")
                break
            
            elif outcome == 'FightRoom':
                player.discoverscene('FightRoom')
                if player.has_Vorpal:
                    player.health = player.health + 20
                    player.power = player.power + 10
                print(f"You have {player.health} HP and {player.power} power.")
                print(f"The monster in front of you has {dragon.health} HP and {dragon.power} power.")
                attackyes = input("Will you attack? ").lower()
                if attackyes == "attack" or attackyes == "yes":
                    battle_engage.do_battle(player, dragon)
                else:
                    dragon.attack(player)

                print(f"Your current health and power are {player.health} and {player.power}")
        
        elif player.classname == 'Gremlin':
            outcome = player.discoverscene('GremlinIntro')
            if outcome == 'DoomRoom':
                print(f"You have {player.health} HP and {player.power} power")
                print(f"Your opponent, {dragon.name}, has {dragon.health} HP and {dragon.power} power.")
                attackornot = input("Are you sure you want to attack?").lower()
                if attackornot == "yes":
                    battle_engage.do_battle(player, dragon)
                else:
                    print("You run in the opposite direction")
                    player.discoverscene('TreasureRoom')
            elif outcome == 'TreasureRoom':
                print("So much treasure!")

        
        elif player.classname == 'Librarian':
            outcome = player.discoverscene('LibrarianIntro')
            if outcome == 'TransformationRoom':
                print("Your thoughts split as a pounding headache descends.")
                print("Something feels...wrong. What's happening to you?")
                player = Gremlin(player.levelinput, player.health, player.power)
                player.discoverscene('MirrorRoom')
            elif outcome == 'FightMelchior':
                battle_engage.do_battle(player, melchior)
            elif outcome == 'RetirementRoom':
                print("Baphomat bows to your mighty commands.")
                print("The East Corridor trembles and shakes, and your eyes gleam with lightning.")
                print("Soon, you will conquer the world.")
                break

main()

# player.doThingToIt(targetofaction)              
                
