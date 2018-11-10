#Template method

ingredients = "spam eggs apple"
line = "-"*10

#skeletons  #这个就相当于最后想生成的模板的skeleton骨架了
def iter_elements(getter, action):
    """Template skeleton that iterates items"""
    for element in getter():
        action(element)
        print(line)

def rev_elements(getter, action):
    """Template skeleton that iterates items in reverse order"""
    for element in getter()[::-1]:
        action(element)
        print(line)

#getters
def get_list():
    return ingredients.split()

def get_lists():
    return [list(x) for x in ingredients.split()]

#action
def print_item(item):
    print(item)

def reverse_item(item):
    print(item[::-1])

#makes templates
def make_template(skeleton, getter, action):
    """Instantiate a template method with getter and action"""
    def template():
        skeleton(getter,action)
    return template

#create our template functions
templates = [make_template(s,g,a)  #总共有2**3组合，每个有len(ingredients)种可能
             for g in (get_list, get_lists) #从()分别取get_list，get_lists
             for a in (print_item, reverse_item)
             for s in (iter_elements, rev_elements)]
for template in templates:
    template()

for g in (get_list, get_lists):
    print(g)