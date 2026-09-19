t = int(input())


for i in range(1, t + 1):
    x, y, target = map(int, input().split())
    count = 0

    while x <= target and y <= target:
        count += 1
        if x < y:
            x += y
        else:
            y += x

    print(count)


# while은 조건이 참일 때 실행하고 거짓일 땐 종료한다

# x += y는 x만 바뀌고 y는 그대로
# y += x는 y만 바뀌고 x는 그대로
# 즉 어떤 수식을 쓰냐에 따라 값이 나오는 속도가 달림