def list(y):
    print(y)


def get_name():
    flag=True 
    while flag :
        selection={}
        name=input("Enter your name :")
        city=input("Enter the name of city you want to visit :")
        selection[name]=city
        userask=input("Do you wish to continue(y/n)?")
        if userask=='n':
            flag=False
            
        else :
         return selection
     
list(get_name())