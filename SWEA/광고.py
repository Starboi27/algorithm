t = int(input())

for tc in range(1, t + 1):
    N, P, B = map(int, input().split())
    # 3, 6, 2
    
    A = list(map(int, input().split()))

    new_A = []
    for ta in A:
        if ta > 3:
            new_A.append(6)
        