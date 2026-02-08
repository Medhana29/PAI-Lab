from collections import deque

def water_jug_dp(a, b, target):
   
    dp = [[False] * (b + 1) for _ in range(a + 1)]
    
    parent = {}
    
    q = deque()
    q.append((0, 0))
    dp[0][0] = True
    parent[(0, 0)] = None

    while q:
        x, y = q.popleft()

       
        if x == target or y == target:
            print("Path from initial state to solution state ::")
            path = []
            cur = (x, y)
            while cur is not None:
                path.append(cur)
                cur = parent[cur]
            for state in reversed(path):
                print(state)
            return

       
        next_states = [
            (a, y),            # fill jug1
            (x, b),            # fill jug2
            (0, y),            # empty jug1
            (x, 0),            # empty jug2
            (x - min(x, b - y), y + min(x, b - y)),  # pour jug1 -> jug2
            (x + min(y, a - x), y - min(y, a - x))   # pour jug2 -> jug1
        ]

        for nx, ny in next_states:
            if not dp[nx][ny]:
                dp[nx][ny] = True
                parent[(nx, ny)] = (x, y)
                q.append((nx, ny))

    print("Solution not possible")


if __name__ == "__main__":
    Jug1 = int(input("Enter the capacity of Jug1: "))
    Jug2 = int(input("Enter the capacity of Jug2: "))
    target = int(input("Enter the target: "))
    water_jug_dp(Jug1, Jug2, target)
