number = int(input("ป้อนอุณหภูมิองศา: "))
oc = str(9 / 5 * number + 32)
print("แปลงเป็นองศาฟาเรนไฮต์ได้:", oc, "F")
print("แปลงเป็นองศาฟาเรนไฮต์ได้: " + oc + " F")
print(f"แปลงเป็นองศาฟาเรนไฮต์ได้: {oc} F")
print("แปลงเป็นองศาฟาเรนไฮต์ได้: {} F".format(oc))