# character.py

class Character:
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        print(f"{self.name} is in this room!")
        print(self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print(f"[{self.name} says]: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you")


class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(f"You defeated {self.name} with the {combat_item}!")
            return True
        else:
            print(f"{self.name} defeated you!")
            return False


class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.gift = None

    def hug(self):
        """Give the friend a hug."""
        print(f"You give {self.name} a big hug! {self.name} smiles warmly at you.")

    def give_gift(self, gift):
        """Offer a gift to the friend."""
        self.gift = gift
        print(f"You give {self.name} a {gift}. {self.name} is very happy with the gift!")
        self.show_appreciation()

    def show_appreciation(self):
        """Friend expresses appreciation after receiving a gift."""
        print(f"{self.name} says: 'Thank you for the {self.gift}! You are a true friend.'")


# item.py

class Item:
    def __init__(self, item_name, item_description):
        self.name = item_name
        self.description = item_description

    def describe(self):
        """Describe the item."""
        print(f"You see a {self.name}: {self.description}")



