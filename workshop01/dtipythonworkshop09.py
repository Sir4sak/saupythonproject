def InputInfo ():
    Number = int(input("รหัสพนักงาน : "))
    Name = str(input("ฃื่อพนักงาน : "))
    AmountOfMoney = float(input("จำนวนเงิน : "))
    return Number,Name,AmountOfMoney

def CalPercent (AmountOfMoney) :
    if AmountOfMoney <=1000 :
        print ("ค่าคอมมิฃั่น 0% ")
    elif AmountOfMoney >=1001 and AmountOfMoney <=2000:
        print ("ค่าคอมมิฃั่น 1% ")
    elif AmountOfMoney >=2001 and AmountOfMoney <=3000:
        print ("ค่าคอมมิฃั่น 3% ")
    elif AmountOfMoney >=3001 :
        print ("ค่าคอมมิฃั่น 5% ")

Number,Name,AmountOfMoney = InputInfo ()
CalPercent(AmountOfMoney)