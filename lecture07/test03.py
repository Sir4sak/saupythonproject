#list Medthod 
var1 = [10,20,"Hello",True,[111,"WOW"],"มานะ"]
#append เพิ่ม 1 ข้อมูล
var1.append(555)
var1.append(["Hi","Hey",999])
print(var1)

#extend เพิ่มแต่ละข้อมูล
var1.extend([10,20,30])
print(var1)
#remove
var1.remove ("Hello")
var1.remove(10)
print(var1)
#---------------------------
var2 = [10,20,"Hello"]
#insert 
var2.insert(2,"HI")
print (var2)

#pop
var2.pop()
print(var2) #[10, 20, 'HI', 'Hello']
var2.pop(1)
print(var2)

#count นับจำนวนข้อมูลนั้นๆ ที่ซ้ำที่อยู่ใน list มีกี่ตัว
print(var1.count(10))
var3 = [10,10,20,"Hi",10,"Hi"]
print ("ใน var3 มี 10 ทั้งหมด",var3.count(10),"ตัว")
print ("ใน var3 มี Hi ทั้งหมด",var3.count("Hi"),"ตัว")
print("HI SAU")
#เมธอดต่อไปนี้ใช้ได้เฉพาะข้อมูลที่เป็นประเภทเดียวกันเท่านั้น
#sort
var4 = [10,10,20,"Hi",10,"Hi"]
#var4.short() error
var5 = [500,123,654,243,440,766]
print(var5)
var5.sort()
print(var5)
var5.sort(reverse=True)
print(var5)