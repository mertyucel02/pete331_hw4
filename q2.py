#### HOMEWORK 4 ####

#### QUESTION 2 ####

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

avg_porosity = (13 + student_id[4] * 1.5) / 100
d_wellbore = 0.708 #ft
r_a = d_wellbore / 2 + 2.5 + student_id[6] * .2 #ft
C_m = .1
C_a = .15
rho_m = 180.979 #lbm/cuft
SG_a = 1.07
rho_pure_water = 62.424 #lbm/cuft
total_formation_thickness = 25 + 2 * student_id[5] #ft

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

#### TO COMPUTE VOLUME OF CAMG(CO3)2 TO BE REMOVED ####

V_m = math.pi * (r_a ** 2 - (d_wellbore / 2) ** 2) * \
      (1 - avg_porosity) * C_m #cuft CaMg(CO3)2/ft pay zone

#### TO CALCULATE INITIAL PORE VOLUME ####
V_P = math.pi * (r_a ** 2 - (d_wellbore / 2) ** 2) * avg_porosity #cuft/ft pay zone

#### TO COMPUTE GRAVIMETRIC DISSOLVING POWER ####

beta_15 = (C_a * v_m * MW_m) / (v_a * MW_a) #lbm CaMg(CO3)2/lbm 15 wt% HCl solution

#### TO CALCULATE VOLUMETRIC DISSOLVING POWER ####

rho_a = SG_a * rho_pure_water #lbm/cuft
X = beta_15 * (rho_a / rho_m) #cuft CaMg(CO3)2/cuft 15 wt% HCl solution

#### TO COMPUTE REQUIRED MINIMUM ACID VOLUME ####

V_a = (V_m / X) + V_P + V_m #cuft 15 wt% HCl solution/ft pay zone
cuft_to_gal = 7.48052 #gal/cuft
V_a_gal = V_a * cuft_to_gal #gal 15 wt% HCl solution/ft pay zone
V_a_for_the_formation_thickness = V_a_gal * total_formation_thickness #gal 15 wt% HCl solution

#### COST ESTIMATION ####

q = 95 + 5 * student_id[6] #STB/day
year = 365 #days
q_for_1_year = q * year #STB/year
oil_price = 40 + student_id[6] * 7 #$/bbl
total_revenue = q_for_1_year * oil_price
main_acid_operation_cost = (student_id[6] + 10) * 10000 #$
preflush_cost = 45 + student_id[5] #$/gal
preflush_cost_for_the_total_formation_thickness = preflush_cost * \
                                                  V_a_for_the_formation_thickness #$
total_cost = main_acid_operation_cost + \
             preflush_cost_for_the_total_formation_thickness #$
profit = total_revenue - total_cost #$


#### RESULTS ####

print("Volume of CaMg(CO3)2 to be removed is " +
      str(V_m) + " cuft CaMg(CO3)2/ft pay zone")
print("Initial pore volume is " + str(V_P) + " cuft/ft pay zone")
print("Gravimetric dissolving power of the 15 wt% HCl solution is "
      + str(beta_15) + " lbm CaMg(CO3)2/lbm 15 wt% HCl solution")
print("Volumetric dissolving power of the 15 wt% HCl solution is " +
      str(X) + " cuft CaMg(CO3)2/cuft 15 wt% HCl solution")
print("The required minimum HCl volume is " +
      str(V_a) + " gal 15 wt% HCl solution/ft pay zone")
print("The required minimum HCl volume is " +
      str(V_a_for_the_formation_thickness) + " gal 15 wt% HCl solution for total formation zone")
print("The profit is " + str(profit) + " $. Economically, there is no lost. Also, "
                                       "if preflush does NOT applied, when acidizing is applied only, "
                                       "formation is damaged. Because of this situation, there could be a loss economically.")
print("The Hydrofluoric acid reacts faster and in a more effective way. Thus using Hydrofluoric acid saves "
      "time and money.")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("The average porosity is " + str(avg_porosity))
print("The wellbore diameter is " + str(d_wellbore) + " ft")
print("The radius of acid treatment is " + str(r_a) + " ft")
print("The mineral content is " + str(C_m))
print("The weight fraction of acid in the acid solution is " + str(C_a))
print("The density of mineral is " + str(rho_m) + " lbm/cuft")
print("The specific gravity of acid is " + str(SG_a))
print("The density of pure water is " + str(rho_pure_water) + " lbm/cuft")
print("Total formation thickness is " + str(total_formation_thickness) + " ft")



