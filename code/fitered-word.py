
'''当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。'''
#正则表达式通常被用来检索、替换那些符合某个模式的文本
import re

def open_file(filepath):
    with open(filepath,'r',encoding='utf-8') as f:
        content = f.read()
    return content
    

def check_filtered_words(filtered_words,input):
    result = re.match(input,filtered_words,flags=0)  #匹配对象，若是匹配成功返回匹配的对象，若是不成功返回None
    return result


def display(result):
    if result != None:
        print("Freedom")
    else:
        print("Human Rights")
    

if __name__ =="__main__":
    filepath = "../doc/filtered_words.txt"
    word = input("输入您想搜索的词： ")
    filtered_words =open_file(filepath)
    result = check_filtered_words(filtered_words,word)
    display(result)
