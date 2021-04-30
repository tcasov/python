profit = int(input('Введите прибыль компании: '))
cost = int(input('А теперь введите издержки: '))
if profit < cost:
    print('Вы работаете в убыток.')
elif profit == cost:
    print('Прибыли нет, но нет и убытков.')
else:
    print('Рентабельность компании ', int(profit / cost) * 100, '%')
    personal = int(input('Сколько у вас персонала? '))
    print('Каждый работник приносит вам доход в размере', "%0.2f" % ((profit - cost) / personal))
