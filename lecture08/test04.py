#self เปรียบเสมือนสิ่งที่ใช้แทน class ตัวเองเพื่อสามารถเรียกใช้ member ใน class ตัวเองได้
class Test04 : 
    data1 = 10 
    #constuctor 
    def __init__(self,data2,data3) :
        print ("HI....")
        self.data1 = data2
        self.data3 = data3
    # method member
    def showSumData (self):
        print (self.data1 + self.data2 + self.data3)
        self.showWow ()
    def showWow(self):
        print("Wow Wow Wow ")

objA = Test04(20,30)
objB = Test04(10,20)
objC = Test04(20,100)