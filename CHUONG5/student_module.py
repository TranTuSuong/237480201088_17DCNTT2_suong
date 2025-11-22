# student_module.py
students = []   # Danh sách lưu các sinh viên (list rỗng ban đầu)

# -----------------------------
# Thêm sinh viên
# -----------------------------
def add_student(student_id, name):
    # Kiểm tra trùng ID
    for s in students:
        if s["id"] == student_id:
            return False
    students.append({"id": student_id, "name": name})
    return True

# -----------------------------
# Xóa sinh viên
# -----------------------------
def delete_student(student_id):
    for s in students:
        if s["id"] == student_id:
            students.remove(s)
            return True
    return False

# -----------------------------
# Sửa sinh viên
# -----------------------------
def update_student(student_id, new_name):
    for s in students:
        if s["id"] == student_id:
            s["name"] = new_name
            return True
    return False

# -----------------------------
# Xem danh sách sinh viên
# -----------------------------
def list_students():
    return students

# main.py
import student_module as sm

def menu():
    print("\n====== CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN ======")
    print("1. Thêm sinh viên")
    print("2. Xóa sinh viên")
    print("3. Sửa sinh viên")
    print("4. Xem danh sách sinh viên")
    print("0. Thoát")
    print("============================================")

while True:
    menu()
    choice = input("Chọn chức năng: ")

    # 1. Thêm
    if choice == "1":
        sid = input("Nhập mã sinh viên: ")
        name = input("Nhập tên sinh viên: ")
        if sm.add_student(sid, name):
            print(">>> Thêm thành công.")
        else:
            print(">>> Mã sinh viên đã tồn tại!")

    # 2. Xóa
    elif choice == "2":
        sid = input("Nhập mã sinh viên cần xóa: ")
        if sm.delete_student(sid):
            print(">>> Xóa thành công.")
        else:
            print(">>> Không tìm thấy mã sinh viên!")

    # 3. Sửa
    elif choice == "3":
        sid = input("Nhập mã sinh viên cần sửa: ")
        new_name = input("Nhập tên mới: ")
        if sm.update_student(sid, new_name):
            print(">>> Sửa thành công.")
        else:
            print(">>> Không tìm thấy sinh viên!")

    # 4. Xem danh sách
    elif choice == "4":
        ds = sm.list_students()
        if not ds:
            print(">>> Danh sách rỗng.")
        else:
            print("\n--- DANH SÁCH SINH VIÊN ---")
            print("{:<10} | {}".format("Mã SV", "Tên sinh viên"))
            print("-----------------------------")
            for s in ds:
                print("{:<10} | {}".format(s['id'], s['name']))

    # 0. Thoát
    elif choice == "0":
        print(">>> Thoát chương trình.")
        break

    else:
        print(">>> Lựa chọn không hợp lệ!")