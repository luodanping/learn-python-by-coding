#observer

class Subject:
    def __init__(self):
        self._observers=[] #观察者的列表

    def attach(self,obesrver):
        if not obesrver in self._observers:
            self._observers.append(obesrver)

    def detach(self,observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None): #遍历观察者
        for observer in self._observers:
            if modifier != observer:
                observer.update(self) #通过self传递数据本身的信息

#Example usage
class Data(Subject):
    def __init__(self, name=""):
        #Subject.__init__(self)
        super(Data,self).__init__()
        self.name =name
        self._data=0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self,value):
        self._data=value
        self.notify()  #设置数据的时候，就会触发这个notify

class HexViewer:
    def update(self,subject):
        print("HexViewer: Subject %s has data 0x%x"%(subject.name,subject.data))

class DecimalViewer:
    def update(self,subject):
        print("DecimalViewer: Subject %s has data %d"%(subject.name,subject.data))

def main():
    data1 = Data("Data1")
    data2 = Data("Data2")
    view1=DecimalViewer()
    view2=HexViewer()
    data1.attach(view1)
    data1.attach(view2)
    data2.attach(view2)
    data2.attach(view1)

    print("Setting Data1 = 10")
    data1.data = 10
    print("Setting Data2 = 15")
    data2.data = 15
    print("Setting Data1 = 3")
    data1.data = 10
    print("Setting Data2 = 5")
    data1.data = 5

    print("Detach HexViewer from data1 and data2")
    data1.detach(view2)
    data2.detach(view2)
    print("Setting data1 =10")
    data1.data=10
    print ("Setting data2 =15")
    data2.data=15

if __name__=="__main__":
    main()