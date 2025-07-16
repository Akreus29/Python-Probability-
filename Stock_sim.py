import numpy as np
import matplotlib.pyplot as plt

def simulate_stock(n_simulations, n_days):
    results = []
    for _ in range(n_simulations):
        stock_prices = np.random.choice([-1, 1], size=n_days)
        cumulative_prices = np.cumsum(stock_prices)
        results.append(cumulative_prices)

    return results

n_simulations = 5
n_days = 10000

simulation_results = simulate_stock(n_simulations, n_days)

# Plot the results
for i, result in enumerate(simulation_results):
    print(f"Simulation {i}: {result} ")
    plt.plot(result, label=f'Simulation {i+1}')

plt.title('Simulation of Stock Prices')
plt.xlabel('Days')
plt.ylabel('Stock Price')
plt.legend()
plt.show()
