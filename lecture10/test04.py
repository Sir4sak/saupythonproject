#เขียนข้อมูลลงไฟล์
#เปิดไฟล์เพื่อเขียนข้อมูลลงไฟล์
f_dti  = open("myfile03.txt","a",encoding='utf-8') #เปิดข้อมูลไฟล์เพื่อเขียนข้อมูลลงไฟล์
f_dti.write("สวัสดี\n")

f_dti.close()
print("บันทึกข้อมูลลงไฟล์เรียบร้อย...")