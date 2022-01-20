import json
# import difflib #lib to compare strings
# from difflib import SequenceMatcher
from difflib import get_close_matches


# loading json file
data = json.load(open("data.json"))

type(data)

# hard searching of a file using a key
# print(data['rain'])

#### .................MINE..............................
# # a function that takes a word and search for its definition in our json file
# def translate(inputText):
#
#     # for any input convert it to lower case
#     word_similar = inputText.lower()
#
#     #for anyword that is entered check to see if the word as a resemblance in our
#     #key list. choose the first incase of error
#     final_word = get_close_matches(word_similar, data.keys())[0]
#
#     #print the most likely word found
#     print("Word entered is %s: " %(final_word))
#
#     if final_word in data:
#         return data[final_word] #passing the word as key to get definition or list of definitions
#     else:
#        return "error, word not found"

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0: #check the closest match of word entered to the keys in data
        print("Did you mean %s instead?" % get_close_matches(w, data.keys())[0]) #this line can be handled by the input next
        response = input("if yes, type 'y', else type 'n': ")
        response = response.lower()
        if response == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        else:
            # print("Reenter the word")
            word = input("Re-enter the word: ")
            word = word.lower()
            return data[word]

    else:
        return "The word doesn't exit. Please double check it"


word = input("Enter a word to get its definition: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
