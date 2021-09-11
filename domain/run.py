# coding=utf-8
import os
from collections import Counter

sumsdata = []
for fname in os.listdir(os.getcwd()):
    if os.path.isfile(fname) and fname.endswith('.txt'):
        with open(fname, 'r') as fp:
            data = fp.readlines()
        sumsdata += [line.strip().lower() for line in data]
cnt = Counter()
for word in sumsdata:
    cnt[word] += 1
cnt = dict(cnt)
for key, value in cnt.items():
    print(key + ":" + str(value))
    file = open('total.txt', 'a+')
    file.write(key + ":" + str(value) + '\n')
    file.close()
