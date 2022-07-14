from antagonistfinder import AntagonistFinder
from skills import Laser, Gun, Fighter


class SuperHero:

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)

    def attack(self):
        arsenal = Gun()
        arsenal.fire_a_gun()

    def ultimate(self):
        arsenal = Gun()
        arsenal.fire_a_machine_gun()


class Superman(SuperHero):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    def attack(self):
        arsenal = Fighter()
        arsenal.kick()

    def ultimate(self):
        arsenal = Laser()
        arsenal.incinerate_with_lasers()

