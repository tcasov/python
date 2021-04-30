first_day = int(input('Сколько бегун пробежал в первый день? '))
last_day = int(input('Сколько км. надо пробежать? '))
distance = first_day
counter = 1
while distance < last_day:
    distance *= 1.1
    counter += 1
print('Бегуну потребовалось', counter, 'дней(я) чтобы пробежать', "%0.2f" % distance, 'км.')
