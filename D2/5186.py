t = int(input())

for i in range(1, t + 1):

    N = float(input())
    ch = ""

    while N > 0:
        N *= 2

        if N >= 1:
            ch += "1"
            N -= 1
        else:
            ch += "0"
        if len(ch) > 12:
            ch = "overflow"
            break

    print(f"#{i} {ch}")
