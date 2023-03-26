text = "X-DSPAM-Confidence:    0.8475"

numfind = text.find('0')
num = text[numfind:]

print(float(num))