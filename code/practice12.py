'''当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。'''

def open_file(filepath):
    senstivite_word = []
    with open(filepath,'r',encoding='utf-8') as f:
        for line in f.readlines():
            senstivite_word.append(line.strip())
    return senstivite_word

def user_input():
    input_word = input('请输入你想搜索的内容：')
    return input_word

def filtered_word(senstivite_word,input_word):
    for word in senstivite_word:
        if word in input_word:
            input_word = input_word.replace(word,'*'*len(word))
    return input_word

def display(out_string):
    print(out_string)


if __name__ == '__main__':
    filepath = "../practice/doc/filtered_words.txt"
    content = open_file(filepath)
    input_word = user_input()
    out_string = filtered_word(content,input_word)
    display(out_string)
    
    


    

