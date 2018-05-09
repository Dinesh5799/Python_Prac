n = int(input())

def isFloat(num):
    d = num.find('.')
    print('num = ',num," d = ",d)
    if d == -1:
        return False
    x = num.split('.')
    #print('x = ',x)
    if not len(x) >= 2:
        return False
    return True

while n:
    s = input()
    print(isFloat(s))
    n -= 1
