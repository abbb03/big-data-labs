def f(dict, val):
    res = []
    for k, v in dict.items():
        if v == val:
            res.append(k)
    
    return res

odno_znach = {'jack': 40928, 'sape': 4139, 'jackk': 42098}
nes_znach = {'jack': 4139, 'sape': 4139, 'jackk': 42098}
net_kluchey = {'jack': 41329, 'sape': 412139, 'jackk': 420398}

print("Одно значение: ", f(odno_znach, 4139))
print("Несколько значений: ", f(nes_znach, 4139))
print("Нет соответствующих ключей: ", f(net_kluchey, 4139))
