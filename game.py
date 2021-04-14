from player import Player
from adadachi import Adadachi
from constants import *
import random

player = Player()

def display(statement):
    print(statement)

def create_adadachi_personality():
    foods = player.inventory["foods"]
    games = player.inventory["games"]
    personality = {}
    fav_food = random.randint(0,len(foods)-1)
    hates_food = random.randint(0,len(foods)-1)
    while fav_food == hates_food:
        hates_food = random.randint(0,len(foods)-1)
    fav_game = random.randint(0,len(games)-1)
    hates_game = random.randint(0,len(games)-1)
    while fav_game == hates_game:
        hates_game = random.randint(0,len(games)-1)
    personality["fav_food"] = fav_food
    personality["hates_food"] = hates_food
    personality["fav_game"] = fav_game
    personality["hates_game"] = hates_game
    return personality



def create_adadachi():
    name = input(GET_NAME + "\n\t")
    personality = create_adadachi_personality()
    player.adadachi = Adadachi(name,personality)



def start_game():
    display(TITLE)
    answer = input(GREETING)
    if answer.lower() == "y":
        create_adadachi()
        while player.adadachi.hunger < 5:
            option = input(OPTIONS).lower()

            if option == "s":
                player.get_status()
            elif option == "c":
                    player.clean()
            elif option == "f":
                if player.inventory["foods"]:
                    player.feed()
                else:
                    break
            elif option == "p":
                player.play_with_adadachi()
            elif option == "x":
                return display(EXIT)
        
        display(LOST)