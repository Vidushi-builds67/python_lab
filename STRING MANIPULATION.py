S= input ("ENTER STRING")
print ("UPPERCASE:", S.upper())
print ("lowerCASE:", S.lower())
#print ("reverse :", S[::-1])
reverse =""
for i in range(len(S) -1,-1,-1):
    reverse=reverse+ S[i]
print ("reverse", reverse)
vowel=0
for ch in S:
    if ch.lower() in "aeiou":
        vowel+=1
print ("number of vowels:", vowel)
