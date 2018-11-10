#Factory method

class ChinaGetter:
    """A simple localizer a la gettext"""
    def __init__(self):
        self.trans = dict(dog=u"小狗", cat=u"小猫")

    def get(self,msgid):
        """we'll punt if we don't have a translation"""
        try:
            return self.trans[msgid]
        except KeyError: #KeyError字典里面没有这个键值就出报错
            return str(msgid)

class EnglishGetter:
    """Simply echoes the msg ids"""
    def get(self, msgid):
        return str(msgid)

def get_localizer(language="English"):
    """The factory method"""
    languages=dict(English=EnglishGetter, China=ChinaGetter)
    return languages[language]() #根据输入的类型，返回一个类

def test_ChinaGetter():
    c=ChinaGetter()
    print(c.get("dog"))
    print(c.get("tiger"))

def test_EnglishGetter():
    e=EnglishGetter()
    print(e.get("monkey"))

def test_factory_method():
    e,c=get_localizer("English"),get_localizer("China")
    #localize some text
    for msgid in "dog parrot cat bear".split(): #"dog parrot cat bear".split()生成一个列表
        print(e.get(msgid), c.get(msgid))

if __name__=="__main__":
    #test_ChinaGetter()
    #test_EnglishGetter()
    test_factory_method()