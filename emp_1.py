employess=[{"vjiss":{"empid" : 111, "emp_name":"Rakesh","emp_age":25,"emp_salary":100000,"emp_dep":"Devloper","emp_exp":3,"emp_wor_days":{"emp_pre":17,"emp_lev":3}
}},
{"vjiss":{"empid" :222, "emp_name":"Ram","emp_age":25,"emp_salary":90000,"emp_dep":"Testing","emp_exp":2,"emp_wor_days":{"emp_pre":16,"emp_lev":4}
}},
{"vjiss":{"empid" : 333,"emp_name":"charan","emp_age":23,"emp_salary":70000,"emp_dep":"Backend","emp_exp":1,"emp_wor_days":{"emp_pre":16,"emp_lev":4}
}},
{"vjiss":{"empid" : 444,"emp_name":"Gowtham","emp_age":27,"emp_salary":90000,"emp_dep":"Testing","emp_exp":2,"emp_wor_days":{"emp_pre":20,"emp_lev":0}
}},
{"vjiss":{"empid" : 555,"emp_name":"Manchu","emp_age":17,"emp_salary":60000,"emp_dep":"Fullstack","emp_exp":3,"emp_wor_days":{"emp_pre":19,"emp_lev":1}
}}
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
