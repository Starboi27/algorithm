t = input()

case = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in t:
    n = int(i)
    if n in case:
        result[n] += 1

print(*case)
print(*result)
