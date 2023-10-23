#list มีลำดับ 
my_list = [10,20,30,"Hi",True,[20,"Hello"],(10,20),{10,20}]

#Tuple มีลำดับ 
my_tuple = (10,20,10,"Hi",True,(20,"Hello"),[10,20],{"SAU","DTI"})
print()
#set เป็นข้อมูลไม่มีลำดับ ใส่ข้อมูลลงไปไม่เรียงลำดับ
my_set = {10,20,10,"Hi",True}
                        #Key : คือ Index คือตัวชี้ที่อ้างอิงไปทาง Value
                        #Value : คือค่าข้อมูลไปใช้งาน 
#Dictionary มีวงเล็บเหมือนกัน set ข้อมูลประกอบด้วย key : Value / Key --> String / Value --> Everthing
my_dict = {"Name":"สมชาย","Age":20,555:999,"Flag":True}
print(my_dict["Name"])
print(my_dict["Age"]+my_dict[555])

#วิธีเพิ่มข้อมูล
my_dict["Name"] = "สมหญิง"
my_dict["Major"] = "DTI"
print(my_dict)

#เอาข้อมูลออก
my_dict.pop("Name")
my_dict.pop(555)

#เอาข้อมูลตัวสุดท้ายออก
my_dict.popitem()

for data in my_dict : 
    print(data, end=' ')
print()

for data in my_dict.keys () :
    print(data, end=' ')
print()

for data in my_dict.values () : 
    print(data, end=' ')
print ("-----------------------------------------")
my_dict1 = {"A":10,"B":20,"C":30}
my_dict2 = my_dict1
my_dict3 = my_dict1.copy()
print()
print(my_dict2)
print(my_dict3)
my_dict2 ["A"] = 999
my_dict3 ["A"] = 888
print ("-----------------------------------------")
print(my_dict1)
print(my_dict2)
print(my_dict3)