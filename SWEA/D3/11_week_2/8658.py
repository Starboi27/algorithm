import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    # 입력
    test = list(map(int, input().split()))
    # 10개의 자연수

    max_cal = 0
    min_cal = float("inf")  # or test[0]

    for i in test:
        cal = 0
        for j in str(i):
            cal += int(j)
        max_cal = max(cal, max_cal)
        min_cal = min(cal, min_cal)

    # 출력
    # 각 자리수를 더한 값에서
    # 최대값, 최소값
    print(f"#{tc} {max_cal} {min_cal}")

# 최소값 선언 하는 방법 복습
