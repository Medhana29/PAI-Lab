states = ['Rainy', 'Sunny']

# Initial probabilities
start_prob = {
    'Rainy': 0.6,
    'Sunny': 0.4
}

# Transition probabilities
transition_prob = {
    'Rainy': {'Rainy': 0.7, 'Sunny': 0.3},
    'Sunny': {'Rainy': 0.4, 'Sunny': 0.6}
}

# Emission probabilities
emission_prob = {
    'Rainy': {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
    'Sunny': {'walk': 0.6, 'shop': 0.3, 'clean': 0.1}
}

# Observation sequence
obs_sequence = ['walk', 'shop', 'clean']


def forward_algorithm(states, observations, start_prob, transition_prob, emission_prob):
    forward = []

    # Step 1: Initialization
    f0 = {}
    for state in states:
        f0[state] = start_prob[state] * emission_prob[state][observations[0]]
    forward.append(f0)

    # Step 2: Recursion
    for t in range(1, len(observations)):
        ft = {}
        for curr in states:
            prob = 0
            for prev in states:
                prob += forward[t-1][prev] * transition_prob[prev][curr]
            ft[curr] = prob * emission_prob[curr][observations[t]]
        forward.append(ft)

    # Step 3: Termination
    total_prob = sum(forward[-1][s] for s in states)
    return total_prob


# Run
result = forward_algorithm(states, obs_sequence, start_prob, transition_prob, emission_prob)

print("Probability of observation sequence:", round(result, 6))
