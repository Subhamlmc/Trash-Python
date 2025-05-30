#file downloader using python from internet
import requests
url=input("Enter the url of the photo:")
userinput=input("Enter the name of the file you want to save as :")
response=requests.get(url)
with open(fr"C:\Users\Dell\OneDrive\{userinput}.jpeg",'wb') as file :
    file.write(response.content)
    print("Successfully Downloaded!!")