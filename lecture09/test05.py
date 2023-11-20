#คุณสมบัติเด่น Inheritance สืบทอด คือ การที่ class นึงสืบทอด class นึง *** (re-use)
#สืบทอด มีแม่ (super class) มีลูก (sub class)
#แม่มีอะไร ลูกมีด้วย
#คุณสมบัติ Polymorphism (พ้องร๔ป : พฤติกรรมเดียวแต่วิธีการต่างกัน) คือ การที่คลาสถูกเอา Method Class แม่มาเขียนใหม่
class Sau01 : 
    infoA = 10

    def ShowHi():
        print("Hi......")
class Sau02 (Sau01):
    infoB = 20

    def ShowHey ():
        print("Hey......")
    # overiding method : Polymorphism
    def ShowHi ():
        print("Hi Hi Hi...")

ob1=Sau01()
ob2=Sau02()
ob2.ShowHi()
