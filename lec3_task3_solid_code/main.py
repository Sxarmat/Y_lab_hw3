from typing import Union
from heroes import Superman, ChackNorris, SuperHero
from places import Kostroma, Tokyo
from mass_media import MassMedia


def save_the_place(hero: SuperHero, place: Union[Kostroma, Tokyo], media: MassMedia):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    media.create_news(hero, place)


if __name__ == '__main__':
    media = MassMedia()
    save_the_place(Superman(), Kostroma(), media)
    print('-' * 20)
    save_the_place(ChackNorris(False), Tokyo(), media)



