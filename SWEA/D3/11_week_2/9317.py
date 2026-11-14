import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    str_len = int(input())
    str1 = input()
    str2 = input()
    cnt = 0

    for idx in range(str_len):
        if str1[idx] == str2[idx]:
            cnt += 1

    print(f"#{tc} {cnt}")
