import emp_1
import copy
import random

print("\n\n__________________________ UPDATED LIST AFTER RESIGNING _____________________________\n\n")

emp2 = copy.deepcopy(emp_1.employess)
emp3 = copy.deepcopy(emp_1.employess)

emp2.pop(3)
emp2.pop(1)

emp3.pop(4)
emp3.pop(2)
emp3.pop(0)
print("EMPID", "\t", "NAME", "\t", "DEPARTMENT", "\t", "SALARY")
print("-" * 60)
for i in emp2:
        print(i["vjiss"]["empid"], "\t", i["vjiss"]["emp_name"], "\t", i["vjiss"]["emp_dep"], "\t", i["vjiss"]["emp_salary"])

print("\n\n______________________________DISPLAY ACTIVE EMPLOYEES_______________________________\n\n")
print("EMPID", "\t", "NAME", "\t", "DEPARTMENT", "\t", "SALARY")
print("-" * 60)
for i in emp2:
	print(i["vjiss"]["empid"], "\t", i["vjiss"]["emp_name"], "\t", i["vjiss"]["emp_dep"], "\t", i["vjiss"]["emp_salary"])

print("\n\n_____________________________________RESIGNED EMPLOYEES________________________________\n\n")
print("EMPID", "\t", "NAME\t", "\t", "DEPARTMENT\t", "\t\t", "\tSALARY")
print("-" * 60)
for i in emp3:
	print(i["vjiss"]["empid"], "\t", i["vjiss"]["emp_name"],"\t\t", i["vjiss"]["emp_dep"], "\t\t", i["vjiss"]["emp_salary"])
