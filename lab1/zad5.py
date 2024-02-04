def joen(inp: list[str]):
    if len(inp) < 2:
        return ''.join(inp)
    for i in range(0, len(inp) - 2):
        inp[i] += ', '
    inp[len(inp)-2] += ' и '

    return ''.join(inp)

input_list = []

while True:
    user_input = input("Введите название элемента списка: ")
    if user_input == '':
        break
    input_list.append(user_input)

print("Результат: ", joen(input_list))