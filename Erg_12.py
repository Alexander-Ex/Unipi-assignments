Ascii_code=[]
Ascii_rev_code=[]
Ascii_rev_character=[]
#Λιστες που θα χρησιμοποιησω

x=input("Give the name of the file")
f = open(x,"r")
a=f.read()
f.close()
#Διαβαζω αρχειο 

for i in a:
    var= ord(i)
    Ascii_code.append(var)
#Γεμιζω την λιστα με τους κωδικους ASCII απο το αρχειο

N=len(Ascii_code)-1
for y in range(N,-1,-1):
    x=128-Ascii_code[y]
    Ascii_rev_code.append(x)
#Διαβαζω αναποδα την λιστα και στελνω τα στοιχεια στην δευτερη λιστα

for z in range(N):
    Ascii_rev_character.append(chr(Ascii_rev_code[z]))
#Μετατρεπω τους κωδικους σε χαρακτηρες και τα στελνω στην τριτη λιστα

abc=""
for c in range(N):
    abc=abc+Ascii_rev_character[c]
    
print (abc)
