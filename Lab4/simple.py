n = int(input("Введите число для проверки на простоту: "))
prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23} # список простых чисел до 25
if n in prime_numbers: # проверка нахождения n в списке
    print('Y')
else:
    print('N')