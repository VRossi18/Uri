while True:
    n,a,b = map(int, input().split(' '))
    if (n != 0 and a != 0 and b != 0):
        count = [i for i in range(1,n+1) if i % a == 0 or i % b == 0]
        print(len(count))
    else:
        break