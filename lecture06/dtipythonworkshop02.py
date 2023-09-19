#โปรแกรมตรวจสอบน้ำหนักรถบรรทุกนั้นมีน้ำหนักรถผ่านเกณทฑ์หรือไม่หากน้ำหนักเกิน 1000 Kg ให้แสดงข้อความว่า "รถน้ำหนักไม่ผ่านเกณฑ์" 
#แต่หากน้ำหนักตั้งแต่ 1000 Kg ลงมาให้แสดงข้อความว่า "รถน้ำหนักผ่านเกณฑ์" โดยให้ป้อนทะเบียนรถบรรทุกและน้ำหนักรถบรรทุกทางแป้นพิมพ์

#วิเคราะห์
#มองหา feature การทำงานว่ามีอะไรบ้าง เพื่อไปสร้างเป็น function 
#รับค่าทะเบียนรถ น้ำหนักรถ -> InputCarDetial 
#ตรวจสอบน้ำหนักรถ และ แสดงผล -> checkCarAndShowWeight 

def InputCarDetial():
    CarNo = input ("ป้อนทะเบียนรถ : ")
    CarWeight = float (input("ป้อนน้ำหนักรถ : "))
    return CarNo,CarWeight

def CheckAndShowWeight(CarNo,CarWeight):
    if CarWeight > 1000 : 
        print (f"รถทะเบียน {CarNo} น้ำหนักไม่ผ่านเกณฑ์")
    else: 
        print (f"รถทะเบียน {CarNo} น้ำหนักผ่านเกณฑ์")

print (" ----------------------------------------- ")
print (" -- Truck Checker -- ")
print (" ----------------------------------------- ")

CarNo,CarWeight = InputCarDetial ()
CheckAndShowWeight(CarNo,CarWeight)