employess=[{"vjiss":{"empid" : 111, "emp_name":"Rakesh","emp_age":25,"emp_salary":90000,"emp_dep":"Devloper","emp_exp":3,"emp_wor_days":{"emp_pre":17,"emp_lev":3}
}},
{"vjiss":{"empid" :222, "emp_name":"Reehan","emp_age":25,"emp_salary":90000,"emp_dep":"Testing","emp_exp":2,"emp_wor_days":{"emp_pre":16,"emp_lev":4}
{"vjiss":{"empid" :222, "emp_name":"Sucharitha","emp_age":25,"emp_salary":90000,"emp_dep":"Testing","emp_exp":2,"emp_wor_days":{"emp_pre":16,"emp_lev":4}
}},
{"vjiss":{"empid" : 333,"emp_name":"charan","emp_age":23,"emp_salary":70000,"emp_dep":"Backend","emp_exp":1,"emp_wor_days":{"emp_pre":16,"emp_lev":4}
}},
{"vjiss":{"empid" : 444,"emp_name":"Gowtham","emp_age":27,"emp_salary":90000,"emp_dep":"Testing","emp_exp":2,"emp_wor_days":{"emp_pre":20,"emp_lev":0}
}},
{"vjiss":{"empid" : 555,"emp_name":"Manchu","emp_age":17,"emp_salary":60000,"emp_dep":"Fullstack","emp_exp":3,"emp_wor_days":{"emp_pre":19,"emp_lev":1}
}}
]
print("\n\n_________Creating Employee Registration Module (Rakesh) _______ \n\n")
print("________________________________________________________________________________________________________________________________________")
print(" emp_id \t emp_name \t \temp_dept \t\t emp_salary \t\t emp_wor_days \t\t \temp_age \t")
print("_________________________________________________________________________________________________________________________________________")
for i in employess:
	print(i["vjiss"]["empid"], "\t" , "\t", i["vjiss"]["emp_name"],"\t",  "\t", i["vjiss"]["emp_dep"], "\t", "\t", i["vjiss"]["emp_salary"], "\t", "\t", i["vjiss"]["emp_wor_days"], "\t","\t",i["vjiss"]["emp_age"] ,"\t")
print("\n\n Employee is eligible to work or not \n\n")

print("____________________________________________________________________________________________________________________")
print("Employee eligibility \t\t\t\t emp_name \t\t emp_id\t")
print("____________________________________________________________________________________________________________________")
for i in employess:	
	if i["vjiss"]["emp_age"]>=18:
		print("Employee  eligible for work \t\t\t",i["vjiss"]["emp_name"], "\t\t",i["vjiss"]["empid"])
	else:
		print("Employee not eligible for work \t\t\t",i["vjiss"]["emp_name"], "\t\t",i["vjiss"]["empid"])
print("\n\n---------end---------\n\n")

