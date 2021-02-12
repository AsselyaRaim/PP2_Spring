a = list(map(int, input().split()))
x = int(1000)
for i in a:
    if i > 0:
        if i < x:
            x = i
print(x)