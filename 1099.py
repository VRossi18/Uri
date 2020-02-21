n = int(input())
for i in range(n):
    count = []
    x,y = map(int, input().split(' '))
    if x < y:
        count = [v for v in range(x+1,y) if v % 2 != 0]
    else:
        count = [c for c in range(y+1,x) if c % 2 != 0]
    print(sum(count))
