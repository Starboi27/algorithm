import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\9_week_3\sample_input.txt", "r")

Data = {"A": 1010, "B": 1011, "C": 1100, "D": 1101, "E": 1110, "F": 1111}

t = int(input())

for tc in range(1, t + 1):
    a, b = input().split()
    solve = []

    for i in b:
        if i.isdigit() == False:
            solve.append(str(Data[i]))
        else:
            binary = ""
            num = int(i)
            for _ in range(4):
                binary = str(num % 2) + binary  # 뒤부터 추가하기 위해서 +=안 씀
                num //= 2
            solve.append(binary)

    print(f"#{tc} {''.join(solve)}")
    # join을 쓰려면 변수안 값이 전부 str형태여야 된다, 쌍 따옴표 쓰면 안 됨 뭔 씨발 바라는 게 많아
