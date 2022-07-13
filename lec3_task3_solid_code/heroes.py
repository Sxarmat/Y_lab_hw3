from antagonistfinder import AntagonistFinder
from skills import Laser, Gun, Fighter
from mass_media import MassMedia


class SuperHero(Gun):

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()
        self.news_creator = MassMedia()

    def find(self, place):
        self.finder.get_antagonist(place)

    def attack(self):
        self.fire_a_gun()

    def ultimate(self):
        self.fire_a_machine_gun()

    def create_news(self, place):
        self.news_creator.create_news(self.name, place)


class Superman(Laser, Fighter, SuperHero):

    def __init__(self, can_use_ultimate_attack=True):
        super(Superman, self).__init__('Clark Kent', can_use_ultimate_attack)

    def attack(self):
        return self.kick()

    def ultimate(self):
        return self.incinerate_with_lasers()

