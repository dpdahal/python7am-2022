print("==============================================")
print("===============Computer Bazar==============")
print("==============================================")

dell_price = 0
toshiba_price = 0
mac_price = 0
quantity = 0
total_price = 0
tax_amount = 0
delivery_price = 0
plastic_price = 0
bag_price = 0
gift_price = 0
location_price = 0

print("1.Dell(Rs:20000) 2.Toshiba(Rs:3000) 3.MAC(Rs:50000)")
option = int(input("Select any option: "))

if option == 1:
    quantity = int(input("Enter quantity: "))
    dell_price += 20000 * quantity

elif option == 2:
    quantity = int(input("Enter quantity: "))
    toshiba_price += 30000 * quantity
elif option == 3:
    quantity = int(input("Enter quantity: "))
    mac_price += 50000 * quantity
else:
    print("Exit")
    exit()

print("Delivery Option:  1.Home(Rs:1000) 2. Pickup(Rs:Free)")
deli_option = int(input("Enter option: "))
if deli_option == 1:
    delivery_price += 1000

print("Packing Option:  1.Plastic(Rs:500) 2. Bag(Rs:1000) 3.Gift Box(Rs:5000) 4. None")
p_option = int(input("Enter option: "))

if p_option == 1:
    plastic_price += 500

elif p_option == 2:
    bag_price += 1000
elif p_option == 3:
    gift_price += 5000
else:
    print("None ")

print("Location: 1. KTM(13% tax) 2. LTP(Free) 3. BKT(Free)")
l_option = int(input("Enter option: "))

total_price += dell_price + toshiba_price + mac_price
if l_option == 1:
    tax_amount += total_price * 0.13

gt = total_price + delivery_price + bag_price + plastic_price + gift_price + tax_amount

print(f"Total Quantity: {quantity} Total Price: {total_price} Tax Amount: {tax_amount} GT: {gt}")

