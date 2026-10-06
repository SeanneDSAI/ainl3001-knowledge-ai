"""
AINL3001 — Knowledge-Driven AI
Week 4 — Local Search and Optimisation
BSP 2026

This week introduces local search.

In previous weeks, search algorithms explored paths through
a state space in order to reach a goal.

Local search takes a different approach:

    1. Start with a state.
    2. Evaluate how good that state is.
    3. Generate neighbouring states.
    4. Move to a better neighbour.
    5. Repeat.

We will explore this using the N-Queens problem.

Tasks
-----

1. Understand the problem representation.
2. Implement conflict counting.
3. Explore neighbouring states.
4. Implement Hill Climbing.
5. Implement Simulated Annealing.
"""

import math
import random

from queens_problem import QueensProblem

N = 8


# --------------------------------------------------
# TASK 0 — UNDERSTANDING THE STATE
# --------------------------------------------------

example_board = [0, 1, 2, 3]

print("Manual Exploration Board:")
print(example_board)

print(
    "\nEach list position represents a column."
)

print(
    "Each value represents the row containing the queen."
)

print(
    "\nQuestion: How many conflicts exist on this board?"
)


# --------------------------------------------------
# TASK 1 — EVALUATE A STATE
# --------------------------------------------------

def count_conflicts(board):
    """
    Return the number of pairs of queens
    that attack each other.

    Lower values are better.

    A solution has:

        conflict count = 0
    """

    # TODO:
    # Compare each queen with every queen
    # that comes after it.
    #
    # Queens conflict when they are:
    #
    #   1. in the same row
    #   2. on the same diagonal

    def count_conflicts(board):
        conflicts = 0
        n = len(board)

        for i in range(n):
            for j in range(i + 1, n):
                if board[i] == board[j]:
                    conflicts += 1
                elif abs(board[i] - board[j]) == abs(i - j):
                    conflicts += 1

        return conflicts


# --------------------------------------------------
# TASK 2 — EXPLORE THE PROBLEM
# --------------------------------------------------

def generate_neighbours(problem, board):
    neighbours = []

    for action in problem.actions(board):
        neighbours.append(problem.result(board, action))

    return neighbours




# --------------------------------------------------
# TASK 3 — HILL CLIMBING
# --------------------------------------------------

def hill_climbing(problem, start_board):
    current = start_board
    current_cost = count_conflicts(current)

    while True:
        neighbours = generate_neighbours(problem, current)

        best = min(neighbours, key=count_conflicts)
        best_cost = count_conflicts(best)

        if best_cost >= current_cost:
            break

        current = best
        current_cost = best_cost

    return current


# --------------------------------------------------
# TASK 4 — SIMULATED ANNEALING
# --------------------------------------------------

def simulated_annealing(problem, start_board):
    current = start_board
    current_cost = count_conflicts(current)

    best = current
    best_cost = current_cost

    temperature = 10.0
    cooling_rate = 0.95
    steps_per_temperature = 100

    while temperature > 0.01 and best_cost > 0:
        for _ in range(steps_per_temperature):
            neighbour = random.choice(generate_neighbours(problem, current))
            neighbour_cost = count_conflicts(neighbour)
            delta = neighbour_cost - current_cost

            if delta < 0 or random.random() < math.exp(-delta / temperature):
                current = neighbour
                current_cost = neighbour_cost

                if current_cost < best_cost:
                    best = current
                    best_cost = current_cost
                    if best_cost == 0:
                        return best

        temperature *= cooling_rate

    return best


# --------------------------------------------------
# TESTING AREA
# --------------------------------------------------

if __name__ == "__main__":

    board = [
        random.randint(0, N - 1)
        for _ in range(N)
    ]

    problem = QueensProblem(board)

    print("\nRandom Board")
    print(board)

    print("\nConflicts")
    print(
        count_conflicts(board)
    )

    print("\nPossible Actions")

    actions = problem.actions(board)

    print(
        f"{len(actions)} actions available"
    )

    print("\nNeighbours")

    neighbours = generate_neighbours(
        problem,
        board
    )

    print(
        f"{len(neighbours)} neighbours generated"
    )