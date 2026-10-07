def palindrome(char):
    print(char)
    if char == char[::-1]:
        print("입력하신 단어는 회문(Palindrome)입니다.")
    else:
        print("입력하신 단어는 회문(Palindrome)이 아닙니다")


char = input()
palindrome(char)

# 처음 문제를 이해를 못 했음
