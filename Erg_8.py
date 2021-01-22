from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def calculations (name):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        "symbol":name
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': "",
    }
    
    session = Session()
    session.headers.update(headers)

    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      parseData = json.dumps(response.json())
      eth0bj = json.loads(parseData)
      y=(eth0bj["data"][name]["quote"]["USD"]["price"])
      return (y)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
#Αυτο ειναι το  API ο οποιο το εβαλα μεσα σε ενα function


cryptoName=[]
cryptoQuan=[]
cryptoSum=[]
#Αυτες ειναι οι λιστες που θα κρατησουν τις τελικες τιμες

x=input("Give the name of the file")
f = open(x,"r")
a=f.read()
abc=""
List=[]
f.close()
#Αυτη ειναι η προχειρη λιστα στην οποια θα επεξεργαστω τα δεδομενα

for b in range(len(a)):
    if (a[b]==" ") or  (a[b]==":") or (a[b]==",") or (a[b]=="{") or (a[b]=="}") or (a[b]=="\""):
        List.append(abc)
        abc=""
    else:
        abc=abc+a[b]
#Εδω ξεχωριζω τα δεδομενα
      
N=len(List)-1
for x in range(N,-1,-1):
    if (List[x]==""):
        List.pop(x)
#Εδω καθαριζω τη λιστα απο μερικα κενα που δημιουργηθηκαν λογω του τροπου ξεχωρισμου

N=len(List)-1
for i in range(len(List)):
    if i%2==0:
        name=str(List[i])
        cryptoName.append(name)
    else:
        q=List[i]
        q=int(q)
        cryptoQuan.append(q)
#Εδω xωριζω τα δεδομενα στις τελικες λιστες

for z in range(len(cryptoName)):
    Sum=calculations(cryptoName[z])
    total_sum=Sum*cryptoQuan[z]
    cryptoSum.append(total_sum)
#Εβαλα το ΑΡΙ σε ενα function για να το καλεσω οποτε το χρειαστω
    
for c in range(len(cryptoName)):
    print ("The amount of ",cryptoName[c],"you have is ",cryptoQuan[c],"and your total ammount in dollars is: ",cryptoSum[c],"$")
#Εμφανιζω τα αποτελεσματα στον χρήστη

