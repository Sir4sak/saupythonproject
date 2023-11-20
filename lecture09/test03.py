#Destructor

class Dtitest04 : 
    data1 = 10 

    def __init__(self,data2) :
        self.data2 = data2
        print ("HI....")

    def doTask1(self):
        print("T_T")

    def doTask2(self,value):
        print(value)

    def __del__(self):
        print("Bye Bye........")

def showHey():
    print("Hey.........")
#----------------------------------------
sauA = Dtitest04 (20)
sauB = Dtitest04 (30)
sauC = Dtitest04 (20)

sauC.doTask2(":>")
sauC.doTask1()
print(sauA.data1 + sauB.data1)        