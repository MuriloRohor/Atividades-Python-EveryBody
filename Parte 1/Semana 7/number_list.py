largest = None
smallest = None
numberlist = []
while True:
    num = input('Enter a number: ')
    if num == "done":
      break
    
    try:
      num = int(num)
      numberlist.append(num)
                
    except ValueError:
      print('Invalid input')
      continue
        
for number in numberlist:
    if smallest is None:
      smallest = number
    elif smallest > number:
        smallest = number
        
for number in numberlist:
    if largest is None:
      largest = number
    
    elif largest < number:
        largest = number
        
print('Maximum is', largest)
print('Minimum is', smallest)