user = input("Input :")
print("Output : ",end=" ")

for c in user:
    if not c.lower() in ["a","i","o","e","u"]:
     print(c,end="")
