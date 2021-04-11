def TechClubproject():

    print(' Available Chemicals are: ')
    print(' Hydrogen (H2), Oxygen (O2), Carbon (C), Chlorine (Cl2) ')
    print(' Please select frm the abv chemicals')

    c1=str(input('Enter chemical 1: '))
    c2=str(input('Enter chemical 2: '))

    if (c1=="Hydrogen" and c2=="Oxygen") or (c1=="Oxygen" and c2=="Hydrogen"):
        print(" H2 + O2 --> 2H2O ")
   
    if (c1=="Carbon" and c2=="Hydrogen") or (c1=="Hydrogen" and c2=="Carbon"):
        print(' C + 2H2 --> CH4 ')
   
    if (c1=="Hydrogen" and c2=="Chlorine") or (c1=="Chlorine" and c2=="Hydrogen"):
        print(' H2 + Cl2 --> 2HCl ')
   
    if (c1=="Oxygen" and c2=="Chlorine") or (c1=="Chlorine" and c2=="Oxygen"):
        print(' Cl2 + 02 --> 2ClO ')
   
    if (c1=="Oxygen" and c2=="Carbon") or (c1=="Carbon" and c2=="Oxygen"):
        print(' C + O2 --> CO2 ')

    if (c1=="Chlorine" and c2=="Carbon") or (c1=="Carbon" and c2=="Chlorine"):
        print(' C + 2Cl2 --> CCl4 ')
    else :
        print(" Enter valid Chemicals ")
      
