'''将student.xlsx文件写入student.xml'''

from city import change_txt_to_xlsx
import xlrd 
import xml.dom.minidom as md

def get_xlsx_data(filepath):
    xlsx_file = xlrd.open_workbook(filepath)
    sheet = xlsx_file.sheet_by_index(0)

    content = {}
    for i in range(sheet.nrows):
        content[i+1] = sheet.row_values(i)[1:]
    return content

def change_to_xml(xlsx_content):
    xml_file = md.Document()  #创建新的xml文件
    root = xml_file.createElement("root")  #创建节点
    students = xml_file.createElement("students")

    xml_file.appendChild(root)  #添加节点
    root.appendChild(students)

    comment = xml_file.createComment('学生信息表 "id" : [名字, 数学, 语文, 英文]')
    #创建评论
    students.appendChild(comment)

    xml_text_note = xml_file.createTextNode(str(xlsx_content))
    students.appendChild(xml_text_note)
    return xml_file

def write_to_xml(xml_file,filename,filepath):
    with open(filename,'wb') as f:
        f.write(xml_file.toprettyxml(encoding = 'utf-8'))  
    return f
 

if __name__ == '__main__':
    filepath = "../doc/student.xlsx"
    xlsx_content = get_xlsx_data(filepath)
    xml_content = change_to_xml(xlsx_content)
    write_to_xml(xml_content,'students.xml')
    