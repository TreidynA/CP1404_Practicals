NUM_OF_WORDS = {}
KEY_LIST = []

text = input("Text: ")
KEY_LIST = text.split()
KEY_LIST.sort()
NUM_OF_WORDS = dict.fromkeys(KEY_LIST, 0)
for word in KEY_LIST:
    if word in NUM_OF_WORDS:
        Num_of_word = NUM_OF_WORDS.get(word)
        Num_of_word += 1
        NUM_OF_WORDS.update({word: Num_of_word})

for word in NUM_OF_WORDS:
    print("{:{}} {}".format(word + " :", (max(len(KEY_LIST) for word in KEY_LIST)), NUM_OF_WORDS.get(word)))
