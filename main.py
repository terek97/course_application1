from difflib import get_close_matches as gcm
import mysql.connector as database


con = database.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)
cursor = con.cursor()


def make_query(key):
    if key == 'expression':
        query = cursor.execute("SELECT Expression FROM Dictionary")
    else:
        query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % key)

    dataset = cursor.fetchall()
    result = []
    for data in dataset:
        for item in data:
            result.append(item)
    return result




def get_value_by_key(key):

    query_keys = [key, key.title(), key.upper()]
 
    for query in query_keys:
        data = make_query(query)
        if data:
            return data
    
    expressions = make_query('expression')
    analog_key = gcm(key, expressions, n=1)
    if len(analog_key) > 0:
        yn = input("the word is not in dictionary. did u mean %s? Enter Y or N: " % analog_key[0].lower())

        if  yn == 'y':
            data = make_query(analog_key[0])
            return data

        elif yn == 'n':
            return "Sorry(((. Try another word."

        else:
            return "we didn`t understent your input."

    else:
        return "the word is not in dictionary."

            
    
word = input("enter the word: ")
output = get_value_by_key(word.lower())
if type(output) == list:
        print('\n'.join(output))
else:
    print(output)