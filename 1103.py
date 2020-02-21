import time
from datetime import datetime

while True:
    h1, m1, h2, m2 = input().split(" ")

    if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
        break

    t1 = datetime.strptime(h1+':'+m1, "%H:%M")
    t2 = datetime.strptime(h2+':'+m2, "%H:%M")

    d = t1 - t2
    print((d.seconds) / 60)  