a = list(map(int, input().split()))
for i in range(len(a) // 2):
    a[i], a[len(a) - i - 1] = a[len(a) - i - 1], a[i]
for i in range(len(a)):
    print(a[i], end = " ")
    
