def word_count(file):
    fin = open(file)
    d = dict()
    for line in fin:
        word = line.strip()
        d[word] = ''
    return d


word_dict = word_count('word_list.txt')

print('bitch' in word_dict)
