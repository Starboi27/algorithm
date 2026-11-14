import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\input.txt", "r")


def b_fare():
    global extra_pay
    if w > r:
        extra_pay = s * (w - r)

    return extra_pay


t = int(input())

# 9: a사의 요금 방식
# 100, 20, 3: 기본 요금, 월간 사용량, extra fare
# 10: 한 달간 사용한 수도 양

for tc in range(1, t + 1):
    p, q, r, s, w = map(int, input().split())
    extra_pay = 0

    a = p * w  # 90
    b = b_fare() + q

    result = min(a, b)

    print(f"#{tc} {result}")

# 복습
