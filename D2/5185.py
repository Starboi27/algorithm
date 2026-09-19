T = int(input())

converter = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

for i in range(1, T + 1):
    result = ""
    # numbers = 1A
    n, numbers = input().split()

    for number in numbers[::-1]:
        if number in converter:
            number = converter[number]

        m = int(number)
        count = 0

        while count < 4:
            remainder = m % 2
            quort = m // 2
            result = str(remainder) + result
            m = quort
            count += 1

    print(f"#{i} {result}")

#   - case.isdigit처럼 괄호 없이 쓴 것
#     → 함수 자체를 확인하는 것이므로 case.isdigit()이어야 함.

#   - "13"을 "1", "3"으로 나눠서 일반 10진수 변환하려 한 것
#     → 일반 정수 13 변환이라면 틀림.
#     → 하지만 이번처럼 16진수 문자열 변환은 한 글자씩 처리하는 게 맞음.

#   - while m > 0 사용
#     → 1은 1만 나오고 0001이 안 됨.
#     → 16진수 한 글자는 무조건 4비트이므로 while count < 4로 4번 반복.

#   - result += str(remainder) 사용
#     → 나머지는 뒤에서부터 나오므로 비트 순서가 거꾸로 됨.

#   - 마지막에 result[::-1] 사용
#     → 전체를 뒤집으면 1A의 글자 순서까지 바뀜.

#   현재 네가 쓰려는 방식의 올바른 조합은 이것 하나예요.

#   for number in numbers[::-1]:       # 16진수는 뒤에서부터 읽기
#       ...
#       result = str(remainder) + result  # 비트는 result 앞에 붙이기

#   print(f"#{i} {result}")            # 마지막에는 뒤집지 않기

#   실수가 아니었던 부분도 있어요.

#   - if number in converter: 뒤에 else를 안 쓴 것: 문제 없음
#   - m = int(number)을 if 아래에 둔 것: 문제 없음
#   - A → 10, B → 11 딕셔너리로 만든 것: 맞음
#   - =+ 대신 +=를 써야 한다는 점: 맞음 (=+는 다른 문법)
