import time


print("hello")

def diamond_draw():
  for j in range(2):
    for i in range(10):
      print(" ",end=" ")
    for i in range(1):
      if j == 0:
        print("*")
      else:
        print(" ")
        time.sleep(.5)
   
    
  for i in range(3):
    for j in range(10-i):
      if i == 2 and j == 6:
        print("*",end=" ")
      else:
        print(" ",end=" ")
    for k in range(2*i+1):
      print("*",end=" ")
    for l in range(1):
      if i == 2:
        print(" ",end=" ")
    for m in range(1):
      if i == 2:
        print("*",end=" ")
    print()
    time.sleep(.5)
  
    
  for i in range(2):
    for j in range(i+9):
      print(" ",end=" ")
    for j in range(3-(2*i)):
      print("*",end=" ")
    print()
    time.sleep(.5)
  
  for j in range(2):
    for i in range(10):
      print(" ",end=" ")
    for i in range(1):
      if j == 1:
        print("*")
      else: 
        print(" ")
        time.sleep(.5)
  print() 
  time.sleep(1)

def bank():
  bank = 0
  deposit = " " ; withdraw = " "
  order = " " ;print() 
  
  time.sleep(1)
  diamond_draw()
  
  print()
  
  print("        Welcome to DIAMOND BANK!!!.") 
  while order != "q":
    time.sleep(1); print()
    print("$$$ Now your balance is",bank)
    time.sleep(1)
    order = input("what do you want to do\n(w) to withdraw\n(d) to deposit and\n(q) to quit\n >>> ").lower()
    print() ; time.sleep(.5)
    if order == "d":
      deposit = float(input("Deposit: "))
      bank += deposit
      print()
    elif order == "w":
      if bank >= 0.6:
        print("fee 0.5") ; time.sleep(.5)
        withdraw = float(input("Withdraw: "))
        fee = 0.5 
        wf = withdraw + fee
        if bank >= wf:
          bank -= wf
          print()
        elif bank < wf:
          print("Insufficienf balance")
          print()
      else:
        print("Not enough money to withdraw (0.6).")
    elif order == "q":
      print("          Thank you see you again.")
      print()
    else:
      print("Input only d,w,and q,please.")
  diamond_draw()
  print("            $ DIAMOND BANK $")


bank()





    
    