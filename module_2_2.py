first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')
if first == second and second == third: #if first == second == third: - другой вариант
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)

#Второе решение
print('')
print('Второе решение')
if not first != second and not second != third:
    print(3)
elif not first != second or not first != third or not second != third:
    print(2)
else:
    print(0)
    