#Câu 1: Kiểm tra năm nhuần
'''
Nhập vào một năm bất kỳ, kiểm tra năm đó có phải năm nhuần hay không. Biết
rằng: Năm nhuần là năm chia hết cho 4 nhưng không chia hết cho 100 hoặc chia
hết cho 400
'''

print("Chương trình kiểm tra năm nhuần")
nam=int(input("Mời fen nhập vào 1 năm:"))
if (nam % 4 ==0 and nam % 100 != 0) or nam % 400 == 0:
 print("Năm ", nam, " là năm nhuần")
else:
 print("Năm ", nam, " không nhuần")