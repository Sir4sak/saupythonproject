name_product = input ("ชื่อสินค้า : ")
cost_price  = float(input ("ต้นทุน : "))

#ราคาต้นทุน + ราคาต้นทุนบวกเพิ่ม10%
sell = (cost_price)  + ((cost_price)* 10/100)

#เพิ่มทศนิยม 2 ตำแหน่ง
sellv2 = format (float(sell),".2f")  #string


print (f"ราคาขายสินค้า {sellv2} บาท ")
print ("ราคาขายสินค้า",sellv2,"บาท")
print ("ราคาขายสินค้า "+sellv2+" บาท")
print ("ราคาขายสินค้า {} บาท ".format(sellv2))
