t = int(input())

for i in range(1, t + 1):
    N = float(input())
    result = ""

    while N > 0:
        N *= 2

        if N >= 1:
            result += "1"
            N -= 1
        else:
            result += "0"
        if len(result) > 12:
            result = "overflow"
            break

    print(f"#{i} {result}")
