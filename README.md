#câu3
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
#câu4
#Câu 4: Python hỗ trợ những kiểu dữ liệu cơ bản nào?
'''
Trả lời:
Các kiểu dữ liệu hỗ trợ cơ bản của Python: 
- Kiểu số (int(số nguyên), float(số thực), complex(số phức)).
- Kiểu chuỗi(str(chuỗi ký tự)).
- Kiểu logic(bool(TRUE OR FALSE)).
- Kiểu dữ liệu phức(list(danh sách), tuple(bộ), range(dãy số nguyên liên tiếp), dictonary(từ điển)).
'''
#câu5
#Câu 5: Trình bày các loại ghi chú trong Python.
#Trả lời:
#-->Ghi chứ 1 dòng

'''
--> Ghi 
    chú 
    nhiều
    dòng 
'''
#câu6
#Câu 6: Trình bày ý nghĩa toán tử /, //, %, **, and, or, is.

'''
    /--> Chia lấy phần nguyên.
    //--> Chia lấy phần nguyên bỏ phần thập phân.
    %--> Chia lấy phần dư.
    **--> Lũy thừa
    and--> Toán tử Và: trả về TRUE nếu cả 2 vế đều đúng.
    Or--> Toán tử Hoặc: trả về TRUE nếu có ít nhất 1 vế đúng.
    is--> Kiểm tra 2 biến có cùng tham chiếu không.
'''
#câu7
#Câu 7: Trình bày một số cách nhập dữ liệu từ bàn phím.
'''
Trả lời:
1.  input().
2.  int(input()).
3.  float(input()).
4.  split().
'''
#câu8
#Câu 8: Trình bày các loại lỗi khi lập trình và cách bắt lỗi trong Python.
'''
Trả lời:
    * Các loại lỗi
    - Lỗi cú pháp.
    - Lỗi Logic.
    - Lỗi thời gian chạy:
        + ZeroDivisionError
        + ValueError
        + TypeError
        + IndexError
        + FileNotFoundError
    * Cách bắt lỗi
    - Dùng try-except
    - Dùng else-finally
'''
#câu9
#Câu 9: Giải thích kết quả tính toán của các biểu thức
'''
Cho các biến
i1 = 2
i2 = 5
i3 = -3
d1 = 2.0
d2 = 5.0
d3 = -0.5


Cho biết kết quả và giải thích cách thực hiện của các lệnh sau:
(a) i1 + (i2 * i3) = -13. Cách thực hiện--> Chương trình sẽ thực hiện phép tính trong () trước nhân i2 với i3 sau đó cộng i1.
(b) i1 * (i2 + i3) = 4. Cách thực hiện--> Chương trình sẽ thực hiện phép tính trong () trước i2 cộng i3 sau đó nhân với i1.
(c) i1 / (i2 + i3) = 1. Cách thực hiện--> Chương trình sẽ thực hiện phép tính trong () trước i2 cộng i3 sau đó chia lấy phần nguyên với i1.
(d) i1 // (i2 + i3) = 1. Cách thực hiện--> Chương trình sẽ thực hiện phép tính trong () trước i2 cộng i3 sau đó chia lấy phần nguyên bỏ phần dư với i1.
(e) i1 / i2 + i3 = -2.6. Cách thực hiện--> Chương trình sẽ thực hiện phép tính theo thứ tự Nhân-Chia-Cộng-Trừ--> i1 chia lấy phần nguyên với i2 sau đó cộng i3
(g) 3 + 4 + 5 / 3 =  8.666666666666666. Cách thực hiện--> Chương trình sẽ thực hiện phép tính theo thứ tự Nhân-Chia-Cộng-Trừ--> 5 chia lấy phần nguyên với 3 sau đó cộng 3 cộng 4.
(h) 3 + 4 + 5 // 3 = 8. Cách thực hiện--> Chương trình sẽ thực hiện phép tính theo thứ tự Nhân-Chia-Cộng-Trừ--> 5 chia lấy phần nguyên bỏ phần dư với 3 sau đó cộng 3 cộng 4.
(i) (3 + 4 + 5) / 3 = 4. Cách thực hiện--> Chương trình sẽ thực hiện phép tính trong () trước 3 cộng 4 cộng 5 sau đó chia lấy phần nguyên với 3.
(j) (3 + 4 + 5) // 3 = 4. Cách thực hiện--> Chương trình sẽ thực hiện phép tính trong () trước 3 cộng 4 cộng 5 sau đó chia lấy phần nguyên bỏ phần dư với 3.
(k) d1 + (d2 * d3) = -0.5. Cách thực hiện--> Chương trình sẽ thực hiện phép tính trong () trước nhân d2 với d3 sau đó cộng d1.
(l) d1 + d2 * d3 = -0.5. Cách thực hiện--> Chương trình sẽ thực hiện phép tính theo thứ tự Nhân-Chia-Cộng-Trừ--> d2 nhân d3 sau đó cộng d1.
(m) d1 / d2 - d3 = 0.9.  Cách thực hiện--> Chương trình sẽ thực hiện phép tính theo thứ tự Nhân-Chia-Cộng-Trừ--> d2 chia lấy phần nguyên d3 sau đó cộng d1.
(n) d1 / (d2 - d3) = 0.36363636363636365. Cách thực hiện--> Chương trình sẽ thực hiện phép tính trong () trước trừ d2 với d3 sau đó chia lấy phần nguyên với d1.
(o) d1 + d2 + d3 / 3 =  6.833333333333333. Cách thực hiện--> Chương trình sẽ thực hiện phép tính theo thứ tự Nhân-Chia-Cộng-Trừ--> cộng d1, d2, d3 sau đó chia lấy phần nguyên với 3.
(p) (d1 + d2 + d3) / 3 = 2.1666666666666665. Cách thực hiện--> Chương trình sẽ thực hiện phép tính trong () cộng d1, d2, d3 sau đó chia lấy phần nguyên với 3.
(q) d1 + d2 + (d3 / 3) =  6.833333333333333. Cách thực hiện--> Chương trình sẽ thực hiện phép tính trong () d3 chia lấy phần nguyên với 3 sau đó cộng d1, d2.
(r) 3 * (d1 + d2) * (d1 - d3) = 52.5. Cách thực hiện--> Chương trình sẽ thực hiện phép tính trong () cộng d1 với d2 và trừ d1 với d3 sau đó nhân 3 với tổng của d1,d2 và nhân với hiệu của d1,d3.

'''
#câu10
#Câu 10: Hãy viết ngắn gọn lại các lệnh dưới đây
'''
Yêu cầu:
Cho các lệnh ban đầu:
(a) x = x + 1 --> x+=1.
(b) x = x / 2 --> x/=2.
(c) x = x - 1 --> x-=1.
(d) x = x + y --> x+=y.
(e) x = x - (y + 7) --> x-=(y+7).
(f) x = 2*x --> x*=2.
(g) number_of_closed_cases = number_of_closed_cases + 2*ncc --> number_of_closed_cases+=2*ncc.

'''
