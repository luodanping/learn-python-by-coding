#decorator

class foo:
    def f1(self):
        print("original f1")

    def f2(self):
        print("original f2")

class foo_decorator:
    def __init__(self, decoratee):
        self._decoratee=decoratee

    def f1(self):
        print("decorated f1")
        self._decoratee.f1()

    def __getattr__(self, name): # 如果属性查找（attribute lookup）在实例以及对应的类中（通过__dict__)失败， 那么会调用到类的__getattr__函数, 如果没有定义这个函数，那么抛出AttributeError异常
        #python __getattr__ 巧妙应用: https://www.cnblogs.com/xybaby/p/6280313.html
        return getattr(self._decoratee,name)

def main():
    u=foo()
    v=foo_decorator(u)
    v.f1()
    #v.f2()

if __name__=="__main__":
    main()
