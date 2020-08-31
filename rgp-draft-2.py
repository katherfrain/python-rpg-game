import random

class Alive:
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.name = name

    def is_alive(self):
        return self.health > 0 #this passes a boolean based on the statement

    def attack(self, enemy):
        enemy.health = enemy.health - self.power
        return enemy.health
    
    def print_status(self):
        print(f'{self.name} has {self.health} HP remaining and {self.power} power.\n')

    def get_item(self, item):
        try:
            item.apply(self, self)
        except TypeError:
            item.apply(self)
    
class Janitor(Alive):
    def __init__(self, health, power):
        self.health = health
        self.power = power
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
                else:
                    print('That was not a legal choice.')

        elif scene == 'LibrarianRoom':
            with open('/home/katherine/DigitalCrafts/python-rpg-game2/janitorscene2.txt') as scenes:
                scenereader = scenes.read().split('\n')
                for line in scenereader:
                    print(line)
                choice = input(" >")
                if choice == '1':
                    self.get_item(Vorpal())            
                return 'FightRoom'
        
        elif scene == 'RetirementRoom':
            print("You decide this has gone far enough.")
            print("The Librarian can mess around with something else magickal and ominous.")
            print("You put up the yellow maintenance sign and start mixing grout out of grave dirt and dragon knuckles.")
            print("Maybe next year you'll take a vacation to Hawai'i after all.")
            self.health = 0
        
class Gremlin(Alive):
    def __init__(self, health, power):
        self.health = health
        self.power = power
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
                    return 'TreasureRoom'
                elif choice == '2':
                    return 'DoomRoom'
                else:
                    print("Illegal input, try again.")
        elif scene == 'MirrorRoom':
            print("Something glints under the threshhold of this door.")
            print("Rubies, maybe. Diamonds. But no - as you walk into")
            print("the room, you see mirrors instead. Walls of them.")
            print(f"You're a handsome {self.classname}, {self.name}.")
            print(f"Your power is {self.power}, and your health is {self.health}.")
            print("You make faces in the mirror for a while before choosing to leave.")
            rightorleft = input('Do you go:\n[1] right\n[2] left\n ')
            if rightorleft == '1':
                return 'TreasureRoom'
            elif rightorleft == '2':
                return 'DoomRoom'
            else:
                print("Choose something legal.")  
        elif scene == 'DoomRoom':
            print("You enter the East Corridor.")

class Librarian(Alive):
    def __init__(self, health, power):
        self.health = health
        self.power = power
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
                else:
                    print("Illegal input, please try again.")
        elif scene == 'RetirementRoom':
            print("You summon the demon inside the circle, cackling the whole time.")
            print("Baphomet appears coughing in a cloud of white smoke.")
            print('"How dare you," it bellows in a voice like kittens through meatgrinders.')
            print('"What could you demand of me?"')
            print("You've waited years for this day.")
            print('"I will go after those who have shamed us - disregarded us - those')
            print('WHO LOSE LIBRARY BOOKS," you shriek.')
            print('Baphomet\'s eyes blaze. "So be it," it says.')
            self.health = 0

class Dragon(Alive):
    def __init__(self, name, health, power):
        self.health = health
        self.power = power
        self.name = name

class Battle(object):
    def do_battle(self, protagonist, enemy):
        self.protagonist = protagonist
        self.enemy = enemy
        print(f"You, {self.protagonist.name}, have chosen to face down {self.enemy.name}.")
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
                    print("You win!")
                    print(f"You have defeated {enemy.name}, and in doing so returned peace to the Library.")
                    print("FINISH")
                elif not protagonist.is_alive() and enemy.is_alive():
                    print("You died!")
            elif choices == "2":
                enemy.attack(protagonist)
            elif choices == "3":
                print("You run away!")
                if protagonist.classname == "Gremlin":
                    print("You run back to the caves where you sprouted and stay there.")
                    print("FINISH")
                    protagonist.health = 0
                elif protagonist.classname == "Librarian":
                    print("This seems like a good time to go into research. Forever.")
                    print("FINISH")
                    protagonist.health = 0
                elif protagonist.classname == "Janitor":
                    print("You know what? This isn't in your job description.")
                    print("You return to mopping messes by the Help Desk.")
                    print("FINISH")
                    protagonist.health = 0
            else:
                print("Pick a legal choice. ")

def startercode():
    levelinput = 0
    while not levelinput:
        try:
            levelinput = int(input("What level (1-10) would you like to start out as? "))
        except ValueError:
            print("Please enter a real integer value.")
    health = 55 - levelinput
    power = 25 - levelinput
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
                            print("Answer the question legally, gremlin.")
                            gremlin_count = +1
                    else:
                        print(question)
                except IndexError:
                    print("WHY")
                
                #totals up answer scores, casts character as answer
                #9 score possibilities?
                
            if gremlin_count > janitor_count: # G > J, possibilities therefrom either G < L, G > L, or G == L
                if gremlin_count > librarian_count: #G > L
                    return Gremlin(health - 5, power +7)
                elif gremlin_count == librarian_count: #G = L
                    print("Smart little chaos demon, are you? We can handle that.")
                    return Gremlin(health -2, power + 7)
                elif gremlin_count < librarian_count:  # G < L
                    return Librarian(health+5, power)

            elif gremlin_count == janitor_count: #G = J, possibilites therefrom G > L, G < L, or G == L
                if gremlin_count > librarian_count:  #G > L
                    print("An odd one. We can handle that.")
                    return Janitor(health - 2, power + 3)
                elif gremlin_count < librarian_count: #G < L
                    print("A classic librarian!")
                    return Librarian(health, power)
                elif gremlin_count == librarian_count:
                    print("A smart trickster, eh?")
                    return Librarian(health-1, power+1)

            elif janitor_count > gremlin_count:
                if janitor_count > librarian_count:
                    return Janitor(health, power)
                elif janitor_count == librarian_count:
                    print("A smart one, but still practical. Hmm.")
                    return Janitor(health - 1, power + 2)

            elif librarian_count > gremlin_count:
                if librarian_count > janitor_count:
                    return Librarian(health + 5, power - 3)
                elif librarian_count == janitor_count:
                    print("Smart and well-rounded. I know what to do.")
                    return Janitor(health + 2, power + 2)
            else:
                print("What did you DO?")
                return Janitor(health - 3, power - 3)

