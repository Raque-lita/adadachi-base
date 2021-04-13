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

    def print_feed(self, favorite_food, least_favorite_food):

        food_menu = ",".join(self.inventory["foods"])
        print(f'Favorite Food: {favorite_food}')
        print(f'Least Favorite Food: {least_favorite_food}')
        food_to_feed = input(f'What would you like to feed {self.adadachi.name}? The menu includes {food_menu}') 
        return food_to_feed  

    def feed(self):
        favorite_food = self.inventory["foods"][self.adadachi.personality_favorites()] 
        least_favorite_food = self.inventory["foods"][self.adadachi.personality_hates()]
        food_to_feed = self.print_feed(favorite_food, least_favorite_food)
        if food_to_feed.lower() == favorite_food:
            self.adadachi.happiness += 1
            self.adadachi.hunger -= 1
        if food_to_feed == least_favorite_food:
            self.adadachi.happiness -= 1
            self.adadachi.hunger += 1
    


    def clean(self):
        pass

    def get_status(self):
        print(self.adadachi.name,"has a hunger level of",self.adadachi.hunger,
        "\na happiness level of", self.adadachi.happiness,
        "\na poop level of",self.adadachi.poop_lvl)

        #Your (adagachi name) is at (hunger), (poop level), (happinesslevel)
        pass