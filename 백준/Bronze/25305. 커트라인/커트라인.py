n, num_win = map(int, input().split())
list = []
list = input().split()

for i in range(0, len(list)):
    list[i] = int(list[i])

for j in range(len(list), 0, -1):
    for k in range(0, j-1):
        if list[k] > list[k+1]:
            temp = list[k]
            list[k] = list[k+1]
            list[k+1] = temp

print(list[n - num_win])