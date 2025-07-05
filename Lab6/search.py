import random
array_size = 100 # Размер массива
random_array = [random.randint(0, 1000000) for i in range(array_size)] # Создание массива случайных чисел 
for i in range(array_size):
        max_ind = i # Находим индекс максимального элемента в неотсортированной части
        for j in range(i + 1, array_size):
            if random_array[j] > random_array[max_ind]:
                max_ind = j
        random_array[i], random_array[max_ind] = random_array[max_ind], random_array[i]
for i in range(array_size):
     if random_array[i] == random_array[i - 1]:
        random_array[i - 1].remove()
print(f"Отсортированный массив случайных чисел без повторений: {random_array}")

target = int(input("Введите искомое значение: ")) # Ввод цели для поиска

print("\nЛинейный поиск:")
linear_index = -1
linear_comparisons = 0
for i in range(array_size):
    linear_comparisons += 1
    if random_array[i] == target:
        linear_index = i
        break

if linear_index != -1:
    print(f"Элемент найден на позиции {linear_index}, Количество сравнений: {linear_comparisons}")
else:
    print(f"Элемент не найден. Количество сравнений: {linear_comparisons}")

print("\nБинарный поиск:")
binary_index = -1
binary_comparisons = 0
left = 0
right = array_size - 1

while left <= right:
    mid = (left + right) // 2
    binary_comparisons += 1
    
    if random_array[mid] == target:
        binary_index = mid
        break
    elif random_array[mid] > target:
        left = mid + 1
    else:
        right = mid - 1

if binary_index != -1:
    print(f"Элемент найден на позиции {binary_index}, Количество сравнений: {binary_comparisons}")
else:
    print(f"Элемент не найден. Количество сравнений: {binary_comparisons}")