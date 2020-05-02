# range is: 402328-864247


def non_decreasing(n):
    n = str(n)
    for idx in range(1, len(n)):
        if n[idx] < n[idx - 1]:
            return False
    return True


def has_repeat(n):
    n = str(n)
    for idx in range(1, len(n)):
        if n[idx] == n[idx - 1]:
            return True
    return False


def find_soln():
    num_solns = 0
    for n in range(402328, 864248):
        # First check if non-decreasing
        if not non_decreasing(n):
            continue
        if has_repeat(n):
            num_solns += 1
    return num_solns

find_soln()
