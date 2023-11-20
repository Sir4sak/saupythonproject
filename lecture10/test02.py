#สร้างไฟล์และเขียนข้อมูลไฟล์
f_dti = open('myfile01.txt','w', encoding='utf-8') #เปิดไฟล์เพื่อเขียนข้อมูลของไฟล์
f_dti.write("wow.... ")
f_dti.write("woo....")
f_dti.write("สวัสดีทุกคน....")

f_dti.close()

print("บันทึกข้อมูลลงไฟล์เรียบร้อย")