#iterator

def count_to(count):
    """Counts by word numbers, up to a maximum of five"""
    numbers=["one","two","three","four","five"]
    #enumerate() returns a tuple containing a count(from start with)
    #defaults to 0) and the values obtained from iteratinf over sequence
    for pos, number in zip(range(count),numbers):  #numbers的数目要是比range的个数多，则只显示range的个数那么多
        #如果range的个数比numbers多，则最多显示numbers个嘛
        yield number  #生成器

#Test the generator
count_to_two=lambda :count_to(2)
count_to_five = lambda :count_to(5)

print("Counting to two...")
for number in count_to_two():
    print(number)

print("")

print("Counting to five...")
for number in count_to_five():
    print(number)

print("")