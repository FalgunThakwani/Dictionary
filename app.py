import json
from difflib import get_close_matches

data = json.load(open("data.json","r"))

def translation(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys(),cutoff=0.88))>0:
        print("Did you mean %s instead?" % get_close_matches(word,data.keys(),cutoff=0.8)[0])
        x=input("Press Y for Yes and N for No")
        if x=="y":
            return  data[get_close_matches(word,data.keys(),cutoff=0.8)[0]]
        elif x=="n":
            return "No such word exist.Please double check"
        else:
            return "We dont understand your querry"
    elif word=="e":
        exit()
    else:
        return "No such word exist.Please double check"
word=" "
while word!="e" :
    word = input("Press 'E' to exit.\nEnter word:  ")
    word=word.strip().lower()
    output=translation(word)
    if type(output)==list:
        for item in output:
            print(item)
    else:
        print(output)
