#variable 
score = 5456  
stu_name = "สมชาย"
flag = True
# -------------------------------------

#list............แก้ไขได้
                             #0   1
    #   0   1     2     3      4        5    
var1 = [10,20,"Hello",True,[111,"WOW"],"มานะ"]
    #  -6  -5   -4     -3      -2        -1
    #                        -2 -1
print(var1[0] + var1[1])
print(var1[-6]+var1[-5])
print(var1[0]+var1[4][0])
print(var1[-6]+var1[2][3])
#Tuple.........แก้ไขไม่ได้
                             #0   1
    #   0   1     2      3     4         5  
var2 = (10,20,"Hello",True,[111,"WOW"],"มานะ")
    #  -6  -5   -4     -3      -2        -1
    #                        -2 -1
print(var2(0)+var2(1))
print(var2(-6)+var2(1))