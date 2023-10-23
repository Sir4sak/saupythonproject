#list Function 
#len()นับจำนวน , min() , max()
var1 = [10,20,"Hello",True,[111,"WOW"],"มานะ"]

var2 = (10,20,"Hello",True,[111,"WOW"],"มานะ")

print ("ใน var1 มีข้อมูลทั้งหมด",len(var1),"ข้อมูล")
print ("ใน var1 มีข้อมูลทั้งหมด",len(var2),"ข้อมูล")
# min กับ max ใช้ไม่ได้กับข้อมูลคนละชนิดกัน 
#print(min(var1)) error เพราะ ตัวอักษร กับตัวเลขปนกัน
#True คือ 1 
#False คือ 0 
var3 = [10,20,30,True,False,10,20]
var4 = (10,20,30,True,10,20)
print(min(var3)) 
print(max(var4))