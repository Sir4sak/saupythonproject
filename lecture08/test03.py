#OOP
class DtiSau : 
    #data/property member ค่าข้อมูล
    stu_name = ""
    score = 0 
    gpa = 0

    #method member คือการทำงาน (เขียนแบบฟังชั่น เพียงแต่ว่ามันอยู่ใน class เท่านั้นเอง)
    def hiStudent(self) : 
        print("สวัสดี",self.stu_name)

    def ShowScoreAndGrade(self) :
        print("คะแนน",self.score,"ได้เกรด",self.gpa)

#สร้าง object 
obj01 = DtiSau () #ชื่อ class ที่มี () เราเรียกว่าเป็นการสั่งให้ constructor ของ class ที่ทำงาน
obj02 = DtiSau ()

obj01.stu_name = "สมชาย"
obj02.hiStudent ()

obj02.stu_name = "สมหญิง"
obj02.score = 99
obj02.gpa = 3.99