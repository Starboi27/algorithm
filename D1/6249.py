t = input()

num_list = "0123456789"
result_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


for i in t:
    if i in num_list:
        result_list[int(i)] += 1

print(" ".join(num_list))
print(*result_list)

# 복습 내용
# 1. join 함수 사용법
# 2. 문자열도 [n]으로 출력 가능
# 3. 리스트를 *리스트로 출력하면 대괄호와 쉼표 없이, 각 값을 공백으로 구분해서 출력
# 4. for i in 문자열 로 써야 하나씩 꺼낼 수 있다
# 5. insert 함수는 값을 입력 받을 때 마다 기존 값들을 뒤로 민다
# 6. 변수 += 1 은 해당 인덱스의 값만 변경함 
#     처음엔 result_list[int(i)] += sum 으로 해서 증가값을 공유 했음