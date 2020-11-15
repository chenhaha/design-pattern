# 建造者模式

"""
LOL中英雄有很多属性，如：名字，英雄模型，,Q技能，W技能，E技能， R技能，被动技能等
当需要创建
"""


import abc


class Skill(object):
    pass


class iHeroBuilder(metaclass=abc.ABCMeta):
    # builder类接口
    def build_name(self, name: str):
        pass

    def build_model(self, model: str):
        pass

    def build_q_skill(self, q: Skill):
        pass

    def build_w_skill(self, w: Skill):
        pass

    def build_e_skill(self, e: Skill):
        pass

    def build_r_skill(self, r: Skill):
        pass

    def build_passivce_skill(self, p: Skill):
        pass

    def build(self):
        pass


class Hero(object):
    # 英雄类
    def __init__(self, name: str):
        self.name = name
        self.model = None
        self.q = None
        self.w = None
        self.e = None
        self.p = None


class HeroBuilder(iHeroBuilder):
    # 英雄builder
    def __init__(self):
        self.name = None
        self.model = None
        self.q = None
        self.w = None
        self.e = None
        self.r = None
        self.p = None

    def build_name(self, name: str):
        self.name = name
        return self

    def build_model(self, model: str):
        self.model = model
        return self

    def build_q_skill(self, q: Skill):
        self.q = q
        return self

    def build_w_skill(self, w: Skill):
        self.w = w
        return self

    def build_e_skill(self, e: Skill):
        self.e = e
        return self

    def build_r_skill(self, r: Skill):
        self.r = r
        return self

    def build_passivce_skill(self, p: Skill):
        self.p = p
        return self

    def build(self):
        return Hero(name=self.name, model=self.model, q=self.q, w=self.w, e=self.e, r=self.r, p=self.passive)


q = Skill()
w = Skill()
e = Skill()
r = Skill()
passive = Skill()
builder = HeroBuilder()
# 创建一个vn
vn = builder().build_name('vn').build_model('/image/hero/Vayne.jpg').build_q_skill(q).build_w_skill(w).build_e_skill(e).build_r_skill(r).build()