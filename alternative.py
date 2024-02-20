# User input variable
user_sentence = input("Enter a sentence to be converted to alternate capital letters and capital words: \n")
# functions
def alternate_Uppercase_word(s):
    i = 0
    word_list = s.split(' ')
    alternate_upper = []
    for w in word_list:
        if i:
            alternate_upper.append(w.upper())
        else:
            alternate_upper.append(w)
        i = int(not i)
    return " ".join(alternate_upper)

altered_sentence = ''.join([e.upper() if i % 2 == 0 else e for i, e in enumerate(user_sentence)])
print()
print("Here is your sentence with alternate capital letters: ")
print(altered_sentence)
print()
print("Here is your sentence with alternate capital words: ")
print(alternate_Uppercase_word(user_sentence))