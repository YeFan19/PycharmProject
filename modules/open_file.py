# 打开某路径文件，读取每一行

import os
os.chdir('C:\\Users\\Ye.Fan\\Desktop')
with open('Renew_ner20190516.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()


