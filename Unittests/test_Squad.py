from unittest import TestCase
from Squad import Squad


class TestSquad(TestCase):
    __squad = Squad("DC", True)
    __heroes = ["Batman", "Superman", "Wonderwoman"]
    __heroes_b = ["Batman", "Superman"]

    def test_name(self):
        self.assertEqual(self.__squad.name, "DC")

    def test_is_resting(self):
        self.__squad.is_resting = False
        self.assertFalse(self.__squad.is_resting)

    def test_add_hero(self):
        self.__squad.add_hero("Batman")
        self.__squad.add_hero("Superman")
        self.__squad.add_hero("Wonderwoman")
        self.assertEqual(self.__squad.heroes,  self.__heroes)

    def test_remove_hero(self):
        self.__squad.add_hero("Batman")
        self.__squad.add_hero("Superman")
        self.__squad.add_hero("Wonderwoman")
        self.__squad.remove_hero("Wonderwoman")
        self.assertEqual(self.__squad.heroes,  self.__heroes_b)

    def test_is_hero_exists(self):
        self.__squad.add_hero("Batman")
        self.__squad.add_hero("Superman")
        self.__squad.add_hero("Wonderwoman")
        self.__squad.remove_hero("Wonderwoman")
        self.assertTrue(self.__squad.is_hero_exists("Batman"))
        self.assertTrue(self.__squad.is_hero_exists("Superman"))
        self.assertFalse(self.__squad.is_hero_exists("Wonderwoman"))
