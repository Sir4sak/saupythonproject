money = input("ป้อนจำนวนเงิน: ")
people = input("ป้อนจำนวนคน: ")
han = int(money)/float(people)
todsaniyom = format(han, ".2f")
print("หารได้คนละ", todsaniyom, "บาท")
print("หารได้คนละ " + todsaniyom + " บาท")
print("หารได้คนละ {} บาท".format(todsaniyom))
print(f"หารได้คนละ {todsaniyom} บาท")