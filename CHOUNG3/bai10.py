#Hàm số chẵn
def is_even(n):
    return n % 2 == 0
#Hàm số hoàn hảo
def is_perfect(n):
    if n<=0:
        return False
    total = 0
    for i in range(1,n):
        if n % i == 0:
            total += i
    return total == n
#hàm số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
#Hàm số chính phương
def is_square_numbers(n):
    if n<2:
        return False
    root = int(n**0.5)
    return root*root == n

#Chương trình chính
num = int(input("Nhập một số nguyên:  "))
print("Số chẵn:  ",is_even(num))
print("Số hoa hảo:  ",is_perfect(num))
print("Số nguyên tố:  ",is_prime(num))
print("Số chính phương:  ",is_square_numbers(num))
