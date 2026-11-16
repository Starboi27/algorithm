import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    # 입력
    # p: a사의 요금, q: b사의 요금, r: 월간 사용량, s: 추가 요금, w: 사용한 수도량
    p, q, r, s, w = map(int, input().split())

    a_company = p * w
    b_company = q

    if w > r:
        b_company = q + (w - r) * s

    result = min(a_company, b_company)

    print(f"#{tc} {result}")
