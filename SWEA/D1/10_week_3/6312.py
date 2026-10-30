def solve(*number):
    mul = 1
    for tc in number:
        if type(tc) == str:
            print("에러발생")
            return
        else:
            mul *= tc

    print(mul)


solve(1, 2, "4", 3)
