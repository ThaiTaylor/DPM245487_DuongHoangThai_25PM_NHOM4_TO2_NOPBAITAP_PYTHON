#Câu 5: Xử lý JSON File, Chuyển đổi Python Object qua String Json 
'''
Yêu cầu:
Cho Python Object có cấu trúc sau:
pythonObject = {
 "ten": "Trần Duy Thanh",
 "tuoi": 50,
 "ma": "nv1"
}
Hãy viết mã lệnh chuyển đổi qua String json.
'''


# Câu 5: Xử lý JSON File

import json  # Thư viện chuẩn để xử lý JSON

# Python Object (dict)
pythonObject = {
    "ten": "Trần Duy Thanh",
    "tuoi": 50,
    "ma": "nv1"
}

# Chuyển Python Object -> JSON String
json_str = json.dumps(pythonObject, ensure_ascii=False)

# Xuất kết quả
print("Dạng JSON String:", json_str)
print("Kiểu dữ liệu:", type(json_str))
