
import sys
import re

WORD_RE = re.compile(r'\w+')
index = {}

with open("zen.txt", encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for math in WORD_RE.finditer(line):
            word = math.group()
            column_no = math.start() + 1
            location = (line_no, column_no)

            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences

for word in sorted(index, key = str.upper):
    print(word, index[word])

