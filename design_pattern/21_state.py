#state

class State:
    """Base state. This is to share functionality"""

    def scan(self): #scan依次调台，会改变状态
        """Scan the dial to the next station"""
        self.pos+=1
        if self.pos==len(self.stations):
            self.pos=0
        print("Scaning ... Station is",self.stations[self.pos], self.name)

class AmState(State): #Am状态
    def __init__(self,radio):
        self.radio = radio
        self.stations =["1250","1380","1510"]
        self.pos=0
        self.name="AM"

    def toggle_amfm(self):
        print("Switching to FM")
        self.radio.state=self.radio.fmstate

class FmState(State): #Fm状态
    def __init__(self,radio):
        self.radio = radio
        self.stations =["81.3","89.1","103.9"]
        self.pos=0
        self.name="FM"

    def toggle_amfm(self):
        print("Switching to AM")
        self.radio.state=self.radio.amstate

class Radio:
    """A radio. It has a scan button and AM/FM toggle switch"""
    def __init__(self):
        """We have an AM state and an FM state"""
        self.amstate = AmState(self) #将对象本身传给了状态对象，因此状态对象也时可以改变对象本身的嘛
        self.fmstate=FmState(self)
        self.state=self.amstate

    def toggle_amfm(self): #允许一个对象在其内部状态改变时改变它的行为。对象看起来似乎修改了它的类。
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()

#Test our radio out
def main():
    radio = Radio()
    actions = [radio.scan]*2 + [radio.toggle_amfm] + [radio.scan]*2
    actions*=2

    for action in actions:
        action()

if __name__=="__main__":
    main()