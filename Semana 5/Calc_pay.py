hrs = float(input("Enter Hours: "))
h = float(input("Pagamento por hora: "))

if hrs > 40:
    h_extra = hrs - 40
    hrs = hrs - h_extra
    payment = (hrs * h) + (h_extra * (h * 1.5))
else:
    payment = hrs * h

print(payment)