salary = 20000
spend = 24000
months = 10
increase = 0.03
grow = increase + 1
need_money = 0
delta = salary - spend
for money in range(1, months + 1):
    money = spend - salary
    spend = spend * grow
    need_money += money
    int(need_money)




print(int(need_money))

