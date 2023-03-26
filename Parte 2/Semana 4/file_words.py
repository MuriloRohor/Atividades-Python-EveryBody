# URL File: https://www.py4e.com/code3/romeo.txt?PHPSESSID=e9acbc95908d4f301b143522e4d57ad5

fname = input("Enter file name: ")
fh = open(fname)
word_list = []
for line in fh:
    words = line.split()
    for word in words:
        if word not in word_list:
            word_list.append(word)
        
        
word_list.sort()   
print(word_list)