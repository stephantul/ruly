import numpy as np


def rule(width, num_steps, start_indices, num):
    """
    Apply a rule for a number of iterations times.

    :param width: The width of the canvas.
    :param num_steps: The number of iterations.
    :param start_indices: The indices of the starting vector which start as 1.
    :param num: The number of the rule.
    """
    vec = np.zeros(width, dtype=np.int32)
    vec[start_indices] = 1

    l = np.array([np.int(x) for x in reversed("{0:08b}".format(num))])

    total = []

    for x in range(num_steps):
        vec = step(vec, l)
        total.append(vec)

    return np.array(total)


def step(vec, rules):
    """
    Perform a single step.

    :param vec: The input vector.
    :param rules: An array of transfer rules.
    :return: A transformed vector.
    """
    # Start with an array of zeros
    n_vec = np.zeros_like(vec, dtype=np.int)
    mask = np.array([4, 2, 1])
    vec = np.stack([vec[:-2], vec[1:-1], vec[2:]], 1) * mask[None, :]
    n_vec[1:-1] = np.array([rules[x] for x in vec.sum(1)])
    return n_vec
