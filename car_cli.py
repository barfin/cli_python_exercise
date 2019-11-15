command = ""
is_car_on = False

while True:
    command = input("> ").lower()
    if command == "start":
        if is_car_on == True:
            print("car has already started")
        else:
            print("car started")
            is_car_on = True
    elif command == "stop":
        if is_car_on == False:
                print("car hasn't started yet")
        elif is_car_on == True:
            is_car_on = False
            print("car stopped")
    elif command == "help":
        print('''
start - to start the car
stop - to stop the car
exit - to exit the game
        ''')
    elif command == "exit":
        break
    else:
        print('''enter "help" for help ''')