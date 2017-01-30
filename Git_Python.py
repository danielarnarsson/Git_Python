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
lagstafir
print("Í þessum texta eru " + hastafir + ", " + lagstafir + " og " + " lágstafir koma strax á eftir hástaf.")
