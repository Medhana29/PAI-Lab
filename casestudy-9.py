states = ["Idle", "Working"]
actions = ["Work", "Charge"]
gamma = 0.9

# Initialize policy & values
policy = {s: "Work" for s in states}
V = {s: 0 for s in states}

# Policy iteration
for _ in range(10):
    # Policy Evaluation
    for s in states:
        V[s] = 5 + gamma * V[s]

    # Policy Improvement
    for s in states:
        policy[s] = "Work" if V[s] > 2 else "Charge"

print("Optimal Warehouse Robot Policy:")
for s in states:
    print(f"{s}: {policy[s]}  (Value: {V[s]:.2f})")
