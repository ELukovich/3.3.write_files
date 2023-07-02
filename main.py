 # Задача 3
import os

lin = []

name = ['1.txt', '2.txt', '3.txt']
text = []
for file in name:
    with open(file, encoding="utf-8") as f:
        lines = 0
        for line in f:
            lines += 1
        lin.append(lines)
        # print(lines)
        # print(text)
# print(lin)

for file in name:
    with open(file, encoding="utf-8") as f:
        text.append(f.read().strip())
# print(text)

lst = [list(el) for el in zip(name, lin, text)]
lst.sort(key=lambda x: x[1])
print(lst)

with open('general.txt', 'w', encoding ="utf-8") as fg:
    for i in range(len(lst)):
        for k in range(len(lst[i])):
            str_f = str(lst[i][k])
            fg.write(f'{str_f}\n')






# file_name1 = os.path.basename('C:/Users/1.txt')
# # name.append(file_name1)
# file_name2 = os.path.basename('C:/Users/2.txt')
# name.append(f2)
# file_name3 = os.path.basename('C:/Users/3.txt')
# name.append(f3)
# name.extend([file_name1, file_name2, file_name3])
# # name = name + [file_name1, file_name2, file_name3]
# zip_name = zip(lin, name)
# zip_list = list(zip_name)
# zip_list.sort()
# print(lin)