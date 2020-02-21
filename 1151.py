lim = int(input())
init = [0,1]
for i in range(lim-2):
    init.append(init[i] + init[i+1])
print(*init, sep=' ')