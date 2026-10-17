Data = list(range(1, 11))  # list는 반복 가능한 대상의 원소를 꺼내 list로 만든다

result = list(map(lambda x: x**2, (Data)))

print(result)
