width = float (input ("ป้อนความกว้าง : "))
long = float (input ("ป้อนความยาว : "))
height = float (input ("ป้อนความสูง : "))
#ตัวแปล
area = round((long * height * 2 )+(long * width * 2)+(long * long * 2) ) / 5 

#คำนวน 
print(f"กล่องสีเหลี่ยมให้มีความกว้าง{width} ยาว {long} สูง {height} ต้องใช้สีทั้งหมด {area} แกลอน ")
print("กล่องสีเหลี่ยมให้มีความกว้าง",width,"ยาว", long, "สูง" ,height, "ต้องใช้สีทั้งหมด", area,"แกลอน" )
print("กล่องสีเหลี่ยมให้มีความกว้าง"+str(width)+" ยาว"+str(long)+" สูง"+str(height)+" ต้องใช้สีทั้งหมด"+ str(area)+ "แกลอน")
print("กล่องสีเหลี่ยมให้มีความกว้าง{} ยาว {} สูง {} ต้องใช้สีทั้งหมด {} แกลอน ".format(width,long,height,area))

    