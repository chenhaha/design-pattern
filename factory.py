# 工厂方法模式

"""
召唤师峡谷和大乱斗地图中有些机制不同
比如：泉水回血机制，防御塔镀层机制
"""

import abc


class Fountain(object):
    """
    泉水类
    """
    def __init__(self, x: int, y: int, can_recover_hp: bool, can_recover_mp: bool, can_buy_when_returning: bool):
        """
        @param x: 横坐标
        @param y: 纵坐标
        @param can_recover_hp: 能否回复生命值
        @param can_recover_mp: 能否回复蓝量/能量
        @param can_buy_when_returning: 出门后回泉水能否购物
        """
        self.x = x
        self.y = y
        self.can_recover_hp = can_recover_hp
        self.can_recover_mp = can_recover_mp
        self.can_buy_when_returning = can_buy_when_returning


class Turret(object):
    """防御塔"""
    def __init__(self, x: int, y: int, max_hp: int, hp: int, has_coat: bool, coat_reward: int):
        """
        @param x: 横坐标
        @param y: 纵坐标
        @param max_hp: 最大血量
        @param hp: 当前血量
        @has_coat: 是否有镀层
        @coat_reward: 镀层奖励金
        """
        self.x = x
        self.y = y
        self.max_hp = hp
        self.hp = hp
        self.has_coat = has_coat
        self.coat_reward = coat_reward


class iMapFactory(metaclass=abc.ABCMeta):
    """地图工厂接口"""
    @abc.abstractmethod
    def create_fountain(self, x: int, y: int) -> Fountain:
        pass

    @abc.abstractmethod
    def create_turret(self, x: int, y: int) -> Turret:
        pass


class RiftFactory(iMapFactory):
    """
    峡谷工厂
    """
    def create_fountain(self, x: int, y: int) -> Fountain:
        return Fountain(x, y, can_recover_hp=True, can_recover_mp=True, can_buy_when_returning=True)

    def create_turret(self, x: int, y: int):
        return Turret(x, y, max_hp=2000, hp=2000, has_coat=True, coat_reward=100) 


class ARAMFactory(iMapFactory):
    """
    大乱斗工厂
    """
    def create_fountain(self, x: int, y: int) -> Fountain:
        return Fountain(x, y, can_recover_hp=False, can_recover_mp=False, can_buy_when_returning=False)

    def create_turret(self, x: int, y: int) -> Turret:
        return Turret(x, y, max_hp=2000, hp=2000, has_coat=False, coat_reward=0)


class Map(metaclass=abc.ABCMeta):
    """
    地图接口
    """
    @abc.abstractmethod
    def init_objs(self):
        """
        地图初始化
        """


class RiftMap(Map):
    """
    召唤师峡谷地图
    """
    def init_objs(self):
        rift_factory = RiftFactory()
        # 蓝色方泉水
        blue_fountain = rift_factory.create_fountain(0, 2000)
        # 红色方泉水
        red_fountain = rift_factory.create_turret(2000, 0)

        turret_1 = rift_factory.create_turret(10, 10)
        turret_2 = rift_factory.create_turret(20, 20)


class ARAMMap(Map):
    """
    大乱斗地图
    """
    def init_objs(self):
        aram_factory = ARAMFactory()
        # 蓝色方泉水
        blue_fountain = aram_factory.create_fountain(0, 2000)
        # 红色方泉水
        blue_fountain = aram_factory.create_fountain(2000, 0)

        turret_1 = aram_factory.create_turret(10, 10)
        turret_2 = aram_factory.create_turret(20, 20)