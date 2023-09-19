#โปรแกรมคำนวนหาพื้นที่วงกลม เส้นรอบวงกลม และปริมาตรทรงกลม จากรัตมีที่ป้อนโดยผู้ใช้ทางแป้นพิมพ์ และแสดงพื้นที่ เส้นรอบและประมาตรหน้าจอ
#5 ฟังชั่น
#inputRaduis

import math

def inputraduis():
    return float(input ("ป้อนรัสมีวงกลม : "))

#calAreaCircle 
def calAreaCircle (r): 
    return math.pi * math.pow(r,2)
#calRoundCirle
def calRoundCircle (r):
    return 2 * math.pi * r 
#calvolumeCirle 
def calvolumeCircle (r):
    return 4/3 * math.pi * math.pow(r,3)

#showResul  
