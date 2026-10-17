n1 = input()
n2 = input()

n1_rsp = input()
n2_rsp = input()


def RSP(n, m):
    if n == m:
        print("비겼습니다!")
    # 가위 바위
    elif (n == "가위" and m == "바위") or (m == "가위" and n == "바위"):
        print("바위가 이겼습니다!")
    # 바위 보
    elif (n == "바위" and m == "보") or (m == "바위" and n == "보"):
        print("보가 이겼습니다!")
    # 보 가위
    elif (n == "보" and m == "가위") or (m == "보" and n == "가위"):
        print("가위가 이겼습니다!")


RSP(n1_rsp, n2_rsp)
