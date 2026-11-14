import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D3\input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    n = input()
    new_words = []

    for word in n:
        if word not in ("a", "e", "i", "o", "u"):
            new_words.append(word)

    result = "".join(new_words)
    print(f"#{tc} {result}")

# join 함수 사용법 복습
