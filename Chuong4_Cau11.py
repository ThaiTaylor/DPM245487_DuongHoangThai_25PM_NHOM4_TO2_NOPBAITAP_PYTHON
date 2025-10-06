#Câu 11: Kiểm tra kết quả thực hiện
'''
Yêu cầu:
Cho 3 hàm dưới đây:
def sum1(n):
 s = 0
 while n > 0:
 s += 1
 n -= 1
 return s
def sum2():
 global val
 s = 0
 while val > 0:
 s += 1
 val -= 1
 return s
def sum3():
 s = 0
 for i in range(val, 0, -1):
 s += 1
 return s

 TRƯỜNG HỢP 1: 
def main():
    global val
    val = 5
    print(sum1(5))  # -> 5
    print(sum2())   # -> 5 (val giảm xuống 0)
    print(sum3())   # -> chạy với val = 0
main()

TRƯỜNG HỢP 2: 
def main():
    global val
    val = 5
    print(sum1(5))   -> 5
    print(sum3())    -> 5 (val vẫn = 5)
    print(sum2())    -> 5 (val giảm xuống 0)
main()


TRƯỜNG HỢP 3:
def main():
    global val
    val = 5
    print(sum2())    -> 5 (val giảm xuống 0)
    print(sum1(5))   -> 5 (không ảnh hưởng)
    print(sum3())    -> val = 0 ⇒ range(0,0,-1) ⇒ 0
main()

'''

