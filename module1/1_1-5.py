# Ввод строки
input_string = input().strip()

# Инициализируем счетчик обратных пар, начинающихся с 'a'
count = 0

# Пройдемся по строке справа налево
for i in range(len(input_string) - 1):
    if input_string[i] == 'a':
        count += input_string[i+1:].count('a')

# Выводим результат
print(count)
