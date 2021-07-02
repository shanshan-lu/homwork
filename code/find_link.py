'''一个HTML文件，找出里面的链接'''
import re

def find_link(filepath):
    with open(filepath,'r') as f:
        html_content = f.read()
    pattern = (r"http://[^\s]*")  #[^...]匹配除了...的所有字符；\s匹配任何空白字符;*匹配前面的子表达式零次或多次
    for i in re.findall(pattern,html_content):  #返回string中所有与pattern匹配的全部字符串,返回形式为数组
        print(i)

if __name__ == '__main__':
    filepath = "E:\\LSS\\practice\\html.txt"
    find_link(filepath)