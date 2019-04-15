import pandas
import sys
import codecs
import json

xls_path = sys.argv[1]
out_json_path = sys.argv[2]
data_frame = pandas.read_excel(xls_path)

data_list = data_frame.get_values()

with codecs.open(out_json_path, 'w', 'utf-8') as fw:
    fw.write(json.dumps(data_list.tolist(), ensure_ascii=False, indent=2))