import string
s= input("enter a string")
result= ""
for ch in s:
    if ch not in string.punctuation:
        result +=ch
print ("STRING WITHOUT PUNCTUtion:", result)
        
