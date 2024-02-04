try:
    inp = input("Введите ваше количество баллов: ")
    dep = int(inp)
except TypeError as te:
    print("Количество ваших баллов не может быть дробным числом")
    exit(1)

if dep < 0 or dep > 100:
    print("Программа бессильна")
elif dep < 52:
    print("2")
elif dep < 70:
    print("3")
elif dep < 85:
    print("4")
else:
    print("5")