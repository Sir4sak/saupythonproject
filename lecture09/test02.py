class DtiTest03 : 
    #data
    infoA = 10 

    # constructure จะเป็นทำให้ Object ที่สร้างจากตลาสเดียวกันไม่จำเป็นต้องเหมือนกัน
    # constructure จะทำงานทุกครั้งที่สร้าง object 
    def __init__ (self,infoB,infoC): 
     self.infoB = infoB
     self.infoC = infoC
     print("WOWOWWOWOOW")
    #method
    def showMixAndInfo(self,mix) :
        print(self.infoA + self.infoB + self.infoC + mix)

    #สร้าง object
sau1 = DtiTest03(20,30)
sau2 = DtiTest03(10,100)
sau3 = DtiTest03(20,30)
