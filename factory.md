# 工厂方法模式

主要目的是隐藏创建细节

设计模式描述的是类之间关系，代码分层的情况下才适用

场景:召唤师峡谷和大乱斗地图中有些机制不同,比如：召唤师峡谷泉水有回血回蓝的效果，大乱斗里没有；召唤师峡谷一塔有镀层，大乱斗也没有。

泉水类是比较底层的类，需要高层的类比如Map类调用，当高层类调用时其实只需要知道把泉水放在什么位置就可以了，并不需要知道其他初始化参数。

假设现在有两个类，一个Fountain类，一个Turret类

```python
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
```

现在有两张地图,召唤师峡谷和大乱斗，需要创建泉水和防御塔，以下为不用工厂模式的时候代码

```python
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
        # 蓝色方泉水
        blue_fountain = Fountain(0, 2000, can_recover_hp=True, can_recover_mp=True, can_buy_when_returning=True)
        # 红色方泉水
        red_fountain = Fountain(2000, 0, can_recover_hp=True, can_recover_mp=True, can_buy_when_returning=True)

        turret_1 = Turret(10, 10, max_hp=2000, hp=2000, has_coat=True, coat_reward=100)
        turret_2 = Turret(10, 10, max_hp=2000, hp=2000, has_coat=True, coat_reward=100)


class ARAMMap(Map):
    """
    大乱斗地图
    """
    def init_objs(self):
        # 蓝色方泉水
        blue_fountain = Fountain(0, 2000, can_recover_hp=False, can_recover_mp=False, can_buy_when_returning=False)
        # 红色方泉水
        blue_fountain = Fountain(0, 2000, can_recover_hp=False, can_recover_mp=False, can_buy_when_returning=False)

        turret_1 = Turret(10, 10, max_hp=2000, hp=2000, has_coat=False, coat_reward=0)
        turret_2 = Turret(10, 10, max_hp=2000, hp=2000, has_coat=False, coat_reward=0
```

当需要创建泉水或防御塔的时候需要传很多参数，但是在某个固定的地图中有些参数是固定的，不容易修改的，比如***能否回复血量***

使用工厂方法模式的代码如下

```python
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
```

在上层代码调用时只需要获取一个工厂实例，在***峡谷地图***中初始化***峡谷工厂***。这个工厂就可以生产出泉水，防御塔等对象,并且只需要传入对象等坐标即可

+ factory pattern: 获取一个简单对象

+ builder pattern: 注重创建对象的过程，一步一步精确的构造出一个复杂对象，通常需要链式调用

[以下为参考](https://www.runoob.com)
> 工厂方法模式注重的是整体对象的创建方法，而建造者模式注重的是部件构建的过程，旨在通过一步一步地精确构造创建出一个复杂的对象。
我们举个简单例子来说明两者的差异，如要制造一个超人，如果使用工厂方法模式，直接产生出来的就是一个力大无穷、能够飞翔、内裤外穿的超人；
而如果使用建造者模式，则需要组装手、头、脚、躯干等部分，然后再把内裤外穿，于是一个超人就诞生了。
>
>工厂方法模式创建的产品一般都是单一性质产品，如成年超人，都是一个模样，而建造者模式创建的则是一个复合产品，它由各个部件复合而成，部件不同产品对象当然不同。
>这不是说工厂方法模式创建的对象简单，而是指它们的粒度大小不同。一般来说，工厂方法模式的对象粒度比较粗，建造者模式的产品对象粒度比较细。
>
>两者的区别有了，那在具体的应用中，我们该如何选择呢？
>是用工厂方法模式来创建对象，还是用建造者模式来创建对象，这完全取决于我们在做系统设计时的意图，如果需要详细关注一个产品部件的生产、安装步骤，则选择建造者，否则选择工厂方法模式。
