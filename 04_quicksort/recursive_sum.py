def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

print(sum([10,20,30,40,50]))
