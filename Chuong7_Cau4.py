#Câu 4: Xử lý JSON File, Chuyển đổi String Json qua Python Object
'''
Yêu cầu:
Cho string Json có cấu trúc sau:
'{ "ma":"nv1", "age":50, "ten":"Trần Duy Thanh"}'
Hãy viết mã lệnh chuyển đổi qua Python Object
'''


# Câu 4: Xử lý JSON File


import json  # Thư viện chuẩn của Python để xử lý JSON

# Chuỗi JSON ban đầu
json_str = '{ "ma":"nv1", "age":50, "ten":"Trần Duy Thanh"}'

# Chuyển từ JSON String sang Python Object (dict)
python_obj = json.loads(json_str)

# Xuất kết quả
print("Dạng Python Object:", python_obj)
print("Kiểu dữ liệu:", type(python_obj))
print("Mã:", python_obj["ma"])
print("Tên:", python_obj["ten"])
print("Tuổi:", python_obj["age"])
