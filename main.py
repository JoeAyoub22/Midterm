login_attempts = 0
admin_correct_username = "admin"
admin_correct_password = "admin123123"
#reference (https://bobbyhadz.com/blog/python-username-password-input-3-attempts)
while login_attempts<5:
  Userinputed_username = input("Enter your username ")
  Userinputed_passowrd = input("Enter your password ")

  if Userinputed_username == admin_correct_username and Userinputed_passowrd == admin_correct_password:
    print("welcome admin")
    break
  else:
    print("Incorrect Username and/or Password")
    login_attempts +=1
    if login_attempts >=5:
      print("sorry no more attemps for you")