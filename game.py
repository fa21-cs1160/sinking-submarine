# Refact room change code
# Add inventory

class State:
    pass

COMMAND_LOOK_AROUND = 'look around'

ROOM_CONTROL = 'control'
ROOM_ENGINE = 'engine'
ROOM_REACTOR = 'reactor'

MESSAGE_CHANGE_ROOM = 'You spin the lock and go through the hatch.'
MESSAGE_MOVEMENT_ERROR = "You can't go there from here."

ROOM_MOVEMENT = [
    ( ROOM_CONTROL, [ ROOM_REACTOR ] ),
    ( ROOM_ENGINE, [ ROOM_REACTOR ] ),
    ( ROOM_REACTOR, [ ROOM_CONTROL, ROOM_ENGINE ] ),
]

def handle_engine_room(state, command):
    print("You can't do that.")

def handle_reactor_room(state, command):
    print("You can't do that.")

def handle_control_room(state, command):
    if command == COMMAND_LOOK_AROUND:
        print("You see a series of panels with flashing lights. It's dim and your feet are wet. That's not a good sign.")
    else:
        print("You can't do that.")

def handle_room_movement(state, command):
    room = command.replace('go to', '')\
                  .replace('room', '')\
                  .strip()

    for source, movement in ROOM_MOVEMENT:
        if state.room == source:
            if room in movement:
                print(MESSAGE_CHANGE_ROOM)
                state.room = room
            else:
                print(MESSAGE_MOVEMENT_ERROR)
            break

def get_room_handler(room):
    if room == ROOM_CONTROL:
        return handle_control_room
    elif room == ROOM_ENGINE:
        return handle_engine_room
    elif room == ROOM_REACTOR:
        return handle_reactor_room
    else:
        return None

def main():
    state = State()
    state.room = ROOM_CONTROL

    while True:
        # Print the room message
        if state.room == ROOM_CONTROL:
            print("You're in the control room.")
        elif state.room == ROOM_ENGINE:
            print("You're in the engine room.")
        elif state.room == ROOM_REACTOR:
            print("You're in the reactor room.")
        else:
            print(f'Unknown Room: {state.room}')

        # Get the command
        print()
        command = input('What do you want to do? ').lower()

        # Check for room movement
        if command.startswith('go to'):
            handle_room_movement(state, command)
            continue

        # Handle the command
        handler = get_room_handler(state.room)
        if handler:
            handler(state, command)
        else:
            print(f'Unknown room: {state.room}')

    print('Game Over')

if __name__ == "__main__":
    main()