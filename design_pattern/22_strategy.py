# strategy

"""
In most of other language Strategy pattern is implemented via creating some base strategy interface/abstract
subclassing it with a number of concreate strategies(as we can see at http://en.wikipedia.org/wiki/Strategy_pattern),
however python supports higher-order functions and allows us to have only one class and inject functions into it's
instances,as shown in this example
"""

import types #types模块中包含python中各种常见的数据类型，如IntType(整型)，FloatType(浮点型)等等。

class StrategyExample:
    def __init__(self, func=None):
        self.name = "Strategy Example 0"
        if func is not None:
            self.execute= types.MethodType(func, self) #https://blog.csdn.net/qq_35075164/article/details/80918072
            # 将方法绑定到对象上第一个参数是要绑定的方法，第二个参数是要绑定的对象，第三个参数是类名（可省略）
            #也可用于将方法绑定在类上，具体见参考文献
            #按照结果：就会覆盖已有的方法属性
    def execute(self):
        print(self.name)

def execute_replacement1(self):
    print(self.name + " from execute1")

def execute_replacement2(self):
    print(self.name + " from execute2")

def main():
    strat0 = StrategyExample()

    strat1=StrategyExample(execute_replacement1)
    strat1.name="Strategy example1"

    strat2=StrategyExample(execute_replacement2)
    strat2.name ="Strategy example2"

    strat0.execute()
    strat1.execute()
    strat2.execute()

if __name__=="__main__":
    main()