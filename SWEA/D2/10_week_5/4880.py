import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\10_week_5\input.txt", "r")


def winner(left, right):
    left_card = card_list[left][0]
    right_card = card_list[right][0]

    if left_card == right_card:
        return min(left, right)

    if left_card == 1 and right_card == 3:
        return left

    if left_card == 2 and right_card == 1:  # 바위 vs 가위
        return left

    if left_card == 3 and right_card == 2:  # 보 vs 바위
        return left

    return right


def tournament(start, end):
    if start == end:
        return start

    mid = (start + end) // 2

    left = tournament(start, mid)
    right = tournament(mid + 1, end)

    return winner(left, right)


t = int(input())

for tc in range(1, t + 1):
    N = int(input())
    card_list = [[] for _ in range(N + 1)]
    card = list(map(int, input().split()))
    for i in range(N):
        card_list[i + 1].append(card[i])

    result = tournament(1, N)

    print(f"#{tc} {result}")
