while True:

    try:
        x = input()
        y = input()

    except EOFError:
        break

    if x.isdigit() and y.isdigit():
        print(f"x * y = {int(x) * int(y)}")
    else:
        print("숫자가 아닙니다. 재입력하세요.")

# 걍 출제자가 병신임 풀지마 문제 오류임
