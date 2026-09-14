s= input("enter a string ")
print ("first 3 characters:", s[:3])
print ("last 2 characters:", s[-2:])
print ("every second character :", s[::2])
#print ("reverse :", s[::-1])
reverse =""
for i in range(len(s) -1,-1,-1):
    reverse=reverse+ s[i]
print ("reverse", reverse)
