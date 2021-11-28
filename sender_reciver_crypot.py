import Blockchain
usernames=[]
User_new="user1","user2","user3","user4","USERn"

users={
    "user":User_new,
}

for x in users.get("user"):
    print(x)
    usernames.append(x)

while True:
    User_name=input("Enter your name:") 
    User_id=input("Who you want send:")
    Amount=float(input("Enter amount:"))
    if User_name not in usernames:
        print("pls enter  user name in above list") 
    else:
        T=User_id+str(Amount)
        print(f'{User_name } send {User_id} {Amount} Rcb')
        Blockchain.hash(T)
        Blockchain.wallet(User_id,Amount)



