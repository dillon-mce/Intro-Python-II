from room import rooms
from player import Player
from parser import Parser

#
# Main
#
player = Player(rooms['outside'])
parser = Parser(player)

print("Welcome to Scranton!\n\n")

player.print_current_room()
while True:

    command = input("\nWhat would you like to do? ").lower()

    if not parser.parse_command(command):
        break

print("\nSee you later!\n")