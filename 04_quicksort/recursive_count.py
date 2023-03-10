def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])

print(count([10,20,30,40,50]))
