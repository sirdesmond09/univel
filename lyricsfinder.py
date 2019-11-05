# lyrics = open('lyrics.txt', 'r', errors='ignore')

# user_input = input('Please enter word \n Seperate by comma for multiple words \n > ')
# could_not_find_word = True

# for word in lyrics.readlines():
#     if user_input in word:
#         lower_case_word = word.lower()
#         lower_case_word = lower_case_word.replace( user_input, f"'{user_input.upper()}'")
#         print(lower_case_word)
#         could_not_find_word = False
#     else:
#         pass
# if could_not_find_word:
#     print("Sorry we could not find your word")

lyrics = open('lyrics.txt', 'r', errors='ignore')

user_input = input('Please enter word \nSeperate by comma for multiple words \n > ')
could_not_find_word = True

words = user_input.split(",")

for lyric in lyrics.readlines():
    lower_case_word = lyric.lower()
    printable_word = False
        
    for word in words:
        
        if word in lower_case_word:
            lower_case_word = lower_case_word.replace( word, f"'{word.upper()}'")
            could_not_find_word = False
            printable_word = True
    if printable_word:
        print(lower_case_word)

        
if could_not_find_word:
    print("Sorry we could not find your word")