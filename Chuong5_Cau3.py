#Câu 3: Xử lý Tách chuỗi
'''
Yêu cầu:
Cho 1 Chuỗi như sau “5;7;8;-2;8;11;13;9;10” (có thể nhập bất kỳ từ bàn phím)
- xuất các chữ số trên các dòng riêng biệt
- Xuất có bao nhiêu chữ số chẵn
- Xuất có bao nhiêu số âm
- Xuất có bao nhiêu chữ số nguyên tố
- Tính giá trị trung bình
'''

def so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Nhập chuỗi
s = input("Nhập chuỗi số (cách nhau bởi dấu ;): ")

# Tách chuỗi thành danh sách số nguyên
ds = [int(x) for x in s.split(';')]

# Xuất từng số trên dòng riêng
print("\nCác số trong chuỗi là:")
for so in ds:
    print(so)

# Đếm số chẵn
chan = sum(1 for x in ds if x % 2 == 0)

# Đếm số âm
am = sum(1 for x in ds if x < 0)

# Đếm số nguyên tố
nguyen_to = sum(1 for x in ds if so_nguyen_to(x))

# Tính trung bình
tb = sum(ds) / len(ds)

# Xuất kết quả
print("\nSố lượng số chẵn:", chan)
print("Số lượng số âm:", am)
print("Số lượng số nguyên tố:", nguyen_to)
print("Giá trị trung bình:", tb)
