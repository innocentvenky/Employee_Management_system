from emp_1 import*
print("_____________salary update_______________")
print("we are updating single emplotyee salary")
employess[0]["vjiss"]["emp_salary"]=employess[0]["vjiss"]["emp_salary"]+employess[0]["vjiss"]["emp_salary"]*0.10
print(employess)

employe_id=int(input("enter empid:"))
for i in employess:
    if i["vjiss"]["empid"]==employe_id:
        department=input("enter department : ")
        i["vjiss"]["emp_dep"]=department

print("\n\n________________________\n")
print(employess)
               

increment=int(input("enter salary increment for employess:" ))
employess[0]["vjiss"]["emp_salary"]=(employess[0]["vjiss"]["emp_salary"])+increment
print(employess)
