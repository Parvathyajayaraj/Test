s1 = ''
s2 = ''

if len(s1) == len(s2):
    c = 0

    for i, j in zip(s1, s2):
        if i == j:
            print(i)
            c += 1

    print(c)

else:
    print('Invalid input')
