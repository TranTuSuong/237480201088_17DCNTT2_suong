h = int(input(' nhap h : 5'))

for i in range(1, h + 1):
    print(' ' * (h - i) + '*' * (2 * i - 1))