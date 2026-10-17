t = int(input())

case = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

for i in range(1, t + 1):
    result = []

    a, b = input().split()
    for j in b:
        if j in case:
            result.append(int(case[j]))
        else:
            result.append(int(j))
        binary = ""

        for k in result[::-1]:
            for _ in range(4):
                remainer = k % 2
                quotient = k // 2
                k = quotient
                binary = str(remainer) + binary

    print(f"#{i} {binary}")

    # binary = str(remainer) + binary 앞에서 부터 추가 됨
    # 4 3 2 1 이런 식으로? 그래서 for에서 뽑을 때 뒤에서 부터 가져와야 됨
    # 그래서 result[::-1]로 했음
