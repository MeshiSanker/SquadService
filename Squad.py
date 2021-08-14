from colorama import Fore


class Squad:
    def __init__(self, name: str, is_resting: bool):
        self.__heroes = []
        self.__name = name
        self.__is_resting = is_resting
        print(Fore.GREEN + "Squad: {} was created successfully.\n".format(self.__name))

    @property
    def name(self) -> str:
        return self.__name

    @property
    def is_resting(self) -> bool:
        return self.__is_resting

    @property
    def heroes(self) -> list:
        return self.__heroes

    @is_resting.setter
    def is_resting(self, is_resting: bool):
        self.__is_resting = is_resting

    def add_hero(self, name: str):
        """
        This method ia adding a hero to the squad.
        Only the name will be added.
        :param name: hero's name
        :return:
        """
        if not self.is_hero_exists(name):
            self.__heroes.append(name)
            print(Fore.GREEN + "Hero: {}, was added to the squad:{}\n".format(name, self.__name))

        else:
            print(Fore.YELLOW + "Hero: {}, is already in the squad: {}.\n".format(name, self.__name))

    def remove_hero(self, name: str):
        """
        This method ia removing a hero to the squad.
        :param name: hero's name
        :return:
        """
        if self.is_hero_exists(name):
            self.__heroes.remove(name)
            print(Fore.GREEN + "Hero: {}, removed from the squad:{}\n".format(name, self.__name))
        else:
            print(Fore.YELLOW + "Hero: {} is already not in squad: {}.\n".format(name, self.__name))

    def is_hero_exists(self, hero_name: str):
        """
        Check if hero is in squad.
        :param hero_name: Hero's name
        :return:
        """
        if next((i for i, hero in enumerate(self.__heroes) if hero == hero_name), -1) >= 0:
            return True
        return False
