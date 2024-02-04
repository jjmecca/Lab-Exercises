import random

filename="wordlist.txt"
f=open(filename,"r")
words=f.readlines()
random_list=[]

while len(random_list)!=10:
    random_list.append(random.choice(words))

def find_shortest_word(word_list):
    shortest_word=word_list[0]
    for i in word_list[1:]:
        if len(i)<len(shortest_word):
            shortest_word=i
    return shortest_word

print(find_shortest_word(random_list))
