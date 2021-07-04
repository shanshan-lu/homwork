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