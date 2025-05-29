#making a dictionary from arguements passed

def make_dict(name,place):
    person={'first':name,'place':place}
    print(person)
    

def args_pass():
    name=input("Enter your name :")
    places=input("Enter the place you want to visit :")
    return name,places

make_dict(*args_pass())