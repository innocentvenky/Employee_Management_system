import emp_1
s=dict()
low_att=[s]
high_att=[]
print("\n\n \t \t \t  empid "  " emp_name " " emp_pre_days " " emp_lev_days " )
for x in emp_1.employess:
	print("Employee working details: ",x["vjiss"]["empid"],x["vjiss"]["emp_name"],x["vjiss"]["emp_wor_days"])
	att_chec=(x["vjiss"]["emp_wor_days"]["emp_pre"]/20)*100
	if att_chec<=80:
		low_att.extend([x["vjiss"]["emp_name"],att_chec])
		print("Low attendance")
	else:
		high_att.append([x["vjiss"]["emp_name"],att_chec])	
		print("High attendance")
print("*******************************************")
print("LOW____________ATTENDACE______________ LIST")
print("*******************************************")
for i in low_att:
	print(i)
print("*******************************************")
print("High attendance candidates ",high_att)
	