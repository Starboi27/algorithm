DataA = [4, 29, 18, 13, 19, 25, 9, 6, 10, 24]
DataB = [18, 6, 23, 10, 27, 16, 11, 29, 13, 28, 9, 3, 15, 22, 19]

temp = []

for tc in DataA:
    if tc in DataB and tc not in temp:
        temp.append(tc)

temp.sort()
print(DataA)
print(DataB)
print(temp)
