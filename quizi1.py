
# ქვიზი 1

# 1
length = 8
width = 5
perimeter = 2 * (length + width)
print("1) პერიმეტრი:", perimeter)

# 4
n = 1
while True:
    if n % 5 == 0:
        break
    print(n)
    n += 1

# 5
for i in range(1, 31):
    if i % 2 != 0:
        continue
    print(i)

# 6
a = int(input("6) პირველი რიცხვი: "))
b = int(input("მეორე რიცხვი: "))

if a > b:
    print("მაქსიმუმია:", a)
else:
    print("მაქსიმუმია:", b)

