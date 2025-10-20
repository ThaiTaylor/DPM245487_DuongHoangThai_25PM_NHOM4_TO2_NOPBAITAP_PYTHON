#Câu 8: Tách lấy tên bài hát
'''
Yêu cầu:
Cho một chuỗi là đường dẫn của 1 file nhạc, ví dụ: d:\\music\muabui.mp3
Hãy viết 2 hàm để:
- Lấy ra muabui.mp3
- Lấy ra muabui
Lưu ý đường dẫn bài hát là bất kỳ. Nên khi truyền vào bài hát nào thì lấy chính xác theo
bài hát đó.
'''

def LayTenFile(dayduongdan):
    # Tách phần sau cùng của đường dẫn (tên file)
    ten_file_day_du = dayduongdan.split("\\")[-1]
    return ten_file_day_du

def LayTenBaiHat(dayduongdan):
    # Lấy tên file đầy đủ trước
    ten_file_day_du = LayTenFile(dayduongdan)
    # Tách bỏ phần đuôi mở rộng (.mp3, .wav, ...)
    ten_bai_hat = ten_file_day_du.split(".")[0]
    return ten_bai_hat

# run
duongdan = input("Nhập đường dẫn file nhạc: ")
print("Tên file (gồm đuôi):", LayTenFile(duongdan))
print("Tên bài hát:", LayTenBaiHat(duongdan))
