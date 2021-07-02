'''read the body of a html file'''

from bs4 import BeautifulSoup

def read_html_body(filepath):
    with open(filepath,'r') as f:
        html_content = f.read()
    soup = BeautifulSoup(html_content, "html.parser")   #实现的文档导航,查找,修改文档的方式
    print(soup.find_all("body"))

if __name__ =="__main__":
    filepath = "E:\\LSS\\practice\\html.txt"
    read_html_body(filepath)