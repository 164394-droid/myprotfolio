print("โปรแกรมคำนวณพื้นที่รูปทรง")

print("1. สี่เหลี่ยมมุมฉาก")
print("2. สามเหลี่ยม")
print("3. วงกลม")

menu = int(input("เลือกเมนู (1-3): "))

if menu == 1:
    width = float(input("กรอกความกว้าง: "))
    length = float(input("กรอกความยาว: "))
    area = width * length
    print("พื้นที่สี่เหลี่ยม =", area, "ตารางหน่วย")

elif menu == 2:
    base = float(input("กรอกความยาวฐาน: "))
    height = float(input("กรอกความสูง: "))
    area = 0.5 * base * height
    print("พื้นที่สามเหลี่ยม =", area, "ตารางหน่วย")

elif menu == 3:
    radius = float(input("กรอกรัศมี: "))
    area = 3.14 * radius * radius
    print("พื้นที่วงกลม =", area, "ตารางหน่วย")

else:
    print("กรุณาเลือกเมนูให้ถูกต้อง")