from numpy.random import randint
from random import seed

step_size = 0.1 # change it to 0.1

n_iter = 100

def objective(x):
    return 2 - (x**2)

def hillclimbing(objective, n_iter, step_size):
    solution = randint(-5, 6)
    solution_eval = objective(solution)
    score = solution_eval

    for i in range(n_iter):
        candidate = solution + randint(-5, 6) * step_size
        candidate_eval = objective(candidate)

        if candidate_eval >= solution_eval:
            solution, solution_eval = candidate, candidate_eval
            print('>%d f(%s) = %.5f' % (i, solution, solution_eval))

    return [solution, solution_eval]

seed(10)

best, best_score = hillclimbing(objective, n_iter, step_size)

print('\nOptimization Objective Reached!')
print(f"Final State Coordinates {best} = {best_score}")