'''babu=[9,3,6,2,5,0,8,2,4,7]
dudu=[6,4,6,1,2,2]
result=[6,2),(4,8)]'''

babu = [9, 3, 6, 2, 5, 0, 8, 2, 4, 7]
dudu = [6, 4, 6, 1, 2, 2]

result = []
bubu_index=set()
for num in dudu:
    index = [i for i, x in enumerate(babu) if x == num]
    for i in index:
        if i not in bubu_index:
            result.append((num, i))
            bubu_index.add(i)
print(result)


