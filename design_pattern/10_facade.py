#facade

import time

SLEEP=0.5

#complex parts
class TC1:
    def run(self):
        print("#"*5+" In Text 1 "+"#"*5)
        time.sleep(SLEEP)
        print("Setting up")
        time.sleep(SLEEP)
        print("Running test")
        time.sleep(SLEEP)
        print("Tearing down")
        time.sleep(SLEEP)
        print("Test finished\n")

class TC2:
    def run(self):
        print("#"*5+" In Text 2 "+"#"*5)
        time.sleep(SLEEP)
        print("Setting up")
        time.sleep(SLEEP)
        print("Running test")
        time.sleep(SLEEP)
        print("Tearing down")
        time.sleep(SLEEP)
        print("Test finished\n")

class TC3:
    def run(self):
        print("#"*5+" In Text 3 "+"#"*5)
        time.sleep(SLEEP)
        print("Setting up")
        time.sleep(SLEEP)
        print("Running test")
        time.sleep(SLEEP)
        print("Tearing down")
        time.sleep(SLEEP)
        print("Test finished\n")

#Facade
class TestRunner:
    def __init__(self):
        self.tc1=TC1()
        self.tc2=TC2()
        self.tc3=TC3()
        self.tests=[i for i in (self.tc1,self.tc2,self.tc3)]

    def runAll(self):
        #[i.run() for i in self.tests]  #跟下面的具有同样的功能
        for i in self.tests:
            i.run()

def main():
    testrunner = TestRunner()
    testrunner.runAll()

if __name__=="__main__":
    main()
