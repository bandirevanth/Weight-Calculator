print("""
========== Weight Calculator ==========
[1] Calculate
[2] Quit
====================================
""")


user_inp = int(input("Option: "))

while True:
    if user_inp == 1:
        mass_inp = int(input("Mass Amount: "))
        
        if mass_inp == 0:
            print("[ERROR] | Mass can't be none! | Try Again!")
        else:
            answer = mass_inp * 9.8 
            answer = int(answer)
            print(f"Calculated Weight: {answer}kg")
            
    if user_inp == 2:
        break
