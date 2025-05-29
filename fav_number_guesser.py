import json
filename=input("Enter the filename you want to save as :")
favouritenumber=int(input("Enter your favorite number :"))
words=(f"{filename}'s favourite number is {favouritenumber}")
with open (fr"C:\Users\Dell\OneDrive\{filename}.json","w") as file :
    json.dump(words,file)
    
    