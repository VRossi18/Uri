x,y = map(int , input().split(' '))
lst = []
[lst.append(i) for i in range(1,y+1)]
for i in range(0,len(lst), x):
    print(*lst[i:i+x])