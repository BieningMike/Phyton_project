name = input("What is your name? ")
email = input("What is your email address? ")
sdate = input("What start date are you looking for (dd/mm/yyyy)? ")
n = input("How many members are there in Fozzy Bear a max of 8 is allowed? ")
days = int(input("How many days? "))

# Set studio charges based on the number of days
studio_charges = 0
if days == 1:
    studio_charges = 300
elif 1 < days < 5:
    studio_charges = 250
elif 4 < days < 9:
    studio_charges = 220
else:
    studio_charges = 200

# Band member info
bmnames , bminsts, bmrates = [], [], []
for i in range(1, int(n) + 1):
    bmname = input(f"What is band member #{i}'s name? ")
    inst = input(f"What is {bmname}'s instrument? ")
    ratepd = float(input(f"What is {bmname}'s rate per day? "))
    bmnames.append(bmname)
    bminsts.append(inst)
    bmrates.append(ratepd)

# Session musician cost
sm = int(input("There is room for 6 session musicians.\nHow many do you want? "))  
smc = 120*sm

# Payment methods
print("Will you pay by\n1: Credit card (5% levy)\n2: Cash (5% discount)\n3: Online")
paym = input("=>: ")
if paym == '1':
    paym = 'Credit card'
elif paym == '2':
    paym = 'Cash'
elif paym == '3':
    paym = 'Online'
    
# Booking summary
print(f"\nBooking for: {name} - {sdate}")
print("----------------------------------------------")
print(f"{'Name':<20}{'Instrument':<20}{'Rate':<20}")
print("----------------------------------------------")

# Highest-paid band member
hpbm = bmnames[0]
hpbmr = bmrates[0]
for i in range(len(bmnames)):
    print(f"{bmnames[i]:<20}{bminsts[i]:<20}€{bmrates[i]:<20}")
    if bmrates[i] > hpbmr:
        hpbmr = bmrates[i]
        hpbm = bmnames[i]
print(f"\nThe highest paid band member is {hpbm} on €{hpbmr}.")
print(f"The average daily rate for a band member is {sum(bmrates)/len(bmrates):.1f}. ")
print(f"There are {sm} session musicians booked. ")
print(f"\nPayment is by              	 	 	      	 	  {paym}")

# Calculations based on the payment method
if paym == 'Credit card':
    studio_charges += studio_charges * 0.05
    smc += smc * 0.05
elif paym == 'Cash':
    studio_charges -= studio_charges * 0.05
    smc -= smc * 0.05
elif paym == 'Online':
    pass

# Total cost
print(f"Daily Rate applied - studio               	 	€    {studio_charges:.2f} ")
print(f"Daily Rate applied - 2 session musicians§ 	  	€    {smc:.2f} ")
print()
print(f"\nTotal Studio Cost                         	 	€    {studio_charges*days:.2f} ")
print(f"Total Session Musician Cost                     €    {smc*days:.2f} ")
print("\n   	=========== \n")
print(f"Total Payment to Studio                   	 	€    {studio_charges*days + smc*days:.2f} ")
print(f"Band Musician Cost                        	 	€    {sum(bmrates)*days:.2f} ")
print("\n   	=========== \n")
print(f"Total Costs                              	 	€    {studio_charges*days + smc*days + sum(bmrates)*days:.2f} ")