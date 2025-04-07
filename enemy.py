import random
from player_char import Entity

class Enemy(Entity):
    def __init__(self, name="Goblin", health=20):
        super().__init__(name, health)

    def act(self, player):
        dmg = random.randint(3, 6)
        print(f"{self.name} attacks!")
        player.take_damage(dmg)
