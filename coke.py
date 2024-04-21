Amount_due = 50
while Amount_due > 0:
 print("Amount Due :50")
 user = int(input("Inser coin :"))

 if user in[25,10,5]:
       Amount_due -=user
       changed_owned = abs(Amount_due)
 print("changed_Owned :",changed_owned)

