#โปรแกรมคำนวนหาพื้นที่ 3 เหลี่ยม โดยรับค่าฐาน-สูง ทางแป้นพิมพ์
#และแสดงผลพื้นที่สามเหลี่ยมที่คำนวณ

#วิเคราะห์
#มองหา feature การทำงานว่ามีอะไรบ้าง เพื่อนจะสร้างเป็น fuction 
#1. รับค้า ฐาน สูง
#2. คำนวนพื้นที่ และแสดงผลออกมา 


def inputBaseHigh ():
    base = float (input("ป้อนฐาน : "))
    high = float (input("ป้อนสูง : "))
    return base,high 
def canAndShowTrainAngleArea (base,high):
    area = base * high / 2 
    print (f"สามเหลี่ยม {base:.2f} สูง {high:.2f} มีพื้นที่ {area:.2f}")
print (" -- Calculate Triangle Area -- ")
print (" ----------------------------------------- ")
base,high = inputBaseHigh()
canAndShowTrainAngleArea (base,high )
print (" ----------------------------------------- ")