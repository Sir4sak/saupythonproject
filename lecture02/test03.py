emp_name = input("ป้อนชื่อพนักงาน : ")
sale_price = input("ป้อนยอดขาย : ")
print("------------------------------------")
comis = float(sale_price) * 10/100
#เพิ่มทศนิยม
sale_price_v2 = format (float(sale_price),".2f")
comis_v2 = format (float(comis),".2f")



print(f"คุณ {emp_name} ยอดขาย {float(sale_price):.2f} บาท ได้ค่าคอม {comis:.2f} บาท")

print("คุณ",emp_name,"ยอดขาย",(sale_price_v2),"บาท ได้ค่าคอม",(comis_v2),"บาท")

print("คุณ "+(emp_name)+" ยอดขาย "+str(sale_price_v2)+" บาท ได้ค่าคอม "+str(comis_v2)+ " บาท")

print("คุณ {} ยอดขาย {} บาท ได้ค่าคอม {} บาท " .format(emp_name,sale_price_v2,comis_v2) ) 