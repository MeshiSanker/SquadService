from Service import Service

s = Service()
choice = 0
print("Welcome to Squads manager!\n")


while choice != 7:
    print("Please chose the action you would like to do:\n")
    print("1. Create a new hero.\n")
    print("2. Create a new squad.\n")
    print("3. Add hero to squad.\n")
    print("4. Send 2 squads to battle.\n")
    print("5. Revive a hero.\n")
    print("6. Remove a hero from a squad.\n")
    print("7. EXIT.\n")

    choice = int(input("Enter the Choice:\n"))

    if choice == 1:
        print("Ok! Lest create a new hero!\n")
        name = str(input("Enter hero name:\n"))
        power = int(input("Enter hero power:\n"))
        good = int(input("If the hero is good press 1, else, press 2.\n"))
        if good == 1:
            s.create_hero(name, 100, True, power)
        elif good == 2:
            s.create_hero(name, 100, False, power)
        else:
            print("Unknown input was entered, please try again.\n")

    elif choice == 2:
        print("Ok! Lest create a new squad!\n")
        name = str(input("Enter squad name:\n"))
        s.create_squad(name, True)

    elif choice == 3:
        print("Ok! Lest add a hero to a squad!\n")
        squad_name = str(input("Enter squad name:\n"))
        hero_name = str(input("Enter hero name:\n"))
        s.add_hero_to_squad(squad_name, hero_name)

    elif choice == 4:
        print("Ok! lets go to Battle!!")
        squad_a_name = str(input("Enter first squad name:\n"))
        squad_b_name = str(input("Enter second squad name:\n"))
        s.go_to_battle(squad_a_name, squad_b_name)

    elif choice == 5:
        print("There's a dead hero uh? ok lets try to revive them!")
        name = str(input("Enter hero name:\n"))
        s.set_hero_hp(name, 100)

    elif choice == 6:
        print("Ok! Lest remove a hero from a squad!\n")
        squad_name = str(input("Enter squad name:\n"))
        hero_name = str(input("Enter hero name:\n"))
        s.remove_hero_from_squad(squad_name, hero_name)

    elif choice == 7:
        print("Ok... it was nice to meet you. Bye Bye.\n")

    else:
        print("You entered a wrong input, please try again...\n")
