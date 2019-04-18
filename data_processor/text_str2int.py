import sys
import codecs
import json
file_path = sys.argv[1]
lines = open(file_path).read().splitlines()
char_map = {}
i = 0
for line in lines:
	img_name, text = line.rsplit('\t', 1)
	for char_ in text:
            if char_ not in char_map:
		char_map[str(i) = ord(char_)
                i += 1
with codecs.open('char_map.json', 'w', 'utf-8') as fw:
	fw.write(json.dumps(char_map, ensure_ascii=False, indent=2))
