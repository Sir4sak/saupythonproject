number = input ("ป้อนรหัสพนันงาน : ")
name = input ("ป้อนชื่อพนักงาน : ")
salary = float(input("ป้อนเงินเดือนพนักงาน : "))

#เงินเดือนสุทธิ = เงินเดือนปกติ - เงินเดือนที่โดนหักไปแล้ว7% - ค่าดอกเบี้ย
net_salary = (salary) - ((salary)*7/100) - 500

#เพิ่มทศนิยม 2 ตำแหน่ง
net_salary_2 = format (float(net_salary),".2f")


print (f"จะได้เงินเดือนสุทธิ {net_salary_2} บาท ")
print ("จะได้เงินเดือนสุทธิ",net_salary_2,"บาท")
print ("จะได้เงินเดือนสุทธิ "+str(net_salary_2)+" บาท")
print ("จะได้เงินเดือนสุทธิ {} บาท ".format(net_salary_2))
