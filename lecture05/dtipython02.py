#funtion 2 : have parameters / no return 
#parameter คือ ตัวแปล (varible)
def funcA(x,y):
    print ("AAA")
    z = x + y
    print(f" {x} + {y} = {z}")
def funcB(x,y,z):
    print("{:.2f} {:.4f} {:.5f}".format(x,y,z))

funcA(10,10) #ข้อมูลที่ส่งให้ Parameter เรียก Argument
funcA(5,10)
funcB(1,5,10)