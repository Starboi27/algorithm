def countdown(t):  # t=0
    if t <= 0:
        print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")
        return
    else:
        for i in range(10):
            print(10 - i)


countdown(0)
countdown(10)
