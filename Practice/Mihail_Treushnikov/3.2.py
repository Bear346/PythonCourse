a = 10894

def number (a):
    string = str(a)
    for i,e in enumerate(string,1):
        print("{} цифра равна {}".format(i,e))

number(a)
