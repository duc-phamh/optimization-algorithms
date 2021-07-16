import numpy as np


def sign(var, coeffs):
    # Return a vector of signs for the input variable and coeffs
    a = np.sum(var * coeffs[:-1], axis=1) + coeffs[-1]
    return 100 * a / np.sqrt(1 + 10000 * a ** 2)


def f(coeffs):
    # Our loss function
    return sum(1 - y * sign(x, coeffs))


def sort(f_val, coeffs):
    # We represent the solutions as 2 numpy arrays
    # f_val: the objective function value of the solutions
    # coeffs: the coefficients of the solutions
    order = np.argsort(f_val)
    return f_val[order], coeffs[order]


def initialize(solution_qty, coeff_length):
    # Randomly initialize 'qty' sets of coefficients and corresponding
    # objective function value
    coeffs = np.random.randint(-10, 10, (solution_qty, coeff_length))
    f_val = np.apply_along_axis(f, 1, coeffs)
    return f_val, coeffs


def optimize(x, y, alpha=1, gamma=2, ro=1 / 2, sigma=1 / 2, max_iter=1000):
    # Get the length of the list of coefficients
    length = len(x[0]) + 1

    # Randomly initialize (length + 1) sets of coefficients
    f_val, coeffs = initialize(length + 1, length)

    iteration = 0
    while f_val[0] > 0 and iteration < max_iter:
        iteration += 1

        # If all solutions have equal result, the algorithm would stuck
        # We'll restart it.
        if len(set(f_val)) == 1:
            f_val, coeffs = initialize(length + 1, length)
            iteration = 0
        if iteration == max_iter:
            return coeffs[0]

        # Sort the solutions
        f_val, coeffs = sort(f_val, coeffs)

        # Calculate the centroid
        centroid = np.mean(coeffs, axis=0)

        # Getting the worst and best current point
        worst = coeffs[-1]
        f_worst = f_val[-1]
        best = coeffs[0]
        f_best = f_val[0]

        # Reflection
        reflection = centroid + alpha * (centroid - worst)
        f_reflection = f(reflection)

        if (f_best <= f_reflection) and (f_reflection < f_worst):
            # Replace the worst point with reflection
            f_val[-1] = f_reflection
            coeffs[-1] = reflection
            continue
        elif f_reflection < f_best:
            # Expansion
            expansion = centroid + gamma * (reflection - centroid)
            f_expansion = f(expansion)

            if f_expansion < f_reflection:
                # Obtain a new simplex by replacing the worst point with the expanded point
                # and continue
                f_val[-1] = f_expansion
                coeffs[-1] = expansion
                continue
            else:
                # Obtain a new simplex by replacing the worst point with the reflected point
                # and continue
                f_val[-1] = f_reflection
                coeffs[-1] = reflection
                continue

        # Contraction:
        contraction = centroid + ro * (worst - centroid)
        f_contraction = f(contraction)
        if f_contraction < f_worst:
            # Obtain a new simplex by replacing the worst point with the contracted point
            # and continue
            f_val[-1] = f_contraction
            coeffs[-1] = contraction
            continue
        else:
            # Shrink
            coeffs = best + sigma * (coeffs - best)
            f_val = np.apply_along_axis(f, 1, coeffs)

    return coeffs[0]


result = optimize(x, y)
print(" ".join([str(i) for i in result]))
