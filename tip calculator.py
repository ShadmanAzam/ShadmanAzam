def main():
 dollars = dollars_to_float(input("how much was the meal ?"))
 percent = percent_to_float(input("what percent would like to tip ?"))
 tip = dollars * percent
 print(f"leave {tip:.2f}")

def dollars_to_float(d):
 return float (d.replace("$"," "))

def percent_to_float(p):
   s = (p.replace("%",""))
            
   return float (s) / 100

main()