employess=[{"vjiss":{"empid" : 111, "emp_name":"Rakesh","emp_age":25,"emp_salary":100000,"emp_dep":"Devloper"}},
{"vjiss":{"empid" :222, "emp_name":"Ram","emp_age":25,"emp_salary":90000,"emp_dep":"Testing"}},
{"vjiss":{"empid" : 333,"emp_name":"charan","emp_age":23,"emp_salary":70000,"emp_dep":"Backend"}},
{"vjiss":{"empid" : 444,"emp_name":"Gowtham","emp_age":27,"emp_salary":90000,"emp_dep":"Testing"}},
{"vjiss":{"empid" : 555,"emp_name":"Manchu","emp_age":17,"emp_salary":60000,"emp_dep":"Fullstack"}}
]
print("\n\n_________Creating Employee Registration Module (Rakesh) _______ \n\n")
for i in employess:
	print(i)
print("\n\n Employee is eligible to work or not \n\n")

for i in employess:	
	if i["vjiss"]["emp_age"]>=18:
		print("They are eligible for work ")
	else:
		print(" not eligible for work")
print("\n\n---------end---------\n")
