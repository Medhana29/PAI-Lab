states = ["Low", "Medium", "High"]
actions = ["Short", "Medium", "Long"]
gamma = 0.9

# Reward based on traffic density
reward = {"Low": 10, "Medium": 5, "High": -10}

# Initialize values
V = {s: 0 for s in states}

# Iterative updates
for _ in range(20):
    for s in states:
        V[s] = reward[s] + gamma * V[s]

print("Optimal State Values for Traffic Control:")
for state, value in V.items():
    print(f"{state}: {value:.2f}")
