import pulp


def event_nuts(names, salaries, points, verbose=0):
    # Create the LP
    team = pulp.LpProblem("MaxScore", pulp.LpMaximize)

    # Create the binary variables
    x = pulp.LpVariable.dict('x_%s', names, cat='Binary')

    # Set up objective function: maximize the dot product of the variable vector and the score vector
    points_dict = dict(zip(names, points))
    team += sum(points_dict[i] * x[i] for i in names)

    # Salary constraint
    salary_dict = dict(zip(names, salaries))
    team += sum(salary_dict[i] * x[i] for i in names) <= 50000

    # Number of fighters constraint
    team += sum(x[i] for i in names) == 6

    # Solve the LP
    team.solve()

    if verbose == 0:
        return [name for name in names if x[name].varValue == 1]
    else:
        return [name for name in names if x[name].varValue == 1], pulp.value(team.objective)
