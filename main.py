print("Welcome user")
login_attempts = 0
admin_correct_username = "admin"
admin_correct_password = "admin123123"

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
  print("Maximum attemps reached you are now locked")

while Userinputed_username == "admin" and Userinputed_passowrd == "admin123123":
  def menu():
    choice=None
    while choice!=7:
      print("Admin Menu:")
      print("1. Display Statistics")
      print("2. Add an Employee")
      print("3. Display all Employees")
      print("4. Change Employee's Salary")
      print("5. Remove Employee")
      print("6. Raise Employee's Salary")
      print("7. Exit")
      choice=int(input())
  menu()



class Employee:
  def __init__(self,employee_id,username,start_date,gender,salary):
    self.emp_id = employee_id
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
            employee_id, username, start_date, gender, salary = line.strip().split(', ')
            employees.append(Employee(employee_id, username, start_date, gender,int(salary)))
    return employees





  
  

    

  








