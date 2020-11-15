# 适配器模式

"""
左伊w捡装备的主动技能
"""

import abc


class ActiveEquipment(object):
    # 有主动效果的装备
    def release(self, *args, **kwargs):
        print('release by an active equipment')


class INonTargetedSkill(metaclass=abc.ABCMeta):
    # 非指向性技能接口
    @abc.abstractmethod
    def attack(self, *args, **kwargs) -> None:
        pass


class Hero(object):
    pass


class ActiveEquipmentAdapter(INonTargetedSkill):
    def __init__(self, active_equipment) -> None:
        self.active_equipment

    def attack(self, *args, **kwargs) -> None:
        self.active_equipment.release(*args, **kwargs)

# 生成左伊
zoe = Hero()
# 左伊捡到救赎
salvation = ActiveEquipment()
salvation_adapter = ActiveEquipmentAdapter(salvation)
# 赋值稍微粗糙 
zoe.w = salvation_adapter

# 左伊释放w技能
zoe.w.attack()