name = input ("ชื่อสินค้า : ")
default_price  =(input ("ราคาสินค้า : "))
#สูตร
sell = (default_price)  + ((default_price)* 10/100)

default_price_v2 = format (float(sell),".2f")
#ตัวแปล

print (f"ราคาขายสินค้า {sell:.2f} บาท ")
    #print(f"คุณ {emp_name} ยอดขาย {float(sale_price):.2f} บาท ได้ค่าคอม {comis:.2f} บาท")

