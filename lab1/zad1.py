try:
    inp = input("Введите размер своего депозита: ")
    dep = float(inp)
except TypeError as te:
    print("Укажите размер депозита числом")
    exit(1)

for i in range(1, 6):
    dep += dep * 0.08
    match i:
        case 1:
            print(f"Размер вашего депозита на конец {i} года: {dep}")
        case 2:
            print(f"Размер вашего депозита на конец {i} года: {dep}")
        case 5:
            print(f"Размер вашего депозита на конец {i} года: {dep}")
