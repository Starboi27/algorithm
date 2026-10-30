char = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"

solve = map(lambda x: 4 if x == "A" else 3 if x == "B" else 2 if x == "C" else 1, char)
# map은 값을 하나씩 꺼낼 수 있는 이터레이터
# 이터레이터: 값을 하나씩 꺼낼 수 있고, 어디까지 꺼냈는지 기억하는 객체
print(sum(solve))
