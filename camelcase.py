camel = input("camelcase :")
print("snakecase :",end="")

for c in camel:
     if c.isupper():
        print("_" + c.lower(),end="")
       
     else:
           print(c , end="")
           

 
