class Hero:

    def __init__(self, name: str, hp: int, is_good: bool, power: int):
        self.__name = name
        self.__hp = hp
        self.__is_good = is_good
        self.__power = power
        print("Hero: {} was created successfully.\n".format(self.__name))

    @property
    def name(self) -> str:
        return self.__name

    @property
    def hp(self) -> int:
        return self.__hp

    @property
    def is_good(self) -> bool:
        return self.__is_good

    @property
    def power(self) -> int:
        return self.__power

    @hp.setter
    def hp(self, hp: int):
        self.__hp = hp

    @is_good.setter
    def is_good(self, is_good: bool):
        self.__is_good = is_good

    @power.setter
    def power(self, power: int):
        self.__power = power
