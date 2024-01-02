import random
import math
import pandas as pd
import matplotlib.pyplot as plt

def throw():
    a = random.uniform(-1, 1)
    b = random.uniform(-1, 1)
    d = math.sqrt(a**2 + b**2)
    return d <= 1

def monte_carlo_simulation(n):
    hits = sum(1 for i in range(n) if throw())
    return 4 * (hits / n)


exp = 10
throws_list = [1000, 10000, 100000, 1000000]


data = {'Throws': [], 'Estimate of PI': []}


for throws in throws_list:
    for i in range(1, exp + 1):
        pi_estimate = monte_carlo_simulation(throws)
        data['Throws'].append(throws)
        data['Estimate of PI'].append(pi_estimate)

df = pd.DataFrame(data)


excel_path = 'dart_simulation_results.xlsx'
df.to_excel(excel_path, index=False)


plt.figure(figsize=(10, 6))
for throws in throws_list:
    subset = df[df['Throws'] == throws]
    plt.plot(subset['Throws'], subset['Estimate of PI'], marker='o', linestyle='-', label=f'Throws = {throws}')

plt.xlabel('Number of Throws in 1000s ')
plt.ylabel('Estimated Pi')
plt.title('Monte Carlo Simulation for getting the Estimated Value of PI')
plt.legend()
plt.grid(True)
plt.show()

print(f'Data saved to {excel_path}')
