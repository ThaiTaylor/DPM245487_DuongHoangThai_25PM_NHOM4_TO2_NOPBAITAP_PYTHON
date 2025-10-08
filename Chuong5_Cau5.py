#Câu 5: Xử lý chuỗi với các hàm cơ bản
'''
Yêu cầu:
Viết chương trình cho phép nhập vào 1 chuỗi. Yêu cầu xuất ra:
- Bao nhiêu chữ IN HOA
- Bao nhiêu chữ in thường
- Bao nhiêu chữ là chữ số
- Bao nhiêu chữ là ký tự đặc biệt
- Bao nhiêu chữ là khoảng trắng
- Bao nhiêu chữ là Nguyên Âm
- Bao nhiêu chữ là Phụ âm
'''

# Nhập chuỗi từ bàn phím
s = input("Nhập vào một chuỗi: ")

# Khởi tạo các biến đếm
hoa = thuong = so = dacbiet = khoangtrang = nguyenam = phuam = 0

# Tập hợp nguyên âm
nguyen_am = "aeiouAEIOU"

# Duyệt từng ký tự trong chuỗi
for ch in s:
    if ch.isupper():
        hoa += 1
    elif ch.islower():
        thuong += 1
    elif ch.isdigit():
        so += 1
    elif ch.isspace():
        khoangtrang += 1
    else:
        dacbiet += 1

    # Kiểm tra nguyên âm và phụ âm (chỉ xét chữ cái)
    if ch.isalpha():
        if ch in nguyen_am:
            nguyenam += 1
        else:
            phuam += 1

# Xuất kết quả
print("\nKết quả thống kê:")
print("Số chữ IN HOA:", hoa)
print("Số chữ in thường:", thuong)
print("Số chữ số:", so)
print("Số ký tự đặc biệt:", dacbiet)
print("Số khoảng trắng:", khoangtrang)
print("Số nguyên âm:", nguyenam)
print("Số phụ âm:", phuam)
