# This is the main file to experiment code analysis

# Configuration
import Keywords_Map
import re

mymap = Keywords_Map.keywords_map
mykeys = (Keywords_Map.keywords)


comment_indicator = '#!'
eol_indicator = '\n'


f = open("Analyser.py","r")
content = f.read().split(eol_indicator)

for line in content:
    print(line)
    sub_line = line.split(comment_indicator)
    if sub_line[0] != '':
        term = sub_line[0].split()[0].lower()
 #       print(term)
        for i in mykeys:
             if re.search(i,term):
                mymap[i]()
                break
    else:
            print(f'Comment: ',sub_line)
f.close()
