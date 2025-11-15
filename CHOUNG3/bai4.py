def find_max_value(numbers):
    """Hàm tìm giá trị lớn nhất trong 1 list số nguyên"""
    if len(numbers) == 0:
        return None
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

#chương trình chính
raw_input= input("Nhập các sô nguyên cách nhau bởi khoảng trắng:  ")

numbers = list(map(int, raw_input.split()))

result = find_max_value(numbers)
print("Giá trị lớn nhất:  ", result)