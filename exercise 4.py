number = int(input('Введите целое положительное число: '))
max = 0
while number > 0:
    x = number % 10
    number = (number - x) / 10
    if max < x:
        max = x
print('Самая большая цифра в числе это', int(max))
