from Hero import Hero
from Squad import Squad
from colorama import Fore


class Service:
    def __init__(self):
        self.__squads = []
        self.__heroes = []

    def create_hero(self, name: str, hp: int, is_good: bool, power: int):
        """
        Creating a new hero to the heroes list.
        In case hero's name is already exists, print an appropriate message.
        :param name:Hero's name
        :param hp: Hero's hp (health points)
        :param is_good: Is the hero good or bad (True/False)
        :param power:Hero's power
        :return:
        """
        if self.is_hero_exists(name):
            print(Fore.YELLOW + "Hero already exists.\n")
        else:
            self.__heroes.append(Hero(name, hp, is_good, power))

    def create_squad(self, name: str, is_resting: bool):
        """
        Creating a new squad to the squads list.
        In case squad's name is already exists, print an appropriate message.
        :param name: Squad's name
        :param is_resting: Is the squad resting or in action (True/False)
        :return:
        """
        if self.is_squad_exists(name):
            print(Fore.YELLOW + "Squad already exists.\n")
        else:
            self.__squads.append(Squad(name, is_resting))

    def is_hero_exists(self, hero_name: str) -> bool:
        """
        Checking if the hero already exists in the list, by name.
        :param hero_name: Hero's name
        :return: True/False
        """
        if self.get_hero_index(hero_name) >= 0:
            return True
        return False

    def is_squad_exists(self, squad_name: str) -> bool:
        """
        Checking if the squad already exists in the list, by name.
        :param squad_name: Squad's name
        :return: True/False
        """
        if self.get_squad_index(squad_name) >= 0:
            return True
        return False

    def is_hero_in_squad(self, squad_name: str, hero_name: str) -> bool:
        """
        Checking if a hero exist in a squad
        :param squad_name: Squad's name
        :param hero_name: Hero's name
        :return: True/False
        """
        return self.__squads[self.get_squad_index(squad_name)].is_hero_exists(hero_name)

    def is_squad_resting(self, squad_name: str) -> bool:
        """
        Checking if the squad is resting
        :param squad_name: Squad's name
        :return: True/False
        """
        return self.__squads[self.get_squad_index(squad_name)].is_resting

    def is_dead_hero_in_squad(self, squad_name) -> bool:
        """
        Check if there's a dead hero in a given squad.
        :param squad_name: Squad's name
        :return: True/False
        """
        for hero in self.__squads[self.get_squad_index(squad_name)].heroes:
            if self.__heroes[self.get_hero_index(hero)].hp == 0:
                print(Fore.RED + "Hero: {} is Dead, you can revive them.\n".format(hero))
                return True
        return False

    def get_hero_index(self, hero_name: str) -> int:
        """
        Find the index of a hero in the heroes array by name.
        :param hero_name: Hero's name
        :return: Hero's index
        """
        return next((i for i, hero in enumerate(self.__heroes) if hero.name == hero_name), -1)

    def get_squad_index(self, squad_name: str) -> int:
        """
        Find the index of a squad in the squad array by name.
        :param squad_name: Squad's name
        :return: Squad's index
        """
        return next((i for i, squad in enumerate(self.__squads) if squad.name == squad_name), -1)

    def get_squad_power(self, squad_name: str) -> int:
        """
        Get the total power of a squad
        :param squad_name: Squad's name
        :return: total power of squad
        """
        heroes_list = [hero for hero in self.__heroes if self.is_hero_in_squad(squad_name, hero.name)]
        return sum(hero.power for hero in heroes_list)

    def add_hero_to_squad(self, squad_name: str, hero_name):
        """
        Add an existing hero to an existing squad
        :param squad_name: Squad's name
        :param hero_name: Hero's name
        :return:
        """
        if self.is_hero_exists(hero_name) and self.is_squad_exists(squad_name):
            self.__squads[self.get_squad_index(squad_name)].add_hero(hero_name)
        else:
            print(Fore.RED + "Squad or hero doesn't exist.")

    def remove_hero_from_squad(self, squad_name: str, hero_name):
        """
        Remove a hero from an existing squad
        :param squad_name: Squad's name
        :param hero_name: Hero's name
        :return:
        """
        if self.is_hero_exists(hero_name) and self.is_squad_exists(squad_name):
            self.__squads[self.get_squad_index(squad_name)].remove_hero(hero_name)

    def set_squad_resting(self, squad_name: str, is_resting: bool):
        """
        Set resting status of a given squad
        :param squad_name: Squad's name
        :param is_resting: Resting status (True/False)
        :return:
        """
        self.__squads[self.get_squad_index(squad_name)].is_resting = is_resting

    def set_hero_hp(self, hero_name: str, hp: int):
        """
        Set wanted hero hp.
        :param hero_name: Hero's name
        :param hp: HP to set to hero
        :return:
        """
        self.__heroes[self.get_hero_index(hero_name)].hp = hp
        print(Fore.GREEN + "Hero: {} HP was set to: {}.\n".format(hero_name, hp))

    def check_if_common_hero(self, squad_a_name: str, squad_b_name: str) -> bool:
        """
        Check if 2 squads share a common hero
        :param squad_a_name: First squad name
        :param squad_b_name: Second squad name
        :return: True/False
        """
        for hero in self.__squads[self.get_squad_index(squad_a_name)].heroes:
            if self.__squads[self.get_squad_index(squad_b_name)].is_hero_exists(hero):
                return True
        return False

    def kill_squad(self, squad_name: str):
        """
        Set all heroes in a squad to 0.
        :param squad_name: Squad's name
        :return:
        """
        for hero in self.__squads[self.get_squad_index(squad_name)].heroes:
            self.set_hero_hp(hero, 0)

    def check_if_valid_battle(self, squad_a_name: str, squad_b_name: str) -> bool:
        """
        Validating that 2 squads can go to battle.
        Both squads should exist and need to resting, there should not be a common hero to the squads.
        :param squad_a_name: First squad name
        :param squad_b_name: Second squad name
        :return: True/False
        """
        if not self.is_squad_exists(squad_a_name) or not self.is_squad_exists(squad_b_name):
            print(Fore.RED + "One of the squads you entered doesn't exist, please try again.\n")
            return False

        if not self.is_squad_resting(squad_a_name) or not self.is_squad_resting(squad_b_name):
            print(Fore.RED + "One or more of the squads are in mid battle, please try again later.\n")
            return False

        if self.check_if_common_hero(squad_a_name, squad_b_name):
            print(Fore.RED + "There's a common hero to the two squads, please try squads that don't share a hero.\n")
            return False

        if self.is_dead_hero_in_squad(squad_a_name) or self.is_dead_hero_in_squad(squad_b_name):
            print(Fore.RED + "There's a dead hero in one of the squads, try to revive them or pick another squad.\n")
            return False

        return True

    def go_to_battle(self, squad_a_name: str, squad_b_name: str):
        """
        Check if the battle is valid and check who's the winner.
        In the start of the battle, change resting status of the squads to False.
        In the end of the battle, kill all heroes in the losing squad and change squads resting status to True.
        :param squad_a_name: First squad's name
        :param squad_b_name: Second squad's name
        :return:
        """
        if self.check_if_valid_battle(squad_a_name, squad_b_name):
            print(Fore.GREEN + "Battle is valid, lets Start!\n")

        else:
            print(Fore.RED + "Battle can't start due the above issue")
            return

        self.set_squad_resting(squad_a_name, False)
        self.set_squad_resting(squad_b_name, False)

        squad_a_power = self.get_squad_power(squad_a_name)
        squad_b_power = self.get_squad_power(squad_b_name)

        if squad_a_power > squad_b_power:
            print(Fore.MAGENTA + "Squad: {} is the winner!\n".format(squad_a_name))
            self.kill_squad(squad_b_name)
        elif squad_a_power == squad_b_power:
            print(Fore.MAGENTA + "There's a tie! no winner or loser!\n")
        else:
            print(Fore.MAGENTA + "Squad: {} is the winner!\n".format(squad_b_name))
            self.kill_squad(squad_a_name)

        self.set_squad_resting(squad_a_name, True)
        self.set_squad_resting(squad_b_name, True)







