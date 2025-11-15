import math



def giai_phuong_trinh_bac_hai(a, b, c):
    print(f"Phương trình: {a}x² + {b}x + {c} = 0")

    # Trường hợp a = 0: phương trình trở thành bậc nhất hoặc vô nghiệm
    if a == 0:
        if b == 0:
            if c == 0:
                print("Phương trình có vô số nghiệm.")
            else:
                print("Phương trình vô nghiệm.")
        else:
            x = -c / b
            print(f"Phương trình bậc nhất có nghiệm duy nhất: x = {x}")
        return

    # Tính delta
    delta = b**2 - 4*a*c
    print(f"Δ = {delta}")

    # Biện luận theo giá trị của delta
    if delta < 0:
        print("Phương trình vô nghiệm.")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép: x = {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Phương trình có hai nghiệm phân biệt:")
        print(f"x₁ = {x1}")
        print(f"x₂ = {x2}")

# Ví dụ sử dụng
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

giai_phuong_trinh_bac_hai(a, b, c)