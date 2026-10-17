arr = [1, 2, 3, 4, 3, 2, 1]


def function(n):
    new_arr = []

    for i in n:
        if i not in new_arr:
            new_arr.append(i)

    return print(new_arr)


print(arr)
function(arr)
