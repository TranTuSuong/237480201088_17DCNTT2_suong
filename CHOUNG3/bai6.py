def vi_tri_min(L):
    """Hàm trả về vị trí của phần tử nhỏ nhất đầu tiên trong danh sách. Nếu danh sách ỗng trả về -1"""
    if len(lst) == 0:
        return -1

    min_value = lst[0]
    min_index = 0

    for i in range(1, len(lst)):
        if lst[i] < min_value:
            min_value = lst[i]
            min_index = i
    return min_index

# Chương trình chính
n =int(input("Nhập số lượng phần tử:   "))
lst = []
print("Nhập các phần tử:  ")
for i in range(n):
    x= int(input(f"Nhập phần tử thứ {i}:  "))
    lst.append(x)

print("Danh sách đã nhập là:  ",lst)
index_min = vi_tri_min(lst)
if index_min == -1:
    print("Ds rỗng, không có giá trị nhỏ nhất!")
else:
    print(f"Vị tri phần tử nhỏ nhất đầu tiên là: {index_min}")