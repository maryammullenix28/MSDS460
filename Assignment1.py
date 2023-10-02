import pulp
from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize

# Problem (Initial)
# define variables
AS = LpVariable("AS", 0, None) # AS>=0
R = LpVariable("R", 0, None) # R>=0
C = LpVariable("C", 0, None) # C>=0
G = LpVariable("G", 0, None) # G>=0
S = LpVariable("S", 0, None) # S>=0

# defines the problem
prob = LpProblem("problem", LpMinimize)

# define constraints
prob +=  65*AS + 670*R + 620*C + 200*G + 25*S <= 5000
prob +=  240*AS + 240*R + 130*C + 340*G + 15*S >= 2000
prob +=  23*AS + 7*R + 3*C + 9*G + 1*S >= 50
prob +=  12.4*AS + 0*R + 0*C + 0*G + 0*S  >= 20
prob +=  0*AS + 10*R + 50*C + 60*G + 30*S >= 1300
prob +=  0.4*AS + 2*R + 0.5*C + 2.5*G + 1*S >= 18
prob +=  410*AS + 174*R + 350*C + 350*G + 190*S >= 4700

# define objective function
prob += 3.12*AS + 0.83*R + 1.75*C + 0.95*G + 1.15*S

# solve the problem
status = prob.solve()
print(f"Problem")
print(f"status={LpStatus[status]}")

# print the results
for variable in prob.variables():
    print(f"{variable.name} = {variable.varValue}")
    
print(f"Objective = {value(prob.objective)}")
print(f"")