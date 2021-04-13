class Adadachi:
    def __init__(self,name, personality):
        self.name = name
        self.hunger = 2
        self.happiness = 1
        self.personality = personality #this is a dictionary
        self.poop_lvl = 0

    def personality_favorites(self):
        return self.personality["fav_food"]
        
        #we have self.personality 

    def personality_hates(self):
        return self.personality["hates_food"]