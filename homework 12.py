# By Hossein Kamkar

reshte = input()
reshte = reshte.lower().strip()

for i in range(0,len(reshte)):
    if 'a' in reshte:
        reshte = reshte.replace('a','')
    elif 'e' in reshte:
        reshte = reshte.replace('e','')
    elif 'i' in reshte:
        reshte = reshte.replace('i','')
    elif 'o' in reshte:
        reshte = reshte.replace('o','')
    elif 'u' in reshte:
        reshte = reshte.replace('u','')
    
i = 0
while i < len(reshte):
    reshte = reshte[:i] + '.' + reshte[i:]
    i += 2
    
print(reshte)