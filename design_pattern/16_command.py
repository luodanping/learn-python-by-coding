#command

import os

class MoveFileCommand:
    def __init__(self,src,dest):
        self.src=src
        self.dest=dest

    def execute(self):
        self()  #注意这个操作

    def __call__(self): #一个类实例也可以变成一个可调用对象，只需要实现一个特殊方法__call__()。
        #https://blog.csdn.net/dongfei2033/article/details/77678312
        print("renaming {} to {}".format(self.src,self.dest))
        os.rename(self.src, self.dest)

    def undo(self):
        print("renaming {} to {}".format(self.dest,self.src))
        os.rename(self.dest, self.src)

def main():
    command_stack=[]

    #command are just pushed into the command stack
    command_stack.append(MoveFileCommand('foo.txt','bar.txt'))
    command_stack.append(MoveFileCommand('bar.txt', 'baz.txt'))

    #they can be executed into the command stack
    for cmd in command_stack:
        cmd.execute()

    #and can also be undone at will
    for cmd in reversed(command_stack):  #先把操作反过来
        cmd.undo()

if __name__=="__main__":
    main()