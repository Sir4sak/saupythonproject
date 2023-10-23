#Slicing data in list and Tuple 

    #   0   1     2     3      4        5    
var1 = [10,20,"Hello",True,[111,"WOW"],"มานะ"]

var2 = (10,20,"Hello",True,[111,"WOW"],"มานะ")

# 20,"Hello",True
print(var1[1:4]) #ได้ index 1-3 
# True,(111,"WOW")
print(var2[3:5])
# 10,20,"Hello"
print(var1[:3])
# "Hello",True,[111,"WOW"],"นานะ"
print(var1[2:])