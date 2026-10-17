# 피보나치 수열 앞 2자리를 더한 값이 뒤에 오는 수열

n = int(input())

fibo_list = [0, 1]

sum_operator = 0

for i in range(0, n - 1):
    sum_operator = fibo_list[i] + fibo_list[i + 1]
    fibo_list.append(sum_operator)

print(fibo_list[1 : n + 1])
