from constants import STATUS
import random


class Player:
    def __init__(self):
        self.adadachi = None #when games, this becomes player.adadachi
        self.inventory = {
            "games": ["hide-n-seek", "tag", "go fish", "red rover"],
            "foods": ["banana cream pie", "carrot sticks", "mashed potatoes", "mac 'n cheese", "tater tots", "chocolate cake", "strawberries", "fried rice"],
        }
        
    def play_with_adadachi(self):
        print(self.adadachi.personality) 

        #if fav_game is chosen, raise happiness point by 2
        #if hates_game is chosen, minus 2 points
        #if any other of the games is chosen, raise happiness by 1
        

    def feed(self):
        print(f'Favorite Food: {self.inventory["foods"][self.adadachi.personality_favorites()]}')
        print(f'Least Favorite Food: {self.inventory["foods"][self.adadachi.personality_hates()]}')
        food_to_feed = input(f'What would you like to feed {self.adadachi.name}? The menu includes: {self.inventory["foods"]}')

    def clean(self):
        pass

    def get_status(self):
        print(self.adadachi.name,"has a hunger level of",self.adadachi.hunger,"\na happiness level of",
        self.adadachi.happiness,"\n a poop level of",self.adadachi.poop_lvl)

        #Your (adagachi name) is at (hunger), (poop level), (happinesslevel)
        pass