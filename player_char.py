import random
from cards import cards

class Entity:
    def __init__(self, name, health):
        self.name = name
        self.max_health = health
        self.health = health
        self.block = 0

    def take_damage(self, amount):
        effective = max(0, amount - self.block)
        self.block = max(0, self.block - amount)
        self.health -= effective
        print(f"{self.name} takes {effective} damage. ({self.health} HP left)")

    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)
        print(f"{self.name} heals for {amount}. ({self.health} HP total)")

    def gain_block(self, amount):
        self.block += amount
        print(f"{self.name} gains {amount} block. ({self.block} Block)")

class Player(Entity):
    def __init__(self, name="You"):
        super().__init__(name, 30)
        self.energy = 3
        self.deck = cards * 2
        random.shuffle(self.deck)
        self.hand = []
        self.discard = []

    def draw_cards(self, n=5):
        self.hand = []
        for _ in range(n):
            if not self.deck:
                self.deck, self.discard = self.discard, []
                random.shuffle(self.deck)
            if self.deck:
                self.hand.append(self.deck.pop())
