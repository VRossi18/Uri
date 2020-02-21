while (True):
    txt = input()
    if (txt == '*'):
        break
    txt = txt.split(" ")
    init = ''
    tautograma = True

    for i in txt:
        f_char = i[0].upper()
        if (init == ''):
            init = f_char 
        if (init != f_char):
            tautograma = False
            break

    if (tautograma):
        print("Y")
    else:
        print("N")

    txt = ''