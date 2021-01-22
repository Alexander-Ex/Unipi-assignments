import math

Ascii_characters=[]
Ascii_number=[]
Ascii_quan=[]
Ascii_perc_single=[]
#Οριζω τις λιστες που θα χρησιμποποιησω

single_counter=0
#Ειναι μετρητης που μετραει το πληθος των μονων αριθμων ASCII

x=input("Give the name of the file")
f = open(x,"r")
a=f.read()
f.close()

for i in a:
    var= ord(i)
    if (var%2)==1:
        if i not in Ascii_characters:
            Ascii_characters.append(i)
            Ascii_number.append(var)
#Βρισκω τους μονους αριθμους και τον αριθμο ASCII και τους βαζω στις λιστες

for y in range(len(Ascii_characters)):
    counter=0
    for x in a:
        if Ascii_characters[y]==x:
            counter=counter+1
            single_counter=single_counter+1
    Ascii_quan.append(counter)
#Μετραω το ποσες φορες εμφανιζονται μαζι με το ποσους μονους αριθμους υπαρχουν

for x in range(len(Ascii_quan)):
    per_single=((Ascii_quan[x]/single_counter)*100)
    if type(per_single)==float:
        per_single=math.ceil(per_single)
    Ascii_perc_single.append(per_single)
#Γεμιζω την λιστα με το στρογγυλοποιημενο ποσοστο εμφανισης του καθε μονου αριθμου


for w in range(len(Ascii_characters)):
    print ("The character ",Ascii_characters[w]," with an odd ASCII number of ",Ascii_number[w]," accounted for ",Ascii_perc_single[w],"% of the odd numbered ASCII code or ",Ascii_perc_single[w]*"*")
#Εμφανιζω τα αποτελεσματα
