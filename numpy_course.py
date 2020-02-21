import numpy as np

l = [1,2,3]
a = np.array([1,2,3])

l.append(4)
l = l + [5]
l2 = []

for i in l:
    l2.append(i + i)

print(a**2)