d={1:['Motichur Ladoo','₹500',500],2:['Kaju katli','₹900',900],3:['Besan ke ladoo','₹800',800],4:['Peda','₹400',400],
   5:['Modak','₹700',700]}
bill=0
for i in d:
    print(i,"::",d[i][0],d[i][1])
order=[]
ch=input("Do you want to order (YES/NO) : ")
while ch.lower()=='yes':
    n=int(input("What do you want yo order : "))
    if n in d.keys():
        order.append(n)
    else:
        print("Invalid Choice")
    ch=input("Do you want to order : ")
print('🥳'*50)
print(" "*30,end='')
print("ALCODERS SWEET SHOP PVT LTD")
print('🥳'*50)
print("You have ordered : ")
for i in order:
    print(d[i][0])
    bill+=d[i][2]
print("The total bill is : ",bill)
print('*'*50)
    

