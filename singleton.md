# 单例模式

+ 确保一个类只有一个实例，节约资源

LOL中防御塔的样子都是一样的，因此只需要在内存里加载一个防御塔模型。假设防御塔的静态资源是一张图片，使用单例模式节约了多次读图片的时间，也节省了内存

```python
def Load(path: str):
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
```

缺点：多线程下可能两个线程都会判断`_instance`为`None`