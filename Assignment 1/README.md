INTRODUCTION
The problem: We are trying to find the cheapest diet consisting of only 5 products that satisfies all of the following nutritional constraints:
- No more than 5000mg of sodium
- No less than 2000kcals of energy/calories
- No less than 50g of protein
- No less than 20mcg of vitamin D
- No less than 1300mg of calcium
- No less than 18mg of iron
- No less than 4700mg of potassium 
----------------------------------------------
PRODUCTS + NUTRITION VALUES

Item 1: Atlantic Salmon Filet
Cost per serving: $24.99 / 8 = $3.12
Nutrients per serving: Sodium: 65 mg, Energy: 240 kcals, Protein: 23 g, Vitamin D: 12.4, Calcium: 0, Iron: 0.4 mg, Potassium: 410 mg

Item 2: Rice Orzo Pilaf Mix
Cost per serving: $2.49 / 3 = $0.83
Nutrients per serving (as packaged): Sodium: 670 mg, Energy: 240 kcals, Protein: 7 g, Vitamin D: 0, Calcium: 10 mg, Iron: 2 mg, Potassium: 174 mg

Item 3: Stir Fried cabbage
Cost per serving: $3.49 / 2 = $1.75
Nutrients per serving: Sodium: 620 mg, Energy: 130 kcals, Protein: 3 g, Vitamin D: 0, Calcium: 50 mg, Iron: 0.5 mg, Potassium: 350 mg

Item 4: Grainless Granola
Cost per serving: $4.29 / 4.5 = $0.95
Nutrients per serving: Sodium: 200 mg, Energy: 340 kcals, Protein: 9 g, Vitamin D: 0, Calcium: 60 mg, Iron: 2.5, Potassium: 350 mg

Item 5: Champs Elysées Salad Mix
Cost per serving: $2.29 / 2 = $1.15
Nutrients per serving: Sodium: 25 mg, Energy: 15 kcals, Protein: 1 g, Vitamin D: 0 mcg, Calcium: 30 mg, Iron: 1 mg, Potassium: 190 mg
----------------------------------------------
THE LP PROBLEM

Objective
Minimize C = 3.12AS + 0.83R + 1.75C + 0.95G + 1.15S

Constraints
Sodium: 65AS + 670R + 620R + 200G + 25S + S1 = 5000
Energy: 240AS + 240R + 130C + 340G + 15S - S2 = 2000
Protein: 23AS + 7R + 3C + 9G + 1S - S3 = 50
Vitamin D: 12.4AS + 0R + 0C + 0G + 0S  - S4 = 20
Calcium:  0AS + 10R + 50C + 60G + 30S - S5 = 1300
Iron:  0.4AS + 2R + 0.5C + 2.5G + 1S - S6 = 18
Potassium:  410AS + 174R + 350C + 350G + 190S - S7 = 4700
AS, R, C, G, S, S1, S2, S3, S4, S5, S6, S7 >= 0

Decisions variables: 
a = Number of atlantic salmon filet servings
b = Number of of rice orzo pilaf mix servings
c = Number of stir-fried cabbage servings
d = Number of mango smoothie servings
e = Number of champs elysées salad mix servings
----------------------------------------------
RESULTS
The solution for this problem is to eat AS = 1.613 servings of Atlantic salmon and 21.667 servings of grainless granola, which would cost $25.62 per day. In total, one would get 4438mg of sodium, 7754kcals of energy, 232g of protein, 20mcg of vitamin D, 1300mg of calcium, 55mg of iron, 8245mg of potassium.
