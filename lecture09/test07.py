import test06
import math
from test08 import calSqareArea,calTriangleArea,calCircleArea

print(f'ผลรวมของ 10+20 = {test06.sumnumber(10,20)}')

test06.ShowHi()

print("ราคาสินค้า 20000 ภาษีเป็ฯเงิน",2000*test06.VAT)

print("7 ยกกำลัง 15 มีค่า",math.pow(7,15))

print("พื้นที่วงกลมรัศมี 3 มีค่า",math.pi*math.pow(3,2))

print("พื้นที่วงกลมรัศมี 8 มีค่า",calCircleArea)
print("พื้นที่สามเหลี่ยมมีค่า กว้าง 10 ยาว 5 มีค่า",calTriangleArea)
