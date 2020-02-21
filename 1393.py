import math as m

while True:
    fact = 1
    n = int(input())
    if n == 0:
        break
    fact = m.factorial(n)
    result = fact / 2 * (m.factorial(n - 2))
    print(result)