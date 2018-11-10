#memento

import copy

def Memento(obj, deep=False): #deep表示是否使用deepcopy
    state = (copy.copy, copy.deepcopy)[bool(deep)](obj.__dict__) #False取第0个元素，True取第一个元素

    def Restore():
        obj.__dict__.clear()
        obj.__dict__.update(state)
    return Restore

class Transaction:
    """A transaction guard. This is really just syntatic suggar arount a memento closure"""
    deep = False

    def __init__(self,*targets):
        self.targets = targets
        self.Commit()

    def Commit(self):
        self.states = [Memento(target, self.deep) for target in self.targets]

    def Rollback(self):
        for st in self.states:
            st()

class transactional:
    """Adds transactional semantics to methods. Methods decorated with
    @transacrional will rollback to entry state upon exceptions"""
    def __init__(self, method):
        self.method=method #通过修饰器传入method

    def __get__(self, obj, T): #https://www.cnblogs.com/saolv/p/6890645.html

        #object.__get__(self, instance, owner) owner是所有者的类，instance是访问descriptor的实例，如果不是通过实例访问，而是通过类访问的话，instance则为None
        # print(obj) #<NumObj:2>调用本身
        #print(T) #<class '__main__.NumObj'> obj的类型
        def transaction(*args, **kwargs):
            state=Memento(obj)
            try:
                return self.method(*args,**kwargs) #使用该method将会报错。
            except:
                state() #进行恢复
                raise
        return transaction #返回一个函数对象，没加()

class NumObj:
    def __init__(self,value):
        self.value=value

    def __repr__(self):
        return "<%s:%r>"%(self.__class__.__name__, self.value)

    def Increment(self):
        self.value+=1

    @transactional  #变成了 DoStuff=transactional(DoStuff)  =>一个类就变成了NumObj的一个属性，当被访问时，由类中的__get__控制
    def DoStuff(self): #当作参数传给transactional
        self.value="1111" #<- invalid value #传入非法值
        self.Increment()  #<- will fail and rollback

def main():
    n=NumObj(-1)
    print(n)
    t=Transaction(n)
    try:
        for i in range(3):
            n.Increment()
            print(n)
        t.Commit()
        print("-- committed")
        for i in range(3):
            n.Increment()
            print(n)
        n.value+="x" #will fail here
        print(n)
    except:
        t.Rollback()
        print("-- rolled back")

    print(n)
    print("-- now doing stuff --")
    try:
        n.DoStuff() #加()执行
    except:
        print("-> doing stuff failed")
        import traceback
        traceback.print_exc(0)
        pass
    print(n)

if __name__=="__main__":
    main()