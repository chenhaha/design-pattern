# 观察者模式

"""
lol玩家发送信号和接收屏蔽信号
"""

import abc


class Signal(object):
    # 各种信号（危险，撤退，正在路上等）
    pass


class Hero(object):
    # 英雄类
    pass


class IObserver(metaclass=abc.ABCMeta):
    def update(self, signal: Signal) -> None:
        pass


class HeroObserver(IObserver):
    def __init__(self, hero: Hero) -> None:
        self.hero = hero

    def update(self, signal: Signal) -> None:
        # 把signal传给hero
        print('hero {} receive the signal'.format(self.hero))


class Subject(object):
    def __init__(self, signal: Signal) -> None:
        self.signal = signal
        self.observers = []

    def add(self, observer: IObserver) -> None:
        self.observers.append(observer)

    def remove(self, observer: IObserver) -> None:
        # 线程不安全
        for index, item in self.observers:
            if item == observer:
                del self.observers[index]
                break

    def notify(self) -> None:
        for observer in self.observers:
            observer.update(self.signal)


signal = Signal()
subject = Subject(signal)
hero1 = Hero()
hero2 = Hero()
hero3 = Hero()
hero1_observer = HeroObserver(hero1)
hero2_observer = HeroObserver(hero2)
hero3_observer = HeroObserver(hero3)

subject.add(hero1)
subject.add(hero2)
subject.add(hero3)

# 有人屏蔽信号时
subject.remove(hero1)
