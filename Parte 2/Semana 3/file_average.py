# Use the file name mbox-short.txt as the file name
#URl https://www.py4e.com/code3/mbox-short.txt?PHPSESSID=99fd5fadeefb618f82d6b26e27354bdd
try:
    fname = input("Enter file name: ")
    fh = open(fname)
    
except:
    print('File invalid')
    quit()
    
    
total = 0.0
cont = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        num = line[19:]
        total = total + float(num)
        cont = cont + 1
        
average = total / cont
print('Average spam confidence:', average)
