n = list(range(3, 21))
for x in n:
    result = ''
    for i in range(1, x):
        for j in range(i, x):
            if x % (i + j) == 0 and i != j:
                result += str(i) + str(j)
    print(int(result))
