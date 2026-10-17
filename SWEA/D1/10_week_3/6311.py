Data = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"

# lambda의 조건 : 참일_때_값 if 조건 else 거짓일_때_값
result = map(lambda x: 4 if x == "A" else 3 if x == "B" else 2 if x == "C" else 1, Data)

print(sum(result))
