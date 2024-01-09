str = input()
a = []
for i in str: 
    if i.isupper():
        a.append(i.lower())
    else:   
        a.append(i.upper()) 
print(("").join(a)) 