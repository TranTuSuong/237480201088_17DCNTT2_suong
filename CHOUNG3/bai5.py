def vi_tri_max(L):
    if len(L) == 0:
        return -1 # ds rỗng

    max_value = L[0]
    max_index = 0

    for i in range(1, len(L)):
        if L[i] > max_value:
            max_value = L[i]
            max_index = i
    return max_index

#chương trình
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("Danh sách: ",L)
print("Vị trí phần tử lớn nhất:  ", vi_tri_max(L))
