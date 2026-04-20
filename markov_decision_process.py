import numpy as np

class GridWorldMDP:
    def __init__(self, size, goal, trap):
        self.size = size
        self.goal = goal
        self.trap = trap
        self.state_space = [(i, j) for i in range(size) for j in range(size)]
        self.action_space = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        self.transitions = self.build_transitions()
        self.rewards = self.build_rewards()

    def build_transitions(self):
        transitions = {}
        for s in self.state_space:
            transitions[s] = {}
            for a in self.action_space:
                transitions[s][a] = self.next_state(s, a)
        return transitions

    def next_state(self, s, a):
        i, j = s
        if a == 'UP': i -= 1
        elif a == 'DOWN': i += 1
        elif a == 'LEFT': j -= 1
        elif a == 'RIGHT': j += 1

        i = max(0, min(i, self.size - 1))
        j = max(0, min(j, self.size - 1))
        return [(1.0, (i, j))]

    def build_rewards(self):
        r = {s: -1 for s in self.state_space}
        r[self.goal] = 0
        r[self.trap] = -10
        return r


def value_iteration(mdp, gamma=0.9, eps=0.01):
    V = {s: 0 for s in mdp.state_space}
    while True:
        delta = 0
        for s in mdp.state_space:
            if s in [mdp.goal, mdp.trap]:
                continue
            v = V[s]
            V[s] = max(sum(p * (mdp.rewards[s2] + gamma * V[s2])
                           for p, s2 in mdp.transitions[s][a])
                       for a in mdp.action_space)
            delta = max(delta, abs(v - V[s]))
        if delta < eps:
            break
    return V


def policy_iteration(mdp, gamma=0.9):
    policy = {s: np.random.choice(mdp.action_space)
              for s in mdp.state_space if s not in [mdp.goal, mdp.trap]}
    V = {s: 0 for s in mdp.state_space}

    while True:
        # Policy Evaluation
        while True:
            delta = 0
            for s in policy:
                v = V[s]
                a = policy[s]
                V[s] = sum(p * (mdp.rewards[s2] + gamma * V[s2])
                           for p, s2 in mdp.transitions[s][a])
                delta = max(delta, abs(v - V[s]))
            if delta < 0.01:
                break

        # Policy Improvement
        stable = True
        for s in policy:
            old = policy[s]
            policy[s] = max(mdp.action_space,
                            key=lambda a: sum(p * (mdp.rewards[s2] + gamma * V[s2])
                                              for p, s2 in mdp.transitions[s][a]))
            if old != policy[s]:
                stable = False
        if stable:
            break

    return policy, V


mdp = GridWorldMDP(3, (2, 2), (1, 1))

# Value Iteration
V = value_iteration(mdp)

print("\nValue Iteration Results:")
for i in range(mdp.size):
    for j in range(mdp.size):
        s = (i, j)
        if s == mdp.goal:
            print(f"State {s}:  {V[s]:.2f} (Goal)")
        elif s == mdp.trap:
            print(f"State {s}: {V[s]:.2f} (Trap)")
        else:
            print(f"State {s}: {V[s]:.2f}")

# Policy Iteration
policy, V_pi = policy_iteration(mdp)

print("\nPolicy Iteration Results:")
for i in range(mdp.size):
    for j in range(mdp.size):
        s = (i, j)
        if s == mdp.goal:
            print(f"State {s}: Goal State")
        elif s == mdp.trap:
            print(f"State {s}: Trap State")
        else:
            print(f"State {s}: Action = {policy[s]:<5}, Value = {V_pi[s]:.2f}")

# Grid View
print("\nGrid Values:")
for i in range(mdp.size):
    for j in range(mdp.size):
        print(f"{V[(i,j)]:6.2f}", end=" ")
    print()

print("\nPolicy Grid:")
symbols = {'UP': '↑', 'DOWN': '↓', 'LEFT': '←', 'RIGHT': '→'}
for i in range(mdp.size):
    for j in range(mdp.size):
        s = (i, j)
        if s == mdp.goal:
            print(" G ", end=" ")
        elif s == mdp.trap:
            print(" X ", end=" ")
        else:
            print(f" {symbols[policy[s]]} ", end=" ")
    print()                  
