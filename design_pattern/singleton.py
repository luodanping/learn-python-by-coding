#The same with 5_singleton.py
#just want to test singleton but the module seems to fail when prefix of number

class Singleton():
    """A python style singleton"""
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"_instance"):
            org=super(Singleton,cls) #super(B, self)首先找到B的父类（就是类A），然后把类B的对象self转换为类A的对象
            cls._instance=org.__new__(cls)
        return cls._instance

class SingleSpam(Singleton):
    def __init__(self,s):
        self.s=s

    def __str__(self):
        return self.s

def main():
    s1 = SingleSpam("spam")
    print(id(s1),s1)
    s2=SingleSpam("spa")
    print(id(s2), s2)
    print(id(s1),s1)

if __name__=="__main__":
    main()