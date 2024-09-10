hotel = {
  1: {
    101: ['George Jefferson', 'Wheezy Jefferson'],
  },
  2: {
    237: ['Jack Torrance', 'Wendy Torrance'],
  },
  3: {
    333: ['Neo', 'Trinity', 'Morpheus']
  }
}

def start_check_in_or_out():
    checkinout = None
    while checkinout == None:
        checkinout = input("Are you checking in, or out?").lower()
        if checkinout == 'in' or checkinout == 'out':
            return checkinout
        else:
            print('I\'m sorry, I only understand "in" or "out". Please reply with "in" or "out."')
            checkinout = None

def get_room_and_floor(in_or_out):
    if in_or_out == 'in':
        floor = int(input('Which floor would you prefer?'))
        room = int(input('Which room would you prefer?'))

    if in_or_out == 'out':
        floor = int(input('Which floor was your room on?'))
        room = int(input('Which room are you checking out of?'))

    return floor, room

def is_room_empty(floor, room):
    if floor in hotel.keys():
        if room in hotel[floor].keys() and len(hotel[floor][room]) > 0:
            return False
        else:
            return True
    else:
        return True
    return False

def add_occupants():
    names = []
    number_of_occupants = None
    while number_of_occupants == None:
        number_of_occupants = int(input("How many in your party? "))
        if number_of_occupants > 6:
            print("I'm sorry, we can only accomodate parties of 6 or less.")
            number_of_occupants = None

    for occupant in range(number_of_occupants):
        name = input("What is occupant #%d's name? " % (occupant + 1, ))
        names.append(name)
    return names

def do_checkin(location):
    names = add_occupants()
    if location[0] in hotel.keys():
        hotel[location[0]][location[1]] = names
    else:
        hotel[location[0]] = {}
        hotel[location[0]][location[1]] = names
    return True

def do_checkout(location):
    del hotel[location[0]][location[1]]
    return True

run = True

while run == True:
    status = start_check_in_or_out()
    if status == 'in':
        checked_in = False
        while checked_in == False:
            location = get_room_and_floor('in')
            room_empty = is_room_empty(location[0], location[1])
            if room_empty == True:
                checked_in = do_checkin(location)
            else:
                print("That room is occupied, please choose another room.")
                checked_in = False

    elif status == 'out':
        checked_out = False
        while checked_out == False:
            location = get_room_and_floor('out')
            room_empty = is_room_empty(location[0], location[1])
            if room_empty == True:
                print("There isn't anyone in that room.")
                checked_out = False
            else:
                checked_out = do_checkout(location)
    print(hotel)