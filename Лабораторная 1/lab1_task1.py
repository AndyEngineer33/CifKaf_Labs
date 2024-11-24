numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

numbers_sum = sum(numbers[:4]) + sum(numbers[5:])  # вычисление суммы чисел списка
numbers_average = numbers_sum / len(numbers)  # вычисление среднего
numbers[4] = round(numbers_average,2) # замена None на среднее, округлённое до сотых

print(f"Измененный список: {numbers}") # вывод списка

