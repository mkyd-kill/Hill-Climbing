from numpy.random import seed, randint
from math import pow

def objective(x):
	return (0.0051 * pow(x, 5)) - (0.1367 * pow(x, 4)) + (1.24 * pow(x, 3)) - (4.456 * pow(x, 2))  + (5.66 * x) - 0.287

step_size = 0.5

n_iter = 20

def random_restart(objective, n_iter, step_size):
	solution = randint(0, 11)
	solution_eval = objective(solution)

	for i in range(n_iter + 1):
		candidate = randint(0, 11) * step_size
		candidate_eval = objective(candidate)

		if candidate_eval >= solution_eval:
			solution, solution_eval = candidate, candidate_eval
			print('>%d f(%s) = %.5f' % (i, solution, solution_eval))

	return [solution, solution_eval]

best, best_score = random_restart(objective, n_iter, step_size)

print('\nObjective Optimization Reached!')
print(f'Final State Coordinates (x, y) : {best} = {best_score}')
