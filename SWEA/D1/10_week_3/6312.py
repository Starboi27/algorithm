# 가변형 인자 : 함수에 전달하는 인자의 개수가 달라져도 받을 수 있게 하는 방식


def mul(*t):
    mul = 1

    for i in t:
        if type(i) is not int:
            return print("에러발생")

    for i in t:
        mul *= i
    return print(mul)


mul("1", 2, 3)
