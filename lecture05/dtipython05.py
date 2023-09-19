#คำนวนเงินที่จะแชร์ ป้อนเงิน ป้อนคน แล้วคำนวนและแสดงเงินที่จะแชร์กันทางหน้าจอ 
#โดยให้เขียเป็นฟังชั่น (2 ฟังชั่น)

#รับค่าข้อมูล
def inputmoneyperson(): 
    money = float (input ("ป้อนเงิน : " ))
    person = int(input("ป้อนจำนวนคน : "))

    return money,person


#คำนวน แล้วแสดงผล 
def calandshowmoney(money,person): 
    a = format (float(money),".2f")
    print(f"จำนวนเงิน {money:.2f} บาท คน {person} คน แชร์กันคนละ {round(float(money/person))} บาท ")
    print("จำนวนเงิน",(a),"บาท คน",person, "คน แชร์กันคนละ" ,round(float(money/person)), "บาท" )
    print("จำนวนเงิน "+str(a)+" บาท คน "+str(person)+" คน แชร์กันคนละ "+str(round(float(money/person)))+" บาท")
    print("จำนวนเงิน {:.2f} บาท คน {} คน แชร์กันคนละ {} บาท ".format(money,person,(round(float(money/person)))))
    print('จำนวนเงิน %.2f บาท คน %d คน แชร์กันคนละ %d บาท ' % (money, person , money/person))
    
money,person = inputmoneyperson ()
calandshowmoney(money,person)

print(inputmoneyperson())
