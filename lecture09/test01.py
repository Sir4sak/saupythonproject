class Dtitest01 : 
    pass
class DtiTest02 :
    #data#attributre/property/fleid คือ ส่วนแแบ่งประเภทหนึ่ง
    infoA = ""
    infoB = 20

    #method คือ ฟังชั่นประเภทหนึ่ง

    def ShowHi(self) :
        print ("HI")

    def ShowInfoAandB (self) :
        print(self.infoA)
        print(self.infoB)
    #สร้าง object 
obA = DtiTest02()
obB = DtiTest02()
sombat = DtiTest02()

obA.infoA = "XXXX"
obB.infoB = 100
print(obA.infoB + obB.infoB)
sombat.ShowInfoAandB