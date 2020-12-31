a=int(input('So you need to first choose the quantity which you would want to find by typing the number assigned to each quantity: \n 1. Electrical Current\n 2. Potential Difference(Voltage)\n 3. Power\n 4. Electrical Energy\n 5. Heat'))

if a==1:
    ia=int(input('For finding the Current please choose the values which are given \n 1. Charge and Time \n 2. Voltage and Resistance \n 3.Power and Resistance \n 4.Power and Voltage \n 5.Heat,Time and Electricity'))
if ia==1:
    iq=int(input('Value of Charge:'))
    it=int(input('Value of Time:'))
    iqt= iq/it
    iqtx=str(iqt)
    print(iqtx+' Amperes')

if a==2:
    print('So you asked Potential Difference')