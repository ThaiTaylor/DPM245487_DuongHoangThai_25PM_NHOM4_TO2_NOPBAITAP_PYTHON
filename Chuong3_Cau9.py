#Câu 9: Nhập vào 1 tháng, xuất ra tháng đó thuộc quý mấy trong năm.

# Nhập dữ liệu
thang = int(input("Nhập tháng (1-12): "))

while thang < 1 or thang > 12:
    print("Tháng không hợp lệ! Vui lòng nhập lại.")
    thang = int(input("Nhập tháng (1-12): "))

# Xử lý và xuất kết quả
if 1 <= thang <= 3:
    print("Tháng", thang, "thuộc quý 1")
elif 4 <= thang <= 6:
    print("Tháng", thang, "thuộc quý 2")
elif 7 <= thang <= 9:
    print("Tháng", thang, "thuộc quý 3")
else:
    print("Tháng", thang, "thuộc quý 4")

