money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
mounth = 0 # Переменная для подсчёта месяцев

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

while money_capital + salary >= spend:
    money_capital += salary
    money_capital -= spend
    mounth += 1
    spend *= 1 + increase

print("Количество месяцев, которое можно протянуть без долгов:", mounth)
