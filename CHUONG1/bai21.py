n = int(input('nhap n: '))

if n < 2:
    print(' khong phai so nguyen to')
else:
    for i in range(2, n):
        if n % i == 0:
            print('khong phai so nguyen to')
            break
    else:
        print('day la so nguyen to')