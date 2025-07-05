import random
array_size = 100 # Размер массива
random_array = [random.randint(0, 1000000) for i in range(array_size)] # Создание массива случайных чисел 
print(f"Массив случайных чисел: {random_array}") # Форматный вывод массива
choice = int(input("Выберите способ сортировки элементов массива(0 - Сортировка пузырьком, 1 - Сортировка выбором): "))
if choice == 0:
        for i in range(array_size):
            swapped = False # проверка на наличие перестановок
            for j in range(0, array_size - i - 1):
                if random_array[j] < random_array[j + 1]:
                    random_array[j], random_array[j + 1] = random_array[j + 1], random_array[j]
                    swapped = True
            if not swapped:
                break
elif choice == 1:
    for i in range(array_size):
        max_ind = i # Находим индекс максимального элемента в неотсортированной части
        for j in range(i + 1, array_size):
            if random_array[j] > random_array[max_ind]:
                max_ind = j
        random_array[i], random_array[max_ind] = random_array[max_ind], random_array[i]
else:
    print("Вы неправильно указали пункт выбора, посмотрите на массив ещё раз.")
print(f"Массив отсортированных чисел: {random_array}")