'''当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。'''
def open_file(filepath):
    senstivite_word = []
    with open(filepath,'r',encoding='utf-8') as f:
        for line in f.readlines():
            senstivite_word.append(line.strip())
    return senstivite_word

def user_input():
    input_word = input('请输入你想搜索的内容：')
    return input_word
'''
def filtered_word(senstivite_word,input_word):
    for word in senstivite_word:
        if input_word.find(word) != -1:
           out_string = 'Freedom'
           return out_string
        else:
            out_string = 'Human Rights'
    return out_string

def display(out_string):
    print(out_string)
'''
def filtered_word(senstivite_word,input_word):
    flag = 0 
    for word in senstivite_word:
        if input_word.find(word) != -1:
          flag = 1
    return flag

def display(flag):
    if flag == 0:
        print('Human Rights')
    else:
        print('Freedom')

if __name__ == '__main__':
    filepath = "../practice/doc/filtered_words.txt"
    content = open_file(filepath)
    input_word = user_input()
    out_string = filtered_word(content,input_word)
    display(out_string)