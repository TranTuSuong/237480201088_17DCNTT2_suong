n = int(input("Nhập số nguyên dương n: "))

tong_le = sum(i for i in range(1, n, 2))
tong_chan = sum(i for i in range(2, n, 2))

print("Tổng các số lẻ nhỏ hơn n là:", tong_le)
print("Tổng các số chẵn nhỏ hơn n là:", tong_chan)