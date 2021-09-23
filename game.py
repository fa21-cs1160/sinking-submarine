class State:
    pass

ROOM_CONTROL = 'control'
ROOM_ENGINE = 'engine'
ROOM_REACTOR = 'reactor'

MESSAGE_CHANGE_ROOM = 'You spin the lock and go through the hatch.'

def handle_engine_room(state, command):
    if command == 'go to reactor room':
        print(MESSAGE_CHANGE_ROOM)
        state.room = ROOM_REACTOR

def handle_reactor_room(state, command):
    if command == 'go to control room':
        print(MESSAGE_CHANGE_ROOM)
        state.room = ROOM_CONTROL
    elif command == 'go to engine room':
        print(MESSAGE_CHANGE_ROOM)
        state.room = ROOM_ENGINE
    else:
        print("You can't do that.")

def handle_control_room(state, command):
    if command == 'go to reactor room':
        print(MESSAGE_CHANGE_ROOM)
        state.room = ROOM_REACTOR
    else:
        print("You can't do that.")

def main():
    state = State()
    state.room = ROOM_CONTROL

    while True:
        if state.room == ROOM_CONTROL:
            print("You're in the control room.")
        elif state.room == ROOM_ENGINE:
            print("You're in the engine room.")
        elif state.room == ROOM_REACTOR:
            print("You're in the reactor room.")
        else:
            print(f'Unknown Room: {state.room}')

        print()
        command = input('What do you want to do? ').lower()

        if state.room == ROOM_CONTROL:
            handle_control_room(state, command)
        elif state.room == ROOM_REACTOR:
            handle_reactor_room(state, command)
        elif state.room == ROOM_ENGINE:
            handle_engine_room(state, command)
        else:
            print(f'Unknown Room: {state.room}')

        # print(state.room)
        # break

    print('Game Over')

if __name__ == "__main__":
    main()