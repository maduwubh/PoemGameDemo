class Poem:
    def __init__(self):
        self.lines = []
        
    def add_line(self, line):
        self.lines.append(line)
        
    def display(self):
        print("\nFinal Poem\n")
        
        
        for line in self.lines:
            print(line)
    
    