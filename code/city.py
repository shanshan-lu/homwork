'''将纯文本文件 city.txt为城市信息, 里面的内容写入xlsx'''


import json
import pandas as pd

def transfer_txt_to_xlsx(filepath):
    with open(filepath,'r',encoding= "utf-8") as f:
        data = f.read() 
        convert_line = json.loads(data)  #将文本类型转化为字典
        result = pd.DataFrame(convert_line.values(),index = convert_line.keys())
        xlsx_file = result.to_excel('city.xlsx',header = False)
    return xlsx_file
    
if __name__ =="__main__":
    filepath = "E:\\LSS\\practice\\city.txt"
    transfer_txt_to_xlsx(filepath)