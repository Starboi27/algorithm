t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())

    list_n = [i for i in range(1, n + 1)]
    list_m = [i for i in range(1, m + 1)]

    cnt_list = [0] * (n + m + 1)

    result = []

    for val_n in list_n:
        for val_m in list_m:
            cnt = val_n + val_m
            cnt_list[cnt] += 1

    max_cnt = max(cnt_list)
    for i in range(len(cnt_list)):
        if cnt_list[i] == max_cnt:
            result.append(i)

    print(f"#{tc}", *result)

# 복습
