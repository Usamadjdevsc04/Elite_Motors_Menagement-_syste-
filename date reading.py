import csv
from datetime import datetime
import pandas as pd
from prettytable import PrettyTable
from prettytable import from_csv


class Human:
    all = []

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Human.all.append(self)


class employee(Human):
    def __init__(self, designation: str, joining_date, department: str, employee_no: int, phone_number: int):
        self.designation = designation
        self.joining_date = joining_date
        self.department = department
        self.employee_no = employee_no
        self.phone_number = phone_number
        employee.all.append(self)


class assets(Human):

    def __init__(self, name, age, designation, joining_date, department, employee_no, phone_number, assets):
        self.name = name
        self.age = age
        self.designation = designation
        self.joining_date = joining_date
        self.department = department
        self.employee_no = employee_no
        self.phone_number = phone_number
        self.assets = assets
        assets.all_.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        with open('syncclouds.csv', 'a', newline="") as csvfile:
            fieldnames = ["name", "age", "designation", "joining_date", "department", "employee_no", "phone_number",
                          "assets"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            while True:
                name = input("Enter the employee name : ")
                age = input("Enter age  :")
                designation = input("Enter the designation: ")
                joining_date = input("Enter the joining date: ")
                department = input("Enter the department  : ")
                employee_no = input("Enter the employee no : ")
                phone_number = input("Enter the phone number  : ")
                assets = input("Enter the assets  : ")
                with open("syncclouds.csv") as f:
                    reader = csv.reader(f)
                    header = next(reader)
                if header == "":
                    writer.writeheader()
                writer.writerow(
                    {"assets": assets, "name": name, "age": age, "designation": designation, "joining_date": joining_date,
                     "department": department, "employee_no": employee_no, "phone_number": phone_number})
                want = input("Do you want more employees Y/N")
                if want == "n":
                    break


assets.instantiate_from_csv()

with open('syncclouds.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)


class attendance(employee):
    def __init__(self, employee_no, date, day, time_in, time_out, break_in, break_out):
        self.employee_no = employee_no
        self.date = date
        self.day = day
        self.time_in = time_in
        self.time_out = time_out
        self.break_in = break_in
        self.break_out = break_out
        attendance.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        with open('attendance.csv', 'a', newline="") as csvfile:
            fieldnames = ["employee_no", "time_in", "time_out", "breakin", "breakout"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            while True:
                employee_no = input("enter employee_no")
                time_in = input("enter the time of entering the office : ")
                time_out = input("enter the time of leaving the office : ")
                break_in = input("enter the time for entering the office after break : ")
                break_out = input("enter the time of leaving the office for break : ")
                with open("attendance.csv") as file:
                    reader = csv.reader(file)
                    header = (reader)
                if header == "":
                    writer.writeheader()
                writer.writerow(
                    {"employee_no": employee_no, "time_in": time_in, "time_out": time_out, "breakin": break_in,
                     "breakout": break_out})
                break

            timein = print("entry time : ", time_in)
            timeout = print("time to exit: ", time_out)
            breakout = print("time to exit from break: ", break_out)
            breakin = print("time to leave for break:", break_in)
attendance.instantiate_from_csv()

e=int(input("enter the employee_no"))
data = pd.read_csv("syncclouds.csv", index_col="employee_no")
first = data.loc[e]
print(first)
mytable=PrettyTable(["name","age","designation","joining_date","department","employee_no","phone_number","assets"])
mytable.add_row(["usama","25","developer","25-12-2022","programming","sc_04","03355571414","no assets"])
mytable.add_row(["Ali","22","developer","01-01-2023","programming","sc_14","03125439569","no assets"])
mytable.add_row(["jawad","23","developer","28-12-2022","programming","sc_10","03215897145","no assets"])
print(mytable)













