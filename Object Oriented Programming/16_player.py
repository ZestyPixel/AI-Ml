class Player:
    player_count = 0
    
    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count += 1

player1 = Player("John", 5)
player2 = Player("Doe", 10)
player3 = Player("Alice", 15)
print("Total players created:", Player.player_count)