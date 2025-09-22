while True: 
    login = input("Enter User Name: ")
   
    while True:
        password = input("Enter password: ")
    
        upper = False
        lower = False
        digit = False
    
        if len(password) < 8:
            print("Enter a strong password again (minimum 8 characters)")
            continue  
    
        for char in password:
            if char.isupper():
                upper = True 
            if char.islower():
                lower = True 
            if char.isdigit():
                digit = True 

        if upper and lower and digit: 
            print("✅ Strong password")
            break
        else: 
            print("❌ Weak password. Please try again:")

            if not upper: 
                print("- Enter at least one uppercase letter")
        
            if not lower: 
                print("- Enter at least one lowercase letter")
        
            if not digit: 
                print("- Enter at least one digit")
    break
