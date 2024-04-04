def main():
  time = input("what time is it ?")
  meal = convert(time)
  if meal >=7 or meal <= 8:
    print("break fast")
  elif meal >=2 or meal <=3:
    print("lunch time")
  elif meal >= 18 or meal <= 19:
    print("dinner time")




def convert(time):
 hours,minutes = time.split(":")
 hours = float(hours) + float(minutes) / 60
 return hours

if __name__=="__main__":
  main()