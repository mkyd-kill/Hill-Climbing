# hill climbing search of a one-dimensional objective function f(x) = 2 - x^2
from numpy import asarray
from numpy.random import randint
from numpy.random import seed

""""
    n_iterations: Number of loop iterations
    bounds: Fixed closed range of values
    step_size: Relative to the bounds of search space
    r_min, r_max: Min & Max range of bound inputs
    x_optima: x at the optimal input point
"""

# objective function
def objective(x):
	return 2 - (x**2)

# hill climbing local search algorithm
def hillclimbing(objective, bounds, n_iterations, step_size):
	# generate an initial point
	solution = bounds[:, 0] + randint(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
	# evaluate the initial point
	solution_eval = objective(solution)
	# run the hill climb
	solutions = list()
	solutions.append(solution)
	for i in range(n_iterations):
		# take a step
		candidate = solution + randint(len(bounds)) * step_size
		# evaluate candidate point
		candidte_eval = objective(candidate)
		# check if we should keep the new point
		if candidte_eval >= solution_eval:
			# store the new point
			solution, solution_eval = candidate, candidte_eval
			# keep track of solutions
			solutions.append(solution)
			# report progress
			print('>%d f(%s) = %.5f' % (i, solution, solution_eval))
	return [solution, solution_eval, solutions]

# seed the pseudorandom number generator
seed(5)

# define range for input
bounds = asarray([[-5.0, 5.0]])

# define the total iterations
n_iterations = 100

# define the maximum step size
step_size = 0.5

# perform the hill climbing search
best, score, solutions = hillclimbing(objective, bounds, n_iterations, step_size)
print('\nOptimization Objective Reached!')
print(f"Final State Coordinates {best} = {score}")