while True:
    try:
        n = input()
    except EOFError:
        break

    if n == "":
        break

    print(">>", n.upper())

# 첫 풀이 때 EOFError 처리가 없었음 떄문에 런타입 에러 발생
# islower()에 ()을 안 쓰고 islower만 씀 검사를 안 함
    
# while 1:
#     result = ""
#     try:
#         n = input()
#     except EOFError:
#         break
#     for i in n:
#         if i.islower():
#             result += i.upper()
#         else:
#             result += i
#     print(f">> {result}")
# 이렇게 굳이 안 쓰고 그냥 마지막 프린트에 n.upprt() 쓰면 됨 
