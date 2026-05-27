import emp_1
attend=[{}]
print("EMPLOYEE ID_____EMPLOYEE NAME____ATTENDANCE")
for i in emp_1.employess:
	attend=i["vjiss"]["emp_wor_days"]["emp_pre"]/20*100
	print(i["vjiss"]["empid"],"\t" ,"\t",i["vjiss"]["emp_name"],"\t",attend)
for i in emp_1.employess:
	print("Employee working details: ",i["vjiss"]["emp_wor_days"])

