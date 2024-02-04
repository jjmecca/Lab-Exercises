list=["apple","rice","gargoyle","pandas","sheep","raptor"]

def find_longest_word(word_list):
    longest_word=word_list[0]
    for i in word_list[1:]:
        if len(i)>len(longest_word):
            longest_word=i
    return longest_word

print(find_longest_word(list))