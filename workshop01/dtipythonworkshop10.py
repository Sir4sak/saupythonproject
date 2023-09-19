def InputInfo ():
    yearclass = int(input("ป้อนชั้นปีนักศึกษา : "))
    return yearclass

def Calyearclass (yearclass):
    if yearclass ==1 :
        print ("Welcome Freshman")
    if yearclass ==2:
        print ("Welcome Sophomore")
    if yearclass ==3 :
        print ("Welcome Junior")
    if yearclass ==4 :
        print ("Welcome Senior")    

yearclass = InputInfo ()    
Calyearclass (yearclass)