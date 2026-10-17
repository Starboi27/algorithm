Data = list(range(1, 11))

result = list(filter(lambda x: x % 2 == 0, Data))
# filter는 왼쪽 조건에 맞는 원소만 추출하는 함수

print(result)
