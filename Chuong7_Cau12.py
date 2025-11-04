#Câu 12: Xử lý CSV File - Viết phần mềm Quản Lý Nhân Viên
'''
Yêu cầu:
Viết hàm cho phép lưu tập tin dưới dạng CSV file, yêu cầu khởi tạo là 10 dòng, mỗi
dòng sẽ có 10 số ngẫu nhiên bất kỳ cách nhau bởi dấu “;”. Xem hình minh họa:
Tiếp theo viết hàm cho phép đọc tập tin ở mục trên, xuất ra tổng giá trị của các phần tử
trên mỗi dòng.

'''
import csv
import random

# HÀM GHI FILE CSV VỚI DỮ LIỆU NGẪU NHIÊN
def tao_file_csv(ten_file):
    with open(ten_file, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        
        for _ in range(10):  # 10 dòng
            hang = [random.randint(1, 100) for _ in range(10)]  # 10 số ngẫu nhiên
            writer.writerow(hang)
    
    print(f" Đã tạo file '{ten_file}' với 10 dòng, mỗi dòng 10 số ngẫu nhiên.")


#  HÀM ĐỌC FILE CSV VÀ TÍNH TỔNG TRÊN MỖI DÒNG 
def doc_va_tinh_tong(ten_file):
    with open(ten_file, mode='r') as file:
        reader = csv.reader(file, delimiter=',')
        for i, hang in enumerate(reader, start=1):
            # Chuyển các phần tử trong hàng sang số nguyên
            so_nguyen = [int(x) for x in hang if x.strip()]
            tong = sum(so_nguyen)
            print(f"Dòng {i}: {hang}  Tổng = {tong}")


# CHƯƠNG TRÌNH CHÍNH 
ten_file = "dulieu.csv"

# Tạo file CSV ngẫu nhiên
tao_file_csv(ten_file)

# Đọc file CSV và in tổng từng dòng
print("\nKết quả tính tổng từng dòng:")
doc_va_tinh_tong(ten_file)
