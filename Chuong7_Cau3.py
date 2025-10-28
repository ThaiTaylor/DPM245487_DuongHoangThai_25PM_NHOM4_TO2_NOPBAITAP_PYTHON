#Câu 3: Xử lý XML File
'''
Yêu cầu:
Cho 1 file XML có cấu trúc và dữ liệu như dưới đây (employees.xml):
<?xml version="1.0" encoding="UTF-8" ?>
<employees>
 <employee>
 <id>1</id>
 <name>Trần Duy Thanh</name>
 </employee>
 <employee>
 <id>2</id>
 <name>Lê Hoành Sử</name>
 </employee>
 <employee>
 <id>3</id>
 <name>Hồ Trung Thành</name>
 </employee>
</employees>
Hãy dùng XML DOM để đọc dữ liệu lên màn hình.
'''

# Thư viện xml.dom.minidom có sẵn trong Python — không cần cài thêm
from xml.dom import minidom

def doc_xml(filename):
    try:
        # Parse file XML
        doc = minidom.parse(filename)

        # Lấy danh sách các thẻ <employee>
        employees = doc.getElementsByTagName("employee")

        print("DANH SÁCH NHÂN VIÊN")
        for emp in employees:
            # Lấy nội dung trong thẻ <id> và <name>
            id_node = emp.getElementsByTagName("id")[0]
            name_node = emp.getElementsByTagName("name")[0]

            id_value = id_node.firstChild.data
            name_value = name_node.firstChild.data

            print(f"Mã: {id_value} - Họ tên: {name_value}")

    except FileNotFoundError:
        print("Không tìm thấy file XML.")
    except Exception as e:
        print("Lỗi khi đọc file XML:", e)


# Chương trình chính
def main():
    filename = "employees.xml"  # Tên file XML cần đọc
    doc_xml(filename)


# Gọi chương trình chính
main()

