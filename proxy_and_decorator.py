"""
代理模式
目的：主要对原来的接口进行访问控制，而非增强功能。主要是做跟原来接口无关的事

使用场景
1.监控、统计、鉴权、限流、事务、幂等、日志
2.RPC
3.缓存

实现:
1.原始类是实现的自己定义的接口，使用依赖注入
2.没有原始类的接口时，继承原始类

装饰模式
目的:对原来的接口进行增强

代理模式和装饰模式代码结构相同，只是应用场景不同。
"""

import abc
import time


class IActiveEquipment(metaclass=abc.ABCMeta):
    # 主动装备接口
    @abc.abstractmethod
    def release(self, *args, **kwargs):
        pass


class ActiveEquipment(IActiveEquipment):
    # 装备类
    def release(self, *args, **kwargs):
        print("release")


class CDActiveEquipmentProxy(IActiveEquipment):
    def __init__(self, active_equipment: IActiveEquipment) -> None:
        self.active_equipment = active_equipment
        # 下次可释放时间的时间戳
        self.enable_time = None
        # 冷却时间
        self.cd_time = 10

    def release(self, *args, **kwargs):
        now = time.time()
        if self.enable_time is None:
            self.enable_time = now + self.cd_time
        elif now > self.enable_time:
            self.enable_time += self.cd_time
        else:
            return

        # 只有cd好了才能释放主动技能
        self.active_equipment.release(*args, **kwargs)


class Hero(object):
    pass


# 如果是训练模式，可以无CD释放
active_equipment = ActiveEquipment()
hero = Hero()
# 假设只有一个主动技能
hero.active_equipment = active_equipment
hero.active_equipment.release()


# 带CD
proxy = CDActiveEquipmentProxy(active_equipment)
hero.active_equipment = proxy
hero.active_equipment.release()

