#Câu 1: Kiểm tra chuỗi đối xứng
'''
Yêu cầu:
Dùng vòng lặp while vĩnh cửu, cho phép Nhập vào một Chuỗi➔Xuất Chuỗi này có phải
đối xứng hay không? Hỏi người sử dụng có tiếp tục phần mềm. Nếu tiếp tục thì nhập
Chuỗi mới, còn không thì thoát và thông báo cảm ơn
'''

while True:
    s = input("Nhập chuỗi cần kiểm tra: ")

    # Chuẩn hóa chuỗi (bỏ khoảng trắng đầu-cuối và so sánh thường)
    s = s.strip()

    # Kiểm tra đối xứng
    if s == s[::-1]:
        print("Chuỗi là đối xứng.")
    else:
        print("Chuỗi không đối xứng.")

    # Hỏi tiếp tục
    tiep_tuc = input("Bạn có muốn kiểm tra chuỗi khác không? (c/k): ").upper()
    if tiep_tuc != 'c':
        print("Cảm ơn bạn đã sử dụng chương trình!")
        break
