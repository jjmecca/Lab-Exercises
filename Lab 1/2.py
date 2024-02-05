import random
random_list=[]
filename="wordlist.txt"

def read_file(file):
    f=open(file,"r")
    words=f.readlines()
    return words

def create_random_word_list(random_list, file):
    while len(random_list)!=10:
        random_list.append(random.choice(file))
    return random_list

def find_shortest_word(word_list):
    shortest_word=word_list[0]
    for i in word_list[1:]:
        if len(i)<len(shortest_word):
            shortest_word=i
    return shortest_word

def create_dictionary(word_list):
    dictionary={word:len(word) for word in word_list}
    return dictionary

word_file=read_file(filename)
create_random_word_list(random_list, word_file)
print(create_dictionary(random_list))
print(find_shortest_word(random_list))