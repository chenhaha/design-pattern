# 策略模式

import abc


class Hero(object):
    def __init__(self, name) -> None:
        self.name = name


class IBuff(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def buff(self, hero: Hero) -> None:
        pass


class RedBuff(IBuff):
    def buff(self, hero: Hero) -> None:
        print("enhance {name} by red buff".format(name=hero.name))


class BlueBuff(IBuff):
    def buff(self, hero: Hero) -> None:
        print("enhance {name} by blue buff".format(name=hero.name))


class BaronBuff(IBuff):
    def buff(self, hero: Hero) -> None:
        print("enhance {name} by blue buff".format(name=hero.name))


red_buff = RedBuff()
blue_buff = BlueBuff()
baron_buff = BaronBuff()
hero = Hero()

buff_map = {
    "red_buff": red_buff,
    "blue_buff": blue_buff,
    "baron_buff": baron_buff
}

# 从map中获取实际得到的buff作用于英雄
buff = buff_map.get('red_buff')
buff.buff(hero)
