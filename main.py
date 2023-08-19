class Employee:
  def __init__(self,emp_id,username,start_date,gender,salary):
    self.emp_id = emp_id
    self.username = username
    self.start_date = start_date
    self.gender = gender
    self.salary = salary

def importemployees():
#references:
# https://www.pythontutorial.net/python-basics/python-read-text-file/)
# https://stackoverflow.com/questions/51977258/appending-data-from-a-text-file-into-a-list-in-python
    employees = []
    with open('employees.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            emp_id, username, start_date, gender, salary = line.strip().split(', ')
            employees.append(Employee(emp_id, username, start_date, gender,salary))
    return employees



login_attempts = 0
admin_correct_username = "admin"
admin_correct_password = "admin123123"
#reference (https://bobbyhadz.com/blog/python-username-password-input-3-attempts)
while login_attempts<5:#runtime= O(n)
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

