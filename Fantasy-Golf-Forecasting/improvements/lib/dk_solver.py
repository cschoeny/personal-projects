import pulp
import pandas as pd
import time
import numpy as np


def main():
    timestr = time.strftime("%Y-%m-%d")
    df_results = pd.read_pickle('../stats/sim_results/results_' + timestr + '.pkl')

    # We don't want to choose someone that we don't have stats for.
    df_results = df_results[df_results['Have_Data']]

    # If we want to filter based on minimum rounds, this is where we would do it.
    # lets try with making it 40 minimum rounds
    # df_results = df_results[df_results['Rounds']>=31]

    # start the writing file
    f = open('../picks/' + timestr + '.txt', 'w')
    f.write(timestr + '\n')

    # %% Let's set up the LP for highest median score

    # initialize the LP problem
    team = pulp.LpProblem("MedianScore", pulp.LpMaximize)

    # create the LP variables (this is a binary variable for each golfer)
    names = list(df_results.index.values)
    x = pulp.LpVariable.dict('x_%s', names, cat='Binary')

    # set up the objective function
    # we want to maximize the dot product of the variable vector and the median score
    score = list(df_results['dk_median'] .values)
    score = dict(zip(names, score))
    team += sum(score[i] * x[i] for i in names)

    # Need to make sure that the players chosen are under the salary budget of 50000
    salary = list(df_results['Salary'].values)
    salary = dict(zip(names, salary))
    team += sum(salary[i] * x[i] for i in names) <= 50000

    # Need to make sure that we only choose 6 players
    team += sum(x[i] for i in names) == 6

    # solve
    team.solve()

    # display the final team
    f.write('\n\nMedian\n\n')
    total_salary = 0
    for i in names:
        if x[i].varValue == 1:
            total_salary += df_results.loc[i]['Salary']
            f.write(i + '\t' + str(salary[i]) + '\t' + str(df_results.loc[i]['dk_median']) + '\t' + 'Rounds: ' + str(df_results.loc[i]['Rounds']) + '\n')
    f.write('Total Salary: $' + str(total_salary))

    # %% Let's set up the LP for highest max score

    # initialize the LP problem
    team = pulp.LpProblem("MaxScore", pulp.LpMaximize)

    # create the LP variables (this is a binary variable for each golfer)
    names = list(df_results.index.values)
    x = pulp.LpVariable.dict('x_%s', names, cat='Binary')

    # set up the objective function
    # we want to maximize the dot product of the variable vector and the median score
    score = list(df_results['dk_max'] .values)
    score = dict(zip(names, score))
    team += sum(score[i] * x[i] for i in names)

    # Need to make sure that the players chosen are under the salary budget of 50000
    salary = list(df_results['Salary'].values)
    salary = dict(zip(names, salary))
    team += sum(salary[i] * x[i] for i in names) <= 50000

    # Need to make sure that we only choose 6 players
    team += sum(x[i] for i in names) == 6

    # solve
    team.solve()

    # display the final team
    f.write('\n\nMax\n\n')
    total_salary = 0

    for i in names:
        if x[i].varValue == 1:
            total_salary += df_results.loc[i]['Salary']
            f.write(i + '\t' + str(salary[i]) + '\t' + str(df_results.loc[i]['dk_max']) + '\t' + 'Rounds: ' + str(df_results.loc[i]['Rounds']) + '\n')
    f.write('Total Salary: $' + str(total_salary))

    # %% Let's set up the LP for highest min score

    # initialize the LP problem
    team = pulp.LpProblem("MinScore", pulp.LpMaximize)

    # create the LP variables (this is a binary variable for each golfer)
    names = list(df_results.index.values)
    x = pulp.LpVariable.dict('x_%s', names, cat='Binary')

    # set up the objective function
    # we want to maximize the dot product of the variable vector and the median score
    score = list(df_results['dk_min'] .values)
    score = dict(zip(names, score))
    team += sum(score[i] * x[i] for i in names)

    # Need to make sure that the players chosen are under the salary budget of 50000
    salary = list(df_results['Salary'].values)
    salary = dict(zip(names, salary))
    team += sum(salary[i] * x[i] for i in names) <= 50000

    # Need to make sure that we only choose 6 players
    team += sum(x[i] for i in names) == 6

    # solve
    team.solve()

    # display the final team
    f.write('\n\nMin\n\n')
    total_salary = 0
    for i in names:
        if x[i].varValue == 1:
            total_salary += df_results.loc[i]['Salary']
            f.write(i + '\t' + str(salary[i]) + '\t' + str(df_results.loc[i]['dk_min']) + '\t' + 'Rounds: ' + str(df_results.loc[i]['Rounds']) + '\n')
    f.write('Total Salary: $' + str(total_salary))

    # %% Let's set up the LP for highest mean score

    # initialize the LP problem
    team = pulp.LpProblem("MeanScore", pulp.LpMaximize)

    # create the LP variables (this is a binary variable for each golfer)
    names = list(df_results.index.values)
    x = pulp.LpVariable.dict('x_%s', names, cat='Binary')

    # set up the objective function
    # we want to maximize the dot product of the variable vector and the median score
    score = list(df_results['dk_mean'] .values)
    score = dict(zip(names, score))
    team += sum(score[i] * x[i] for i in names)

    # Need to make sure that the players chosen are under the salary budget of 50000
    salary = list(df_results['Salary'].values)
    salary = dict(zip(names, salary))
    team += sum(salary[i] * x[i] for i in names) <= 50000

    # Need to make sure that we only choose 6 players
    team += sum(x[i] for i in names) == 6

    # solve
    team.solve()

    # display the final team
    f.write('\n\nMean\n\n')
    total_salary = 0
    for i in names:
        if x[i].varValue == 1:
            total_salary += df_results.loc[i]['Salary']
            f.write(i + '\t' + str(salary[i]) + '\t' + str(df_results.loc[i]['dk_mean']) + '\t' + 'Rounds: ' + str(df_results.loc[i]['Rounds']) + '\n')
    f.write('Total Salary: $' + str(total_salary))

    # %% Let's set up the LP for highest 75% score

    # initialize the LP problem
    team = pulp.LpProblem("75Score", pulp.LpMaximize)

    # create the LP variables (this is a binary variable for each golfer)
    names = list(df_results.index.values)
    x = pulp.LpVariable.dict('x_%s', names, cat='Binary')

    # set up the objective function
    # we want to maximize the dot product of the variable vector and the median score
    score = list(df_results['dk_75'] .values)
    score = dict(zip(names, score))
    team += sum(score[i] * x[i] for i in names)

    # Need to make sure that the players chosen are under the salary budget of 50000
    salary = list(df_results['Salary'].values)
    salary = dict(zip(names, salary))
    team += sum(salary[i] * x[i] for i in names) <= 50000

    # Need to make sure that we only choose 6 players
    team += sum(x[i] for i in names) == 6

    # solve
    team.solve()

    # display the final team
    f.write('\n\n75th\n\n')
    total_salary = 0
    for i in names:
        if x[i].varValue == 1:
            total_salary += df_results.loc[i]['Salary']
            f.write(i + '\t' + str(salary[i]) + '\t' + str(df_results.loc[i]['dk_75']) + '\t' + 'Rounds: ' + str(df_results.loc[i]['Rounds']) + '\n')
    f.write('Total Salary: $' + str(total_salary))

    # %% Let's set up the LP for highest 25% score

    # initialize the LP problem
    team = pulp.LpProblem("25Score", pulp.LpMaximize)

    # create the LP variables (this is a binary variable for each golfer)
    names = list(df_results.index.values)
    x = pulp.LpVariable.dict('x_%s', names, cat='Binary')

    # set up the objective function
    # we want to maximize the dot product of the variable vector and the median score
    score = list(df_results['dk_25'] .values)
    score = dict(zip(names, score))
    team += sum(score[i] * x[i] for i in names)

    # Need to make sure that the players chosen are under the salary budget of 50000
    salary = list(df_results['Salary'].values)
    salary = dict(zip(names, salary))
    team += sum(salary[i] * x[i] for i in names) <= 50000

    # Need to make sure that we only choose 6 players
    team += sum(x[i] for i in names) == 6

    # solve
    team.solve()

    # display the final team
    f.write('\n\n25th\n\n')
    total_salary = 0
    for i in names:
        if x[i].varValue == 1:
            total_salary += df_results.loc[i]['Salary']
            f.write(i + '\t' + str(salary[i]) + '\t' + str(df_results.loc[i]['dk_25']) + '\t' + 'Rounds: ' + str(df_results.loc[i]['Rounds']) + '\n')
    f.write('Total Salary: $' + str(total_salary))

    # %% Let's set up the LP for highest make the cut percentage

    # initialize the LP problem
    team = pulp.LpProblem("MakeCut", pulp.LpMaximize)

    # create the LP variables (this is a binary variable for each golfer)
    names = list(df_results.index.values)
    x = pulp.LpVariable.dict('x_%s', names, cat='Binary')

    # set up the objective function
    # we want to maximize the dot product of the variable vector and the median score
    # need to do this a little different. Need to take the logarithm so that when we add them its the same as all 6 multiplying
    score = df_results['dk_makecut'] .values
    score = list(np.log(score))
    score = dict(zip(names, score))
    team += sum(score[i] * x[i] for i in names)

    # Need to make sure that the players chosen are under the salary budget of 50000
    salary = list(df_results['Salary'].values)
    salary = dict(zip(names, salary))
    team += sum(salary[i] * x[i] for i in names) <= 50000

    # Need to make sure that we only choose 6 players
    team += sum(x[i] for i in names) == 6

    # solve
    team.solve()

    # display the final team
    f.write('\n\nCut\n\n')
    total_salary = 0
    for i in names:
        if x[i].varValue == 1:
            total_salary += df_results.loc[i]['Salary']
            f.write(i + '\t' + str(salary[i]) + '\t' + str(df_results.loc[i]['dk_makecut']) + '\t' + 'Rounds: ' + str(df_results.loc[i]['Rounds']) + '\n')
    f.write('Total Salary: $' + str(total_salary))
    f.close()


if __name__ == '__main__':
    main()
