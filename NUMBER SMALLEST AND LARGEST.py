number=[]
for i in range (7):
    n= int (input ("enter integer:"))
    number.append(n)
smallest =number[0]
largest=number[0]
for n in number:
    if n<smallest:
        smallest=n
    if n>largest:
        largest=n
print("SMALLEST", smallest)
print("LARGEST", largest)
