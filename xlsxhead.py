import os

import pandas as pd
import hashlib
path_o = r""
excelNames = os.listdir(path_o)
# print(type(excelNames))
print("一共有%d个文件" % (len(excelNames)))
i = 0
head_has = []
for excelName in excelNames:
    if excelName.endswith('.xlsx'):
        path = path_o + '\\' + excelName
        # print(path)
        data = pd.read_excel(path)
        i += 1
        h = hashlib.md5(str(data.columns).encode('utf-8'))
        head_has.append(h)
        print(h)
print(head_has)
# h_len = len(head_has)
# for i in h_len:





