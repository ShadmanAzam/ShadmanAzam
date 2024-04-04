expression = input("Expression : ")
x,y,z = expression.split(" ")

x = int(x) 
y = ["+","-","/","*"]
z = int(z)

if "+"  in expression:
  print(x + z)
elif "-" in expression:
  print(x - z)
elif "/" in expression:
  print(x / z)
elif "*" in expression:
  print(x * z)