with open('text.txt', encoding = 'utf-8', mode = 'r') as f:
    print(max(f.read().split(' '), key=len))