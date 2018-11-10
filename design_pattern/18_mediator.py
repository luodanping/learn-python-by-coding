#mediator
#用一个中介对象来封装一系列的对象交互。中介者使各对象不需要显式地相互引用，从而使其耦合松散，而且可以独立地改变它们之间的交互。
#https://www.cnblogs.com/snaildev/p/7686908.html

import time

class TC: #理解：通过其控制整个test
    def __init__(self):
        self._tm=None#tm #FIXME
        #print(tm)
        self._bProblem=0

    def setup(self):
        print("Setting up the Test")
        time.sleep(1)
        self._tm.prepareReporting() #理解：通过TestManager来管理

    def execute(self):
        if not self._bProblem:
            print("Executing the test")
            time.sleep(1)
        else:
            print("Problem in setup. Test not executed.")

    def tearDown(self):
        if not self._bProblem:
            print("Tearing down")
            time.sleep(1)
            self._tm.publishReport()
        else:
            print("Test not executed.No tear down require")

    def setTM(self,tm):
        self._tm=tm

    def setProblem(self,value):
        self._bProblem=value

class Reporter:
    def __init__(self):
        self._tm=None

    def prepare(self):
        print("Reporter Class is preparing to report the results")
        time.sleep(1)

    def report(self):
        print("Reporting the results of Test")
        time.sleep(1)

    def setTM(self,tm):
        self._tm=tm

class DB:
    def __init__(self):
        self._tm=None

    def insert(self):
        print("Inserting the execution begin status in the Database")
        #Following code is to simulate a commucaition from DB to TC
        import random
        if random.randrange(1,4)==3:
            return -1

    def update(self):
        print("Updating the test results in Database")
        time.sleep(1)

    def setTM(self, tm):
        self._tm=tm

class TestManager:  #属于中介者，其他三个都跟它交互
    def __init__(self):
        self._reporter=None
        self._db =None
        self._tc=None

    def prepareReporting(self):
        rvalue=self._db.insert()
        if rvalue==-1:
            self._tc.setProblem(1)
            self._reporter.prepare()

    def setReporter(self,reporter):
        self._reporter=reporter

    def setDB(self,db):
        self._db=db

    def publishReport(self):
        self._db.update()
        rvalue=self._reporter.report()

    def setTC(self,tc):
        self._tc=tc

if __name__=="__main__":
    reporter=Reporter()
    db=DB()
    tm=TestManager()
    tm.setDB(db)  #db跟tm交互
    tm.setReporter(reporter)
    reporter.setTM(tm)#reporter跟tm交互
    db.setTM(tm)
    #for simplification we are looping on the same test
    #partically , it could be about various unique test classes and their objects
    while(True):
        tc = TC()
        tc.setTM(tm) #tc跟tm交互
        tm.setTC(tc)
        tc.setup()
        tc.execute()
        tc.tearDown()