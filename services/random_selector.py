import random 

class RandomSelector:
    
    @staticmethod
    def select_random_item(players):
        return random.choice(players)