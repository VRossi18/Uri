num1 = int(input())
num2 = int(input())
lst = []

if (num1 < num2):
    for i in range(num1 + 1,num2):
        if (i % 2 == 1):
            lst.append(i)
else:
    for i in range(num2 + 1,num1):
        if (i % 2 == 1):
            lst.append(i)

print(sum(lst))