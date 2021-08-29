i = 1

while i < 10:
    j = 1
    while j < 10:
        print(i, j, i * j)
        if j == 5:
            break
        j = j + 1
    i = i + 1
