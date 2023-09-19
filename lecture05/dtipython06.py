#คำสั่ง return ที่ไม่มีอะไรต่อท้าย หมายถึง เป็นการบ่งบอกการทำงานนั้นๆ ว่าเสร็จแล้ว
def example ():
    print (111)
    print (222)
    return 
    print (333)
    print (444)
    return



#Default Parameter 
def dtitest (x,y,z,a) :
    print (f"{x} + {y} + {z} + {a} = {x+y+z+a}")

dtitest (5,100)

dtitest (9,8,10)