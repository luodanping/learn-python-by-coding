# flyweight

import weakref #对一个对象的弱引用。相对于通常的引用来说，如果一个对象有一个常规的引用，它是不会被垃圾收集器销毁的，但是如果一个对象只剩下一个弱引用，那么它可能被垃圾收集器收回。
#并非所有的对象都支持weakref，例如list和dict就不支持，但是文档中介绍了可以通过继承dict来支持weakref。

class Card:
    """The object pool. Has builtbin reference counting"""
    _CardPool = weakref.WeakValueDictionary()

    """Flyweight implementation. If the object exists in the 
    pool just return it(instead of creating a new one)"""
    def __new__(cls, value, suit):
        obj = Card._CardPool.get(value+suit, None)
        if not obj:
            obj= object.__new__(cls)
            Card._CardPool[value+suit]=obj
            obj.value, obj.suit = value, suit
        return obj

    def __repr__(self):
        return "<Card: %s%s>"%(self.value, self.suit)

def main():
    c1=Card("9","h")
    c2=Card("9","h")
    print(c1,c2)
    print(c1==c2)
    print(id(c1),id(c2))

if __name__=="__main__":
    main()