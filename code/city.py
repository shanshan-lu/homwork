'''将纯文本文件 city.txt为城市信息, 里面的内容写入xlsx'''


import json
import pandas as pd

def open_file_to_dict(filepath):
    with open(filepath,'r',encoding= "utf-8") as f:
        data = f.read()
        dictionary = json.loads(data)  #将文本类型转化为字典 
    return dictionary 

def change_txt_to_xlsx(content:dict,name):
    dataframe = pd.DataFrame(content.values(),index = content.keys())
    xlsx_file = dataframe.to_excel(name,header = False)
    return xlsx_file
    
if __name__ =="__main__":
    filepath = "../doc/city.txt"
    content = open_file_to_dict(filepath)
    name = 'city.xlsx'
    change_txt_to_xlsx(content,name)