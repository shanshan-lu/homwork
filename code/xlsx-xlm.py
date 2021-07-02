'''将student.xlsx文件写入student.xml'''

import xlrd 
import xml.dom.minidom as md

def get_xlsx_data(filepath):
    xlsx_file = xlrd.open_workbook(filepath)
    sheet = xlsx_file.sheet_by_index(0)
    content = {}
    for i in range(sheet.nrows):
        content[i+1] = sheet.row_values(i)[1:]
    return content
def change_to_xml(content):
    xml_file = md.Document()  #创建新的xml文件
    root = xml_file.createElement("root")  #创建节点
    
 

if __name__ == '__main__':
    filepath = "E:\\LSS\\practice\\student.xlsx"
    print(type(get_xlsx_data(filepath)))