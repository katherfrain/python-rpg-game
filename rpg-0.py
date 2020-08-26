"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
class Hero:
    def __init__(self, health, power):
        self.health = health
        self.power = power
        
    
    def attack(self, enemy):
        enemy.health = (enemy.health - self.power)
        return enemy.health
    
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            print("The valiant hero is vanquished! Try again later.")
            return False 

class Goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            print("You have killed the goblin!")
            return False 
    
    def attack(self, enemy):
        enemy.health = (enemy.health - self.power)
        return enemy.health
            

def main():

    firsthero = Hero(10, 5)
    firstgoblin = Goblin(6, 2)

    while firsthero.is_alive() and firstgoblin.is_alive():
        print(f"You have {firsthero.health} HP and {firsthero.power} attack power")
        print(f"The goblin has {firstgoblin.health} HP and {firstgoblin.power} attack power")
        attackorfight = input("Would you like to attack, do nothing, or flee? ")
        attackorfight.lower()
        
        if attackorfight == "attack":
            firsthero.attack(firstgoblin)
            firstgoblin.attack(firsthero)
            print("You and the goblin have attacked each other!")
            print(f"Your health is now {firsthero.health} HP, while the goblin has {firstgoblin.health} HP remaining.")
        elif attackorfight == "do nothing":
            firstgoblin.attack(firsthero)
            print(f"The goblin attacks! Your health is now {firsthero.health} HP.")
        elif attackorfight == "flee":
            print("You ran away!")
            break
        else:
            attackorfight = input("Would you like to attack, do nothing, or flee? ")

main() 