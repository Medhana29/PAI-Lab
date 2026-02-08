def Solution(a, b, target):
    visited = set()

    def dfs(x, y, path):
        # invalid state
        if x < 0 or y < 0 or x > a or y > b:
            return False

        
        if (x, y) in visited:
            return False

        visited.add((x, y))
        path.append((x, y))

       
        if x == target or y == target:
            print("Path from initial state to solution state ::")
            for state in path:
                print(state)
            return True

      
        next_states = [
            (a, y),          # fill jug1
            (x, b),          # fill jug2
            (0, y),          # empty jug1
            (x, 0),          # empty jug2
        ]

       
        pour = min(x, b - y)
        next_states.append((x - pour, y + pour))

       
        pour = min(y, a - x)
        next_states.append((x + pour, y - pour))

        for nx, ny in next_states:
            if dfs(nx, ny, path):
                return True

       
        path.pop()
        return False

    if not dfs(0, 0, []):
        print("Solution not possible")


if __name__ == "__main__":
    Jug1 = int(input("Enter the capacity of Jug1: "))
    Jug2 = int(input("Enter the capacity of Jug2: "))
    target = int(input("Enter the target: "))
    Solution(Jug1, Jug2, target)
