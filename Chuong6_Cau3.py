#Câu 3: Xử lý List Đa chiều
'''
Yêu cầu:
Viết chương trình cho phép:
- Khởi tạo và nhập vào ma trận MxN phần tử ngẫu nhiên
- Xuất dòng bất kỳ nhập từ bàn phím
Trang 52/84
- Xuất cột bất kỳ từ bàn phím
- Xuất số MAX trong ma trận
'''
import random

def tao_ma_tran(m, n):
    #Tạo ma trận m dòng, n cột với phần tử ngẫu nhiên từ 0-99
    return [[random.randint(0, 99) for _ in range(n)] for _ in range(m)]

def xuat_ma_tran(matrix):
    #In ma trận dạng đẹp
    for row in matrix:
        print(row)

def main():
    print("=== CHƯƠNG TRÌNH XỬ LÝ MA TRẬN ===")
    
    #  Nhập kích thước ma trận
    m = int(input("Nhập số dòng (M): "))
    n = int(input("Nhập số cột (N): "))

    #  Khởi tạo ma trận ngẫu nhiên
    matrix = tao_ma_tran(m, n)
    print("\nMa trận vừa tạo là:")
    xuat_ma_tran(matrix)

    #  Xuất dòng bất kỳ
    dong = int(input(f"\nNhập chỉ số dòng muốn xem (0 - {m-1}): "))
    if 0 <= dong < m:
        print("Dòng", dong, "là:", matrix[dong])
    else:
        print("Dòng không hợp lệ!")

    #  Xuất cột bất kỳ
    cot = int(input(f"\nNhập chỉ số cột muốn xem (0 - {n-1}): "))
    if 0 <= cot < n:
        cot_duoc_chon = [matrix[i][cot] for i in range(m)]
        print("Cột", cot, "là:", cot_duoc_chon)
    else:
        print("Cột không hợp lệ!")

    # Tìm số lớn nhất trong ma trận
    max_value = max(max(row) for row in matrix)
    print("\nSố lớn nhất trong ma trận là:", max_value)

# Gọi hàm main
main()
