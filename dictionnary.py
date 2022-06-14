import json
from difflib import SequenceMatcher, get_close_matches
data = json.load(open("data.json"))


def meaning(w):
    for m in data[w]:
        print(m)
        print('')


def translate(w):
    w = w.lower()
    if w in data:
        print(w, ':', data[w])
    else:
        print('Word does not exist')
        suggs = get_close_matches(w, data.keys(), 10, 0.8)
        if suggs:
            decision = input('Do you want to show similar words that were found (press "Y" for Yes)')
            if decision == 'Y':
                print(f'NOTE : Found {len(suggs)} similar words')
                for sugg in suggs:
                    ratio = SequenceMatcher(None, w, sugg).ratio()
                    print(f'{sugg} ({ratio*100}%)')
                    meaning(sugg)


word = input('enter word : ')
translate(word)
