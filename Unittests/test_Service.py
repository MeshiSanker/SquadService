from unittest import TestCase
from Service import Service


class TestService(TestCase):
    __service = Service()

    def test_create_hero(self):
        self.__service.create_hero("Batman", 100, True, 80)
        self.assertTrue(self.__service.is_hero_exists("Batman"))

    def test_get_hero_index(self):
        self.__service.create_hero("Batman", 100, True, 80)
        self.assertEqual(self.__service.get_hero_index("Batman"), 0)

    def test_create_squad(self):
        self.__service.create_squad("DC", True)
        self.assertTrue(self.__service.is_squad_exists("DC"))

    def test_get_squad_index(self):
        self.__service.create_squad("DC", True)
        self.assertEqual(self.__service.get_squad_index("DC"), 0)

    def test_add_hero_to_squad(self):
        self.__service.create_hero("Batman", 100, True, 80)
        self.__service.create_squad("DC", True)
        self.__service.add_hero_to_squad("DC", "Batman")
        self.assertTrue(self.__service.is_hero_in_squad("DC", "Batman"))

    def test_remove_hero_from_squad(self):
        self.__service.create_hero("Batman", 100, True, 80)
        self.__service.create_squad("DC", True)
        self.__service.add_hero_to_squad("DC", "Batman")
        self.__service.remove_hero_from_squad("DC", "Batman")
        self.assertFalse(self.__service.is_hero_in_squad("DC", "Batman"))

    def test_go_to_battle(self):
        self.__service.create_hero("Batman", 100, True, 80)
        self.__service.create_hero("Superman", 100, True, 90)
        self.__service.create_squad("DC", True)
        self.__service.create_squad("Justice League", True)
        self.__service.add_hero_to_squad("DC", "Batman")
        self.__service.add_hero_to_squad("Justice League", "Superman")
        self.__service.go_to_battle("Justice League", "DC")
        self.assertTrue(self.__service.is_dead_hero_in_squad("DC"))

    def test_check_if_valid_battle(self):
        self.__service.create_hero("Batman", 100, True, 80)
        self.__service.create_hero("Superman", 100, True, 80)
        self.__service.create_squad("DC", True)
        self.__service.create_squad("Justice League", True)
        self.__service.add_hero_to_squad("DC", "Batman")
        self.__service.add_hero_to_squad("Justice League", "Superman")
        self.__service.set_hero_hp("Batman", 0)
        self.assertFalse(self.__service.check_if_valid_battle("DC", "Justice League"))

    def test_is_squad_resting(self):
        self.__service.create_squad("DC", True)
        self.__service.set_squad_resting("DC", False)
        self.assertFalse(self.__service.is_squad_resting("DC"))

    def test_check_if_common_hero(self):
        self.__service.create_hero("Batman", 100, True, 80)
        self.__service.create_squad("DC", True)
        self.__service.create_squad("Justice League", True)
        self.__service.add_hero_to_squad("DC", "Batman")
        self.__service.add_hero_to_squad("Justice League", "Batman")
        self.assertTrue(self.__service.check_if_common_hero("DC", "Justice League"))

    def test_get_squad_power(self):
        self.__service.create_hero("Batman", 100, True, 80)
        self.__service.create_hero("Superman", 100, True, 80)
        self.__service.create_squad("DC", True)
        self.__service.add_hero_to_squad("DC", "Batman")
        self.__service.add_hero_to_squad("DC", "Superman")
        self.assertEqual(self.__service.get_squad_power("DC"), 160)

    def test_kill_squad(self):
        self.__service.create_hero("Batman", 100, True, 80)
        self.__service.create_squad("DC", True)
        self.__service.add_hero_to_squad("DC", "Batman")
        self.__service.kill_squad("DC")
        self.assertTrue(self.__service.is_dead_hero_in_squad("DC"))

    def test_set_hero_hp(self):
        self.__service.create_hero("Batman", 100, True, 80)
        self.__service.create_squad("DC", True)
        self.__service.add_hero_to_squad("DC", "Batman")
        self.__service.set_hero_hp("Batman", 0)
        self.assertTrue(self.__service.is_dead_hero_in_squad("DC"))

