a = int(input())
mid = a // 2
b = []

for i in range(a):

    b.append([])

    for j in range(a):
        if i == mid or j == mid or i == j or a-i-1 == j:
            b[i].append('*')
        else:
            b[i].append(' ')

print(*b, sep = '\n')
