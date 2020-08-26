
class Character:
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name
        
    def attack(self, enemy):
        enemy.health = (enemy.health - self.power)
        return enemy.health
    
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False 
    
    def print_status(self):
        if self.is_alive():
            print(f"{self.name} has {self.health} HP left.")
        else:
            print(f"{self.name} has died!")

def main():

    heroname = input("What would you like to call your knight? ")
    firsthero = Character(10, 5, heroname)
    firstgoblin = Character(6, 2, "Zadoo")
    
    print(f"You have {firsthero.health} HP and {firsthero.power} attack power")
    print(f"Zadoo the Goblin has {firstgoblin.health} HP and {firstgoblin.power} attack power")
    
    
    while firsthero.is_alive() and firstgoblin.is_alive():

        attackorfight = input("Would you like to attack, do nothing, or flee? ").lower()
        
        if attackorfight == "attack":
            firsthero.attack(firstgoblin)
            firstgoblin.attack(firsthero)
            print("You and the goblin have attacked each other!")
            firsthero.print_status()
            firstgoblin.print_status()
            
        elif attackorfight == "do nothing":
            firstgoblin.attack(firsthero)
            print(f"The goblin attacks! Your health is now {firsthero.health} HP.")
        elif attackorfight == "flee":
            print("You ran away!")
            break
        else:
            print("DUDE. SPELLING.")
main() 