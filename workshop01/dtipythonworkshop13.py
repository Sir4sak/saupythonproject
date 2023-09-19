def InputInfo () : 
    Number = int(input("รหัสนักเรียน : "))
    Name = input("ชื่อนักเรียน : ")
    Grade = float(input("เกรดที่ได้ : "))   
    return Number,Name,Grade
def CalGrade (Number,Name,Grade):
    if Grade >=2 : 
        print("ผ่าน ")
    elif Grade < 2 :
        print("ไม่ผ่าน ")


Number,Name,Grade = InputInfo ()
CalGrade (Number,Name,Grade)