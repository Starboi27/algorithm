import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    # 입력
    # n명이 m개의 문제를 품
    # [[1, 0, 0, 1, 0], [1, 1, 1, 0, 0], [0, 0, 0, 1, 0]]
    # 1번 2문제를 품, 2번 3문제를 품, 3번 2문제를 품
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    solve_cnt = 0
    winner = 0

    for i in range(n):
        cnt = 0
        for j in range(m):
            if arr[i][j] == 1:
                cnt += 1
        if solve_cnt < cnt:
            solve_cnt = cnt
            winner = 1
        # 풀이 수가 최대가 될 때 최대값 갱신하고 우승자를 1로 초기화

        elif solve_cnt == cnt:
            winner += 1
        # 풀이 수랑 최대값이 같을 때 우승자 추가

    # 출력
    # 1등의 수, 1등이 푼 문제의 수
    print(f"#{tc} {winner} {solve_cnt}")
