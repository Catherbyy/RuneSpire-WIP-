import time
from player_char import Player
from enemy import Enemy

def main():
    player = Player()
    enemy = Enemy()

    print("--- RuneSpire: Battle Start! ---")

    while player.health > 0 and enemy.health > 0:
        print("\n--- Your Turn ---")
        player.energy = 3
        player.block = 0
        enemy.block = 0
        player.draw_cards()

        while player.energy > 0 and player.hand:
            print(f"\nEnergy: {player.energy}")
            for i, card in enumerate(player.hand):
                print(f"[{i}] {card['name']} (Cost: {card['cost']})")
            choice = input("Choose a card to play (or press Enter to end turn): ")
            if choice == "":
                break
            if not choice.isdigit() or int(choice) >= len(player.hand):
                print("Invalid choice.")
                continue

            card = player.hand.pop(int(choice))
            if card['cost'] > player.energy:
                print("Not enough energy.")
                player.hand.append(card)
                continue

            player.energy -= card['cost']
            player.discard.append(card)

            if card['type'] == 'attack':
                enemy.take_damage(card['damage'])
            elif card['type'] == 'defense':
                player.gain_block(card['block'])
            elif card['type'] == 'special' and 'heal' in card:
                player.heal(card['heal'])

            if enemy.health <= 0:
                print("\nYou win!")
                return

        print("\n--- Enemy Turn ---")
        time.sleep(1)
        enemy.act(player)

    if player.health <= 0:
        print("\nYou were defeated...")

if __name__ == '__main__':
    main()
