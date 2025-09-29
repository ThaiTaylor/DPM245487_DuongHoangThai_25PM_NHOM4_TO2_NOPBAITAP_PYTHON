#Câu 8: Nhập vào 2 giá trị a, b và phép toán ‘+’, ‘-’, ‘*’, ‘/’ . Hãy xuất kết quả theo đúng phép toán đã nhập.

# Nhập dữ liệu
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))

# Nhập phép toán, kiểm tra hợp lệ
phep_tinh = input("Nhập phép toán (+, -, *, /): ")
while phep_tinh not in ["+", "-", "*", "/"]:
    print("Phép toán không hợp lệ! Vui lòng nhập lại.")
    phep_tinh = input("Nhập phép toán (+, -, *, /): ")

# Xử lý
if phep_tinh == "+":
    kq = a + b
elif phep_tinh == "-":
    kq = a - b
elif phep_tinh == "*":
    kq = a * b
elif phep_tinh == "/":
    if b != 0:
        kq = a / b
    else:
        kq = "Lỗi! Không thể chia cho 0."

# Xuất kết quả
print("Kết quả:", kq)

