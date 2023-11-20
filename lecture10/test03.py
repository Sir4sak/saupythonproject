#เขียนข้อมูลไฟล์
f_dti = open('myfile01.txt','w', encoding='utf-8') #เปิดไฟล์เพื่อเขียนข้อมูลของไฟล์
f_dti.write("wow\n ")
f_dti.write("wuuu\n ")
f_dti.write("สวัสดี\n ")
f_dti.close()

print("บันทึกข้อมูลลงไฟล์เรียบร้อย")