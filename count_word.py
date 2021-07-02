'''count the number of words in the text'''

import collections 

def count_word(filepath):
    with open(filepath,'r') as f:
        content = f.read().split(" ")
    result = collections.Counter(content)
    print(result)
    


if __name__ == "__main__":
    filepath = "E:\\LSS\\practice\\english.txt"
    count_word(filepath)