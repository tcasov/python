x = int(input('Введите количество секунд: '))
h = x // 3600
m = (x - h * 3600) // 60
s = x - h * 3600 - m * 60
print('Итого получилось: ', "%02d" % h, ':', "%02d" % m, ':', "%02d" % s, sep="")
