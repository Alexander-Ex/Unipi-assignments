import tweepy

auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")

api = tweepy.API(auth)
screen_name=input("Give the name of the user") 
stuff =api.user_timeline(screen_name,count= 10,include_rts = True )
#Twitter API

List=[]
y=""
for info in stuff[:]:
    for z in str(info.text):
        if z==" ":
                List.append(y)
                y=""
        else:
            y=y+z
#Παιρνω τα tweets και τα βαζω ολα σε σε μια λίστα

N=len(List)
for i in range(1,N,1):
    for x in range(N-1,i-1,-1):
        if len(List[x])<len(List[x-1]):
            List[x],List[x-1]=List[x-1],List[x]
#Χρησιμοποιω την Bubble Sort για να ταξινομησω την λιστα σε φθινουσα σειρα

Num=["1","2","3","4","5","6","7","8","9","0"]
for w in range(N-1,-1,-1):
    if ("https" in List[w]) or ("#" in List[w]) or ("\\" in List[w]) or ("/" in List[w]) or ("@" in List[w]) or ("\"" in List[w]) or ("\'" in List[w]) or ("_" in List[w]) or ("." in List[w]) or ("," in List[w]) or (":" in List[w]) or ("!" in List[w]) or ("-" in List[w]):
        List.pop(w)
    elif True:
        for y in range(10):
            if Num[y] in List[w]:
                List.pop(w)
#Εδω διατρέχω την λιστα αναποδα για να δω αμα καποιο στοιχειο της λιστα εχει αριθμους ή καποιο special character

print ("The longest words are:",List[-5],List[-4],List[-3],List[-2],List[-1])
print ("The shortest words are:",List[0],List[1],List[2],List[3],List[4])
