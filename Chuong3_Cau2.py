#Câu 2: Đếm số ngày trong tháng
'''
Yêu cầu:
Nhập vào 1 tháng, xuất tháng đó có bao nhiêu ngày.
1,3,5,7,8,10,12➔31 ngày
4,6,9,11➔có 30 ngày
Nếu là tháng 2 thì yêu cầu nhập thêm năm. Năm nhuần thì tháng 2 có 29 ngày,
không nhuần có 28 ngày
'''

print("Chương trình đếm số ngày trong tháng")
thang=int(input("Nhập vào 1 tháng:"))
if thang in (1,3,5,7,8,10,12):
    print("Tháng ", thang, " có 31 ngày")
elif thang in (4,6,9,11):
    print("Tháng ", thang, " có 30 ngày")
elif thang==2:
    nam=int(input("Mời bạn nhập vào năm:"))
    if (nam % 4 ==0 and nam % 100 != 0) or nam % 400==0:
        print("Tháng ",thang, " có 29 ngày")
    else:
        print("Tháng ", thang, " có 28 ngày")
else:
    print("Tháng ", thang, " không hợp lệ")
