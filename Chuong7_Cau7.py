#Câu 7: Xử lý lưu Excel File
'''
Yêu cầu:
Hãy dùng thư viện xlsxwriter để lưu ra file Excel có cấu trúc như dưới đây(bao
gồm cả logo):

'''
# Tạo file Excel bằng xlsxwriter

import xlsxwriter

# Tạo file Excel mới
workbook = xlsxwriter.Workbook("sanpham.xlsx")
worksheet = workbook.add_worksheet("DanhSachSP")

# Thêm định dạng cho tiêu đề
header_format = workbook.add_format({
    "bold": True,
    "align": "center",
    "valign": "vcenter",
    "bg_color": "#D7E4BC",
    "border": 1
})

# Ghi tiêu đề cột
headers = ["Logo", "Mã SP", "Tên Sản Phẩm", "Đơn Giá"]
for col, header in enumerate(headers):
    worksheet.write(0, col, header, header_format)

# Dữ liệu sản phẩm
data = [
    ["sp1", "CocaCola", 15.5],
    ["sp2", "Bia 333", 14.5],
    ["sp3", "Pepsi", 17.0],
]

# Ghi dữ liệu ra file Excel (bắt đầu từ dòng 1)
row = 1
for item in data:
    worksheet.write(row, 1, item[0])  # Mã SP
    worksheet.write(row, 2, item[1])  # Tên
    worksheet.write(row, 3, item[2])  # Đơn giá
    row += 1

# Chèn logo (ảnh PNG/JPG) vào ô A2
worksheet.insert_image('A2', 'logo.png', {'x_scale': 0.5, 'y_scale': 0.5})

# Điều chỉnh độ rộng cột
worksheet.set_column("A:A", 15)
worksheet.set_column("B:D", 20)

# Đóng và lưu file Excel
workbook.close()

print("Đã tạo file Excel: sanpham.xlsx")
