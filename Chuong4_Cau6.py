#Câu 6: Những giá trị nào có thể xuất hiện trong randrange(0, 100)
'''
Yêu cầu:
Những giá trị nào có thể xuất hiện khi chạy randrange(0, 100)?
4.5 , 34 , -1, 100, 0, 99
'''
'''
Trả lời
Cú pháp randrange(start, stop) sinh ngẫu nhiên một số nguyên từ start đến stop - 1.
Với randrange(0, 100) --> sinh ngẫu nhiên số nguyên trong khoảng 0 <= value <= 99.
Suy ra
4.5 -->  không thể, vì chỉ sinh số nguyên.

34 -->  có thể, vì nằm trong [0, 99].

-1 -->  không thể, vì nhỏ hơn 0.

100 -->  không thể, vì stop = 100 là giới hạn trên, không bao gồm.

0  --> có thể (là giá trị nhỏ nhất).

99 -->  có thể (là giá trị lớn nhất).
'''