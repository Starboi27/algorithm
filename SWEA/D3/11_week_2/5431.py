import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    # n: 수강생 수, m: 제출한 수
    arr = list(map(int, input().split()))
    # 제출한 학생 들
    students = [i for i in range(1, n + 1)]
    # 전체 학생 수

    result = []

    for i in students:
        if i not in arr:
            result.append(i)

    print(f"#{tc}", *result)
