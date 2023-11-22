from itertools import combinations

def my_sum(x, y):
    """A function that sums. """
    return x+y


def my_mul(x, y):
    """A function that multiply. """
    return x*y
    
def subconjuntos(conjunto):
    todos = []
    for i in range(len(conjunto)+1):
        for sub in combinations(conjunto, i):
            todos.append(set(sub))

    return todos
