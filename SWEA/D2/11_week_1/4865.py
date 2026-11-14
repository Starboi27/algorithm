import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    str1 = input()
    str2 = input()
    result = 0

    for str1_val in str1:
        count = 0
        for str2_val in str2:
            if str1_val == str2_val:
                count += 1
                result = max(count, result)

    print(f"#{tc} {result}")
