# character_test.py
from character import Character, Friend, Enemy
from item import Item

# Create a friend character
tahfia = Friend("Tahfia", "your humble friend")
tahfia.describe()

# Set and use conversation for the friend character
tahfia.set_conversation("I am always here to help you!")
tahfia.talk()

# Create a key item
key = Item("key", "A small rusty key that seems to open a door.")
key.describe()

# Player's inventory (starts empty)
inventory = []

# Ask the player if they want to pick up the key
take_key = input("Do you want to take the key? (yes/no): ").strip().lower()

if take_key == "yes":
    inventory.append(key)  # Add key to the inventory
    print("You have picked up the key.")
else:
    print("You left the key where it is.")

# Create an enemy character
dave = Enemy("Dave", "a scary zombie")
dave.describe()

# Set and use conversation for the enemy character
dave.set_conversation("I will eat your brains!")
dave.talk()

# Set Dave's weakness
dave.set_weakness("silver sword")

# Ask the player what they will fight with
fight_with = input("What will you fight Dave with?: ").strip().lower()

# Try fighting Dave
if isinstance(dave, Enemy):
    result = dave.fight(fight_with)
    if not result:
        print("You lost the fight!")
    else:
        print("You won the fight!")

# Door mechanic
print("\nYou see a locked door.")
open_door = input("Do you want to try to open the door? (yes/no): ").strip().lower()

# Check if the player has the key in their inventory
if open_door == "yes":
    if any(item.name == "key" for item in inventory):
        print("You use the key to open the door. The door unlocks and you escape!")
    else:
        print("The door is locked. You need a key to open it.")
else:
    print("You decided not to open the door.")
