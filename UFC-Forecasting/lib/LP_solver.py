import pulp


def event_nuts(names, salaries, points):
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

    return [name for name in names if x[name].varValue == 1]
#
#
# Initialize the LP
# team = pulp.LpProblem("MaxScore", pulp.LpMaximize)
#
# # small example FIRST
# names = ['clayton', 'matt', 'diego', 'jeff']
# salaries = [50, 60, 30, 25]
# scores = [100, 200, 150, 115]
# # set up variables
# x = pulp.LpVariable.dict('x_%s', names, cat='Binary')
# x
# # set up objective function
# # maximize the dot product of the variable vector and the score vector
# score = dict(zip(names, scores))
# team += sum(score[i] * x[i] for i in names)
# # salary constraint
# salary = dict(zip(names, salaries))
# team += sum(salary[i] * x[i] for i in names) <= 100
# # num fighters constraint
# team += sum(x[i] for i in names) == 2
# team
# # solve
# team.solve()
#
# for i in names:
#     print(x[i].varValue)
