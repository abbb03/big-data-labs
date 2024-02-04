try:
    inp = input("Введите расстояние в км: ")
    dist = float(inp)
except TypeError as te:
    print("Расстояние должно быть числом")
    exit(1)

print(380 + dist * 500)