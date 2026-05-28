import emp_1

print("EMPLOYEE SEARCH MANAGEMENT SYSTEM")

while True:

    print("\n1.Search by Employee ID")
    print("2.Search by Employee Name")
    print("3.Search by Department")
    print("4.Search by Salary Range")
    print("5.Search using Logical Operators")
    print("6.Exit")

    choice = int(input("Enter Choice : "))
    if choice == 1:

        emp_id = int(input("Enter Employee ID : "))

        for i in emp_1.employess:

            emp = i["vjiss"]

            if emp["empid"] == emp_id:

                print("\nSEARCH RESULT")
                print("Employee ID :", emp["empid"])
                print("Employee Name :", emp["emp_name"])
                print("Employee Age :", emp["emp_age"])
                print("Employee Salary :", emp["emp_salary"])
                print("Employee Department :", emp["emp_dep"])

    elif choice == 2:

        name = input("Enter Employee Name : ")

        for i in emp_1.employess:

            emp = i["vjiss"]

            if emp["emp_name"].lower() == name.lower():

                print("\nSEARCH RESULT")
                print("Employee ID :", emp["empid"])
                print("Employee Name :", emp["emp_name"])
                print("Employee Age :", emp["emp_age"])
                print("Employee Salary :", emp["emp_salary"])
                print("Employee Department :", emp["emp_dep"])

    elif choice == 3:

        dep = input("Enter Department : ")

        for i in emp_1.employess:

            emp = i["vjiss"]

            if emp["emp_dep"].lower() == dep.lower():

                print("\nSEARCH RESULT")
                print("Employee ID :", emp["empid"])
                print("Employee Name :", emp["emp_name"])
                print("Employee Age :", emp["emp_age"])
                print("Employee Salary :", emp["emp_salary"])
                print("Employee Department :", emp["emp_dep"])

    elif choice == 4:

        min_salary = int(input("Enter Minimum Salary : "))
        max_salary = int(input("Enter Maximum Salary : "))

        for i in emp_1.employess:

            emp = i["vjiss"]

            if emp["emp_salary"] >= min_salary and emp["emp_salary"] <= max_salary:

                print("\nSEARCH RESULT")
                print("Employee ID :", emp["empid"])
                print("Employee Name :", emp["emp_name"])
                print("Employee Age :", emp["emp_age"])
                print("Employee Salary :", emp["emp_salary"])
                print("Employee Department :", emp["emp_dep"])

    elif choice == 5:

        dep = input("Enter Department : ")
        salary = int(input("Enter Minimum Salary : "))

        for i in emp_1.employess:

            emp = i["vjiss"]

            if emp["emp_dep"].lower() == dep.lower() and emp["emp_salary"] >= salary:

                print("\nSEARCH RESULT")
                print("Employee ID :", emp["empid"])
                print("Employee Name :", emp["emp_name"])
                print("Employee Age :", emp["emp_age"])
                print("Employee Salary :", emp["emp_salary"])
                print("Employee Department :", emp["emp_dep"])

    elif choice == 6:

        print("\nProgram Closed")
        break

    else:

        print("\nInvalid Choice")