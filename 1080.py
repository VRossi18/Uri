lst = []
maior = 0
ind = 0
while (len(lst) != 100):
    num = int(input())
    lst.append(num)
    if (num > maior):
        maior = num
        ind = lst.index(num)
print(maior, ind+1, sep='\n')