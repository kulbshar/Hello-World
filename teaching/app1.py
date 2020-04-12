import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("C:\\Users\\ksharma\\python\\python_mega_course\\teaching\\data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if yn.upper() == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn.upper() == 'N':
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. please double check it."

# In [22]: SequenceMatcher(None, "Rainn", "Rain")
# Out[22]: <difflib.SequenceMatcher at 0x273a03c1d88>
    
# In [23]: SequenceMatcher(None, "Rain", "Rainn").ratio()
# Out[23]: 0.8888888888888888

# In [28]: from difflib import get_close_matches

# In [29]: get_close_matches("rainn", ["help", "pyramid", "rain"])
# Out[29]: ['rain']

# In [33]: get_close_matches("rainn", data.keys())
# Out[33]: ['rain', 'train', 'rainy']


# In [35]: get_close_matches("rainn", data.keys(), n = 5)
# Out[35]: ['rain', 'train', 'rainy', 'grain', 'drain']


# In [36]: get_close_matches("rainn", data.keys(), n = 1)
# Out[36]: ['rain']

# In [37]: get_close_matches("rainn", data.keys(), n = 5)[0]
# Out[37]: 'rain'


# In [42]: get_close_matches("cacacaa", data.keys(), cutoff=0.5)
# Out[42]: ['acacia', 'Sciacca', 'cacao']


word = input("Enter word: ")
# print(translate(word))
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

