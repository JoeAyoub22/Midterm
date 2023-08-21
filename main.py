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
#https://blogboard.io/blog/knowledge/python-sorted-lambda/
    sorted_employees = sorted(employees, key=lambda employee: employee.start_date, reverse=True)
    for employee in sorted_employees:
      print("employee_id: ", employee.employee_id, "username: ", employee.username, "start date: ", employee.start_date, "gender: ", employee.gender, "salary: ", employee.salary)

def change_salary(employees):
  emp_id = input("Enter the id of the employee: ")
  new_salary = int(input("Enter desired salary: "))
  for employee in employees:
    if employee.employee_id == int(emp_id):
      employee.salary = new_salary
      print("New salary inserted")
      return
  print("not an employee")

def remove_employee(employees):
  emp_id = input("Enter the id of the employee: ")
  for employee in employees:
    if employee.employee_id == int(emp_id):
      employees.remove(employee)
      print("employee removed from database")
      return
  print("employee not in database")

def raise_emp_salary(employees):
  emp_id = input("Enter the id of the employee: ")
  raise_percentage = float(input("Enter raise percentage: "))
  for employee in employees:
    if employee.employee_id == int(emp_id):
      employee.salary = int(employee.salary * raise_percentage)
      print("salary raise done")
      return
  print("employee not in database")
      
def save_changes(filename, employees):
#Reference:
#https://www.pythontutorial.net/python-basics/python-write-text-file/
#https://www.geeksforgeeks.org/python-string-concatenation/
    with open(filename, 'w') as f:
        for employee in employees:
          new_employee = "{} {} {} {} {}".format(employee.employee_id, employee.username, employee.start_date, employee.gender, employee.salary)
          f.write(new_employee + '\n')
          print("changes saved")
  
def check_salary(employees):
  print("Your salary is", employee.salary)

print("Welcome user")
employees = import_employees("employees.txt")
login_attempts = 0
max_attempts =5
while login_attempts < max_attempts:
  username = input("Enter your username ")
  password = input("Enter your password ")

  if username == "admin" and password == "admin123123":
    print("welcome admin")
    break
  else:
    print("Incorrect Username and/or Password")
    login_attempts +=1
    
if login_attempts >=5:
  print("Maximum attemps reached you are now locked")

if username == "admin" and password == "admin123123":
  def admin_menu():
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
      choice=int(input("what would you like to do? "))

      if choice == 1:
        display_stats(employees)
      elif choice == 2:
        add_employee(employees)
      elif choice == 3:
        display_employees(employees)
      elif choice == 4:
        change_salary(employees)
      elif choice == 5:
        remove_employee(employees)
      elif choice == 6:
        raise_emp_salary(employees)
      elif choice == 7:
        save_changes('employees.txt', employees)
        break
      else:
        print("not an option select another")
  admin_menu()

else:
  for employee in employees:
    if username == employee.username and password =="":
      if employee.gender == "male":
        print("Hi Mr.", employee.username)
      else:
        print("Hi Ms.", employee.username)
  
  def employee_menu():
    choice=None
    while choice!=2:
      print("employee menu: ")
      print("1. Check my salary")
      print("2. exit")
      choice=int(input("what would you like to do? "))
      if choice == 1:
        check_salary(employees)
      elif choice ==2:
        break
      else:
        print("not an option select another")
  employee_menu()     



    

  








