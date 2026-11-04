import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\10_week_5\input.txt", "r")


def 승부(left, right):
    if candidate == 1:
        return

    if candidate[left] == candidate[right]:
        return min(left, right)

    if candidate[left] == 1 and candidate[right] == 3:
        return left
    elif candidate[left] == 2 and candidate[right] == 1:
        return left
    elif candidate[left] == 3 and candidate[right] == 2:
        return left
    else:
        return right


def 토너먼트(left, right):
    if left == right:  # left랑 right의 값이 같을 때 값 리턴
        return left

    mid = (left + right) // 2

    left_candidate = 토너먼트(left, mid)
    right_candidate = 토너먼트(mid + 1, right)

    return 승부(left_candidate, right_candidate)


t = int(input())
# 1: 가위
# 2: 바위
# 3: 보

for tc in range(1, t + 1):
    N = int(input())
    candidate = list(map(int, input().split()))

    result = 토너먼트(0, N - 1)
    print(result)
