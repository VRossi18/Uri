while True:
    try:
        sentence = input().lower()
        dance = []
        flag = True
        for i in range(0,len(sentence)):
            if flag and sentence[i] != ' ':
                dance.append(sentence[i].upper())
                flag = False
            elif sentence[i] != ' ':
                dance.append(sentence[i])
                flag = True
            else:
                dance.append(sentence[i])
        print(*dance,sep='')
    except EOFError:
        break