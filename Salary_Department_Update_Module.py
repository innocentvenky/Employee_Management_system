import emp_1 
print("\n\n\n Name:Sucharitha (task)\n\n")
print("________________________________________________________________________________________________")
print("empid\temp_name\temp_age\temp_salary\temp_dep\temp_exp\temp_wor_days")
print("_____________________________________________________________________________________________________")
for i in emp_1.employess:
    print(i["vjiss"]["empid"],"\t",i["vjiss"]["emp_name"],"\t",i["vjiss"]["emp_age"],"\t",i["vjiss"]["emp_salary"],"\t\t",i["vjiss"]["emp_dep"])
employe_id=int(input("enter empid:"))
for i in emp_1. employess:
    if i["vjiss"]["empid"]==employe_id:
        salary=int(input("enter employess salary : "))
        i["vjiss"]["emp_salary"]=salary

print("________________________________________________________________________________________________")
print("empid\temp_name\temp_age\temp_salary\temp_dep\temp_exp\temp_wor_days")
print("_____________________________________________________________________________________________________")
for i in emp_1.employess:
    print(i["vjiss"]["empid"],"\t",i["vjiss"]["emp_name"],"\t",i["vjiss"]["emp_age"],"\t",i["vjiss"]["emp_salary"],"\t\t",i["vjiss"]["emp_dep"])
print("________department update____________________")
employe_id=int(input("enter empid:"))
for i in emp_1.employess:
    if i["vjiss"]["empid"]==employe_id:
        department=input("enter department : ")
        i["vjiss"]["emp_dep"]=department
print("________________________________________________________________________________________________")
print("empid\temp_name\temp_age\temp_salary\temp_dep\temp_exp\temp_wor_days")
print("_____________________________________________________________________________________________________")
for i in emp_1.employess:
    print(i["vjiss"]["empid"],"\t",i["vjiss"]["emp_name"],"\t",i["vjiss"]["emp_age"],"\t",i["vjiss"]["emp_salary"],"\t\t",i["vjiss"]["emp_dep"])
  
print(i["vjiss"]["emp_salary"])     
print("______________salary increment________________")
emp_id=int(input("enter empid: "))
for z in emp_1.employess:
    if (z["vjiss"]["empid"])==emp_id:
        salary_1=int(input("enter salary increment: "))
        z["vjiss"]["emp_salary"] += salary_1
#i["vjiss"]["emp_salary"] += salary
print("________________________________________________________________________________________________")
print("empid\temp_name\temp_age\temp_salary\temp_dep\temp_exp\temp_wor_days")
print("_____________________________________________________________________________________________________")
for i in emp_1.employess:
    print(i["vjiss"]["empid"],"\t",i["vjiss"]["emp_name"],"\t",i["vjiss"]["emp_age"],"\t",i["vjiss"]["emp_salary"],"\t\t",i["vjiss"]["emp_dep"])

print("\n Generate department-wise employee reports \n")
dept_name=input("enter the dept_name : ")
depts=[]
for i in emp_1.employess:
    if i["vjiss"]["emp_dep"] == dept_name:
        dept=i
        depts.append(dept)

print("________________________________________________________________________________________________")
print("empid\temp_name\temp_age\temp_salary\temp_dep\temp_exp\temp_wor_days")
print("_____________________________________________________________________________________________________")
for i in depts:
    print(i["vjiss"]["empid"],"\t",i["vjiss"]["emp_name"],"\t",i["vjiss"]["emp_age"],"\t",i["vjiss"]["emp_salary"],"\t\t",i["vjiss"]["emp_dep"])


		

    




