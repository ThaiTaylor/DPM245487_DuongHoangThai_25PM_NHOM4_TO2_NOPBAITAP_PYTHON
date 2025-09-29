#Câu 7: Nhập vào một ngày (ngày, tháng, năm). Tìm ngày kế sau ngày vừa nhập (ngày/tháng/năm).

import datetime

# Nhập dữ liệu
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

try:
    # Tạo đối tượng ngày
    ngay_nhap = datetime.date(nam, thang, ngay)
    # Cộng thêm 1 ngày
    ngay_ke = ngay_nhap + datetime.timedelta(days=1)
    print("Ngày kế tiếp là:", ngay_ke.strftime("%d/%m/%Y"))
except ValueError:
    print("Ngày không hợp lệ!")
