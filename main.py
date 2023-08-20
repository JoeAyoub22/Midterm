import itertools
from datetime import datetime
class Employee:
  id_obj = itertools.count(1)
  def __init__(self,employee_id,username,start_date,gender,salary):
    self.employee_id = next(Employee.id_obj)
    self.username = username
    self.start_date = start_date
    self.gender = gender
    self.salary = salary

def import_employees(filename):
#references:
# https://www.pythontutorial.net/python-basics/python-read-text-file/)
# https://stackoverflow.com/questions/51977258/appending-data-from-a-text-file-into-a-list-in-python
    employees = []
    with open('employees.txt', 'r') as file:
        for line in file:
            employee_id, username, start_date, gender, salary = line.strip().split(', ')
            employees.append(Employee(employee_id, username, start_date, gender,int(salary)))
    return employees

def display_stats(employees):
  num_employees = len(employees)
  male_count = 0
  female_count = 0
  for employee in employees:
    gender = employee.gender
    if gender == "male":
      male_count +=1
    else:
      female_count +=1
  male_percentage = (male_count / num_employees) * 100
  female_percentage = (female_count / num_employees) * 100
  print("The number of male employees is: " , male_count)
  print("Percentage of male employees is :" , male_percentage, "%")
  print("The number of female employees is: " , female_count) 
  print("Percentage of female employees is :" , female_percentage, "%")

def add_employee(employees):
#References:
#https://bobbyhadz.com/blog/python-create-incremental-id-in-class
#https://www.geeksforgeeks.org/get-current-date-using-python/
#https://www.programiz.com/python-programming/datetime/current-datetime#:~:text=If%20we%20need%20to%20get,class%20of%20the%20datetime%20module.&text=Here%2C%20we%20have%20used%20datetime,and%20time%20in%20another%20format.
  employee_id = next(Employee.id_obj)
  username = input("Enter employee's username: ")
  gender = input("Enter employee's gender: ")
  salary = int(input("Enter employees's salary: "))
  start_date = datetime.now().strftime("%y/%m/%d")
  employees.append(Employee(employee_id, username, start_date, gender, salary))
  print("Employee has been added")

def display_employees(employees):
#Reference:
#https://www.tutorialspoint.com/How-to-sort-a-Python-date-string-list
#https://stackoverflow.com/questions/29510219/python-list-splitting-sorting-by-date-then-joining
    sorted_employees = sorted(employees, key=lambda x: x.start_date, reverse=True)
    for employee in sorted_employees:
      print("employee_id: ", employee.employee_id, "username: ", employee.username, "start date: ", employee.start_date, "gender: ", employee.gender, "salary: ", employee.salary)

print("Welcome user")
employees = import_employees("employees.txt")
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

      if choice == 1:
        display_stats(employees)
      elif choice == 2:
        add_employee(employees)
      elif choice == 3:
        display_employees(employees)
  menu()




  
  

    

  








