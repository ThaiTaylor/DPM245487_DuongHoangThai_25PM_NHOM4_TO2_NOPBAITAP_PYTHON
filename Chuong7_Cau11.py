#Câu 11: Xử lý Excel File - Viết phần mềm Quản Lý Nhân Viên

'''
Yêu cầu:
Viết phần mềm quản lý Nhân viên lưu bằng Excel. Mỗi nhân viên có Mã, Tên, Tuổi.
− Phần mềm cho phép lưu Nhân viên vào File Excel
− Phần mềm cho phép đọc danh sách Nhân viên trong File Excel
− Phần mềm cho phép sắp xếp Nhân viên theo Tuổi tăng dần

'''
from openpyxl import Workbook, load_workbook

# ======= HÀM GHI DANH SÁCH NHÂN VIÊN VÀO FILE EXCEL =======
def ghi_nhan_vien(file_path, danh_sach_nv):
    wb = Workbook()
    ws = wb.active
    ws.title = "NhanVien"

    # Ghi tiêu đề cột
    ws.append(["STT", "Mã", "Tên", "Tuổi"])

    # Ghi dữ liệu nhân viên vào bảng
    for i, nv in enumerate(danh_sach_nv, start=1):
        ws.append([i, nv["ma"], nv["ten"], nv["tuoi"]])

    wb.save(file_path)
    print(f"✅ Đã lưu {len(danh_sach_nv)} nhân viên vào file '{file_path}'.")


# ======= HÀM ĐỌC DANH SÁCH NHÂN VIÊN TỪ FILE EXCEL =======
def doc_nhan_vien(file_path):
    wb = load_workbook(file_path)
    ws = wb.active

    danh_sach_nv = []
    for row in ws.iter_rows(min_row=2, values_only=True):  # Bỏ hàng tiêu đề
        nv = {"stt": row[0], "ma": row[1], "ten": row[2], "tuoi": row[3]}
        danh_sach_nv.append(nv)

    return danh_sach_nv


# ======= HÀM SẮP XẾP NHÂN VIÊN THEO TUỔI TĂNG DẦN =======
def sap_xep_theo_tuoi(danh_sach_nv):
    return sorted(danh_sach_nv, key=lambda x: x["tuoi"])


# ======= CHƯƠNG TRÌNH CHÍNH =======
file_excel = "NhanVien.xlsx"

# 1️⃣ Nhập danh sách nhân viên mẫu
danh_sach_nv = [
    {"ma": "NV1", "ten": "An", "tuoi": 18},
    {"ma": "NV2", "ten": "Lành", "tuoi": 22},
    {"ma": "NV3", "ten": "Giải", "tuoi": 20},
    {"ma": "NV4", "ten": "Thoát", "tuoi": 19},
    {"ma": "NV5", "ten": "Hạnh", "tuoi": 25},
    {"ma": "NV6", "ten": "Phúc", "tuoi": 24},
]

# 2️⃣ Ghi danh sách vào file Excel
ghi_nhan_vien(file_excel, danh_sach_nv)

# 3️⃣ Đọc lại danh sách từ file Excel
ds_doc = doc_nhan_vien(file_excel)
print("\n📋 Danh sách nhân viên đọc từ file:")
for nv in ds_doc:
    print(nv)

# 4️⃣ Sắp xếp danh sách theo tuổi tăng dần
ds_sap_xep = sap_xep_theo_tuoi(ds_doc)
print("\n📈 Danh sách nhân viên sau khi sắp xếp theo tuổi tăng dần:")
for nv in ds_sap_xep:
    print(nv)
