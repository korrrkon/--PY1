salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение

sum = 0
months = 10
for i in range(months):
    new_spend = spend + spend * increase
    need_money = new_spend - salary
    spend = new_spend
    sum = sum + need_money
print(round(sum))

