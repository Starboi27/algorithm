numbers = list(range(1, 11))

result = map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))
print(list(result))

# map : 원소를 원하는 값으로 변환
# filter : 조건이 참인 원소만 선택