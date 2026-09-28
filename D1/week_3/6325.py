arr = [2, 4, 6, 8, 10]


def array(num):
    if num in arr:
        return print(f"{num} => True")
    print(f"{num} => False")


print(arr)
array(5)
array(10)
