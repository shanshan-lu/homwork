
'''当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。'''
#正则表达式通常被用来检索、替换那些符合某个模式的文本
import re
def check_filtered_words(filepath,input):
    with open(filepath,'r',encoding='utf-8') as f:
        filter_words = f.read()
        result = re.match(input,filter_words,flags=0)  #匹配对象，若是匹配成功返回匹配的对象，若是不成功返回None
    return result 
def display(result):
    if result != None:
        print("Freedom")
    else:
        print("Human Rights")
    

if __name__ =="__main__":
    filepath = "E:\\LSS\\practice\\filtered_words.txt"
    word = input("输入您想搜索的词： ")
    result = check_filtered_words(filepath,word)
    display(result)
