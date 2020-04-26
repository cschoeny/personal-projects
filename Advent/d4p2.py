# range is: 402328-864247


def non_decreasing(n):
    n = str(n)
    for idx in range(1, len(n)):
        if n[idx] < n[idx - 1]:
            return False
    return True

# okay, just need to make sure there is 1 valid one. forget about others. once we find 2 in a row, check before and after and return true, else continue
def has_repeat(n):
    n = str(n)
    for idx in range(1, len(n)):
        if n[idx] == n[idx - 1]:
            try:
                before = n[idx-2]
            except IndexError:
                before = -1
            try:
                after = n[idx+1]
            except IndexError:
                after = -1
            if before != n[idx] and after != n[idx]:
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
