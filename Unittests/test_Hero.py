from unittest import TestCase
from Hero import Hero


class TestHero(TestCase):
    __hero = Hero("Batman", 100, True, 80)

    def test_name(self):
        self.assertEqual(self.__hero.name, "Batman")

    def test_hp(self):
        self.__hero.hp = 0
        self.assertEqual(self.__hero.hp, 0)

    def test_is_good(self):
        self.__hero.is_good = False
        self.assertFalse(self.__hero.is_good)

    def test_power(self):
        self.__hero.power = 90
        self.assertEqual(self.__hero.power, 90)
