
def country_list(name,city):
    list={'name':name,'city':city}
    print(*list)


def get_list():
    name=input("Enter your name :")
    city=input("Enter your city ")
    return name,city
     

country_list(*get_list())