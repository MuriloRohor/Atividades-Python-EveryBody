try:
    fname = input("Enter file name: ")
    fh = open(fname)

except:
    print('File invalid')
    quit()

for line in fh:
    lineCut = line.rstrip()
    print(lineCut.upper())