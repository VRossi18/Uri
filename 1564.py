while True:
    try:
        n = int(input())
        if n >= 1:
            print('vai ter duas!')
        else:
            print('vai ter copa!')
    except EOFError:
        break
