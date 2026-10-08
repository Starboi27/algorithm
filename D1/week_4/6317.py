def function(num):
    max = num[0]

    for i in num:
        if max < i:
            max = i

    return print(f"max{num} => {max}")


tuple = (3, 5, 4, 1, 8, 10, 2)
function(tuple)
