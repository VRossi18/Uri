import math

while True:
    try:
        r1,x1,y1,r2,x2,y2 = map(int, input().split(' '))
        d = math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))
        if r1 - d >= r2:
            print('RICO')
        else:
            print('MORTO')
    except EOFError:
        break