n = int(input())
list = []

for i in range(0, n):
    num = int(input())
    list.append(num)

for j in range(n, 0, -1):
    for k in range(0, j-1):
        if list[k] > list[k+1]:
            temp = list[k]
            list[k] = list[k+1]
            list[k+1] = temp

for l in range(0, n):
    print(list[l])