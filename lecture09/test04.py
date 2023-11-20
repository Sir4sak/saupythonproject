#คุณสมบัติ Encapsulation (ห่อหุ้ม)
class Dtitest05 : 
    #data
    infoA = 10 #ไม่ได้ห่อหุ้ม
    __infoB = 20 #ห่อหุ้ม

    def __init__(self,infoC,infoD) :
        self.infoC = infoC  #ไม่ได้ Encap
        self.__infoD = infoD #Encap ดูจาก __???? เป็นการกำหนด access_modifier เป็น private 
        #เมื่อใดก็ตาม Encap จะต้องมี Method 2 ตัวนี้เสมอคือ get, set ของ Data ตัวนั้น
    def setInfoB(self,infoB): #กำหนดให้กับ Data
        self.__infoB = infoB

    def getInfoB(self): #เอาค่า Data ไปใช้ 
        return self.__infoB
    
    def setInfoD(self,infoD):
        self.__infoD = infoD

    def getInfoD(self):
        return self._infoD
    def showInfo(self):
        print(self.infoA, end='')
        print(self.__infoB, end='')
        print(self.infoC, end='')
        print(self.__infoD, end='')
        print("----------------------")

ob1 = Dtitest05(30,40)
ob2 = Dtitest05(30,100)
ob1.showInfo() # 10 20 30 40
ob1.infoA = 555
ob1.setInfoB(999)
ob1.showInfo() #444 999 30 40

print(ob1.getInfoB()+ob1.getInfoD())