"""
TU850-3
AINL3001 — Knowledge-Driven AI
Dr. Bianca Schoen-Phelan
2026

Week 4 Tutorial
Introducing the Problem Class

This solution shows how the familiar grid-world problem
can be represented using the common Problem class.
"""

from common.problem import Problem


GRID_SIZE = 5


class GridProblem(Problem):
    """
    A simple grid-world problem.

    A state is represented as an (x, y) coordinate.

    Example:

        (0, 0) = top-left corner
        (4, 4) = bottom-right corner
    """

    def actions(self, state):
        """
        Return the valid actions from this state.

        Possible actions:

            UP
            DOWN
            LEFT
            RIGHT
        """

        x, y = state
        actions = []

        # Can we move up?
        if y > 0:
            actions.append("UP")

        # Can we move down?
        if y < GRID_SIZE - 1:
            actions.append("DOWN")

        # Can we move left?
        if x > 0:
            actions.append("LEFT")

        # Can we move right?
        if x < GRID_SIZE - 1:
            actions.append("RIGHT")

        return actions

    def result(self, state, action):
        """
        Return the new state produced by performing an action.

        Example:

            state  = (0, 0)
            action = "RIGHT"

            result = (1, 0)
        """

        x, y = state

        if action == "UP":
            return (x, y - 1        
        if action == "DOWN":
            return (x, y + 1        
        if action == "LEFT":
            return (x - 1, y        
        if action == "RIGHT":
            return (x + 1, y)

        raise ValueError(f"Unknown action: {action}")


# --------------------------------------------------
# CREATE A PROBLEM
# --------------------------------------------------

problem = GridProblem(
    initial=(0, 0),
    goal=(4, 4)
)


# --------------------------------------------------
# EXPLORE THE PROBLEM
# --------------------------------------------------

print("Initial state:", problem.initial)
print("Goal:", problem.goal)


print("\nActions from (0, 0):")

actions = problem.actions((0, 0))

print(actions)


print("\nResults of those actions:")

for action in actions:

    new_state = problem.result(
        (0, 0),
        action
    )

    print(
        action,
        "->",
        new_state
    )


print("\nIs (4, 4) the goal?")

print(
    problem.goal_test((4, 4))
)


# --------------------------------------------------
# TRY ANOTHER STATE
# --------------------------------------------------

test_state = (2, 2)

print(
    f"\nActions from {test_state}:"
)

actions = problem.actions(test_state)

print(actions)


print("\nResults of those actions:")

for action in actions:

    new_state = problem.result(
        test_state,
        action
    )

    print(
        action,
        "->",
        new_state
    )


# --------------------------------------------------
# REFLECTION QUESTIONS
# --------------------------------------------------

"""
Be ready to discuss:

1. What information is stored in problem.initial?

2. What information is stored in problem.goal?

3. What is the difference between:

       problem.actions(state)

   and:

       problem.result(state, action)

4. Why doesn't Problem know anything about grids?

5. Why doesn't GridProblem know anything about search?

6. Could the same Problem structure be used for something
   other than a grid?
"""