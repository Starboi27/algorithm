def countdown(t):

    if t < 1:
        print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")
        return
    for i in range(10):
        print(10 - i)


countdown(0)
countdown(10)

# if문 조건을 만족한 다음 for을 실행하기 때문에 if문 안에 return을 붙여야 한다
