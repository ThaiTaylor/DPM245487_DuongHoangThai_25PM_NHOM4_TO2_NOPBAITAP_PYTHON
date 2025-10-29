#Câu 6: Xử lý CSV File
'''
Yêu cầu:
Cho cấu trúc CSV được ngăn cách bởi dấu chấm phẩy ;
Hãy viết lệnh xuất ra mã, tên trong file CSV trên

'''

import csv
with open('datacsv.csv', newline='') as f:
 reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
 for row in reader:
    print(row[0],"\t",row[1])