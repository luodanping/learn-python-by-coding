#visitor

class Node:
    pass

class A(Node):
    pass

class B(Node):
    pass

class C(A,B):
    pass

class Visitor:
    def visit(self,node, *args, **kwargs):
        meth=None
        for cls in node.__class__.__mro__: #mro: method resolution order
            meth_name="visit_"+cls.__name__
            print(meth_name)
            meth=getattr(self,meth_name,None)  #查看是否能与visit_B匹配
            if meth:  #如果出现会立刻跳出for循环的
                break

        if not meth:
            meth=self.generic_visit
        return meth(node, *args,**kwargs)

    def generic_visit(self,node,*args,**kwargs):
        print("generic_visit"+node.__class__.__name__)

    def visit_B(self,node,*args,**kwargs):
        print("visit_B"+node.__class__.__name__)

a=A()
b=B()
c=C()
visitor=Visitor()
visitor.visit(a)
visitor.visit(b)
visitor.visit(c)