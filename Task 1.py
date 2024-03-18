#cДан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

def find_duplicates(listik):
    return list(set([x for x in listik if listik.count(x) > 1]))

listik = [5, 65, 5, 65, 8, 3, 8, 5, 65, 3]
print(find_duplicates(listik))