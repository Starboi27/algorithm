Data = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

solve = []

for tc in Data:
    if tc not in solve:
        solve.append(tc)

print(solve)
