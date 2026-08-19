class Poem:
    """Holds the poem title and the growing list of lines contributed
    by each player, in the order they were written."""

    def __init__(self, title="Untitled Poem"):
        self.title = title
        self.lines = []  # list of {"player": str, "text": str}

    def add_line(self, player_name, text):
        self.lines.append({"player": player_name, "text": text})

    def get_lines(self):
        return self.lines

    def full_text(self):
        return "\n".join(entry["text"] for entry in self.lines)

    def display(self):
        print(f"\n{self.title}\n" + ("=" * len(self.title)))
        for entry in self.lines:
            print(f"{entry['text']}  (— {entry['player']})")