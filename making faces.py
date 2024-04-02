def main():
 user =input("")

 print(convert(user))

def convert(emoji):
  emoji1 = emoji.replace(":)","😁")
  emoji2 = emoji1.replace(":(","👹")

  return emoji2

main()