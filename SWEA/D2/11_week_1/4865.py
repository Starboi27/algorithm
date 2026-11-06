import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    str1 = input()
    str2 = input()
    result = 0

    for i in str1:
        count = 0
        for j in str2:
            if i == j:
                count += 1
        result = max(result, count)

    print(f"#{tc} {result}")

# 최댓값 갱신 패턴사용하기
