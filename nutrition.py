user = input("item:")
print("calories: ",end="")
d = {"apple":130,"banana":110,"chocolate":80}
for k in d:
    if user in[k]:
        print(d[k], end="")
    