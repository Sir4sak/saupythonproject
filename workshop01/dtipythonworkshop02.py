def InputInfo ():
    Name = input ("ชื่อนักเรียก : ")
    Point_1 = input ("คะแนนครั้งที่ 1 : ")
    Point_2 = input ("คะแนนครั้งที่ 2 : ")
    Point_3 = input ("คะแนนครั้งที่ 3 : ")
    return Name,Point_1,Point_2,Point_3

def calAverage (Name,Point_1,Point_2,Point_3):
 
Name,Point_1,Point_2,Point_3 = InputInfo ()