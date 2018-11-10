import singleton

def main():
    s1 = singleton.SingleSpam("spam")
    print(id(s1),s1)
    s2=singleton.SingleSpam("spa")
    print(id(s2), s2)
    print(id(s1),s1)

if __name__=="__main__":
    print("obj in the module singleton:")
    singleton.main()
    print("\nobject in the main :")
    main()