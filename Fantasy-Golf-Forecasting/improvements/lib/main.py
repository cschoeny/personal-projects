import create_2019
import stats_2019
import combine_stats_reg
import dk_filter
import simulation

print('Gathering the 2019 PGA Data\n')
create_2019.main()

print('Calculating the 2019 PGA Stats\n')
stats_2019.main()

print('Aggregating the previous 3 years of stats\n')
combine_stats_reg.main()

print('Combining our stats with the latest Draftkings contest\n')
dk_filter.main()

print('Running the contest simulation\n')
dk_final_score, made_cut = simulation.sim_conditions(par3=4, par4=10, par5=4, sims=1000)

print('Aggregating the results of the simulation\n')
simulation.aggregate_results(dk_final_score=dk_final_score, made_cut=made_cut)
