try :
    num1 = int(input("Input Number1  = "))
    num2 = int(input("Input Number2  = "))

    result1 = num1 * num2
    result2 = num1 / num2

    print(num1,"x",num2,"=",result1)
    print(num1,"x",num2,"=",result2)
except ValueError :
    print("ตรวจสอบการป้อนข้อมูลเนื่องจากป้อนข้อมูลไม่ถูกต้อง")
except ZeroDivisionError : 
    print("ตรวจสอบการป้อมข้อมูลตัวเลขตัวที่สองห้ามเป็น 0 ")
except Exception : 
    print("ติดต่อหมา ")
finally :
    print ("WOw WoW WOW")