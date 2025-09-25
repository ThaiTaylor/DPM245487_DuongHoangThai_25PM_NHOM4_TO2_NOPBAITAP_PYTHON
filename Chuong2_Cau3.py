'''
Yêu cầu:
Viết chương trình nhập vào điểm ba môn Toán, Lý, Hóa của một học sinh. In ra
điểm trung bình của học sinh đó với hai số lẻ thập phân.
'''

DiemToan = float (input("Nhập điểm Toán: "))
DiemLy = float (input("Nhập điểm Lý: "))
DiemHoa = float (input("Nhập điểm Hóa: "))
dtb = (DiemToan+DiemLy+DiemHoa)/3
print("Vậy điểm trung bình là: ", dtb)
print("Vậy điểm trung bình sau khi làm tròn là: ", round(dtb,2))