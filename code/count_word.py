'''count the number of words in the text'''

import collections 

def open_file(filepath):
    with open(filepath,'r') as f:
        content = f.read().split(" ")
    return content

def count_word_in_file(content):
    result = collections.Counter(content)
    return result
    


if __name__ == "__main__":
    filepath = "../doc/english.txt"
    content = open_file(filepath)
    count_word_in_file(content)

'''大文件的读取方式
1、f.read(参数)通过参数指定每次读取的长度
2、f.readline()每次读取一行
3、分块读取：将大文件分割成小文件，然后每次读完后释放内存。'''