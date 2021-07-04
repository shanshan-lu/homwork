'''read the body of a html file'''

from bs4 import BeautifulSoup

def open_file(filepath):
    with open(filepath,'r') as f:
        content = f.read()
    return content

def read_html_body(html_content):
    soup = BeautifulSoup(html_content, "html.parser")   #实现的文档导航,查找,修改文档的方式
    return soup.body

if __name__ =="__main__":
    filepath = "../doc/html.txt"
    html_content = open_file(filepath)
    print(read_html_body(html_content))
    