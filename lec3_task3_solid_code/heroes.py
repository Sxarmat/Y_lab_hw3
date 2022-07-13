from abc import ABC, abstractmethod
from antagonistfinder import AntagonistFinder
from skills import Laser, Gun, Fighter


class SuperHero(ABC):

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def ultimate(self):
        pass


class Superman(Laser, Fighter, SuperHero):

    def __init__(self, can_use_ultimate_attack=True):
        super(Superman, self).__init__('Clark Kent', can_use_ultimate_attack)

    def attack(self):
        return self.kick()

    def ultimate(self):
        return self.incinerate_with_lasers()


class ChackNorris(Gun, SuperHero):

    def __init__(self, can_use_ultimate_attack=True):
        super(ChackNorris, self).__init__('Chack Noris', can_use_ultimate_attack)

    def attack(self):
        return self.fire_a_gun()

    def ultimate(self):
        return self.fire_a_machine_gun()
