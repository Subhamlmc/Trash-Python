import json
filename=r"C:\Users\Dell\OneDrive\data.json"
username=input("Enter your name and it will be easier to remember for us if you have visited :")
with open (filename,'w') as file :
    json.dump(username,file)
    print(f"You will be remembered soon {username}!")
    
    