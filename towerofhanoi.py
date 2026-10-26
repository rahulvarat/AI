
from collections import deque

def bfs(n):
    start = (tuple(range(n, 0, -1)), (), ())
    goal = ((), (), tuple(range(n, 0, -1)))

    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        for s in range(3):
            if not state[s]:
                continue

            disk = state[s][-1]

            for d in range(3):
                if s != d and (not state[d] or state[d][-1] > disk):
                    pegs = [list(p) for p in state]
                    pegs[s].pop()
                    pegs[d].append(disk)
                    new_state = tuple(tuple(p) for p in pegs)

                    if new_state not in visited:
                        visited.add(new_state)
                        move = f"Move disk {disk} from {chr(65+s)} to {chr(65+d)}"
                        queue.append((new_state, path + [move]))

    return None


n = int(input("Enter number of disks: "))
solution = bfs(n)

print("\nSolution:")
for i, move in enumerate(solution, 1):
    print(i, move)

print("Total moves:", len(solution))
