import random
from player_char import Entity

class Enemy(Entity):
    def __init__(self, name="Goblin", health=20):
        super().__init__(name, health)
        self.intent = ""

    def decide_intent(self):
        action = random.choice(["attack", "defend", "heal"])
        if action == "attack":
            dmg = random.randint(4, 7)
            self.intent = f"Attack for {dmg}"
            self._next_move = ("attack", dmg)
        elif action == "defend":
            block = random.randint(3, 5)
            self.intent = f"Defend for {block}"
            self._next_move = ("defend", block)
        elif action == "heal":
            heal = random.randint(3, 6)
            self.intent = f"Heal for {heal}"
            self._next_move = ("heal", heal)

    def act(self, player):
        move, value = self._next_move
        if move == "attack":
            print(f"{self.name} attacks!")
            player.take_damage(value)
        elif move == "defend":
            print(f"{self.name} defends!")
            self.gain_block(value)
        elif move == "heal":
            print(f"{self.name} heals!")
            self.heal(value)
