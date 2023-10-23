#โปรแกรมคำนวนหาพื้นที่วงกลม เส้นรอบวงกลม และปริมาตรทรงกลม จากรัตมีที่ป้อนโดยผู้ใช้ทางแป้นพิมพ์ และแสดงพื้นที่ เส้นรอบและประมาตรหน้าจอ
#5 ฟังชั่น
#inputRaduis

import math
#กรอกข้อมูล
def inputRadius():
    return float(input("พื้นที่วงกลม : "))

#คำนวนพื้นที่
def AreaCircle(r):
    return math.pi*math.pow(r,2)
#คำนวนเส้นรอบวง
def RoundCirle(r):
    return 2 * math.pi * r
#คำนวนปริมาตร
def VolumeCirle(r):
    return 4/3 * math.pi * math.pow(r,3)
#แสดงผล
def showResult():
    r = inputRadius()
    print(f"พื้นที่วงกลมเป็นรัศมี {AreaCircle(r):.2f} เส้นรอบวงกลมเป็น {RoundCirle(r):.2f} ปริมาตรทรงกลมเป็น {VolumeCirle(r):.2f}")

showResult()