import numpy as np
import random
random.seed(10)
from numpy import asarray

values=np.arange(-5,6)
def objective(x):
    return 2-(x**2)
#objective function
#step_size
stp=0.5
#number of interations
n=100
def hill_climbing(objective,n_interations,step_size):
    solution=np.random.randint(-5,6)
    solution_eval=objective(solution)
    scores=solution_eval
    for i in range(n_interations):
        cand=solution+np.random.randint(-5,6)*step_size
        cand_eval=objective(cand)
        if cand_eval>=solution_eval:
            solution,solution_eval=cand,cand_eval
            scores=solution_eval
        return [solution,scores]
    
hill_climbing(objective,n,stp)