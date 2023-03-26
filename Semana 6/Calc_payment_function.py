def computepay(h, r):
    if h > 40:
        h_extra = h - 40
        h = h - h_extra
        payment = h * r + (h_extra * (r * 1.5)) 
        
        return payment

hrs = float(input("Enter Hours:"))
p_hr = float(input('Enter rate per hour'))
p = computepay(hrs, p_hr)

print("Pay", p)