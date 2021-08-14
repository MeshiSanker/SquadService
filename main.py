from Service import Service
from colorama import Fore

s = Service()
choice = 0
print(Fore.BLUE + "Welcome to Squads manager!\n")


while choice != 7:
    print(Fore.BLUE + "Please chose the action you would like to do:\n")
    print(Fore.BLUE + "1. Create a new hero.\n")
    print(Fore.BLUE + "2. Create a new squad.\n")
    print(Fore.BLUE + "3. Add hero to squad.\n")
    print(Fore.BLUE + "4. Send 2 squads to battle.\n")
    print(Fore.BLUE + "5. Revive a hero.\n")
    print(Fore.BLUE + "6. Remove a hero from a squad.\n")
    print(Fore.BLUE + "7. EXIT.\n")

    choice = int(input(Fore.BLUE + "Enter the Choice:\n"))

    if choice == 1:
        print(Fore.BLUE + "Ok! Lest create a new hero!\n")
        name = str(input(Fore.BLUE + "Enter hero name:\n"))
        power = int(input(Fore.BLUE + "Enter hero power:\n"))
        good = int(input(Fore.BLUE + "If the hero is good press 1, else, press 2.\n"))
        if good == 1:
            s.create_hero(name, 100, True, power)
        elif good == 2:
            s.create_hero(name, 100, False, power)
        else:
            print(Fore.BLUE + "Unknown input was entered, please try again.\n")

    elif choice == 2:
        print(Fore.BLUE + "Ok! Lest create a new squad!\n")
        name = str(input(Fore.BLUE + "Enter squad name:\n"))
        s.create_squad(name, True)

    elif choice == 3:
        print(Fore.BLUE + "Ok! Lest add a hero to a squad!\n")
        squad_name = str(input(Fore.BLUE + "Enter squad name:\n"))
        hero_name = str(input(Fore.BLUE + "Enter hero name:\n"))
        s.add_hero_to_squad(squad_name, hero_name)

    elif choice == 4:
        print(Fore.BLUE + "Ok! lets go to Battle!!")
        squad_a_name = str(input(Fore.BLUE + "Enter first squad name:\n"))
        squad_b_name = str(input(Fore.BLUE + "Enter second squad name:\n"))
        s.go_to_battle(squad_a_name, squad_b_name)

    elif choice == 5:
        print(Fore.BLUE + "There's a dead hero uh? ok lets try to revive them!")
        name = str(input(Fore.BLUE + "Enter hero name:\n"))
        s.set_hero_hp(name, 100)

    elif choice == 6:
        print(Fore.BLUE + "Ok! Lest remove a hero from a squad!\n")
        squad_name = str(input(Fore.BLUE + "Enter squad name:\n"))
        hero_name = str(input(Fore.BLUE + "Enter hero name:\n"))
        s.remove_hero_from_squad(squad_name, hero_name)

    elif choice == 7:
        print(Fore.BLUE + "Ok... it was nice to meet you. Bye Bye.\n")

    else:
        print(Fore.BLUE + "You entered a wrong input, please try again...\n")
