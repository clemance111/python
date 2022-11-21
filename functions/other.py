#temp = {}
#temp['name']="clara"
#temp={"name":"clara"}
#print(temp)
#print(temp.values())
i=0
database = {}
list_data = []
while i<2:
    username=input("Enter your username:")
    database["username"] = username
    Email=input("Enter your Email:")
    database["Email"] = Email
    password=input("Enter your password:")
    database["password"] = password

    list_data.append(database)
    i +=1
print(list_data)
print(database.values())
