import re 

file = input('Enter file: ')
file = 'Atividades-Python-EveryBody/Parte 3/' + file
fh = open(file)

listNumbers = list()

for line in fh:
    words = line.split()
    for word in words:
        number = re.findall(r'[0-9]+', word)
        if number != []:
            for n in number:
                listNumbers.append(int(n))

sumNumber = 0
for n in listNumbers:
    sumNumber = sumNumber + n


print(listNumbers)
print(sumNumber)