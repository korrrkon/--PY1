money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

#month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
month = 1
money_capital_new = 9000 #для первого месяца
while money_capital >= spend:
    new_spend = spend + spend*increase
    money_capital_new = money_capital_new + salary - new_spend
    spend = new_spend
    money_capital = money_capital_new
    month = month + 1
    #print(money_capital)
print(month)









