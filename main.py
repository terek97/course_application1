import json
from difflib import get_close_matches as gcm

data = json.load(open("data.json"))

def get_value_by_key(key):
    while True:
        if key in data.keys():
            return data[key]
            break
        else:
            analog_key = gcm(key, data, n=1)
            if input("the word is not in dictionary. did u mean %s? Enter Y or N: " % analog_key).lower() == 'y':
                return data[analog_key[0]]
                break
            else:
                return "Sorry(((. Try another word."
                break
            
    
word = input("enter the word: ")
print(get_value_by_key(word.lower()))