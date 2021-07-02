'''transfer txt to xlsx'''
import pandas as pd
import json


def transfer_txt_to_xlsx(filepath):
    with open(filepath,'r',encoding= "utf-8") as f:
        data = f.read() 
        convert_line = json.loads(data) #将文本转化为字典
        result = pd.DataFrame(convert_line.values(),index = convert_line.keys())
        xlsx_file = result.to_excel('student.xlsx',header = False)
    
    
        
if __name__ =="__main__":
    filepath = "E:\\LSS\\practice\\student.txt"
    transfer_txt_to_xlsx(filepath)   
    
    
    

    
    




        
