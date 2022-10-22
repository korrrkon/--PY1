src = not False and True or False and not True

# TODO расписать упрощение выражения
# result = True and True or False and False # избавились от отрицаний
# result = True or False # избавились от логического "И"
# result = True # избавились от логического "ИЛИ"

result = True  # TODO подставить результат выражения

print(src == result)
