
#Daemi 1
tala1=int(input("Sláðu inn tölu "))
tala2=int(input("Sláðu inn aðra tölu "))
samlagning=tala1+tala2
print("Tölurnar lagðar saman: ", samlagning)
margfoldun=tala1*tala2
print("Tölurnar margfaldaðar saman: ", margfoldun)

#Daemi 2
fornafn=input("Fornafn? ")
eftirnafn=input("Eftirnafn: ")
print("Halló " + fornafn +" "+ eftirnafn)

#Daemi 3
text=input("Sláðu inn texta. ")
hastafir=sum(1 for c in text if c.isupper())
lagstafir=sum(1 for c in text if c.islower())
'''
count=0
lageftirha=text.isupper() and text.islower() in text.char(2)
for lageftirha in text:
    count=count+1
print(count)
'''
print("Í þessum texta eru ", hastafir, " hastafir, ", lagstafir, " lágstafir og... ",)
