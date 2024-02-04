numbers_list = []

while True:
    user_input = input("Введите цену: ")
    if user_input == '':
        break
    try:
        price = float(user_input)
    except TypeError as te:
        print("Цена не может быть не числовым значением")
        exit(1)
    numbers_list.append(price)

print("Сумма введенных цен: ", sum(numbers_list))
print("Сумма введенных цен наличными: ", round(sum(numbers_list) / 5) * 5)
