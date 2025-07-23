pin=2025
balance=1000
attemps=0
maxattemp=3
trans=[]

#Login process
while True:
 correct=int(input("Enter your pin:"))

 if pin==correct:
    print("Login is Suceessfully")
    break
    
 else:
    attemps+=1
    print("Your attemps is:",(attemps-maxattemp))  
    if attemps>maxattemp:
        print('Your Atm is blocked thank you!') 
        exit()
        
        
#core functionality
while True:
    print('-----MENU-----')
    print("select 1 is blance:")
    print('select 2 is withdrwal:')
    print("select 3 is deposit")
    print('select 4 is transaction')
    print("select 5 is exit ")  
    

    choice=input("Enter Your Choice:")
    
    if choice=="1":
       print('Your balance is:',balance )
    
    elif choice=="2":
        withd=int(input("Enter your withdrwal amount:"))
        if withd>0 and withd<=balance:
            balance=balance-withd
            trans.append(f"Withdrwal amount is:{withd}")
            if len(trans)>5: 
                 trans.pop(0) 
            print("Your withdrwal successfully, New balance is:",balance)   
        else:
             print("insufficient balance or invalid amount") 
             
                
    elif choice=="3":
        deposit=int(input("Enter your amount:"))
        if deposit>0:
           balance+=deposit
           trans.append(f"Deposit amount is {deposit}")
           if len(trans)>5:
              trans.pop(0)
           print("Your deposit successfully,New balance is:",balance)
        else:
            print("Invalid amount:",deposit)   
            
                
    elif choice=="4":
         print("Transactoins list is:")
         if len(trans)==0:
          print("No transcatoin in last:",trans)
         else:
             for i in trans:
                 print(i)
        
    elif choice=="5":
        print("Thank You Visit Again" )
        break
    else:
        print("invalid option") 
        exit()                       
                             