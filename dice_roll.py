import random

def dice_throw(num_of_sim):
    outcomes = 0

    for _ in range(num_of_sim):
        dice_results = [random.randint(1, 6) for _ in range(10)]
        if sum(dice_results) == 32:
            outcomes += 1

    prob = outcomes / num_of_sim
    return prob


num_of_sim_input = input("Enter the number of simulations: ")
num_of_sim = int(num_of_sim_input)


simulation_result = dice_throw(num_of_sim)
print(f"Simulated Probability (based on {num_of_sim} throws): {simulation_result}")
