'''生成200个激活码'''

import random
ALPHABET = "abcdefghigklmnopqrstuvwsyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def gen_random_code(total,code_len):
   code_list = []
   for i in range(total):
       code = random.sample(ALPHABET,code_len)  #sample返回一个长度为k新列表，新列表存放list所产生k个随机唯一的元素
       code_str ="".join(code)
       code_list.append(code_str)
   return code_list

if __name__ =="__main__":
   print(gen_random_code(10,5))


  


        
   




    
        


    

