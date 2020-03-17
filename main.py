import json
from difflib import get_close_matches as gcm

data = json.load(open("data.json"))

def get_value_by_key(key):
    if key in data.keys():
        return str(data[key])
            
    else:
        analog_key = gcm(key, data, n=1)
        yn = input("the word is not in dictionary. did u mean %s? Enter Y or N: " % analog_key).lower()

        if len(analog_key) > 0 and yn == 'y':
            return data[analog_key[0]]
                
        elif len(analog_key) > 0 and yn == 'n':
            return "Sorry(((. Try another word."
            
        else:
            return "we didn`t understent your input."
            
    
word = input("enter the word: ")
print(get_value_by_key(word.lower()))