while True:
    n = int(input())
    if n == 0:
        break
    div_x, div_y = map(int, input().split(" "))
    for i in range(n):
        x, y = map(int,input().split(" "))
        
        if x == div_x or y == div_y:
            print("divisa")

        elif x > div_x and y > div_y:
            print("NE")

        elif x > div_x and y < div_y:
            print("SE")

        elif x < div_x and y > div_y:
            print("NO")

        elif x < div_x and y < div_y:
            print("SO")