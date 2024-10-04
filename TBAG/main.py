from room import Room
from character import Enemy

kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")

dave = Enemy("Dave", "a smelly zombie")
dave.set_conversation("Hi, I'm Dave and totally won't eat your brains")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom.set_description("A vast room with a shiny wooden floor")
dining_hall.set_description("A large room with ornate decorations")

kitchen.link_room(dining_hall, "South")
dining_hall.link_room(kitchen, "North")
dining_hall.link_room(ballroom, "West")
ballroom.link_room(dining_hall, "East")

current_room = kitchen

while True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
        
        
    command = input("> ")
    current_room = current_room.move(command)

