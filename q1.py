#### HOMEWORK 4 ####

#### QUESTION 1 ####

#### Mert Yücel ####

#### 2515401 ####

#### PETE 331: Petroleum Production Engineering I ####

#### Section 1 ####

#### Asst. Prof. Dr. İsmail Durgut ####

#### 01/12/2023 ####

#### LIBRARIES USED ####

import math

#### STUDENT ID ####

student_id = [2, 5, 1, 5, 4, 0, 1]

#### GIVEN VALUES ####
S = 3.5 + 0.5 * student_id[6]
q = 10000 #STB/year
coiled_tubing_id = 2 #in
A = 120 + 10 * student_id[5] #acres
p_res = 3000 + student_id[6] * 75 #psia
d_welbore = 0.708 #ft
SG_pure_water = 1
SG_acid_soln = SG_pure_water * 1.07
mu_acid = 1.3 #cP
fracture_gradient = 0.68 #psi/ft
depth = 6200 + student_id[6] * 125 #ft
h = 27 + student_id[4] #ft
k = 31 + student_id[5] #md
p_sf = 325 #psi
pure_water_gradient = 0.433 #psi/ft

#### TO FIND RADIUS OF RESERVOIR IN TERMS OF FT ####

acre_to_sq_ft = A * 43560 #ft^2
r_e = math.sqrt(acre_to_sq_ft / math.pi) # ft

#### TO COMPUTE MAXIMUM ACID INJECTION RATE ####

p_bd = fracture_gradient * depth

q_i_max = (4.917 * math.pow(10, -6) * k * h *
           (p_bd - p_res - p_sf))/\
          (mu_acid * (math.log((0.472 * r_e) / (d_welbore / 2)) + S)) #bbl/min

#### TO COMPUTE FLOWING BOTTOM-HOLE PRESSURE ####

p_wf = fracture_gradient * depth - p_sf #psia

#### TO CALCULATE HYDROSTATIC PRESSURE DROP ####

change_in_p_h = pure_water_gradient * SG_acid_soln * depth #psi

#### TO COMPUTE FRICTIONAL PRESSURE DROP ####

change_in_p_f = (518 * SG_acid_soln ** .79 * q_i_max ** 1.79 * mu_acid ** .207 *
                 depth) / (1000 * coiled_tubing_id ** 4.79)

#### TO COMPUTE SURFACE INJECTION PRESSURE ####

p_si = p_wf - change_in_p_h + change_in_p_f

#### RESULTS ####

print("The maximum acid injection rate is " + str(q_i_max) + " bbl/min")
print("The flowing bottom-hole pressure is " + str(p_wf) + " psia")
print("The hydrostatic pressure drop is " + str(change_in_p_h) + " psia")
print("The frictional pressure drop is " + str(change_in_p_f) + " psia")
print("The surface injection pressure is " + str(p_si) + " psia")




