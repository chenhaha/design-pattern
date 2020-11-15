from os import pathconf


def load(path: str):
    # 假设是加载图片的函数
    return path


class TurretModel(object):
    # 防御塔3D模型
    _instance = None

    def __new__(cls, *args, **kwargs):
        # 初始化的参数(args, kwargs)会传给__new__和__init__
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, path: str) -> None:
        self.model = load(path) 


m1 = TurretModel('/img/turret.jpg')
m2 = TurretModel('/img/turret.jpg')
print(id(m1) == id(m2))