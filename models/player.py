

class Player:
    def __init__(self, name, score=0):
        self.name = name
        self.has_played = False

    def mark_as_played(self):
        self.has_played = True
        
        
    def __str__(self):
        return self.name