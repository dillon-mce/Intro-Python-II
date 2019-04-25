# Implement a class to hold room information. This should have name and
# description attributes.
from item import *
import textwrap

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.adjacent_rooms = {}

    def get_opposite(self, direction):
        if direction == "north":
            return "south"
        elif direction == "south":
            return "north"
        elif direction == "east":
            return "west"
        elif direction == "west":
            return "east"
        else:
            return None

    def add_addjacent_room(self, room, direction, reciprocal = True):

        self.adjacent_rooms[direction] = room
        if reciprocal:
            opposite_direction = self.get_opposite(direction)

            room.adjacent_rooms[opposite_direction] = self

    def adjacent_room_for(self, direction):
        if direction in self.adjacent_rooms:
            return self.adjacent_rooms[direction]
        else:
            print(f'\nCan\'t go {direction} from here.')
            return self

    def print_room(self):
        print(f'\n\nYou are now in {self.name}\n')
        print(textwrap.fill(f'"{self.description}"'))

    def list_visible_items(self):
        print("\nLooking around you see:")
        if len(self.items) < 1:
            print("Nothing interesting...")
        else:
            for item in self.items:
                print(f'- {item}')

    def get_item_named(self, item_name):
        return next((item for item in self.items if item.name == item_name), None)

    def add_items(self, *items):
        for item in items:
            self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)


# Declare all the rooms

rooms = {
    'outside':  Room("The Parking Lot",
                     "You see the office entrance to the north"),

    'lobby':    Room("The Lobby", """Not much to see here. The elevator lies to the north, stairs to the east, and W.B. Jones Heating and Air to the west."""),

    'elevator': Room("The Elevator", """Not much room in here, but you can choose any of the three floors: '1', '2', '3'"""),

    'second_floor_hallway':   Room("The Second Floor Hallway", """To the west you see the Vance Refrigeration Offices, to the east is Dunder Mifflin. To the south, between the restrooms, is an empty closet that looks like it might be useful for something someday."""),

    'reception': Room("Reception", """Pam sits at her desk. To the north you see Jim and Dwight's desk clump."""),

    'desk_clump_1': Room("Jim and Dwight's Desk Clump", "Jim appears to have put Dwight's stapler in jello. Michael's office is to the west, Meredith's Desk is to the east, and Phyllis and Stanley's desk clump is to the north."),

    'michael_office': Room("Michael's Office", "You are greeted with a \"Whazzzzaaaap\" as you enter. Michael looks like he'd love some distraction from his work. The only exit is to the east."),

    'meredith_desk': Room("Meredith's Desk", "Meredith is distracted trying to find the hand sanitizer in her desk drawers and doesn't notice you. Accounting is to the south and Creed sits to the north."),

    'desk_clump_2': Room("Phyllis and Stanley's Desk Clump", "Phyllis is knitting and Stanley appears to be asleep. The conference room is to the west, Creed's desk is to the east, and the kitchen is to the north."),

    'accounting': Room("Accounting Department", "Angela, Kevin and Oscar sit at their respective desks, hard at work on crunching the numbers."),

    'creed_desk': Room("Creed's Desk", "Creed sits furtively glancing around the room, occasionally sneaking mung beans from his desk drawer. Meredith sits to the south and Phyllis and Stanely sit to the west."),

    'conference_room': Room("The Conference Room", "It is empty now, but it look's like Michael might be planning a meeting for later. The only exit is south."),

    'kitchen': Room("The Kitchen", "Smells like someone burnt some popcorn in here. The annex is to the north.")
}


# Link rooms together
rooms['outside'].add_addjacent_room(rooms['lobby'], "north")
rooms['lobby'].add_addjacent_room(rooms['elevator'], "north", False)
rooms['elevator'].add_addjacent_room(rooms['lobby'], "first", False)
rooms['elevator'].add_addjacent_room(rooms['second_floor_hallway'], "second", False)
rooms['second_floor_hallway'].add_addjacent_room(rooms['elevator'], "north", False)
rooms['second_floor_hallway'].add_addjacent_room(rooms['reception'], "east")
rooms['reception'].add_addjacent_room(rooms['desk_clump_1'], "north")
rooms['desk_clump_1'].add_addjacent_room(rooms['michael_office'], "west")
rooms['desk_clump_1'].add_addjacent_room(rooms['meredith_desk'], "east")
rooms['desk_clump_1'].add_addjacent_room(rooms['desk_clump_2'], "north")
rooms['meredith_desk'].add_addjacent_room(rooms['accounting'], "south")
rooms['meredith_desk'].add_addjacent_room(rooms['creed_desk'], "north")
rooms['desk_clump_2'].add_addjacent_room(rooms['creed_desk'], "east")
rooms['desk_clump_2'].add_addjacent_room(rooms['conference_room'], "west")
rooms['desk_clump_2'].add_addjacent_room(rooms['kitchen'], "north")

# Add items to rooms
rooms['lobby'].add_items(Item("mug", """It is empty, but you can fill it up with some of that life-giving liquid."""), Food("apple", "Looks tasty."))
rooms['reception'].add_items(Item("candy", "Jelly beans today, lots of flavors to choose from."))