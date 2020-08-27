import random
import pygame

class Librarian:
    def __init__(self):
        self.name = input("You are a librarian at the Unseen University. What is your name? ")


class Janitor:
    def __init__(self):
        print("clean")

class Gremlin:
    def __init__(self):
        print('greea')


def startercode():
    levelinput = int(input("What level (1-10) would you like to start out as? "))
    health = 25 - levelinput
    power = 13 - levelinput
    print("Let's figure out what kind of character you are.")
    
    with open('/home/katherine/DigitalCrafts/python-rpg-game2/classquiz.txt', 'r') as classq:
            classquestionnaire = classq.read().split("\n")
            
            for question in classquestionnaire:
                
                if question[0] == " ":
                    answer = input(f"{question}") 
                    if answer == "1":
                        Librarian()
                    elif answer == "2":
                        Janitor()
                    elif answer == "3":
                        Gremlin()
                else:
                    print(question)


startercode()

               
                
