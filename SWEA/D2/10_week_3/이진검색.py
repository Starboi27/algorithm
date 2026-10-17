# 이진검색 : 데이터의 중앙 값을 찾는 값과 비교하여 다음 검색 위치를 다시 중앙값으로 찾는다
# 단 데이터가 정렬이 된 상태여야 가능하다

list = [1, 3, 5, 6, 9]

key = 1
start = 0
end = len(list) - 1
success = 0

while start <= end and success == 0:
    middle = (start + end) // 2

    if list[middle] > key:
        end = middle - 1
    elif list[middle] < key:
        start = middle + 1
    else:
        success = 1
        index = middle

if success == 0:
    print("데이터를 찾지 못 했습니다")
else:
    print(f"{index}자리에 {key}가 있습니다")
