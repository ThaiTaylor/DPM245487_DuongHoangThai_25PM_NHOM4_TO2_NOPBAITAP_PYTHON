#Câu 7: Tối ưu chuỗi danh từ
'''
Yêu cầu:
Viết chương trình tối ưu Chuỗi danh từ
Một Chuỗi được gọi là tối ưu khi: Không chứa các khoảng trắng dư thừa, các từ cách
nhau bởi một khoảng trắng, Ký tự đầu tiên của các từ Viết Hoa
Ví dụ:
Input “ TRần duY thAnH ”
Output “Trần Duy Thanh”

'''

def ToiUuChuoiDanhTu(s):
    # Bỏ khoảng trắng ở đầu và cuối
    s = s.strip()
    # Tách chuỗi thành các từ
    words = s.split()
    # Viết hoa ký tự đầu, còn lại viết thường
    words = [word.capitalize() for word in words]
    # Ghép lại thành chuỗi hoàn chỉnh
    result = " ".join(words)
    return result

# --- Chạy thử ---
chuoi = input("Nhập chuỗi danh từ: ")
print("Chuỗi sau khi tối ưu là:", ToiUuChuoiDanhTu(chuoi))
