#!/usr/bin/env python
# coding :utf8

file = open('ALL.txt', 'r', encoding='utf-8')
for line in file:
    content = line[0:-1]
    if 'http' in content:
        result_file = open("temp.txt", "a+", encoding='utf-8')
        result_file.write(content + "\r")
        result_file.close()
        result_file.close()
        print(content)
    else:
        content = 'http://' + content
        result_file = open("temp.txt", "a+", encoding='utf-8')
        result_file.write(content + "\r")
        result_file.close()
        result_file.close()
        print(content)
file.close()

file = open('temp.txt', 'r')
# 拼接不合适的url
# 不关闭两次有时候会出现玄学读写错误


a = 0
writeDir = "ALL.txt"
lines_seen = set()
outfile = open(writeDir, "w")
f = open('temp.txt', "r")
for line in f:
    if line not in lines_seen:
        a += 1
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
f.close()
print("success")