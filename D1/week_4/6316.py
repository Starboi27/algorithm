arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = map(lambda y: y**2, filter(lambda x: x % 2 == 0, arr))

print(list(result))

# 람다랑 filter 함수 사용법을 몰랐음
