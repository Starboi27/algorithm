# 선택정렬
# 최대 값 구하는 초기값은 인덱스 0번으로 설정하기
# 리스트에 가장 작은 값을 찾고 앞 인덱스로 이동
# 정렬된 배열은 건들지 않기

list = [3, 2, 5, 4, 1]

for i in range(len(list)):  # i = 3
    print(list)

    min = list[i]  # min = 4
    wheremin = i  # wheremin = 3
    for j in range(i + 1, len(list)):  # j = 4
        if min > list[j]:  # 4 > 3
            min = list[j]  # min = 4
            wheremin = j  # wheremin = 4
            print(min, wheremin)
    list[i], list[wheremin] = list[wheremin], list[i]
    # list[2], list[3] = 4, 5

    # list = [1, 2, 4, 5, 3]
