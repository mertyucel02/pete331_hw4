#### HOMEWORK 4 ####

#### QUESTION 3 ####

#### Mert Yücel ####

#### 2515401 ####

#### PETE 331: Petroleum Production Engineering I ####

#### Section 1 ####

#### Asst. Prof. Dr. İsmail Durgut ####

#### 01/12/2023 ####

#### LIBRARIES USED ####

import math
import cv2

#### STUDENT ID ####

student_id = [2, 5, 1, 5, 4, 0, 1]

#### GIVEN VALUES ####
C_a = .15
V_matrix_percentage = 100 - (12 + 2 * student_id[5]) #%
D = 1.2 * math.pow(10, -9) #m^2/s
PV_bt = 3.5 + student_id[6] * .2
q_h = .31 + .01 * student_id[4] #bbl/min-ft
SG_m = 2.87
SG_a = 1.07
d_wellbore = .708 #ft
r_wellbore = d_wellbore / 2 #ft
d_f = 1.6
b = 1.5 * math.pow(10, -5)
acidized_zone = 30 #ft


#To find radius of wormhole
r_wh = r_wellbore + 2.23 + student_id[6] * .7 #ft

# To find stoichiometry numbers of mineral and acid with the balanced eqn
balanced_eqn = cv2.imread("balance1.png", cv2.IMREAD_COLOR)
cv2.imshow("balanced equation", balanced_eqn)

v_m = 1
v_a = 4

# To find molecular weights of mineral and acid using atomic weights
periodic_table = cv2.imread("PeriodicTable.png", cv2.IMREAD_COLOR)
cv2.imshow("periodic table", periodic_table)

AW_C = 12.0107 #u
AW_Ca = 40.078 #u
AW_H = 1.00794 #u
AW_Cl = 35.453 #u
AW_O = 15.9994 #u
AW_Mg = 24.3050 #u

MW_m = AW_Ca + AW_Mg + 2 * (AW_C + AW_O * 3) #g/mol
MW_a = AW_Cl + AW_H #g/mol

#### TO FIND POROSITY ####

porosity = (100 - V_matrix_percentage) / 100

#### DACCORD'S MODEL ####

#### TO COMPUTE GRAVIMETRIC DISSOLVING POWER ####

beta_15 = (C_a * v_m * MW_m) / (v_a * MW_a) #lbm CaMg(CO3)2/lbm 15 wt% HCl solution

#### TO COMPUTE ACID CAPACITY NUMBER ####

N_Ac = (porosity * beta_15 * SG_a) / ((1 - porosity) * SG_m)

#### TO CONVERT OIL-FIELD UNITS TO SI UNITS ####

bbl_to_m3 = .1589872949 #m3/bbl
ft_to_m = .3048 #m/ft
min_to_sec = 60 #sec/min
gal_to_m3 = .00378541 #m3/gal

q_h_in_term_of_SI_units = q_h * bbl_to_m3 /(min_to_sec * ft_to_m) #m^3/sec-m

r_wh_in_term_of_m = r_wh * ft_to_m #m

#### TO COMPUTE REQUIRED ACID VOLUME PER UNIT THICKNESS OF FORMATION ####

V_h_daccord = (math.pi * porosity * math.pow(D, 2/3) *
       math.pow(q_h_in_term_of_SI_units, 1/3) * math.pow(r_wh_in_term_of_m,
                                                         d_f)
       ) / (b * N_Ac) #m^3/m

V_h_in_term_of_oil_field_units_daccord = V_h_daccord * ft_to_m / gal_to_m3 #gal/ft


#### VOLUMETRIC MODEL ####

#### TO COMPUTE REQUIRED ACID VOLUME PER UNIT THICKNESS OF FORMATION ####

V_h_volumetric_cuft = math.pi * porosity * (r_wh ** 2 - r_wellbore ** 2) * PV_bt #cuft/ft

cuft_to_gal = 7.48052 #gal/cuft

V_h_volumetric_gal = V_h_volumetric_cuft * cuft_to_gal

#### RESULTS ####

print("The required acid volume by Daccord's Model is " +
      str(V_h_in_term_of_oil_field_units_daccord) + " gal/ft")
print("The required acid volume by Volumetric Model is " +
      str(V_h_volumetric_gal) + " gal/ft")
print("The Daccord's Model is more reliable to develop a field-scale acid injection "
      "since when the Daccord's Model uses, the operation becomes more effective by using small amount of acid solution"
      "thanks to diffusion in Dolomite")

cv2.waitKey(0)
cv2.destroyAllWindows()


