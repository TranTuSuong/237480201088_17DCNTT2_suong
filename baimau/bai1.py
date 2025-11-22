# Bài 1: Quản lý sinh viên (Python OOP)

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def __str__(self):
        return f"{self.student_id:10} | {self.name}"


class StudentManager:
    def __init__(self):
        self.students = []     # danh sách sinh viên rỗng ban đầu

    def add_student(self, student_id, name):
        # kiểm tra trùng ID
        for s in self.students:
            if s.student_id == student_id:
                print("❌ ID sinh viên đã tồn tại!")
                return
        self.students.append(Student(student_id, name))
        print("✅ Thêm sinh viên thành công.")

    def delete_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                self.students.remove(s)
                print("✅ Xóa thành công.")
                return
        print("❌ Không tìm thấy sinh viên.")

    def update_student(self, student_id, new_name):
        for s in self.students:
            if s.student_id == student_id:
                s.name = new_name
                print("✅ Sửa thành công.")
                return
        print("❌ Không tìm thấy sinh viên.")

    def search_student(self, keyword):
        keyword = keyword.lower()
        found = [s for s in self.students if keyword in s.student_id.lower() or keyword in s.name.lower()]
        if not found:
            print("❌ Không tìm thấy sinh viên.")
        else:
            print("🔎 Kết quả tìm kiếm:")
            for s in found:
                print(s)

    def show_all(self):
        if not self.students:
            print("📭 Danh sách rỗng.")
            return
        print("📋 DANH SÁCH SINH VIÊN:")
        print("----------------------------")
        for s in self.students:
            print(s)


def menu():
    manager = StudentManager()

    while True:
        print("""
======== MENU =========
1. Thêm sinh viên
2. Xóa sinh viên
3. Sửa sinh viên
4. Tìm kiếm sinh viên
5. Xem danh sách sinh viên
0. Thoát
=======================
""")
        choice = input("👉 Nhập lựa chọn: ")

        if choice == "1":
            sid = input("Nhập ID sinh viên: ")
            name = input("Nhập tên sinh viên: ")
            manager.add_student(sid, name)

        elif choice == "2":
            sid = input("Nhập ID cần xóa: ")
            manager.delete_student(sid)

        elif choice == "3":
            sid = input("Nhập ID cần sửa: ")
            new_name = input("Tên mới: ")
            manager.update_student(sid, new_name)

        elif choice == "4":
            key = input("Nhập tên hoặc ID để tìm: ")
            manager.search_student(key)

        elif choice == "5":
            manager.show_all()

        elif choice == "0":
            print("👋 Thoát chương trình.")
            break

        else:
            print("❌ Lựa chọn không hợp lệ.")


# ---- CHẠY CHƯƠNG TRÌNH ----
menu() 