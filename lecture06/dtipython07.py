#คำสั่ง break กับ continue ที่มักใช้ร่วมกับ Control Flow 
for x in range (5) : 
    if x == 3 : 
        break; 3 #reak ทำงานเมื่อจบ loop ทันที
    print (f"SAU...{x}")

print ("_________________________________________")

for y in range (5) :
    if y == 3 :
      continue ; # continution ทำงานเมื่อจบรอบนั้น ไปรอบต่อไปทันที 
    print (f"DTI... {y}")   
