a=int(input('So you need to first choose the quantity which you would want to find by typing the number assigned to each quantity: \n 1. Electrical Current\n 2. Potential Difference(Voltage)\n 3. Power\n 4. Electrical Energy\n 5. Heat'))

if a==1:
    ia=int(input('For finding the Current please choose the values which are given \n 1. Charge and Time \n 2. Voltage and Resistance \n 3.Power and Resistance \n 4.Power and Voltage \n 5.Heat,Time and Electricity'))
if ia==1:
    iq=int(input('Value of Charge:'))
    it=int(input('Value of Time:'))
    iqt= iq/it
    iqtx=str(iqt)
    print(iqtx+' Amperes')
if ia==2:
    iv=int(input('Value of Voltage:'))
    ir=int(input('Value of Resistance:'))
    ivr=iv/ir
    ivrx=str(ivr)
    print(ivrx+' Amperes')
if ia==3:
    ip=int(input('Value of Power:'))
    ir=int(input('Value of Resistance:'))
    ipr=ip/ir
    iprx= ipr**0.5
    iprxy=str(iprx)
    print(iprxy+' Amperes')
if ia==4:
    ip=int(input('Value of Power:'))
    iv=int(input('Value of Voltage:'))
    ipv=ip/iv
    ipvx=str(ipv)
    print(ipvx+' Amperes')
if ia==5:
    ih=int(input('Value of Heat:'))
    ir=int(input('Value of Resistance'))
    it=int(input('Value of Time:'))
    irt= ir*it
    ihrt=ih/irt
    ihrtx=ihrt**0.5
    ihrtxy=str(ihrtx)
    print(ihrtxy+' Amperes')
if a==2:
    print('So you asked Potential Difference')