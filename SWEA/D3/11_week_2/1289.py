t = int(input())

for tc in range(1, t + 1):
    goal = list(map(int, input().strip()))
    current = 0
    cnt = 0

    for i in range(len(goal)):
        if goal[i] != current:
            cnt += 1
            current = goal[i]

    print(f"#{tc} {cnt}")

# 복습 필요 또또