class Vorpal(object):
    name = 'Vorpal Sword'
    def apply(self, protagonist):
        print('The sword whispers.')
        print('You think you can almost make out tales about blood, long ago.')
        print('It sends shivers down your spine.')
        print('The blade gleams with unholy light.')
        print('You pick it up.')
        protagonist.health = protagonist.health + 30
        protagonist.power = protagonist.power + 10
        protagonist.print_status()

class Diamond(object):
    name = 'Diamond of Transformation'
    def apply(self, protagonist):
        change = input('Would you like your world to change? ').lower()
        if change == "yes":
            main()
        else:
            print('No? Fine to stay safe?')
            print("Doesn't matter, the Treasure Room can help you there too.")
            print('Take the Diamond.')
            protagonist.health = protagonist.health + 100
            protagonist.print_status()

class TreasureRoom(object):
    items = [Vorpal, Diamond]
    def picktreasure(self, protagonist):
        while True:
            print('Welcome to the Treasure Room, child.')
            print('Everything here glitters and sparkles, like a dream.')
            print('What will you take?')
            take = False
            while take == False:
                for i in range(len(TreasureRoom.items)):
                    item = TreasureRoom.items[i]
                    takethis = input(f"Will you take {item.name}? Keep in mind you can only have one thing. ").lower()
                    if takethis == "yes": 
                        protagonist.get_item(item)
                        take = True
                    elif takethis == "vorpal" or takethis == "sword":
                        protagonist.get_item(Vorpal)
                        take = True
                    elif takethis == "diamond" or takethis == "gem":
                        protagonist.get_item(Diamond)
                    else:
                        print("I didn't understand that. Try again? ")
            print("You feel brave enough to take on the beast now.")                    

def main():
    
    player = startercode()
    dragon = Dragon('The Dragon', 40,10)
    melchior = Dragon('Melchior', 30, 5)
    battle_engage = Battle()
    treasure = TreasureRoom()

    you_and_dragon_live = player.is_alive() and melchior.is_alive()
    you_and_melchior_live = player.is_alive() and dragon.is_alive()

    print(f"You have started out as {player.name} the {player.classname}.")
    player.print_status()

    while you_and_dragon_live and you_and_melchior_live:
    
        if player.classname == 'Janitor':
            outcome = player.discoverscene('EastCorridor')
            if outcome == 'LibrarianRoom':
                outcome2 = player.discoverscene('LibrarianRoom')
                if outcome2 == 'FightRoom':
                    player.discoverscene('FightRoom')
                    battle_engage.do_battle(player, melchior)
            elif outcome == 'RetirementRoom':
                player.discoverscene('RetirementRoom')
            
            elif outcome == 'FightRoom':
                player.discoverscene('FightRoom')
                print(f"You have {player.health} HP and {player.power} power.")
                print(f"The monster in front of you has {melchior.health} HP and {melchior.power} power.")
                attackyes = input("Will you attack? ").lower()
                if attackyes == "attack" or attackyes == "yes":
                    battle_engage.do_battle(player, melchior)
                else:
                    dragon.attack(player)
                    player.print_status()

        elif player.classname == 'Gremlin':
            outcome = player.discoverscene('GremlinIntro')
            if outcome == 'DoomRoom':
                print(f"You have {player.health} HP and {player.power} power")
                print(f"Your opponent, {dragon.name}, has {dragon.health} HP and {dragon.power} power.")
                attackornot = input("Are you sure you want to attack? ").lower()
                if attackornot == "yes" or attackornot == "attack":
                    battle_engage.do_battle(player, dragon)
                else:
                    print("You run in the opposite direction")
                    treasure.picktreasure(player)
                    player.discoverscene('DoomRoom')
            elif outcome == 'TreasureRoom':
                treasure.picktreasure(player)
                player.discoverscene('DoomRoom')
            elif outcome == 'MirrorRoom':
                player.discoverscene('MirrorRoom')

        elif player.classname == 'Librarian':
            outcome = player.discoverscene('LibrarianIntro')
            if outcome == 'TransformationRoom':
                print("Your thoughts split as a pounding headache descends.")
                print("Something feels...wrong. What's happening to you?")
                player = Gremlin(player.health, player.power)
                player.discoverscene('MirrorRoom')
            elif outcome == 'FightMelchior':
                battle_engage.do_battle(player, melchior)
            elif outcome == 'RetirementRoom':
                player.discoverscene('RetirementRoom')
    
        you_and_dragon_live = player.is_alive() and melchior.is_alive()
        you_and_melchior_live = player.is_alive() and dragon.is_alive()        

main()

# player.doThingToIt(targetofaction)              
                
