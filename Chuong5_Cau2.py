#Câu 2: Viết chương trình tối ưu chuỗi
'''
Yêu cầu:
Một Chuỗi được gọi là tối ưu khi: Không chứa các khoảng trắng dư thừa, các từ cách
nhau bởi một khoảng trắng
'''
while True:
    s = input("Nhập chuỗi cần tối ưu: ")

    # Xóa khoảng trắng đầu – cuối và tách các từ (split tự loại bỏ khoảng trắng thừa)
    words = s.strip().split()

    # Ghép các từ lại bằng 1 dấu cách
    s_toi_uu = ' '.join(words)

    print("Chuỗi sau khi tối ưu:", s_toi_uu)

    # Hỏi người dùng có muốn tiếp tục không
    tiep_tuc = input("Bạn có muốn tối ưu chuỗi khác không? (C/K): ").upper()
    if tiep_tuc != 'C':
        print("Cảm ơn bạn đã sử dụng chương trình!")
        break
