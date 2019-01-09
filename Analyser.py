# This is the main file to experiment code analysis

# Import of external files and modules
import Keywords_Map # Own module where keywords are associated with fonctions to perform
import re # Regular expressions

mymap = Keywords_Map.keywords_map
mykeys = (Keywords_Map.keywords)


comment_indicator = '#'
eol_indicator = '\n'


f = open("Analyser.py","r")
content = f.read().split(eol_indicator)

for line in content:
    sub_line = line.split(comment_indicator)
    if sub_line[0] != '':
        term = sub_line[0].split()[0].lower()
        for i in mykeys:
             if re.search(i,term):
                mymap[i]()
                break
    else:
        if len(sub_line) > 1:
            print(f'Comment: ',sub_line[1])
f.close()
