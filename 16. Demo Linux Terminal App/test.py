import json


name=input("input a name   ")
with open('users.json', 'r') as file:
    data = json.load(file)
    #print(len(data["users"]))
    x=0
    for i in data["users"]:
        #print(data["users"][x].get("username"))
        if name == data["users"][x].get("username"):
            print("egaa")
            break
        else:
            x=x+1

"""new_user = {
            'id':"aidi",
            'username':"gio".lower(),
            'userpass':"pass",
            'mail':"mail"
        }
data["users"].append(new_user)

with open('users.json', 'w') as file:
    json.dump(data, file, indent=4)"""
