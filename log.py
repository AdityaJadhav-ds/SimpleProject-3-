
while True : 
    login = input("Enter User Name: ")
   
    while True :
        password = input("Enter password : ")
    
        upper = False
        lower = False
        digit = False
    
    
        if len(password) < 8 :
         print("Enter the Strong password again minimum 8 character")
         continue  
    
        for i in password :
            if i.isupper(): 
                upper = True 
            if i.islower(): 
                lower = True 
            if i.isdigit(): 
                digit = True 

        if upper and lower and digit : 
            print("strong password")
            break

        else : 
            print(" enter Strong pass again ")

            if not upper : 
              print(" print atleat one upper ")
        
            if not lower : 
              print(" print atleat one lower ")
        
            if not digit : 
              print(" add atleat one digit ")
    break    
