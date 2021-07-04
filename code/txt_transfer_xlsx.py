'''transfer txt to xlsx'''
import pandas as pd
import json

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
    filepath = "../doc/student.txt"
    name = "student.xlsx"
    content = open_file_to_dict(filepath) 
    change_txt_to_xlsx(content,name)  
    
    
    

    
    




        
