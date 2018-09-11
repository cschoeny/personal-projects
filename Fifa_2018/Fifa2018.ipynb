{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# <center>FIFA 18 Player Dataset Exploration</center>\n",
    "![fifa](images\\fifa.jpg)\n",
    "\n",
    "# Table of contents\n",
    "1. [Initial Exploration](#initial)\n",
    "2. [Positions](#positions)\n",
    "3. [Height and Weight](#height)\n",
    "4. [Top 5 Leagues](#leagues)\n",
    "5. [England vs. Germany PKs](#PKs)\n",
    "6. [Southpaws](#southpaws)\n",
    "6. [Similarity](#similarity)\n",
    "\n",
    "# Initial Exploration <a name=\"initial\"></a>\n",
    "The FIFA videogame franchise is a worldwide phenomenon, accounting for [roughly 40%](https://www.forbes.com/sites/greatspeculations/2017/10/10/fifa-remains-eas-bread-and-butter/#4b55f3ef2140) of Electronic Arts' yearly revenue. FIFA 18, released in Nov. 2017, sold 5.9 million units in its first week alone, and surpassed 10 million units by the end of the year. In order to meet the demands of soccer fanatics across the globe, EA strives for accuracy, and as such, each FIFA iteration includes an enormous database of player statistics. In this notebook, we explore the FIFA 18 database (retrieved from [Kaggle](https://www.kaggle.com/thec03u5/fifa-18-demo-player-dataset)).\n",
    "\n",
    "Let's begin by getting an idea at the scope of the dataset."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline\n",
    "import numpy as np\n",
    "\n",
    "plt.style.use('seaborn')\n",
    "\n",
    "fifa = pd.read_csv('complete.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Players:\t17994\n",
      "Nationalities:\t164\n",
      "Clubs:\t\t647\n",
      "Leagues:\t41\n"
     ]
    }
   ],
   "source": [
    "print('Players:', '\\t', fifa.shape[0], '\\n',\n",
    "      'Nationalities:', '\\t', fifa.groupby('nationality')['ID'].count().size, '\\n',\n",
    "      'Clubs:', '\\t\\t', fifa.groupby('club')['ID'].count().size, '\\n',\n",
    "      'Leagues:', '\\t', fifa.groupby('league')['ID'].count().size, sep='')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Wow, that is a lot of players and clubs. Now let's look at what data the dataframe actually contains. Note that the players in the dataframe are indexed in descending order based on the **overall** stat, which is commonly viewed as the most important/significant stat for a player."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ID</th>\n",
       "      <th>name</th>\n",
       "      <th>full_name</th>\n",
       "      <th>club</th>\n",
       "      <th>club_logo</th>\n",
       "      <th>special</th>\n",
       "      <th>age</th>\n",
       "      <th>league</th>\n",
       "      <th>birth_date</th>\n",
       "      <th>height_cm</th>\n",
       "      <th>weight_kg</th>\n",
       "      <th>body_type</th>\n",
       "      <th>real_face</th>\n",
       "      <th>flag</th>\n",
       "      <th>nationality</th>\n",
       "      <th>photo</th>\n",
       "      <th>eur_value</th>\n",
       "      <th>eur_wage</th>\n",
       "      <th>eur_release_clause</th>\n",
       "      <th>overall</th>\n",
       "      <th>potential</th>\n",
       "      <th>pac</th>\n",
       "      <th>sho</th>\n",
       "      <th>pas</th>\n",
       "      <th>dri</th>\n",
       "      <th>def</th>\n",
       "      <th>phy</th>\n",
       "      <th>international_reputation</th>\n",
       "      <th>skill_moves</th>\n",
       "      <th>weak_foot</th>\n",
       "      <th>work_rate_att</th>\n",
       "      <th>work_rate_def</th>\n",
       "      <th>preferred_foot</th>\n",
       "      <th>crossing</th>\n",
       "      <th>finishing</th>\n",
       "      <th>heading_accuracy</th>\n",
       "      <th>short_passing</th>\n",
       "      <th>volleys</th>\n",
       "      <th>dribbling</th>\n",
       "      <th>curve</th>\n",
       "      <th>free_kick_accuracy</th>\n",
       "      <th>long_passing</th>\n",
       "      <th>ball_control</th>\n",
       "      <th>acceleration</th>\n",
       "      <th>sprint_speed</th>\n",
       "      <th>agility</th>\n",
       "      <th>reactions</th>\n",
       "      <th>balance</th>\n",
       "      <th>shot_power</th>\n",
       "      <th>jumping</th>\n",
       "      <th>stamina</th>\n",
       "      <th>strength</th>\n",
       "      <th>long_shots</th>\n",
       "      <th>aggression</th>\n",
       "      <th>interceptions</th>\n",
       "      <th>positioning</th>\n",
       "      <th>vision</th>\n",
       "      <th>penalties</th>\n",
       "      <th>composure</th>\n",
       "      <th>marking</th>\n",
       "      <th>standing_tackle</th>\n",
       "      <th>sliding_tackle</th>\n",
       "      <th>gk_diving</th>\n",
       "      <th>gk_handling</th>\n",
       "      <th>gk_kicking</th>\n",
       "      <th>gk_positioning</th>\n",
       "      <th>gk_reflexes</th>\n",
       "      <th>rs</th>\n",
       "      <th>rw</th>\n",
       "      <th>rf</th>\n",
       "      <th>ram</th>\n",
       "      <th>rcm</th>\n",
       "      <th>rm</th>\n",
       "      <th>rdm</th>\n",
       "      <th>rcb</th>\n",
       "      <th>rb</th>\n",
       "      <th>rwb</th>\n",
       "      <th>st</th>\n",
       "      <th>lw</th>\n",
       "      <th>cf</th>\n",
       "      <th>cam</th>\n",
       "      <th>cm</th>\n",
       "      <th>lm</th>\n",
       "      <th>cdm</th>\n",
       "      <th>cb</th>\n",
       "      <th>lb</th>\n",
       "      <th>lwb</th>\n",
       "      <th>ls</th>\n",
       "      <th>lf</th>\n",
       "      <th>lam</th>\n",
       "      <th>lcm</th>\n",
       "      <th>ldm</th>\n",
       "      <th>lcb</th>\n",
       "      <th>gk</th>\n",
       "      <th>1_on_1_rush_trait</th>\n",
       "      <th>acrobatic_clearance_trait</th>\n",
       "      <th>argues_with_officials_trait</th>\n",
       "      <th>avoids_using_weaker_foot_trait</th>\n",
       "      <th>backs_into_player_trait</th>\n",
       "      <th>bicycle_kicks_trait</th>\n",
       "      <th>cautious_with_crosses_trait</th>\n",
       "      <th>chip_shot_trait</th>\n",
       "      <th>chipped_penalty_trait</th>\n",
       "      <th>comes_for_crosses_trait</th>\n",
       "      <th>corner_specialist_trait</th>\n",
       "      <th>diver_trait</th>\n",
       "      <th>dives_into_tackles_trait</th>\n",
       "      <th>diving_header_trait</th>\n",
       "      <th>driven_pass_trait</th>\n",
       "      <th>early_crosser_trait</th>\n",
       "      <th>fan's_favourite_trait</th>\n",
       "      <th>fancy_flicks_trait</th>\n",
       "      <th>finesse_shot_trait</th>\n",
       "      <th>flair_trait</th>\n",
       "      <th>flair_passes_trait</th>\n",
       "      <th>gk_flat_kick_trait</th>\n",
       "      <th>gk_long_throw_trait</th>\n",
       "      <th>gk_up_for_corners_trait</th>\n",
       "      <th>giant_throw_in_trait</th>\n",
       "      <th>inflexible_trait</th>\n",
       "      <th>injury_free_trait</th>\n",
       "      <th>injury_prone_trait</th>\n",
       "      <th>leadership_trait</th>\n",
       "      <th>long_passer_trait</th>\n",
       "      <th>long_shot_taker_trait</th>\n",
       "      <th>long_throw_in_trait</th>\n",
       "      <th>one_club_player_trait</th>\n",
       "      <th>outside_foot_shot_trait</th>\n",
       "      <th>playmaker_trait</th>\n",
       "      <th>power_free_kick_trait</th>\n",
       "      <th>power_header_trait</th>\n",
       "      <th>puncher_trait</th>\n",
       "      <th>rushes_out_of_goal_trait</th>\n",
       "      <th>saves_with_feet_trait</th>\n",
       "      <th>second_wind_trait</th>\n",
       "      <th>selfish_trait</th>\n",
       "      <th>skilled_dribbling_trait</th>\n",
       "      <th>stutter_penalty_trait</th>\n",
       "      <th>swerve_pass_trait</th>\n",
       "      <th>takes_finesse_free_kicks_trait</th>\n",
       "      <th>target_forward_trait</th>\n",
       "      <th>team_player_trait</th>\n",
       "      <th>technical_dribbler_trait</th>\n",
       "      <th>tries_to_beat_defensive_line_trait</th>\n",
       "      <th>poacher_speciality</th>\n",
       "      <th>speedster_speciality</th>\n",
       "      <th>aerial_threat_speciality</th>\n",
       "      <th>dribbler_speciality</th>\n",
       "      <th>playmaker_speciality</th>\n",
       "      <th>engine_speciality</th>\n",
       "      <th>distance_shooter_speciality</th>\n",
       "      <th>crosser_speciality</th>\n",
       "      <th>free_kick_specialist_speciality</th>\n",
       "      <th>tackling_speciality</th>\n",
       "      <th>tactician_speciality</th>\n",
       "      <th>acrobat_speciality</th>\n",
       "      <th>strength_speciality</th>\n",
       "      <th>clinical_finisher_speciality</th>\n",
       "      <th>prefers_rs</th>\n",
       "      <th>prefers_rw</th>\n",
       "      <th>prefers_rf</th>\n",
       "      <th>prefers_ram</th>\n",
       "      <th>prefers_rcm</th>\n",
       "      <th>prefers_rm</th>\n",
       "      <th>prefers_rdm</th>\n",
       "      <th>prefers_rcb</th>\n",
       "      <th>prefers_rb</th>\n",
       "      <th>prefers_rwb</th>\n",
       "      <th>prefers_st</th>\n",
       "      <th>prefers_lw</th>\n",
       "      <th>prefers_cf</th>\n",
       "      <th>prefers_cam</th>\n",
       "      <th>prefers_cm</th>\n",
       "      <th>prefers_lm</th>\n",
       "      <th>prefers_cdm</th>\n",
       "      <th>prefers_cb</th>\n",
       "      <th>prefers_lb</th>\n",
       "      <th>prefers_lwb</th>\n",
       "      <th>prefers_ls</th>\n",
       "      <th>prefers_lf</th>\n",
       "      <th>prefers_lam</th>\n",
       "      <th>prefers_lcm</th>\n",
       "      <th>prefers_ldm</th>\n",
       "      <th>prefers_lcb</th>\n",
       "      <th>prefers_gk</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>20801</td>\n",
       "      <td>Cristiano Ronaldo</td>\n",
       "      <td>C. Ronaldo dos Santos Aveiro</td>\n",
       "      <td>Real Madrid CF</td>\n",
       "      <td>https://cdn.sofifa.org/18/teams/243.png</td>\n",
       "      <td>2228</td>\n",
       "      <td>32</td>\n",
       "      <td>Spanish Primera División</td>\n",
       "      <td>1985-02-05</td>\n",
       "      <td>185.0</td>\n",
       "      <td>80.0</td>\n",
       "      <td>C. Ronaldo</td>\n",
       "      <td>True</td>\n",
       "      <td>https://cdn.sofifa.org/flags/38@3x.png</td>\n",
       "      <td>Portugal</td>\n",
       "      <td>https://cdn.sofifa.org/18/players/20801.png</td>\n",
       "      <td>95500000.0</td>\n",
       "      <td>565000.0</td>\n",
       "      <td>195800000.0</td>\n",
       "      <td>94</td>\n",
       "      <td>94</td>\n",
       "      <td>90</td>\n",
       "      <td>93</td>\n",
       "      <td>82</td>\n",
       "      <td>90</td>\n",
       "      <td>33</td>\n",
       "      <td>80</td>\n",
       "      <td>5</td>\n",
       "      <td>5</td>\n",
       "      <td>4</td>\n",
       "      <td>High</td>\n",
       "      <td>Low</td>\n",
       "      <td>Right</td>\n",
       "      <td>85</td>\n",
       "      <td>94</td>\n",
       "      <td>88</td>\n",
       "      <td>83</td>\n",
       "      <td>88</td>\n",
       "      <td>91</td>\n",
       "      <td>81</td>\n",
       "      <td>76</td>\n",
       "      <td>77</td>\n",
       "      <td>93</td>\n",
       "      <td>89</td>\n",
       "      <td>91</td>\n",
       "      <td>89</td>\n",
       "      <td>96</td>\n",
       "      <td>63</td>\n",
       "      <td>94</td>\n",
       "      <td>95</td>\n",
       "      <td>92</td>\n",
       "      <td>80</td>\n",
       "      <td>92</td>\n",
       "      <td>63</td>\n",
       "      <td>29</td>\n",
       "      <td>95</td>\n",
       "      <td>85</td>\n",
       "      <td>85</td>\n",
       "      <td>95</td>\n",
       "      <td>22</td>\n",
       "      <td>31</td>\n",
       "      <td>23</td>\n",
       "      <td>7</td>\n",
       "      <td>11</td>\n",
       "      <td>15</td>\n",
       "      <td>14</td>\n",
       "      <td>11</td>\n",
       "      <td>92.0</td>\n",
       "      <td>91.0</td>\n",
       "      <td>91.0</td>\n",
       "      <td>89.0</td>\n",
       "      <td>82.0</td>\n",
       "      <td>89.0</td>\n",
       "      <td>62.0</td>\n",
       "      <td>53.0</td>\n",
       "      <td>61.0</td>\n",
       "      <td>66.0</td>\n",
       "      <td>92.0</td>\n",
       "      <td>91.0</td>\n",
       "      <td>91.0</td>\n",
       "      <td>89.0</td>\n",
       "      <td>82.0</td>\n",
       "      <td>89.0</td>\n",
       "      <td>62.0</td>\n",
       "      <td>53.0</td>\n",
       "      <td>61.0</td>\n",
       "      <td>66.0</td>\n",
       "      <td>92.0</td>\n",
       "      <td>91.0</td>\n",
       "      <td>89.0</td>\n",
       "      <td>82.0</td>\n",
       "      <td>62.0</td>\n",
       "      <td>53.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>158023</td>\n",
       "      <td>L. Messi</td>\n",
       "      <td>Lionel Messi</td>\n",
       "      <td>FC Barcelona</td>\n",
       "      <td>https://cdn.sofifa.org/18/teams/241.png</td>\n",
       "      <td>2158</td>\n",
       "      <td>30</td>\n",
       "      <td>Spanish Primera División</td>\n",
       "      <td>1987-06-24</td>\n",
       "      <td>170.0</td>\n",
       "      <td>72.0</td>\n",
       "      <td>Messi</td>\n",
       "      <td>True</td>\n",
       "      <td>https://cdn.sofifa.org/flags/52@3x.png</td>\n",
       "      <td>Argentina</td>\n",
       "      <td>https://cdn.sofifa.org/18/players/158023.png</td>\n",
       "      <td>105000000.0</td>\n",
       "      <td>565000.0</td>\n",
       "      <td>215300000.0</td>\n",
       "      <td>93</td>\n",
       "      <td>93</td>\n",
       "      <td>89</td>\n",
       "      <td>90</td>\n",
       "      <td>86</td>\n",
       "      <td>96</td>\n",
       "      <td>26</td>\n",
       "      <td>61</td>\n",
       "      <td>5</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>Medium</td>\n",
       "      <td>Medium</td>\n",
       "      <td>Left</td>\n",
       "      <td>77</td>\n",
       "      <td>95</td>\n",
       "      <td>71</td>\n",
       "      <td>88</td>\n",
       "      <td>85</td>\n",
       "      <td>97</td>\n",
       "      <td>89</td>\n",
       "      <td>90</td>\n",
       "      <td>87</td>\n",
       "      <td>95</td>\n",
       "      <td>92</td>\n",
       "      <td>87</td>\n",
       "      <td>90</td>\n",
       "      <td>95</td>\n",
       "      <td>95</td>\n",
       "      <td>85</td>\n",
       "      <td>68</td>\n",
       "      <td>73</td>\n",
       "      <td>59</td>\n",
       "      <td>88</td>\n",
       "      <td>48</td>\n",
       "      <td>22</td>\n",
       "      <td>93</td>\n",
       "      <td>90</td>\n",
       "      <td>78</td>\n",
       "      <td>96</td>\n",
       "      <td>13</td>\n",
       "      <td>28</td>\n",
       "      <td>26</td>\n",
       "      <td>6</td>\n",
       "      <td>11</td>\n",
       "      <td>15</td>\n",
       "      <td>14</td>\n",
       "      <td>8</td>\n",
       "      <td>88.0</td>\n",
       "      <td>91.0</td>\n",
       "      <td>92.0</td>\n",
       "      <td>92.0</td>\n",
       "      <td>84.0</td>\n",
       "      <td>90.0</td>\n",
       "      <td>59.0</td>\n",
       "      <td>45.0</td>\n",
       "      <td>57.0</td>\n",
       "      <td>62.0</td>\n",
       "      <td>88.0</td>\n",
       "      <td>91.0</td>\n",
       "      <td>92.0</td>\n",
       "      <td>92.0</td>\n",
       "      <td>84.0</td>\n",
       "      <td>90.0</td>\n",
       "      <td>59.0</td>\n",
       "      <td>45.0</td>\n",
       "      <td>57.0</td>\n",
       "      <td>62.0</td>\n",
       "      <td>88.0</td>\n",
       "      <td>92.0</td>\n",
       "      <td>92.0</td>\n",
       "      <td>84.0</td>\n",
       "      <td>59.0</td>\n",
       "      <td>45.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>190871</td>\n",
       "      <td>Neymar</td>\n",
       "      <td>Neymar da Silva Santos Jr.</td>\n",
       "      <td>Paris Saint-Germain</td>\n",
       "      <td>https://cdn.sofifa.org/18/teams/73.png</td>\n",
       "      <td>2100</td>\n",
       "      <td>25</td>\n",
       "      <td>French Ligue 1</td>\n",
       "      <td>1992-02-05</td>\n",
       "      <td>175.0</td>\n",
       "      <td>68.0</td>\n",
       "      <td>Neymar</td>\n",
       "      <td>True</td>\n",
       "      <td>https://cdn.sofifa.org/flags/54@3x.png</td>\n",
       "      <td>Brazil</td>\n",
       "      <td>https://cdn.sofifa.org/18/players/190871.png</td>\n",
       "      <td>123000000.0</td>\n",
       "      <td>280000.0</td>\n",
       "      <td>236800000.0</td>\n",
       "      <td>92</td>\n",
       "      <td>94</td>\n",
       "      <td>92</td>\n",
       "      <td>84</td>\n",
       "      <td>79</td>\n",
       "      <td>95</td>\n",
       "      <td>30</td>\n",
       "      <td>60</td>\n",
       "      <td>5</td>\n",
       "      <td>5</td>\n",
       "      <td>5</td>\n",
       "      <td>High</td>\n",
       "      <td>Medium</td>\n",
       "      <td>Right</td>\n",
       "      <td>75</td>\n",
       "      <td>89</td>\n",
       "      <td>62</td>\n",
       "      <td>81</td>\n",
       "      <td>83</td>\n",
       "      <td>96</td>\n",
       "      <td>81</td>\n",
       "      <td>84</td>\n",
       "      <td>75</td>\n",
       "      <td>95</td>\n",
       "      <td>94</td>\n",
       "      <td>90</td>\n",
       "      <td>96</td>\n",
       "      <td>88</td>\n",
       "      <td>82</td>\n",
       "      <td>80</td>\n",
       "      <td>61</td>\n",
       "      <td>78</td>\n",
       "      <td>53</td>\n",
       "      <td>77</td>\n",
       "      <td>56</td>\n",
       "      <td>36</td>\n",
       "      <td>90</td>\n",
       "      <td>80</td>\n",
       "      <td>81</td>\n",
       "      <td>92</td>\n",
       "      <td>21</td>\n",
       "      <td>24</td>\n",
       "      <td>33</td>\n",
       "      <td>9</td>\n",
       "      <td>9</td>\n",
       "      <td>15</td>\n",
       "      <td>15</td>\n",
       "      <td>11</td>\n",
       "      <td>84.0</td>\n",
       "      <td>89.0</td>\n",
       "      <td>88.0</td>\n",
       "      <td>88.0</td>\n",
       "      <td>79.0</td>\n",
       "      <td>87.0</td>\n",
       "      <td>59.0</td>\n",
       "      <td>46.0</td>\n",
       "      <td>59.0</td>\n",
       "      <td>64.0</td>\n",
       "      <td>84.0</td>\n",
       "      <td>89.0</td>\n",
       "      <td>88.0</td>\n",
       "      <td>88.0</td>\n",
       "      <td>79.0</td>\n",
       "      <td>87.0</td>\n",
       "      <td>59.0</td>\n",
       "      <td>46.0</td>\n",
       "      <td>59.0</td>\n",
       "      <td>64.0</td>\n",
       "      <td>84.0</td>\n",
       "      <td>88.0</td>\n",
       "      <td>88.0</td>\n",
       "      <td>79.0</td>\n",
       "      <td>59.0</td>\n",
       "      <td>46.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>176580</td>\n",
       "      <td>L. Suárez</td>\n",
       "      <td>Luis Suárez</td>\n",
       "      <td>FC Barcelona</td>\n",
       "      <td>https://cdn.sofifa.org/18/teams/241.png</td>\n",
       "      <td>2291</td>\n",
       "      <td>30</td>\n",
       "      <td>Spanish Primera División</td>\n",
       "      <td>1987-01-24</td>\n",
       "      <td>182.0</td>\n",
       "      <td>86.0</td>\n",
       "      <td>Normal</td>\n",
       "      <td>True</td>\n",
       "      <td>https://cdn.sofifa.org/flags/60@3x.png</td>\n",
       "      <td>Uruguay</td>\n",
       "      <td>https://cdn.sofifa.org/18/players/176580.png</td>\n",
       "      <td>97000000.0</td>\n",
       "      <td>510000.0</td>\n",
       "      <td>198900000.0</td>\n",
       "      <td>92</td>\n",
       "      <td>92</td>\n",
       "      <td>82</td>\n",
       "      <td>90</td>\n",
       "      <td>79</td>\n",
       "      <td>87</td>\n",
       "      <td>42</td>\n",
       "      <td>81</td>\n",
       "      <td>5</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>High</td>\n",
       "      <td>Medium</td>\n",
       "      <td>Right</td>\n",
       "      <td>77</td>\n",
       "      <td>94</td>\n",
       "      <td>77</td>\n",
       "      <td>83</td>\n",
       "      <td>88</td>\n",
       "      <td>86</td>\n",
       "      <td>86</td>\n",
       "      <td>84</td>\n",
       "      <td>64</td>\n",
       "      <td>91</td>\n",
       "      <td>88</td>\n",
       "      <td>77</td>\n",
       "      <td>86</td>\n",
       "      <td>93</td>\n",
       "      <td>60</td>\n",
       "      <td>87</td>\n",
       "      <td>69</td>\n",
       "      <td>89</td>\n",
       "      <td>80</td>\n",
       "      <td>86</td>\n",
       "      <td>78</td>\n",
       "      <td>41</td>\n",
       "      <td>92</td>\n",
       "      <td>84</td>\n",
       "      <td>85</td>\n",
       "      <td>83</td>\n",
       "      <td>30</td>\n",
       "      <td>45</td>\n",
       "      <td>38</td>\n",
       "      <td>27</td>\n",
       "      <td>25</td>\n",
       "      <td>31</td>\n",
       "      <td>33</td>\n",
       "      <td>37</td>\n",
       "      <td>88.0</td>\n",
       "      <td>87.0</td>\n",
       "      <td>88.0</td>\n",
       "      <td>87.0</td>\n",
       "      <td>80.0</td>\n",
       "      <td>85.0</td>\n",
       "      <td>65.0</td>\n",
       "      <td>58.0</td>\n",
       "      <td>64.0</td>\n",
       "      <td>68.0</td>\n",
       "      <td>88.0</td>\n",
       "      <td>87.0</td>\n",
       "      <td>88.0</td>\n",
       "      <td>87.0</td>\n",
       "      <td>80.0</td>\n",
       "      <td>85.0</td>\n",
       "      <td>65.0</td>\n",
       "      <td>58.0</td>\n",
       "      <td>64.0</td>\n",
       "      <td>68.0</td>\n",
       "      <td>88.0</td>\n",
       "      <td>88.0</td>\n",
       "      <td>87.0</td>\n",
       "      <td>80.0</td>\n",
       "      <td>65.0</td>\n",
       "      <td>58.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>167495</td>\n",
       "      <td>M. Neuer</td>\n",
       "      <td>Manuel Neuer</td>\n",
       "      <td>FC Bayern Munich</td>\n",
       "      <td>https://cdn.sofifa.org/18/teams/21.png</td>\n",
       "      <td>1493</td>\n",
       "      <td>31</td>\n",
       "      <td>German Bundesliga</td>\n",
       "      <td>1986-03-27</td>\n",
       "      <td>193.0</td>\n",
       "      <td>92.0</td>\n",
       "      <td>Normal</td>\n",
       "      <td>True</td>\n",
       "      <td>https://cdn.sofifa.org/flags/21@3x.png</td>\n",
       "      <td>Germany</td>\n",
       "      <td>https://cdn.sofifa.org/18/players/167495.png</td>\n",
       "      <td>61000000.0</td>\n",
       "      <td>230000.0</td>\n",
       "      <td>100700000.0</td>\n",
       "      <td>92</td>\n",
       "      <td>92</td>\n",
       "      <td>91</td>\n",
       "      <td>90</td>\n",
       "      <td>95</td>\n",
       "      <td>89</td>\n",
       "      <td>60</td>\n",
       "      <td>91</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>Medium</td>\n",
       "      <td>Medium</td>\n",
       "      <td>Right</td>\n",
       "      <td>15</td>\n",
       "      <td>13</td>\n",
       "      <td>25</td>\n",
       "      <td>55</td>\n",
       "      <td>11</td>\n",
       "      <td>30</td>\n",
       "      <td>14</td>\n",
       "      <td>11</td>\n",
       "      <td>59</td>\n",
       "      <td>48</td>\n",
       "      <td>58</td>\n",
       "      <td>61</td>\n",
       "      <td>52</td>\n",
       "      <td>85</td>\n",
       "      <td>35</td>\n",
       "      <td>25</td>\n",
       "      <td>78</td>\n",
       "      <td>44</td>\n",
       "      <td>83</td>\n",
       "      <td>16</td>\n",
       "      <td>29</td>\n",
       "      <td>30</td>\n",
       "      <td>12</td>\n",
       "      <td>70</td>\n",
       "      <td>47</td>\n",
       "      <td>70</td>\n",
       "      <td>10</td>\n",
       "      <td>10</td>\n",
       "      <td>11</td>\n",
       "      <td>91</td>\n",
       "      <td>90</td>\n",
       "      <td>95</td>\n",
       "      <td>91</td>\n",
       "      <td>89</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>92.0</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       ID               name                     full_name  \\\n",
       "0   20801  Cristiano Ronaldo  C. Ronaldo dos Santos Aveiro   \n",
       "1  158023           L. Messi                  Lionel Messi   \n",
       "2  190871             Neymar    Neymar da Silva Santos Jr.   \n",
       "3  176580          L. Suárez                   Luis Suárez   \n",
       "4  167495           M. Neuer                  Manuel Neuer   \n",
       "\n",
       "                  club                                club_logo  special  age  \\\n",
       "0       Real Madrid CF  https://cdn.sofifa.org/18/teams/243.png     2228   32   \n",
       "1         FC Barcelona  https://cdn.sofifa.org/18/teams/241.png     2158   30   \n",
       "2  Paris Saint-Germain   https://cdn.sofifa.org/18/teams/73.png     2100   25   \n",
       "3         FC Barcelona  https://cdn.sofifa.org/18/teams/241.png     2291   30   \n",
       "4     FC Bayern Munich   https://cdn.sofifa.org/18/teams/21.png     1493   31   \n",
       "\n",
       "                     league  birth_date  height_cm  weight_kg   body_type  \\\n",
       "0  Spanish Primera División  1985-02-05      185.0       80.0  C. Ronaldo   \n",
       "1  Spanish Primera División  1987-06-24      170.0       72.0       Messi   \n",
       "2            French Ligue 1  1992-02-05      175.0       68.0      Neymar   \n",
       "3  Spanish Primera División  1987-01-24      182.0       86.0      Normal   \n",
       "4         German Bundesliga  1986-03-27      193.0       92.0      Normal   \n",
       "\n",
       "   real_face                                    flag nationality  \\\n",
       "0       True  https://cdn.sofifa.org/flags/38@3x.png    Portugal   \n",
       "1       True  https://cdn.sofifa.org/flags/52@3x.png   Argentina   \n",
       "2       True  https://cdn.sofifa.org/flags/54@3x.png      Brazil   \n",
       "3       True  https://cdn.sofifa.org/flags/60@3x.png     Uruguay   \n",
       "4       True  https://cdn.sofifa.org/flags/21@3x.png     Germany   \n",
       "\n",
       "                                          photo    eur_value  eur_wage  \\\n",
       "0   https://cdn.sofifa.org/18/players/20801.png   95500000.0  565000.0   \n",
       "1  https://cdn.sofifa.org/18/players/158023.png  105000000.0  565000.0   \n",
       "2  https://cdn.sofifa.org/18/players/190871.png  123000000.0  280000.0   \n",
       "3  https://cdn.sofifa.org/18/players/176580.png   97000000.0  510000.0   \n",
       "4  https://cdn.sofifa.org/18/players/167495.png   61000000.0  230000.0   \n",
       "\n",
       "   eur_release_clause  overall  potential  pac  sho  pas  dri  def  phy  \\\n",
       "0         195800000.0       94         94   90   93   82   90   33   80   \n",
       "1         215300000.0       93         93   89   90   86   96   26   61   \n",
       "2         236800000.0       92         94   92   84   79   95   30   60   \n",
       "3         198900000.0       92         92   82   90   79   87   42   81   \n",
       "4         100700000.0       92         92   91   90   95   89   60   91   \n",
       "\n",
       "   international_reputation  skill_moves  weak_foot work_rate_att  \\\n",
       "0                         5            5          4          High   \n",
       "1                         5            4          4        Medium   \n",
       "2                         5            5          5          High   \n",
       "3                         5            4          4          High   \n",
       "4                         5            1          4        Medium   \n",
       "\n",
       "  work_rate_def preferred_foot  crossing  finishing  heading_accuracy  \\\n",
       "0           Low          Right        85         94                88   \n",
       "1        Medium           Left        77         95                71   \n",
       "2        Medium          Right        75         89                62   \n",
       "3        Medium          Right        77         94                77   \n",
       "4        Medium          Right        15         13                25   \n",
       "\n",
       "   short_passing  volleys  dribbling  curve  free_kick_accuracy  long_passing  \\\n",
       "0             83       88         91     81                  76            77   \n",
       "1             88       85         97     89                  90            87   \n",
       "2             81       83         96     81                  84            75   \n",
       "3             83       88         86     86                  84            64   \n",
       "4             55       11         30     14                  11            59   \n",
       "\n",
       "   ball_control  acceleration  sprint_speed  agility  reactions  balance  \\\n",
       "0            93            89            91       89         96       63   \n",
       "1            95            92            87       90         95       95   \n",
       "2            95            94            90       96         88       82   \n",
       "3            91            88            77       86         93       60   \n",
       "4            48            58            61       52         85       35   \n",
       "\n",
       "   shot_power  jumping  stamina  strength  long_shots  aggression  \\\n",
       "0          94       95       92        80          92          63   \n",
       "1          85       68       73        59          88          48   \n",
       "2          80       61       78        53          77          56   \n",
       "3          87       69       89        80          86          78   \n",
       "4          25       78       44        83          16          29   \n",
       "\n",
       "   interceptions  positioning  vision  penalties  composure  marking  \\\n",
       "0             29           95      85         85         95       22   \n",
       "1             22           93      90         78         96       13   \n",
       "2             36           90      80         81         92       21   \n",
       "3             41           92      84         85         83       30   \n",
       "4             30           12      70         47         70       10   \n",
       "\n",
       "   standing_tackle  sliding_tackle  gk_diving  gk_handling  gk_kicking  \\\n",
       "0               31              23          7           11          15   \n",
       "1               28              26          6           11          15   \n",
       "2               24              33          9            9          15   \n",
       "3               45              38         27           25          31   \n",
       "4               10              11         91           90          95   \n",
       "\n",
       "   gk_positioning  gk_reflexes    rs    rw    rf   ram   rcm    rm   rdm  \\\n",
       "0              14           11  92.0  91.0  91.0  89.0  82.0  89.0  62.0   \n",
       "1              14            8  88.0  91.0  92.0  92.0  84.0  90.0  59.0   \n",
       "2              15           11  84.0  89.0  88.0  88.0  79.0  87.0  59.0   \n",
       "3              33           37  88.0  87.0  88.0  87.0  80.0  85.0  65.0   \n",
       "4              91           89   NaN   NaN   NaN   NaN   NaN   NaN   NaN   \n",
       "\n",
       "    rcb    rb   rwb    st    lw    cf   cam    cm    lm   cdm    cb    lb  \\\n",
       "0  53.0  61.0  66.0  92.0  91.0  91.0  89.0  82.0  89.0  62.0  53.0  61.0   \n",
       "1  45.0  57.0  62.0  88.0  91.0  92.0  92.0  84.0  90.0  59.0  45.0  57.0   \n",
       "2  46.0  59.0  64.0  84.0  89.0  88.0  88.0  79.0  87.0  59.0  46.0  59.0   \n",
       "3  58.0  64.0  68.0  88.0  87.0  88.0  87.0  80.0  85.0  65.0  58.0  64.0   \n",
       "4   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   \n",
       "\n",
       "    lwb    ls    lf   lam   lcm   ldm   lcb    gk  1_on_1_rush_trait  \\\n",
       "0  66.0  92.0  91.0  89.0  82.0  62.0  53.0   NaN              False   \n",
       "1  62.0  88.0  92.0  92.0  84.0  59.0  45.0   NaN              False   \n",
       "2  64.0  84.0  88.0  88.0  79.0  59.0  46.0   NaN              False   \n",
       "3  68.0  88.0  88.0  87.0  80.0  65.0  58.0   NaN              False   \n",
       "4   NaN   NaN   NaN   NaN   NaN   NaN   NaN  92.0               True   \n",
       "\n",
       "   acrobatic_clearance_trait  argues_with_officials_trait  \\\n",
       "0                      False                        False   \n",
       "1                      False                        False   \n",
       "2                      False                        False   \n",
       "3                      False                        False   \n",
       "4                      False                        False   \n",
       "\n",
       "   avoids_using_weaker_foot_trait  backs_into_player_trait  \\\n",
       "0                           False                    False   \n",
       "1                           False                    False   \n",
       "2                           False                    False   \n",
       "3                           False                    False   \n",
       "4                           False                    False   \n",
       "\n",
       "   bicycle_kicks_trait  cautious_with_crosses_trait  chip_shot_trait  \\\n",
       "0                False                        False            False   \n",
       "1                False                        False             True   \n",
       "2                False                        False            False   \n",
       "3                False                        False            False   \n",
       "4                False                        False            False   \n",
       "\n",
       "   chipped_penalty_trait  comes_for_crosses_trait  corner_specialist_trait  \\\n",
       "0                  False                    False                    False   \n",
       "1                  False                    False                    False   \n",
       "2                  False                    False                    False   \n",
       "3                  False                    False                    False   \n",
       "4                  False                     True                    False   \n",
       "\n",
       "   diver_trait  dives_into_tackles_trait  diving_header_trait  \\\n",
       "0        False                     False                False   \n",
       "1        False                     False                False   \n",
       "2         True                     False                False   \n",
       "3         True                     False                False   \n",
       "4        False                     False                False   \n",
       "\n",
       "   driven_pass_trait  early_crosser_trait  fan's_favourite_trait  \\\n",
       "0              False                False                  False   \n",
       "1              False                False                  False   \n",
       "2              False                False                  False   \n",
       "3              False                False                  False   \n",
       "4              False                False                  False   \n",
       "\n",
       "   fancy_flicks_trait  finesse_shot_trait  flair_trait  flair_passes_trait  \\\n",
       "0               False               False         True               False   \n",
       "1               False                True        False               False   \n",
       "2               False               False         True               False   \n",
       "3               False               False        False               False   \n",
       "4               False               False        False               False   \n",
       "\n",
       "   gk_flat_kick_trait  gk_long_throw_trait  gk_up_for_corners_trait  \\\n",
       "0               False                False                    False   \n",
       "1               False                False                    False   \n",
       "2               False                False                    False   \n",
       "3               False                False                    False   \n",
       "4               False                 True                    False   \n",
       "\n",
       "   giant_throw_in_trait  inflexible_trait  injury_free_trait  \\\n",
       "0                 False             False              False   \n",
       "1                 False             False              False   \n",
       "2                 False             False              False   \n",
       "3                 False             False              False   \n",
       "4                 False             False              False   \n",
       "\n",
       "   injury_prone_trait  leadership_trait  long_passer_trait  \\\n",
       "0               False             False              False   \n",
       "1               False             False              False   \n",
       "2               False             False              False   \n",
       "3               False             False              False   \n",
       "4               False             False              False   \n",
       "\n",
       "   long_shot_taker_trait  long_throw_in_trait  one_club_player_trait  \\\n",
       "0                   True                False                  False   \n",
       "1                   True                False                   True   \n",
       "2                  False                False                  False   \n",
       "3                  False                False                  False   \n",
       "4                  False                False                  False   \n",
       "\n",
       "   outside_foot_shot_trait  playmaker_trait  power_free_kick_trait  \\\n",
       "0                    False            False                   True   \n",
       "1                    False             True                  False   \n",
       "2                    False            False                  False   \n",
       "3                    False            False                  False   \n",
       "4                    False            False                  False   \n",
       "\n",
       "   power_header_trait  puncher_trait  rushes_out_of_goal_trait  \\\n",
       "0               False          False                     False   \n",
       "1               False          False                     False   \n",
       "2               False          False                     False   \n",
       "3               False          False                     False   \n",
       "4               False          False                      True   \n",
       "\n",
       "   saves_with_feet_trait  second_wind_trait  selfish_trait  \\\n",
       "0                  False              False          False   \n",
       "1                  False              False          False   \n",
       "2                  False              False          False   \n",
       "3                  False              False          False   \n",
       "4                  False              False          False   \n",
       "\n",
       "   skilled_dribbling_trait  stutter_penalty_trait  swerve_pass_trait  \\\n",
       "0                     True                  False              False   \n",
       "1                     True                  False              False   \n",
       "2                     True                  False              False   \n",
       "3                    False                  False              False   \n",
       "4                    False                  False              False   \n",
       "\n",
       "   takes_finesse_free_kicks_trait  target_forward_trait  team_player_trait  \\\n",
       "0                           False                 False              False   \n",
       "1                           False                 False              False   \n",
       "2                            True                 False              False   \n",
       "3                           False                 False              False   \n",
       "4                           False                 False              False   \n",
       "\n",
       "   technical_dribbler_trait  tries_to_beat_defensive_line_trait  \\\n",
       "0                     False                               False   \n",
       "1                     False                               False   \n",
       "2                      True                               False   \n",
       "3                      True                                True   \n",
       "4                     False                               False   \n",
       "\n",
       "   poacher_speciality  speedster_speciality  aerial_threat_speciality  \\\n",
       "0               False                  True                     False   \n",
       "1               False                 False                     False   \n",
       "2               False                  True                     False   \n",
       "3               False                 False                     False   \n",
       "4               False                 False                     False   \n",
       "\n",
       "   dribbler_speciality  playmaker_speciality  engine_speciality  \\\n",
       "0                 True                 False              False   \n",
       "1                 True                 False              False   \n",
       "2                 True                 False              False   \n",
       "3                False                 False              False   \n",
       "4                False                 False              False   \n",
       "\n",
       "   distance_shooter_speciality  crosser_speciality  \\\n",
       "0                         True               False   \n",
       "1                        False               False   \n",
       "2                        False               False   \n",
       "3                        False               False   \n",
       "4                        False               False   \n",
       "\n",
       "   free_kick_specialist_speciality  tackling_speciality  tactician_speciality  \\\n",
       "0                            False                False                 False   \n",
       "1                             True                False                 False   \n",
       "2                            False                False                 False   \n",
       "3                            False                False                 False   \n",
       "4                            False                False                 False   \n",
       "\n",
       "   acrobat_speciality  strength_speciality  clinical_finisher_speciality  \\\n",
       "0                True                False                          True   \n",
       "1                True                False                          True   \n",
       "2                True                False                         False   \n",
       "3                True                False                          True   \n",
       "4               False                False                         False   \n",
       "\n",
       "   prefers_rs  prefers_rw  prefers_rf  prefers_ram  prefers_rcm  prefers_rm  \\\n",
       "0       False       False       False        False        False       False   \n",
       "1       False        True       False        False        False       False   \n",
       "2       False       False       False        False        False       False   \n",
       "3       False       False       False        False        False       False   \n",
       "4       False       False       False        False        False       False   \n",
       "\n",
       "   prefers_rdm  prefers_rcb  prefers_rb  prefers_rwb  prefers_st  prefers_lw  \\\n",
       "0        False        False       False        False        True        True   \n",
       "1        False        False       False        False        True       False   \n",
       "2        False        False       False        False       False        True   \n",
       "3        False        False       False        False        True       False   \n",
       "4        False        False       False        False       False       False   \n",
       "\n",
       "   prefers_cf  prefers_cam  prefers_cm  prefers_lm  prefers_cdm  prefers_cb  \\\n",
       "0       False        False       False       False        False       False   \n",
       "1        True        False       False       False        False       False   \n",
       "2       False        False       False       False        False       False   \n",
       "3       False        False       False       False        False       False   \n",
       "4       False        False       False       False        False       False   \n",
       "\n",
       "   prefers_lb  prefers_lwb  prefers_ls  prefers_lf  prefers_lam  prefers_lcm  \\\n",
       "0       False        False       False       False        False        False   \n",
       "1       False        False       False       False        False        False   \n",
       "2       False        False       False       False        False        False   \n",
       "3       False        False       False       False        False        False   \n",
       "4       False        False       False       False        False        False   \n",
       "\n",
       "   prefers_ldm  prefers_lcb  prefers_gk  \n",
       "0        False        False       False  \n",
       "1        False        False       False  \n",
       "2        False        False       False  \n",
       "3        False        False       False  \n",
       "4        False        False        True  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "with pd.option_context('display.max_rows', None, 'display.max_columns', None):\n",
    "    display(fifa.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Each row represents a different player, and each player has 185 different stat fields in the dataframe. The columns contain a variety of different data types including strings, ints, and booleans. Let's examine the most common nationalities over the entire dataframe. (We also add a \"Rank\" column, in case our grouping later on changes the initial indexing.)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "nationality\n",
       "England        1631\n",
       "Germany        1147\n",
       "Spain          1020\n",
       "France          966\n",
       "Argentina       962\n",
       "Brazil          806\n",
       "Italy           800\n",
       "Colombia        593\n",
       "Japan           471\n",
       "Netherlands     430\n",
       "Name: ID, dtype: int64"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fifa['Rank']=fifa.index+1\n",
    "fifa.groupby('nationality')['ID'].count().sort_values(ascending=False).head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's also take a look at the 30 least common nationalities."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "nationality\n",
       "New Caledonia          2\n",
       "Kuwait                 2\n",
       "Namibia                2\n",
       "Cuba                   2\n",
       "Ethiopia               2\n",
       "Mauritania             2\n",
       "Libya                  2\n",
       "Gibraltar              2\n",
       "Liberia                2\n",
       "El Salvador            2\n",
       "Oman                   1\n",
       "São Tomé & Príncipe    1\n",
       "Kyrgyzstan             1\n",
       "Hong Kong              1\n",
       "Turkmenistan           1\n",
       "Barbados               1\n",
       "Guatemala              1\n",
       "Vietnam                1\n",
       "Fiji                   1\n",
       "Eritrea                1\n",
       "Swaziland              1\n",
       "Belize                 1\n",
       "Guam                   1\n",
       "St Lucia               1\n",
       "Sri Lanka              1\n",
       "Somalia                1\n",
       "San Marino             1\n",
       "Burundi                1\n",
       "Mauritius              1\n",
       "Grenada                1\n",
       "Name: ID, dtype: int64"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fifa.groupby('nationality')['ID'].count().sort_values(ascending=False).tail(30)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In later explorations, for statistical significance, we will filter out countries that have very few players.\n",
    "\n",
    "Instead of just looking at the raw number of players from each country, let's see how many players from each country have an overall FIFA rating of 80 or above. (80 is a very high score; these players are ranked as the top 524 players in the world)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "nationality\n",
       "Spain        80\n",
       "Germany      48\n",
       "Brazil       48\n",
       "France       47\n",
       "Italy        37\n",
       "England      33\n",
       "Argentina    31\n",
       "Portugal     21\n",
       "Belgium      19\n",
       "Croatia      13\n",
       "Name: ID, dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fifa[fifa.overall>=80].groupby('nationality')['ID'].count().sort_values(ascending=False).head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Comparing this filtered player count to the raw player count, we see that Spain vastly outperforms expectations in terms of great players with 80 players out of 1020 with an overall ranking 80 or higher. On the other hand, England seems to be underperforming with only 33 players out of 1631 meeting the same ranking requirement. Let's compare the distribution of the overall ratings."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0,0.5,'Probability Density')"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\nbWeXhgAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x29e6292a470>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.kdeplot(fifa[fifa.nationality=='Spain']['overall'], label='Spain', shade=True)\n",
    "sns.kdeplot(fifa[fifa.nationality=='England']['overall'], label='England', shade=True)\n",
    "plt.xlabel('Overall Rating')\n",
    "plt.ylabel('Probability Density')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This PDF comparison is illuminating, showing how many more elite-level players Spain has as compared to England.\n",
    "\n",
    "# Positions <a name=\"positions\"></a>\n",
    "Let's shift our focus towards positions. At the very basic level, soccer positions can be split into Goalkeepers, Defenders, Midfielders, and Forwards. At a more detailed level, there are more nuanced positions and roles such as the False 9, Poacher, No. 10, etc. Let's choose to take a middling approach and categorize the positions into\n",
    "\n",
    "* GK\n",
    "* Center-back\n",
    "* Outside-back\n",
    "* Center-mid\n",
    "* Outside-mid\n",
    "* Forward\n",
    "\n",
    "The dataframe includes columns indicating which (highly specific) position the player prefers to play. Let's write some code to perform our categorization."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "fifa['Position']= np.nan\n",
    "\n",
    "fifa.loc[fifa.prefers_lm == True, ['Position']] = 'Outside-mid'\n",
    "fifa.loc[fifa.prefers_rm == True, ['Position']] = 'Outside-mid'\n",
    "fifa.loc[fifa.prefers_lw == True, ['Position']] = 'Outside-mid'\n",
    "fifa.loc[fifa.prefers_rw == True, ['Position']] = 'Outside-mid'\n",
    "fifa.loc[fifa.prefers_cam == True, ['Position']] = 'Center-mid'\n",
    "fifa.loc[fifa.prefers_cm == True, ['Position']] = 'Center-mid'\n",
    "fifa.loc[fifa.prefers_cdm == True, ['Position']] = 'Center-mid'\n",
    "fifa.loc[fifa.prefers_rb == True, ['Position']] = 'Outside-back'\n",
    "fifa.loc[fifa.prefers_lb == True, ['Position']] = 'Outside-back'\n",
    "fifa.loc[fifa.prefers_cb == True, ['Position']] = 'Center-back'\n",
    "fifa.loc[fifa.prefers_st == True, ['Position']] = 'Forward'\n",
    "fifa.loc[fifa.prefers_cf == True, ['Position']] = 'Forward'\n",
    "fifa.loc[fifa.prefers_gk == True, ['Position']] = 'GK'\n",
    "\n",
    "pos_order = ['GK', 'Center-back', 'Outside-back', 'Center-mid', 'Outside-mid', 'Forward']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "I wonder if any countries excel at producing world-class soccer players for specific positions. Let's take a look at the top 50 players per position, counting the number from each country."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "nationality\n",
       "Spain      8\n",
       "Germany    7\n",
       "France     5\n",
       "Italy      5\n",
       "England    3\n",
       "Name: ID, dtype: int64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "top_gk = fifa[fifa.Position=='GK'].head(50)\n",
    "top_gk.groupby('nationality')['ID'].count().sort_values(ascending=False).head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "nationality\n",
       "Germany      7\n",
       "Spain        5\n",
       "Brazil       5\n",
       "France       5\n",
       "Argentina    4\n",
       "Name: ID, dtype: int64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "top_cb = fifa[fifa.Position=='Center-back'].head(50)\n",
    "top_cb.groupby('nationality')['ID'].count().sort_values(ascending=False).head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "nationality\n",
       "Spain       10\n",
       "England      7\n",
       "Brazil       6\n",
       "Portugal     5\n",
       "Germany      4\n",
       "Name: ID, dtype: int64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "top_def = fifa[fifa.Position=='Outside-back'].head(50)\n",
    "top_def.groupby('nationality')['ID'].count().sort_values(ascending=False).head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "nationality\n",
       "Spain      12\n",
       "Germany     6\n",
       "Brazil      5\n",
       "France      4\n",
       "Croatia     3\n",
       "Name: ID, dtype: int64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "top_cm = fifa[fifa.Position=='Center-mid'].head(50)\n",
    "top_cm.groupby('nationality')['ID'].count().sort_values(ascending=False).head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "nationality\n",
       "Spain       9\n",
       "Brazil      5\n",
       "Portugal    4\n",
       "France      4\n",
       "Italy       3\n",
       "Name: ID, dtype: int64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "top_om = fifa[fifa.Position=='Outside-mid'].head(50)\n",
    "top_om.groupby('nationality')['ID'].count().sort_values(ascending=False).head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "nationality\n",
       "Argentina    6\n",
       "Italy        6\n",
       "France       6\n",
       "Spain        5\n",
       "Germany      4\n",
       "Name: ID, dtype: int64"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "top_for = fifa[fifa.Position=='Forward'].head(50)\n",
    "top_for.groupby('nationality')['ID'].count().sort_values(ascending=False).head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We see that Spain tops 4 out of the 6 lists. The most impressive figure here is surely the fact that 12 of the top 50 center midfielders (including attacking and defensive) are Spanish. Let's take a look to see who they are. Soccer fans will recognize these names as some of the best in the world."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>overall</th>\n",
       "      <th>club</th>\n",
       "      <th>league</th>\n",
       "      <th>nationality</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>Thiago</td>\n",
       "      <td>88</td>\n",
       "      <td>FC Bayern Munich</td>\n",
       "      <td>German Bundesliga</td>\n",
       "      <td>Spain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>42</th>\n",
       "      <td>David Silva</td>\n",
       "      <td>87</td>\n",
       "      <td>Manchester City</td>\n",
       "      <td>English Premier League</td>\n",
       "      <td>Spain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>45</th>\n",
       "      <td>Iniesta</td>\n",
       "      <td>87</td>\n",
       "      <td>FC Barcelona</td>\n",
       "      <td>Spanish Primera División</td>\n",
       "      <td>Spain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>48</th>\n",
       "      <td>Isco</td>\n",
       "      <td>86</td>\n",
       "      <td>Real Madrid CF</td>\n",
       "      <td>Spanish Primera División</td>\n",
       "      <td>Spain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>53</th>\n",
       "      <td>Sergio Busquets</td>\n",
       "      <td>86</td>\n",
       "      <td>FC Barcelona</td>\n",
       "      <td>Spanish Primera División</td>\n",
       "      <td>Spain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>65</th>\n",
       "      <td>Cesc Fàbregas</td>\n",
       "      <td>86</td>\n",
       "      <td>Chelsea</td>\n",
       "      <td>English Premier League</td>\n",
       "      <td>Spain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>74</th>\n",
       "      <td>Koke</td>\n",
       "      <td>85</td>\n",
       "      <td>Atlético Madrid</td>\n",
       "      <td>Spanish Primera División</td>\n",
       "      <td>Spain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>95</th>\n",
       "      <td>Marco Asensio</td>\n",
       "      <td>84</td>\n",
       "      <td>Real Madrid CF</td>\n",
       "      <td>Spanish Primera División</td>\n",
       "      <td>Spain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>107</th>\n",
       "      <td>Ander Herrera</td>\n",
       "      <td>84</td>\n",
       "      <td>Manchester United</td>\n",
       "      <td>English Premier League</td>\n",
       "      <td>Spain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>112</th>\n",
       "      <td>Bruno</td>\n",
       "      <td>84</td>\n",
       "      <td>Villarreal CF</td>\n",
       "      <td>Spanish Primera División</td>\n",
       "      <td>Spain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>119</th>\n",
       "      <td>Juan Mata</td>\n",
       "      <td>84</td>\n",
       "      <td>Manchester United</td>\n",
       "      <td>English Premier League</td>\n",
       "      <td>Spain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>158</th>\n",
       "      <td>Parejo</td>\n",
       "      <td>83</td>\n",
       "      <td>Valencia CF</td>\n",
       "      <td>Spanish Primera División</td>\n",
       "      <td>Spain</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                name  overall               club                    league  \\\n",
       "22            Thiago       88   FC Bayern Munich         German Bundesliga   \n",
       "42       David Silva       87    Manchester City    English Premier League   \n",
       "45           Iniesta       87       FC Barcelona  Spanish Primera División   \n",
       "48              Isco       86     Real Madrid CF  Spanish Primera División   \n",
       "53   Sergio Busquets       86       FC Barcelona  Spanish Primera División   \n",
       "65     Cesc Fàbregas       86            Chelsea    English Premier League   \n",
       "74              Koke       85    Atlético Madrid  Spanish Primera División   \n",
       "95     Marco Asensio       84     Real Madrid CF  Spanish Primera División   \n",
       "107    Ander Herrera       84  Manchester United    English Premier League   \n",
       "112            Bruno       84      Villarreal CF  Spanish Primera División   \n",
       "119        Juan Mata       84  Manchester United    English Premier League   \n",
       "158           Parejo       83        Valencia CF  Spanish Primera División   \n",
       "\n",
       "    nationality  \n",
       "22        Spain  \n",
       "42        Spain  \n",
       "45        Spain  \n",
       "48        Spain  \n",
       "53        Spain  \n",
       "65        Spain  \n",
       "74        Spain  \n",
       "95        Spain  \n",
       "107       Spain  \n",
       "112       Spain  \n",
       "119       Spain  \n",
       "158       Spain  "
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "key_attr = ['name', 'overall', 'club', 'league', 'nationality']\n",
    "top_cm[top_cm.nationality=='Spain'][key_attr]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Height and Weight <a name=\"height\"></a>\n",
    "At the professional level, soccer players must be in peak physical shape to be competitive. However, players come in all shapes and sizes. Let's take a look at a KDE plot with height on the x_axis and weight on the y_axis. Also, the marginal distributions are included outside the plot."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.JointGrid at 0x29e62c23588>"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x29e62c231d0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.jointplot(x='height_cm', y='weight_kg', data=fifa, kind=\"kde\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's take a quick glance at the statistics for the height and weight metrics."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    17994.000000\n",
       "mean       181.271980\n",
       "std          6.690392\n",
       "min        155.000000\n",
       "25%        177.000000\n",
       "50%        181.000000\n",
       "75%        186.000000\n",
       "max        205.000000\n",
       "Name: height_cm, dtype: float64"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fifa.height_cm.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    17994.000000\n",
       "mean        75.400856\n",
       "std          6.994824\n",
       "min         49.000000\n",
       "25%         70.000000\n",
       "50%         75.000000\n",
       "75%         80.000000\n",
       "max        110.000000\n",
       "Name: weight_kg, dtype: float64"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fifa.weight_kg.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Converting to imperial units, we see that the average height is 5'11.4\" (min: 5'1\", max: 6'8.7\"), and the average weight is 166.2 lbs (min: 108 lbs, max: 242.5 lbs).\n",
    "\n",
    "Let's see if there are any countries that produce significantly taller or shorter players than other countries. We first filter out any countries that contain fewer than 50 players in the dataframe. Then, we find the countries with the tallest and shortest average heights for their players.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "nationality\n",
       "Bosnia Herzegovina    185.625000\n",
       "Serbia                184.736842\n",
       "Czech Republic        184.698630\n",
       "Croatia               184.373832\n",
       "Senegal               183.952381\n",
       "Name: height_cm, dtype: float64"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fifa_sig = fifa.groupby('nationality')\n",
    "fifa_sig = fifa_sig.filter(lambda x:x['nationality'].count()>=50)\n",
    "fifa_sig.groupby('nationality')['height_cm'].mean().sort_values(ascending=False).head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "nationality\n",
       "Saudi Arabia    175.654434\n",
       "South Africa    176.387500\n",
       "Mexico          176.980609\n",
       "Japan           177.794055\n",
       "Ghana           178.280702\n",
       "Name: height_cm, dtype: float64"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fifa_sig.groupby('nationality')['height_cm'].mean().sort_values(ascending=False).head(5)\n",
    "fifa_sig.groupby('nationality')['height_cm'].mean().sort_values().head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's create a KDE plot comparing the heights and weights of the two countries at the extremes."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x29e635b2390>"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\nk046CUIIzJs3D1u2bGnkJREREcVaQ3vkiUQC1157LS6//HJ88sknuO6669Dc3Bx9PZ1O43//+1+v\njzNuXAqWZQ7oWlpamgb088cbtld92F71YXvVh+1Vn9HeXg0N8unTp+Pkk0+GEALTp09HU1MTDh8+\nHH09l8t1CfZjOXQoP6DraGlpwr592QE9xvGE7VUftld92F71YXvVZ7S0V08vRho6tP7cc8/hvvvu\nAwC0tbWhUCgglUph165dUErh9ddfx+zZsxt5SURERLHW0B75woULcdttt2HJkiUQQuCee+6BYRj4\nyU9+gjAMMW/ePHz5y19u5CURERHFWkOD3HEc3H///Ud9fsOGDY28DCIiolGDh6YQERHFGIOciIgo\nxhjkREREMcYgJyIiijEGORERUYwxyImIiGKMQU5ERBRjDHIiIqIYY5ATERHFGIOciIgoxhjkRERE\nMcYgJyIiijEGORERUYwxyImIiGKMQU5ERBRjDHIiIqIYY5ATERHFGIOciIgoxhjkREREMcYgJyIi\nijEGORERUYwxyImIiGKMQU5ERBRjDHIiIqIYY5ATERHFGIOciIgoxhjkREREMcYgJyIiijEGORER\nUYwxyImIiGKMQU5ERBRjDHIiIqIYY5ATERHFGIOciIgoxoRSSg33RRAREVH/sEdOREQUYwxyIiKi\nGGOQExERxRiDnIiIKMYY5ERERDHGICciIoqxURvkb7/9NpYtWwYA2LFjB772ta9h2bJlWLZsGV58\n8UUAwEMPPYSFCxfiiiuuwDvvvDOclzvsqtvrwIEDuP7663HllVfiiiuuwK5duwAAGzZswIIFC7Bo\n0SJs3rx5OC932FW318qVK6N764ILLsDKlSsB8P6qVt1e77//PhYtWoQlS5bgtttug5QSAO+vWrXP\nYQsXLsTSpUuxdu3aqM14jwG+7+Pmm2/G0qVLsXDhQmzatAk7d+7EkiVLsHTpUqxZs2b0t5cahR5/\n/HE1f/58dfnllyullNqwYYN64oknunzPu+++q5YtW6aklOqzzz5TCxYsGI5LHRFq2+uWW25RGzdu\nVEoptWXLFrV582a1d+9eNX/+fOV5nmpvb4/+fDyqba+Kw4cPq29/+9uqra2N91eV2vb64Q9/qF55\n5RWllFI//vGP1aZNm3h/1ahts+985ztq+/btSimlHnjgAfWnP/2J91jZc889p9atW6eUUurgwYPq\n/PPPVz/4wQ/UP/7xD6WUUnfeeaf6y1/+Mqrba1T2yE866SSsX78++vjdd9/FK6+8giuvvBI//elP\n0dHRge3bt2PevHkQQmDKlCkIwxAHDx4cxqsePrXt9a9//QttbW343ve+hxdeeAFz5szBO++8g698\n5StwHAdNTU046aST8MEHHwzjVQ+f2vaqWL9+Pa666ipMmjSJ91eV2vb60pe+hMOHD0MphVwuB8uy\neH/VqG2ztrY2zJw5EwAwc+ZMbN++nfdY2Te/+U386Ec/ij42TRM7duzAnDlzAADnnXce3nzzzVHd\nXqMyyC+66CJYlhV9fPbZZ2PVqlV45plnMG3aNDz88MPo6OhAJpOJviedTiObzQ7H5Q672vb67LPP\n0NzcjN/85jc48cQT8etf/xodHR1oamqKviedTqOjo2M4LnfY1bYXoKcjtmzZggULFgAA768qte31\nuc99DnfffTcuvvhiHDhwAHPnzuX9VaO2zaZNm4Z//vOfAIDNmzejUCjwHitLp9PIZDLo6OjAjTfe\niJtuuglKKQghoq9ns9lR3V6jMshrXXjhhTjzzDOjP7/33nvIZDLI5XLR9+RyuS5PJMezsWPH4oIL\nLgAAXHDBBXj33XfZXr14+eWXMX/+fJimCQBsrx7cfffdeOaZZ/Dyyy/jsssuw3333cf26sU999yD\nxx57DMuXL8eECRMwbtw4tlmV3bt34+qrr8all16KSy65BIbRGW25XA7Nzc2jur2OiyC/9tpro4UN\nW7ZswRlnnIGZM2fi9ddfh5QSra2tkFJi/Pjxw3ylI8OsWbPw6quvAgC2bduGU045BWeffTa2b98O\nz/OQzWbxn//8B6eeeuowX+nIsWXLFpx33nnRx7y/jm3MmDFRz2jSpElob2/n/dWLV199Fffccw8e\nf/xxHD58GOeeey7vsbL9+/fjmmuuwc0334yFCxcCAE4//XRs3boVAPDaa69h9uzZo7q9rN6/Jf7u\nuusurF27FrZtY+LEiVi7di0ymQxmz56NxYsXQ0qJ1atXD/dljhi33HIL7rjjDjz77LPIZDK4//77\nMWbMGCxbtgxLly6FUgorV66E67rDfakjxn//+19MmzYt+vjMM8/k/XUM69atw8qVK2FZFmzbxtq1\na9HS0sL7qwcnn3wyli9fjmQyiblz5+L8888HAN5jAB599FG0t7fjkUcewSOPPAIAuP3227Fu3To8\n8MADmDFjBi666CKYpjlq24unnxEREcXYcTG0TkRENFoxyImIiGKMQU5ERBRjDHIiIqIYY5ATERHF\nGIOcaJTYunVrdMhGX1x66aU9fv2Pf/wjbr311qM+n81msWLFirqvj4iGBoOc6Dj1/PPP9+vnjhw5\ngvfff3+Qr4aI+uu4KAhDdLw4ePAgrrvuOuzatQvTp0/Hgw8+iBdffBFPPfUUpJQ444wzsGbNGriu\niy9+8Yv48MMPkc1msWrVKuzatQvTpk3Dnj178NBDDwEAdu7ciWXLlqG1tRXnnHMO1q1bh3Xr1mHv\n3r1YsWIFHn744WNeywsvvIBf/epXEELgrLPOwtq1a/Hoo4+itbUVn3zyCQ4ePIjrr78eW7Zswdtv\nv43TTjsNv/zlL6Ma2UTUN+yRE40ira2tWL16NV566SXs378ff/jDH7BhwwY8++yzeP755zFhwgQ8\n8cQTXX7m4YcfxvTp07Fx40asWLECH330UfS13bt3Y/369XjppZfw2muv4eOPP8Ydd9yBSZMm9Rji\nbW1tuPfee/Hkk09i48aNCMMwKvv70Ucf4emnn8batWtx22234brrrsOf//xnvPfee/jwww+HpmGI\nRjH2yIlGkdNOOy0qFfv5z38ehw4dws6dO7Fo0SIAgO/7OP3007v8zBtvvIFf/OIXAICzzjqrS43z\n2bNnY+zYsQD00ZqHDh1CMpns9TreeustzJw5EyeccAIA4Oc//zkA4P3338e5554Ly7IwZcoUtLS0\n4JRTTgEATJ48GUeOHBnIr090XGKQE40i1UdfCiHQ1NSEiy++GHfccQcAfeJTGIZdfsY0TRyrUnPt\n4/W1orNlWV2GyKvPfbZtu9vHJ6L+4dA60Sj317/+FQcOHIBSCnfddReeeuqpLl8/55xz8MILLwAA\nPvzwQ3z88cc9zlNbloUgCHr8O8866yz8+9//xr59+wDoYzg3bdo0wN+EiLrDICcaxZqamnDDDTfg\nu9/9Lr71rW9BSonly5d3+Z4VK1Zg165duOSSS/Dggw9i4sSJSCQSx3zMCRMmYMqUKT1udZs8eTJu\nv/12XHvttZg/fz4SiQQWLFgwaL8XEXXi6WdEx7nnn38eU6dOxaxZs9Da2oqrrroKf/vb32AYfJ1P\nFAecoCI6zs2YMQNr1qyBlBKGYeBnP/tZn0K8WCxi8eLF3X7txhtvxDe+8Y3BvlQi6gZ75ERERDHG\nsTMiIqIYY5ATERHFGIOciIgoxhjkREREMcYgJyIiijEGORERUYz9f+BPYpnF9L2pAAAAAElFTkSu\nQmCC\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x29e635c8438>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "bosnia=fifa[fifa.nationality=='Bosnia Herzegovina']\n",
    "saudi=fifa[fifa.nationality=='Saudi Arabia']\n",
    "sns.kdeplot(bosnia.height_cm, bosnia.weight_kg, cmap='Reds')\n",
    "sns.kdeplot(saudi.height_cm, saudi.weight_kg, cmap='Blues')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The plots clearly shows that players from Bosnia Herzegovina tend to be significantly taller and heavier than the players from Saudi Arabia. This agrees with various lists of [average human height worldwide](https://en.wikipedia.org/wiki/List_of_average_human_height_worldwide), all of which list Bosnia Herzegovina either first or second in terms of average height (and Saudi Arabia near the bottom).\n",
    "\n",
    "Let's shift our attention to the body composition per position. We use a boxplot; the box itself contains the interquartile range (IQR), i.e., from 25% to 75%. The whiskers extend above and below the box, each with a length of $1.5*IQR$. Outside of the whiskers, the outliers are included as marks. The notch in the box displays the median of the data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x29e639911d0>"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAfIAAAFXCAYAAABZQMyNAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz\nAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMS4wLCBo\ndHRwOi8vbWF0cGxvdGxpYi5vcmcvpW3flQAAIABJREFUeJzt3XtcVHX+P/DXMFwah7uhGymlqaBr\nmoaiq+WqGxaJmCbewtQ291uKiWma4qW8hOIllZ+klmvOelkMDS3XL6WG3y0vlamljGvqqnhFBYEB\nuczM7w+ak8gIwzBzLszr+Xj06MMwZ857Ph7mPe9zPufzUZnNZjOIiIhIkdykDoCIiIjsx0RORESk\nYEzkRERECsZETkREpGBM5ERERArGRE5ERKRg7lIHYI/c3EKpQyAiIhJNUJDPA3/HipyIiEjBmMiJ\niIgUjImciIhIwZjIiYiIFIyJnIiISMGYyImIiBSMiZyIiEjBmMiJiIgUjIncAfT6U9DrT0kdBhER\nuSBFzuwmNxkZ6QCAsLB2EkdCRESuhhV5Pen1p3D6dDZOn85mVU5ERKJjIq8nSzV+f5uIiEgMTORE\nREQKxkReTzExg622iYiIxMDBbvUUFtYOoaFthTYREZGYmMgdgJU4ERFJRWU2m81SB1FXubmFUodA\nREQkmqAgnwf+jtfIiYiIFIyJnIiISMGYyB1Ap1sPnW691GFQA8Jpf4mkocS/PQ52c4CsrH0AgLi4\nsRJHQg0Fp/0lkoYS//ZYkdeTTrceJpMJJpOJVTk5BKf9JZKGUv/2mMjryVKN398mshen/SWShlL/\n9pjIiYiIFIyJvJ569epjtU1kL077SyQNpf7tcbBbPcXFjcX+/V8LbaL64rS/RNIIC2uH5s1DhLZS\nMJE7gFqtljoEamCUVA0QkbR4ar2eMjN3w2g0wmg0IjNzt9ThUAMRFtZOURUBUUOg15/CpUsXcenS\nRY5adyUZGduttomISFk4ap2IiIhEx0ReTzExg6y2yTolTn9IRK5BqaPWmcjrKTIyymqbrMvISFfU\nKSsich33jktR0hgVJvJ6SkycarVN1Sl1+kMicg0LFsyx2pY7JvJ6unLlstU2VafUgSRE5BrOnj1j\ntS13TOREREQKxkReT8HBj1ptU3VKHUhCRK7hiSdaW23LncpsNpud8cLl5eWYMWMGLl++jLKyMrzx\nxhto1aoVpk+fDpVKhdatW2POnDlwc3NDSkoKvvnmG7i7u2PGjBno0KFDja+dm1vojJDtNnbsCADA\n+vWbJY5E/qZNmwQAWLToQ4kjISKqTq6f50FBPg/8ndOmaN25cyf8/f2RnJyMvLw8vPTSSwgLC8Ok\nSZMQERGB2bNnY+/evQgODsaRI0ewbds2XL16FfHx8UhPV9b1U1bitisouCN1CERED6SkStzCaYn8\n+eefR79+/YSf1Wo1Tp48ia5duwIAnn32WXz77bdo0aIFevbsCZVKheDgYBiNRty+fRuBgYHOCs3h\n5s9PljoERcjM3I3S0lKhzdv1iEhuZs58T+oQ6sxpiVyr1QIAioqKMHHiREyaNAmLFi2CSqUSfl9Y\nWIiioiL4+/tX2a6wsFD0RJ6Wtgnff3/Yrm0NBgOA399zXXXpEoHY2JF2bask909ny0RORFR/Tl39\n7OrVqxg/fjxGjBiB6OhoJCf/XrkaDAb4+vrC29tbSISWx318HnwtAAACAhrB3d2xK45pNJ5Qq+0b\n+1dWVlll+vrWHHdN+67p+kdD8dt3OKHtCu+ZiMjZnJbIb968ibFjx2L27Nno3r07AKBdu3Y4fPgw\nIiIicODAAXTr1g0hISFITk7Ga6+9hmvXrsFkMtVajeflFTs83ujoIYiOHmLXtlOnTgQAJCXZP4BL\nbgP4nGHAgEHYuvUfQtsV3jMRKYtOtx4AEBc3VuJIqpJksNtHH32EgoICrF69GqtXrwYAzJw5E/Pn\nz8eyZcvQsmVL9OvXD2q1GuHh4Rg6dChMJhNmz57trJBIYpGRUUhL2yy0iYjkJitrHwD5JfKaOO32\nM2eSWyVnqciTk1dKHIm86fWnsHjxfADAO+8kKmouYyJq+HS69di//2sAQO/ef5FVMq+pIueEMCQa\nTtFKRHJmqcbvb8sdEzkREZGCMZGTaDhFKzka17cnR+rVq4/Vttw59fYzonuFhbVDaGhboU1UX5ZL\nNDyeyBHi4sYK18jldH28NqzISVQxMYNZjZNDcH17cjTLwOX723LHipzqTKpZ8FxlBjyyzf2DJ1mV\nU33dunXTalvuWJGTqMrKSoWZ8IiIqP5YkVOdxcaOtLsy5j335CgxMYOFeQl4uYYcoXHjh4VKvHHj\nhyWOxnasyIlIkcLC2sHPzx9+fv48rU4OcW+BoaRigxU5ESkW17cnR1NSJW7BRE5EiqTTrYdlhmmd\nbr2ibhci+VJSJW7BRE5EinT/dJpM5GQh1Z01gDR31/AaORER0W+UeGcNK3IiGbJMcMJBXA/Wq1cf\nYRYuJU2nSc7nanfWsCInkqGMjHSuEFeLe0+l87Q6uTImciKZ4dSjtlmwYI7VNpGrYSInkhmu226b\ns2fPWG0TuRomciIiIgVjIieSGa7bbpsnnmhttU3kapjIiWTGsm57aGhbjlqvwcyZ71ltE7ka3n5G\nJEOsxInIVqzIiWQoLKwdq/FacNQ6USUmciJSJI5aJ6rERE5ERKRgTOREMpSZuRuZmbulDkPWOGqd\nqBITOZEMZWRsR0bGdqnDkDWOWieqxEROJDOZmbtRUlKMkpJiVuU1+NvfXrXaJnI1TOREMnNvJc6q\n/MHKy8uttolcDRM5ERGRgjGRE8lMTMwgq22qysPDw2qbyNUwkRPJTGRkFNzc3ODm5obIyCipw5Gt\nNWs+tdom63gnRMPFKVqJZMhkMkkdAjUwlvEW/HLY8LAiJ5KZlSuXWG1TVa+9NtJqm6rjnRANGxM5\nkcwcO3bUapuqMpvNVttUHe+EaNiYyImIiBSMiZxIZp56qrPVNlWlUqmstqk63gnRsDGRE8nMxIlT\nrLapqk8+2WS1TdXxToiGjaPWiWSIlbhtWInbRq8/JdwJodef4lr3DQwTOZGTpKVtwvffH7ZrW4PB\nAACYOnWiXdt36RKB2FjljOS2t6+8vB4C4Dr9ZK+MjPQqbSbyhoWn1olkqKysFGVlpVKHIXvsJyJW\n5EROExs70u5qz1JhJievdGRIsmVvX7laP9krJmYwFi+eL7SpYWEiJyJq4MLC2iEoqInQpoaFiZyI\nyAUUFNyROgRyEl4jJyJq4DIzd6O0tBSlpaWcorUBalAV+cKFc5GXd1v0/Vr2ae/I2foICAjEjBlz\nRd8vESnH/VO08l7yhqVBJfK8vNu4desWVB4aUfdr/u3Exu2CYnH3W14i6v6IiEh+GlQiBwCVhwbe\nrQZIHYYoin7dKXUIRKQAMTGDsHXrP4Q2NSxOvUZ+/PhxxMXFAQBOnjyJl19+GSNGjMC8efOEWYZS\nUlLw8ssvY9iwYThx4oQzwyEickmRkVHQaBpBo2nE0+oNkNMq8nXr1mHnzp3QaCpPc8+aNQuJiYno\n3Lkzli9fjl27dqFVq1Y4cuQItm3bhqtXryI+Ph7p6em1vDIREdUVK/GGy2mJPCQkBKtWrcI777wD\nALh+/To6d66cP7pz587Yu3cv7ty5g549e0KlUiE4OBhGoxG3b99GYGCgs8IiIlIsR0z7+9VXe+za\n3lWms1UipyXyfv36IScnR/i5efPmOHLkCLp27Yr9+/ejpKQERUVF8Pf3F56j1WpRWFhYayIPCGgE\nd3d1tcfVate7m06tdkNQkI/UYdjM8m+kpJilwH6yjav1k0bjaffnnGUqW19f+/pKo/F0iX5W4jEl\n2mC3hQsXYsGCBfj444/x5JNPwtPTE97e3sK3RKDyG6OPT+2dl5dnfXS40WhyWLxKYTSakJtbKHUY\nNrP8GykpZimwn2zjav0UHT0E0dFD7NrWcntsUtKHdu/fFfpZrsdUTV8sRCths7KysHDhQqxduxb5\n+fno0aMHOnfujH//+98wmUy4cuUKTCYTT6sTERHVgWgV+WOPPYZx48ZBo9EgIiICvXr1AgCEh4dj\n6NChMJlMmD17tljhEBERNQhOTeTNmjVDWloaAKBPnz7o06dPtefEx8cjPj7emWGQFa42Cx5nwCOi\nhqrBTQhDtsnLu41bt2/CTSPuIWByM1fuvyRfvH2WVIi2LyIisTGRuzA3jTsCng+ROgyny9tzUeoQ\niIicxvXu1yIiImpAmMiJiIgUjImciIhIwRrUNXKDwQBz+V2XWRXMXF4Cg8EsdRhERCQhVuREREQK\n1qAqcq1Wi1KjyqXWI9dqG0kdBhERSYgVORERkYIxkRMRESkYEzkREZGCMZETEREpGBM5ERGRgjGR\nExERKRgTORERkYIxkRMRESlYg5oQhmxnMBhgKq1wiSU+TSUVMJgMUodBROQUrMiJiIgUjBW5i9Jq\ntShzK0fA8yFSh+J0eXsuQqvRSh0GEZFTsCInIiJSMCZyIiIiBWtwp9bN5SWir0duNpYBAFRqT3H3\nW14CgKufEVHDs3DhXOTl3RZ9v5Z9Tp06UfR9BwQEYsaMuXXerkEl8oCAQEn2m5d3t3L/vmIn1UaS\nvWciImfKy7uNW7dvwV3rI+p+zerKtHintEzU/VYYCu3etkElcnu+yTiC5ZtbcvJKSfZPRNQQuWt9\n0CJ2nNRhiOJ82lq7t+U1ciIiIgVjIiciIlIwm0+tnz59GgUFBVUe69Kli8MDIiIiItvZlMgnT56M\nkydPokmTJsJjKpUKGzdudFpgREREVDubEnl2djZ2794NtVrt7HiIiIioDmy6Rt6xY0dcuHDB2bEQ\nERFRHdlUkXfr1g39+/dHkyZNoFarYTaboVKpsHfvXmfHR0RERDWwKZGvWbMGn376KYKDg50dDxER\nEdWBTYk8ICAA4eHhUKlUzo6HRGQqEX89clOZEQDg5ineeAtTSQWgEW13RESisimRP/7444iNjcWf\n/vQneHh4CI9PmDDBaYGRc0k2ne3dynmMAzT+4u1UI937JSJyNpsSeXBwME+rNzCczpaIqGGwKZH/\nz//8D7KystC3b1/cvn0b+/btw+DBg50dGxEREdXCptvPZs2ahczMTOHnw4cPY86cOU4LioiIiGxj\nU0X+yy+/YNeuXQCAwMBAJCcnIzo62qmBEckB10S2nRR9pcR+InI0mxK5yWTCjRs3hClab926BTc3\nrrdCDV9e3m3cvnUT3iIf72qTCQBQJnJiLPptv/bIy7uNW7duwcujkQMjqpkKlXc/FBWUiLZPACgt\nLxZ1f0Q1sfka+UsvvYSnn34aAHD8+HHMnDnTqYERyYW3mxte8XONUe//uFO/Lw5eHo3QuW3DHz9z\nNDtd6hCIBDYl8ujoaHTt2hXHjh2Du7s7EhMThep8//796N27t1ODJCIiIutsXsa0adOm6NevX7XH\nV65cyUROREQkkXpf+DObzY6Ig4iIiOxgc0X+IJy2lYiIHM1gMKCi9C7Op62VOhRRVBgKYah4yK5t\nOfSciIhIwepdkRMRETmaVqtFhbsHWsSOkzoUUZxPWwutl6dd2zr1Gvnx48cRFxcHAMjOzkZsbCyG\nDx+Od999F6bf7ldNS0vDoEGDEBsbi/3799c3HCIiIpdiUyKPj4+v9tirr74KAPjnP/9pdZt169Yh\nMTERpaWlAICUlBSMHz8eW7ZsQVlZGb755hvk5uZCp9Nh69at+OSTT7Bs2TKUlZXZ+16IiIhcTo2n\n1idMmIDs7GzcuHEDffv2FR43Go34wx/+AADw8vKyum1ISAhWrVqFd955BwDQtm1b5Ofnw2w2w2Aw\nwN3dHSdOnECnTp3g6ekJT09PhISEQK/Xo0OHDo56f0REssJpf8nRakzkSUlJyM/Px4IFC5CYmPj7\nRu7uaNy4cY0v3K9fP+Tk5Ag/P/7443j//feRmpoKHx8fREREYM+ePfDx8RGeo9VqUVRUVGvQAQGN\n4O6urvV5YlGrK09sBAX51PJMUlpfWeJ1JWq1m13/Pq7WV/b2U0FBPm7fvgkfrX3XQ+1l+cgsLy0Q\ndb+FhjK7+srVjifA/mOqxkTu7e0Nb29vpKam4uzZs8jLyxOuiV+8eBFdunSxeUcLFizApk2b0Lp1\na2zatAlJSUno2bMnDAaD8ByDwVAlsT9IXp685jk2Giuv9+fmFkocifwpra8s8boSo9Fk17+Pq/VV\nffrJR+uJv4180glRyc+aTT/b1VeudjwBNR9TNSV4m0atz549G1lZWQgJCREeU6lU2Lhxo80B+vn5\nwdvbGwDQpEkTHD16FB06dMCHH36I0tJSlJWV4ezZs2jTpo3Nr0lEROTqbErk3333Hb766it4etp/\nKmj+/PlISEiAu7s7PDw8MG/ePAQFBSEuLg4jRoyA2WxGQkLCA6+5ExERUXU2JfJHHnkEpaWldU7k\nzZo1Q1paGgAgPDwcW7durfac2NhYxMbG1ul1iYiIqFKNifzdd98FUDlKPSYmBuHh4VCrfx9k9sEH\nHzg3OiIiIqpRjYm8a9euVf5PRERE8lJjIn/ppZcAAFeuXKnyuEql4rVsIiIiGbDpGvn48eNx5swZ\ntGnTBmazGWfOnEFQUBDUajXmzZuH7t27OztOIiIissKmO+6bNm2KrVu3Yvv27dixYwfS09PRvn17\n6HQ6LFmyxNkxEhER0QPYVJFfvnwZ7du3F34ODQ3FxYsX8cgjjwiLnxA1RAaDAaUmE/5xR/wpNaVQ\nZDLB655JmurCYDCgtPwujmanOzgq+SktL4bKwM8+kgebEnnz5s2xZMkSxMTEwGQy4YsvvsBjjz2G\nn376CW5urjeNHhERkVzYlMgXL16MlJQUvP3221Cr1ejevTsWLlyIffv24b333nN2jESS0Wq18Cgr\nxSt+gVKHIop/3LkNT63Wrm21Wi3MRjd0bjvYwVHJz9HsdGi1GqnDIAJgYyL39vbG9OnTqz0+YMAA\nhwdEREREtqv19rMdO3YgLCwMKpVKeNxsNkOlUiE7O9vpARIREdGD1ZjId+zYAQDQ6/WiBENERER1\nY9Op9bKyMqxfvx7nz5/HrFmzsGHDBowbN65ei6jITVraJnz//WG7ts3LqxzRPHXqRLu279IlArGx\nI+3aloiUxWAwoLS0DGs2/Sx1KKIoNJTBq8K+OyEqDIU4n7bWwRHVzFh6FwCg9npI1P1WGAoBr8Z2\nbWtTIn///fcRGBiIkydPQq1W48KFC5gxYwbvIf+NpydnuSMicqSAAGkGmOYVFwEA/LxELlS9Gtv9\nnm1K5CdPnsSOHTtw4MABaDQaLF68GNHR0XbtUK5iY0eyKiYip9NqtfB0N+JvI5+UOhRRrNn0Mzy8\n6n4nxIwZcx0fjA0sZ1aTk1dKsn972HQTuEqlQllZmTDgLS8vr8rgNyIiIpKGTRX5qFGjMGbMGOTm\n5mLBggX4+uuvMX78eGfHRkRERLWwKZFHRUXBYDAgLy8Pfn5+GDNmDNzdbdqUiIiInMimbDxp0iTk\n5ubiiSeewOXLl4XHBw4c6LTAiIiIqHY2JfJz585hz549zo5FsXS69QCAuLixEkdCRESuxqbBbiEh\nIbhy5YqzY1GsrKx9yMraJ3UYRETkgmqsyOPi4qBSqXD79m1ER0cjLCwMarVa+P3GjRudHqDc6XTr\nhaVcdbr1rMqJiEhUNSby+Ph4seJQrHsr8aysfUzkDVCRBOuR3/3ty+FDIi8TXGQyoT7TcJSWF4u6\nHnmFsQwA4K4Wd/KO0vJieIOrn5E81JjIu3btKlYcRLIk1exSht+m/fUUef+BsP89S9FXeXklAABv\nX3GTqjc0kh0bRPfjPWT11KtXH+zf/7XQpoaFs0vZToq+UmI/ETmauOftGqC4uLFQqVRQqVQ8rU5E\nRKJjRe4Avr5+UodAREQuihV5Pen1p3DnTj7u3MmHXn9K6nCIiMjFsCKvp4yM9CrtsLB2EkYjDqnW\nbue67URE1TGRk6i4djsRkWMxkddTTMxgLF48X2i7gvqs3T527AgAwOrVnzgyJCIil8VEXk9hYe0Q\nGtpWaBMREYmJg90cICZmsMtU4/VhqcbvbxMRkf1YkTsAK3EiqotCQxnWbPpZ1H3eLa0AADzkJe7H\nfqGhDIEcGuNUTORERCKSamrXouLKO0Y8vHxF3W+gl3Tv2VUwkRMRiYjT/pKj8Rq5A2Rm7kZm5m6p\nw5C99es3W20TEZH9WJE7QEbGdgBAZGSUxJEQEZGrYUVeT5mZu1FSUoySkmJW5bVITJxqtU1ERPZj\nIq8nSzV+f5uqu3LlstU2ERHZj4mciIhIwZjI6ykmZpDVNlUXHPyo1TYREdmPibyeIiOjoNE0gkbT\niIPdajF/frLVNhER2Y+J3AFiYgaxGrfBypVLrLaJiMh+vP3MAViJ2+bYsaNW20REZD9W5ERERArG\nRE6ieeqpzlbbRERkPyZyEs3EiVOstomIyH5OvUZ+/PhxLFmyBDqdDgkJCbh58yYA4PLly+jYsSOW\nL1+OlJQUfPPNN3B3d8eMGTPQoUMHZ4ZERETUoDgtka9btw47d+6ERqMBACxfvhwAcOfOHYwaNQrv\nvvsuTp48iSNHjmDbtm24evUq4uPjkZ6e7qyQSGL3T9HKW9CIiOrPaafWQ0JCsGrVqmqPr1q1Cq+8\n8gqaNGmCH3/8ET179oRKpUJwcDCMRiNu377trJBIYpyilYjI8ZxWkffr1w85OTlVHrt16xYOHjyI\nd999FwBQVFQEf39/4fdarRaFhYUIDKx5EfqAgEZwd1c7PmgSVVCQj9QhyJZaXfkdm31UM/aT7dhX\ntlFiP4l6H/mePXvQv39/qNWVSdjb2xsGg0H4vcFggI9P7Z2Xl1fstBjJeYKDHxUq8eDgR5GbWyhx\nRPJlNJoAgH1UC/aT7dhXtpFrP9X0xULUUesHDx7Es88+K/zcuXNn/Pvf/4bJZMKVK1dgMplqrcZJ\nuThFKxGR44lakZ8/fx7NmzcXfm7fvj3Cw8MxdOhQmEwmzJ49W8xwSGT3rteembmbM+IRETmAUxN5\ns2bNkJaWJvz85ZdfVntOfHw84uPjnRkGycT9a7czkRMR1R8nhCEiIlIwJnISDdduJyJyPCZyEk1k\nZBTc3T3g7u7B0+pERA7CZUxJVCqV1BEQETUsrMhJNJmZu1FeXo7y8vIqI9iJiMh+TOQkmvtHrRMR\nUf0xkRMRESkYEzmJhqPWiYgcj4mcRBMZGQU3Nze4ublx1DoRkYMwkZNo9PpTMJlMMJlM0OtPSR0O\nEVGDwEROosnISLfaJiIi+zGRExERKRgTOYkmJmaw1TYREdmPM7uRaMLC2iE0tK3QJiKi+mMiJ1Gx\nEiciciwmchIVK3EiIsfiNXIiIiIFYyInIiJSMCZyIiIiBWMiJyIiUjAmciIiIgVTmc1ms9RB1FVu\nbqHUIRDVKi1tE77//rBd2+bl3QYABAQE2rV9ly4RiI0dade2UrC3r1ytn+pj6tSJAIDk5JUSR+J8\nDfFvLyjI54G/4+1nRDLk6ekldQiKwH4iR1PiMcWKnEiGLKvD8b77mk2Y8FcAQErKxxJHIn+uVJHX\nh063HgAQFzdW4kiqYkVOpDCW1eGYyGtWXFwsdQjUwGRl7QMgv0ReEw52I5IZvf4UTp/OxunT2Vy3\nvQaWavz+NpG9dLr1MJlMMJlMQmWuBEzkRDLDddttc281zsqcHMFSjd/fljsmciIiIgVjIieSGa7b\nbptGjRpZbRPZq1evPlbbcsdETiQzlnXbQ0PbcrBbDe4dqc5R6+QI9w5wU9JgN45aJ5IhVuJEZCtW\n5EQyFBbWjtV4LV5/Pc5qm8he945UV9KodVbkRKRIRqPRarshc8TUo5aJYerKFaazvX/UulJOrzOR\nExG5ACVOPUq2YSInkqHMzN0AgMjIKIkjkS+1Wi1U4mq1WuJoxBEbO9LuqliuU4/KSa9efbB//9dC\nWyl4jZxIhjIytiMjY7vUYcjaunU6q22yLitrn6ImOZGCUketM5ETyUxm5m6UlBSjpKRYqMypunv7\nhv1UM6VOPSo2pR5TTOREMnNvJc6q/MHYT7ZT6tSjYlPqMcVETkREpGBM5EQyExMzyGqbqmI/2U6p\nU4+KTanHFBM5kcxERkbBy8sLXl5eHLVeg8jIKKjVaqjVavZTLeLixsLNzQ1ubm6KGsQltsjIKGg0\njaDRNFLUMcXbz4hkyNfXT+oQFMFoNEkdgmKwEreNkipxCyZyIpnR608hN/eG0OZUrdZVjr42C21W\nmjVj/9hGSZW4BU+tE8lMRka61TZVxZHYRJWYyImIiBSMiZxIZu5dwpTLmT4YR2LXTWbmbkVNciIV\nnW694ibNcWoiP378OOLiKpcXvHXrFt544w2MHDkSw4YNw8WLFwEAaWlpGDRoEGJjY7F//35nhkOk\nCGFh7RAa2hahoW15fbwGSp1OUyqc9tc2SpzK1mmD3datW4edO3dCo9EAAJKTkxEdHY2oqCgcOnQI\n586dg0ajgU6nQ3p6OkpLSzFixAj06NEDnp6ezgqLSBFYidfu/rWjmcwfzDLtr6WtxAFdYrBMZWtp\nK+WYclpFHhISglWrVgk/Hz16FNevX8fo0aOxa9cudO3aFSdOnECnTp3g6ekJHx8fhISEQK/XOysk\nIsUIC2vHarwWHOxmO6VOPSo2pR5TTqvI+/Xrh5ycHOHny5cvw9fXFxs2bEBKSgrWrVuHxx9/HD4+\nPsJztFotioqKan3tgIBGcHd3jWULicg2QUE+tT/JRalUVdvsK9sopZ9Eu4/c398fffpUDkjp06cP\nli9fjvbt28NgMAjPMRgMVRL7g+TlFTstTiI50OtPAQCr8hrcv3Z0bm6hxBHJ14ABg7B16z+ENvvK\nOjkfUzV9qRBt1PrTTz+NrKwsAMD333+PVq1aoUOHDvjxxx9RWlqKwsJCnD17Fm3atBErJCLZyshI\n5z3kteC0o7aLjIwS+orXxx9MqQMoRavIp02bhsTERGzduhXe3t5YunQp/Pz8EBcXhxEjRsBsNiMh\nIQFeXl5ihUQkS3r9KZw+nS20WZU/GG87s41ef0oYxMVj6sHuX49cKV96VGaz2Sx1EHUlp9MdRI62\naNE8IZGHhrbFtGmzJI6IlI6bQY3IAAARzklEQVTHlG3Gj/+rMLpfo2mE//f/PpY4ot/J4tQ6ERER\nOR4TOZHMcGY3cjQeU7ZR6nrkXP2MSGYsM7tZ2vRglmuaSrmWKZWwsHZo3jxEaJN1kZFR2LFjm9BW\nCiZyIhli1WQby+QmSvrQJXnz9fWTOoQ646l1IhnizG61s0w7WlJSzMVAaqHXn8KlSxdx6dJFYY4C\nqk6vP4Xc3BvIzb2hqH5iIiciReK0o7bjGve2UWo/MZETEREpGBM5ESmSUkcYS4Gj1m2j1H5iIici\nRYqMjIJG0wgaTSMOdqsF17i3TVhYO+GYUlI/cdQ6ESkWK3HbKanClIpef0qY2U1JU9kykRORYrES\nt51SkpKU7h/sppQ+46l1IiIiBWMiJyIignIHu/HUOhEplmXSDqWcAiV5U+r0yEzkRKRYlmuaSvrQ\nJXlTUiVuwURORIqk158S1thW0ghjkjclHke8Rk5EiqTU6TSJHI2JnIiISMGYyIlIkZQ6wpjkLTNz\nt+JW0+M1ciJSJKWOMCZ5U+Ia90zkRKRYrMTJkSxr3FvaSknmPLVORIoVFtaO1Tg5jFLXuGciJyIi\nUjAmciIiIih3jXsmciIiIih3jXsOdiMiIvqNkipxC5XZbDZLHURd5eYWSh0CERGRaIKCfB74O55a\nJyIiUjAmciIiIgVjIiciIlIwJnIiIiIFYyInIiJSMCZyIiIiBWMiJyIiUjAmciIiIgVjIiciIlIw\nRc7sRkRERJVYkRMRESkYEzkREZGCMZETEREpGBM5ERGRgjGRExERKRgTORERkYIxkdvh0qVLmDhx\nImJjYzFq1CiMGzcOZ86cwapVq7BlyxbheR988AHefPNNlJWVSRit7c6cOYNx48YhLi4OgwcPxsqV\nK1HXuxP/+c9/ory83K799+jRw67tLPr06YPS0tJ6vUZNLl26hPj4eMTFxWHYsGGYO3cuioqKHvj8\nr776CtevX3/g7ydMmFDtsS1btmDVqlU2xXP48GEkJCTY9FxrcnJyEBsba/f2dSH1sVWbtWvX4sSJ\nE1UeKy0tRZ8+fZyyv/vJ7diyRUJCQrXPtgMHDmD69OkO24c9cnJy0LlzZ8TFxQn/paSkiB5HQkIC\nDh8+LM7OzFQnxcXF5hdffNF89OhR4bHjx4+bX3nlFfPKlSvNmzdvNptMJvP7779vfvvtt83l5eUS\nRmu7O3fumPv3728+f/682Ww2mysqKszjx483b968uU6v07t3b/Pdu3ftiuFPf/qTXds5Yt+1KSkp\nMffv39987Ngx4bHt27ebx40b98BtXnnlFfOvv/5ap/1s3rzZvHLlSpuee+jQIfOkSZPq9Pr3unTp\nknnIkCF2b28rORxb9rh79665d+/eTt+PHI8te2VlZZmnTZvm1H3URqzjujaTJk0yHzp0SJR9uYvz\ndaHh2L9/P7p164ZOnToJj3Xo0AEbN25ESkoKzGYz5syZg4qKCixevBhubso46bF3715ERETg8ccf\nBwCo1WosWrQIHh4eWLp0Kb7//nuYzWaMHj0aL7zwAuLi4hAWFoYzZ86gqKgIK1aswHfffYfc3Fwk\nJCRg9erVD9wuICAABQUF+OSTT6BWq4UYysrKkJCQgKtXryI0NBRz587F9evXMXfuXJSWliI/Px/j\nx4/HX/7yF+zfv1/4lt2uXTu89957wuts2bIF3377LZYtWwZPT0+H9M8333yDLl26oGPHjsJjL730\nErZs2YJ33nkH/fv3x7PPPosDBw5g9+7deP7555GdnY1p06Zhw4YNmDJlCoqKinD37l1MnToVERER\n6NGjB7799lv88MMPWLhwIfz8/ODm5oannnoKAKDT6fDFF19ApVIhKioKo0aNqhbXhQsX8NprryEv\nLw/Dhw/HkCFDcOTIEaFv7t69i0WLFqFFixZYvXo1vv76axiNRgwfPhw9e/YEABiNRkyfPh2tW7fG\nuHHjHNJf95LDsfXcc8+hU6dOuHDhArp164bCwkKcOHECLVq0QHJyMqZPn46oqCg8/fTTmDJlCgoK\nChASEuLwvrBGjsfW4cOHsXbtWnh4eODatWsYNmwYDh06BL1ej1GjRmHEiBHo06cP/vWvfyEnJwcz\nZsyARqOBRqOBn5+fKP1WV0lJSfjxxx8BAP3798err76K6dOnIz8/H/n5+QgICMCbb76JJ598Ev36\n9cOUKVPw3HPPYezYsfjggw/w1VdfITMzExUVFfDx8cGqVavwxRdfID09HSaTCRMnTsS5c+ewbds2\nBAUF4datW6K9NybyOsrJyanyB/7GG2+gqKgIN27cQHh4OD777DO0aNECarUaKpVKwkjr5saNG2je\nvHmVx7RaLbKyspCTk4OtW7eitLQUsbGxwinwDh06YObMmVi+fDm+/PJLjBs3DqmpqVi+fHmN20VH\nR+O5556rFsPdu3cxZcoUPProo3jrrbewb98+aDQajBkzBhERETh69ChWrVqFP//5z5g3bx62bduG\nxo0bIyUlBdeuXQNQ+QGVnZ2NFStWVPkgr69Lly5Z/WBv1qwZfvjhB/Tv37/K43/+85/Rtm1bzJ07\nF1evXsXNmzexYcMG3Lp1C//973+rPPeDDz7A0qVL0aJFC8yZMwcA8Ouvv2L37t3YvHkzVCoVRo8e\njZ49e6Jly5ZVti0vL0dqaipMJhNiYmLQt29fnDlzBsnJyWjatCk++ugj7NmzB7169cKBAwewbds2\nlJWVYenSpejRowcqKiowZcoUhIeHY+TIkQ7rr3vJ4di6fPkyPv30UwQFBaFr167Ytm0bZs2ahb59\n+6KgoEB43o4dO9CmTRskJCTg+PHjopwaleuxde3aNXz++ec4efIk3nrrLeF0/oQJEzBixAjheStW\nrMDEiRPRo0cPrF27FufOnXNQz9jv119/RVxcnPDzoEGDkJOTg7S0NFRUVGDEiBHo1q0bAKBbt24Y\nPXo0Pv/8cxw4cAD+/v7w8vLCt99+i27duqG0tBRBQUHIz8/Hhg0b4Obmhtdeew0///wzAMDX1xep\nqakoLCzE3LlzsWvXLqhUKgwaNEi098tEXkd/+MMf8Msvvwg/p6amAgBiY2NhNBrRt29fzJ49GxMn\nTkRqairefPNNqUKtk+DgYJw6darKY5cuXcLPP/+MkydPCn8UFRUVuHLlCoDKShio7JObN29W2fY/\n//nPA7dr0aIFAGD58uU4evQoAGDDhg0IDg7Go48+CgDo1KkTzp8/j169eiE1NRWfffYZVCoVKioq\nkJeXB19fXzRu3BhA1euBBw8ehFqtdmgSB4CmTZtWu4YKAP/9738RHh4u/Gy2ct23devWGDlyJCZP\nnoyKiooqHzAAcP36daFPOnfujIsXL+I///kPrly5gtGjRwMA7ty5g4sXL2LRokUoLi5GmzZtEBkZ\niaeeeko46/DEE08gJycHTZs2xYIFC9CoUSNcv34dnTt3xvnz59GhQweo1WpoNBokJiYiJycHp0+f\n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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x29e6292a2e8>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(x='Position', y='height_cm', data=fifa, order=pos_order)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Wow, there are a few notable things to point out.\n",
    "\n",
    "* The goalkeepers are tallest, which is to be expected since there is a high correlation between height and wingspan.\n",
    "* The IQR of the center-backs and the outside-backs do not even overlap! This makes sense and highlights why we separated the two defender positions. Center-backs tend to be tall so that they can win headers in and around the 18-yard box. Outside-backs need to man-mark speedy forwards, and thus tend to be smaller in stature.\n",
    "* The outside-mids are the shortest on average. They need to be able to fly down the wings at incredible speeds to deliver crosses to the trailing forwards.\n",
    "\n",
    "It appears that forwards have the most spread out height distribution. Let's glance at the violin plot for further details."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x29e644576d8>"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAfIAAAFXCAYAAABZQMyNAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz\nAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMS4wLCBo\ndHRwOi8vbWF0cGxvdGxpYi5vcmcvpW3flQAAIABJREFUeJzsnXd8XNWZ93/ntunqXbIs994bxTEY\nMA4thEBMwpLkze6+CbtgQgosEEI2S5JNJXlpsQmEFtNsgxs2uGBh2cZNlrssuan3MtL0du/7x2jG\nkq0y0tw79450vp+PPx6NZs55ZjRzf+c85ylEkiQJFAqFQqFQ4hJGbQMoFAqFQqEMHSrkFAqFQqHE\nMVTIKRQKhUKJY6iQUygUCoUSx1Ahp1AoFAoljqFCTqFQKBRKHMOpbcBQaG62qW0ChUKhUCgxIz3d\n0ufv6I6cQqFQKJQ4hgo5hUKhUChxDBVyCoVCoVDiGCrkFAqFQqHEMVTIKRQKhUKJY6iQUygUCoUS\nx1Ahp1AoFAoljqFCTqFQKBRKHEOFnEKhUCiUOIYKOYVCoVAocQwVcgqFQqFQ4hgq5BQKhUKhxDFU\nyGXA4bDjqad+iv37i9Q2hUKhUCgjDCrkMnDixDE0Ntbjtdf+prYpFAqFQhlhUCGnUCgUCiWOoUJO\noVAoFEocQ4WcQqFQKJQ4hgo5hUKhUChxDBVyCoVCoVDiGCrkFAqFQqF04ff78dprf0N5+Vm1TYkY\nKuQUCoVCoXRx/PhR7N9fhFde+avapkQMFXIKRYP4fD4cO1YMn8+ntikUyojC4/EAADo7O1W2JHKo\nkFMoGmTHjm144YU/Y+fOT9U2hUKhaBwq5BSKBjlx4hgA4OTJ4ypbQqFQtA4VcgpFg0iSpLYJFAol\nTqBCTqFoGEKI2iZQKCOKePzOUSGnUCgUCqWLePSGUSGXgXj8w1PiA/rZolBiC92Rj1D8fr/aJlCG\nKfF4UaFQKLGFCrkM0FxfilLQHTmFQhkIKuQyQIWcohR0R06hUAaCCrkM+HxetU2gUCgUygiFCrkM\neL1UyCPF6XSivb1dbTPiBupap1AoA0GFXAbojjxy/vKX3+PJJx9T2wzNQ13qFAolUji1DRgO0B15\n5Fy4cE5tEygUCqVP4tELRnfkMtA92I2molEoFAolllAhl4HuO3IawU6Rg3jcFVAoFHWgQi4D3cWb\nnpdHBhUqCoVCkQcq5DLQXbzpjjwyqJBTKBQtEo/XJirkMkDPyAePKIpqm6BpaNQ6haIO8XhtokIu\nA93Fmwp5ZMTjl4VCoQx/4vHaRIVcBgIBf6+3KX0Tj1+WWBKP7j0KZTgQj9cmKuQyEAgEwrfpjjwy\n4vHLogbUxU6hxJr4W0RTIZeB7kLe/Talb6jngkKhaBFRjD8hV6yym8/nw9NPP43a2lp4vV78x3/8\nB8aPH48nn3wShBBMmDABv/zlL8EwDF566SUUFhaC4zg8/fTTmDlzplJmKQINdhs8dEceGdTFTqHE\nlni8Nikm5Js2bUJSUhL++Mc/or29Hffccw8mT56Mxx57DIsWLcKzzz6LXbt2IScnB4cOHcLatWtR\nX1+PlStXYv369UqZpQjdC8LQcq2REY9fllhCXeoUijrE4+JZMSH/6le/iuXLl4d/ZlkWp0+fxsKF\nCwEAS5Yswb59+zBmzBgsXrwYhBDk5OQgEAigra0NKSkpSpkmOw6HPXzb43GraEn8QI8gKHLx/vvv\nIDs7FzfccJPaplCGAfG4yVBMyE0mEwDAbrfj0UcfxWOPPYbf//734Z2GyWSCzWaD3W5HUlJSj+fZ\nbLZ+hTw52QiOY5UyfVD4fL4rRMmH9HSLavbEC4mJevo+9QPPBz/fgsDR92kAtm/fBgC47767VbaE\nMhwwGC7LYrx89xTtflZfX4+HH34YDzzwAO666y788Y9/DP/O4XAgISEBZrMZDoejx/0WS/9vXnu7\nUzGbB0tLS3OPn2tqGtDcbFPJmvihsdEKno+PL4ka+HzBxaHX66efpwih7xNFDjo7XeHbWvpM9beo\nUCxqvaWlBf/6r/+Kxx9/HPfddx8AYOrUqTh48CAAYM+ePZg/fz7mzp2LvXv3QhRF1NXVQRTFuHKr\nNzc3BW+Q4A7qSmGnXKa754KWsqVQKFokHjNqFNuRr1q1Cp2dnXjllVfwyiuvAAB+/vOf49e//jWe\nf/55jB07FsuXLwfLspg/fz7uv/9+iKKIZ599VimTFKGurjZ4g2EBEaitrVHXIA3j8XjCt71eTz+P\npFAiIx4DkyjaJh43GYoJ+TPPPINnnnnmqvv/+c9/XnXfypUrsXLlSqVMUZTKyksAAEIYEJ0FdXU1\n8Pl84HleZcu0h9t92WXldGrneIQSv1Ahp8hNPHawpAVhoqS8/GzXLQasIRWBQAAXL55X1Sat0j0W\nwul09PNICiUyqJBT5KZ7CnG8fL6okEdBS0szmpoag+fjBOBMmQCAM2dOqWyZNuns7Ajfttk6VbSE\nMlyIlwstJX5wuy+nEMfLESAV8ig4duxo8EZXoBtrzAAIg5KSYhWt0i7dhdxqtapoCWW4EI85vxRt\n013Iu9/WMlTIo+Dw4QMAAMIEhZywPFhTFmpqqtDQUK+maZqkra0tfNtqbevnkRRKZNDCQhS5cbku\nx+/ESywPFfIh0tTUiHPnyrp24ZfLafIJ+QCAffu+UMs0zdLW1hq+3draoqIl2oe6jCODCjlFbrrH\n78RLLA8V8iGyZ89uAACfNKbH/ZwlD4ThsXfvHtpA5QqamxvDt5uamlS0JH6gNdf7hwo5RW6uLFAW\nD1AhHwIejxuFhbtAWB04y6gevyMMBy5pDDo6rGHXOyVI+LiBIbDZOuNmtasmdGfeP/FYvIOiXSRJ\ngt1+uXdG9z4aWoYK+RDYs6cQTqcDfPJ4EObqVHwheSIAgq3bNtNgnC48Hnew6h2D8KcuXEyH0id0\nR94/dEdOkROv1wO//3JBGLtdOyVa+4MK+SDx+bzYum0zCMOBT57Y62MYwQwuIR+1NdU4doxGsANA\nVVVl8AZDQJigOIWK6VAoQ4UeX1HkxGYLCjdnsvT4WetQIR8khYWfo8PaDi5pPBhO1+fjhLSpAIAN\nG9bTXTkQLpJDGAJ0CfmFC7RwzkBQ13r/UNc6RU7C9S0I0/NnjUOFfBB4PG5s2bIBhOEhpE7p97Gs\nLhFcYgFqaqroWTm6VcDr2pETgUV5+VkqVANAXev9Q3fkFDkJCXfAEywn3dlJhXzYsXPnZ7DZOsGn\nTOx3Nx5ClzYdIAQff7xuRJ/liaKIs2fPgDFxYbc6n6ZHW1vr5e5xlF6hC53+6S7kI/k7RpGHkHAT\nhgEIoTvy4YbT6cDWrZtBWAFCyuSInsMIZvCJ49DU1IB9+/YobKF2qay8BJfLBT7NEL6PT9cDAEpL\nT6tlVlxAd+T9013I6e6cEi0h4SaEAas3UCEfbuzatR0ulxN8ymQQNvLOZkLaVIAw2PLJxhG7YwjV\nnuczuwl5RvD26dMnVbGJMjzoHmHc/TaFMhTCrnRCwOqN6Ojo6P8JGoEKeQR4PG5s3741uBtPnjCo\n5zK8EXziWLQ0N+HQoS8VslDbhM7H+TR9+D7GzIPRsyg/R8/J+4O+N/3Tc0c+MhfKFPkI94PoEnK3\n2xUXbU2pkEfAvn1FcDgc4JMnDGo3HkJInQyA4LPPto64C7Moijh/4RwYEwdGfznnnhACLlWPzo6O\nYH45pVeoa71/ego53ZFToiMk5IQQcAYTgPhIQaNCPgCiKGL79m0AYcAPcjceghHM4Cx5qKqqQFlZ\nqcwWapvW1ha4nE5wyVcHB3JJwfvCOeaUMCEBH2kLv8Hi8/l6vU2hDIWwK50QsAZj133a79RIhXwA\nTpwoQVNTA7iE0WA4/cBP6AMhZRIAYMeObXKZFhfU1FQBALhE4arfsV33VVdTIb8SKuCRQYU8cjwe\nD100D0BHhzWcQ84ZzQDio+UyFfIB+PTTTwBcFuKhwhhSwehTcOzYUdTX18lhWlxQW1sDAGATehHy\nrvvq6mpiahNl+NBdvL1e7Z9lqsmaNW/iv//7KVRXV6ltiibx+/2w2TrD3jA2LOTab7lMhbwfzp49\ng/Lys2BN2WD1SVGNRQiBkDoFkiRhy5YNMlmoffoTcsbAgvAMamqqY21W3EDPyPvH6/WEb8dDUJKa\n7N0bbK1cX097HPRGuM0yE5RFvqtMa/f2y1qFCnkfiKKIdeveAwDo0qfLMiZnyQOjS8KBA/tGTJ3x\nixfPg/AMGOPVzWUIIWCTBDQ2NsDpdKpgHSXe6b4L7y7qlL6hxza9Ewq6JSHXujmh6/4W1WyKFCrk\nfVBUVIiLFy+AS8gHa0iVZUxCCHSZsyFJEt555x/DvgZ7qHIbl6Lrc2fJJ+shSRLKy0dWEOBA0GC3\nyPB43N1uUyGPBOrl6Z1wlcmu6pOc0QzCMHFRfZIKeS80Nzfhgw/WgDA8dBmzZR2bM2WBS8jHxYsX\n8Nlnn8g6ttYoLj4EABCyTX0+hs8xdj32cExsiheogEeG2+3u9Talb+hnq3dCsUuEYbv+Z8AnJKOu\nrlbz7xkV8ivw+/149dWX4Xa7oMucC4Y3yj6HLnMuCKfH+vUf4NKlC7KPrwUkScKePbsBAgg5fb+H\nXLIOjJHDkSMH4XDYY2ghZThAhXzw0B1579TVBWMHCHNZFoWkVLjdLlit7WqZFRFUyK9g3br3cOHC\nOXAJ+eASCxSZg+H00GdfA1EU8fIr/y9umtcPhhMnjqG2tgZCnrlHIZgrIYRAPzYBHo8Hn3++M4YW\nxgf0ots/VMgHj9Z3l2pRU1MVTDnr9p0TkoLHqlpPkaVC3o0jRw5i+/ZtYIQE6LMWKHoR5cxZENKm\noa21Ba+++sqwOi8XRRHr138AADBMTBzw8boxCSACg08/3Rw3bQNjBb3o9o/b7QrfdrlowGQk0MXh\n1Vit7bBa26FLy+xxvy4tCwBQUaHt4GQq5F00NTXi9X+sBmE46POuH1Ip1sEipE0Ha8rGqVPHsW3b\nFsXnixVffPE5amqqoMs3g0scuN0rwzMwTE6Gy+XChg1rY2AhZbjQXby7izqFMhgqKi4CuCzcIfRd\nwk6FPA4IBAJYtepFeNxu6LLmgdUNvIuUA0II9DmLQDgDPv74Q1y4cD4m8ypJZ2cH1q9/H4RjYJyW\nEvHz9GMTwFp4fPHF58PifYgWuhOPDJfL1ettSt/Qz9bVnD9/DgCgv0LIOaMZnMmC8+fLNf2+USEH\nsH37VlRUXASXWAA+cUxM52Y4PfQ5wfPyN954Ne57Kn/wwRo4nU4YpiWDMfR9Nn4lhCEwzUmDJEl4\n663XRmzLV8rgcDqdELoCUqlrPTLi/RqjBOfOlQGEQJ+Rc9Xv9Jm5sNttaGioV8GyyBjxQt7W1ooN\nG9aDsDroM+aoYgNnygSfNA51dTXYvn2rKjbIQWnpaXz55V6wSQL0YxMG/Xw+zQDdaAtqaqqwa9dn\nClgYP4RiJuhFt28kSQoKOWcEAaFFhSKELpJ74vV6cfHSBehSMsAKVx8FGjLzAEDTDa9GvJBv3vwx\nfD4vdBmzQLiBz3OVQpcxC4QVsHXrZjidDtXsGCp+vx///OcbAADznPQhB9QYp6eACCw+/ngt2tu1\nnfKhJKEqZbRaWd94vR6IYgAsK4Blhbj83qgBXRz25Pz5cgT8fhiyR/X6e2PX/WfPnomlWYNiRAt5\nS0sziooKwQgWxVLNIoWwAviUyXA6Hdi5M/52ozt3fob6+jroxiT02rI0UhgdC+O0ZHg8Hqxd+66M\nFsYXodKjHg+tH94XDkdQuHlOB44Vwj9T+icQoELendLSUwAAY3Z+r7/nE1PAGU0oLT2t2XPyES3k\n27dvgyiKEFKnhuvrqomQMgGEFbBz52dxVW6yvb0dGzetByMERThadAUWsEkCDhzYp2l3lpKEhJzu\nyPvGbg8WEOJYARyrg8Nh1+yFVkvQHXlPzpw5BTAMDFl5vf6eEAJD9mjYbJ2a7RynvnqpRGdnJ/bs\n2Q3CGcAl9r4SizWE4cEnjYfdbkNRUaHa5kTMe++9DY/bHQxwE9ioxyOEwDQ7DQDw9tuvj8gLj7dr\nIde9ljilJzZbsOYAzxnAc3r4/X4auR4Bfj89Iw9hs3WiouISDBk5YPirOzSGMOaOBgCcPn0iVqYN\nihEr5J999gm8Xg+E1CkgJHrxkQs+ZSIIw+GTrZvioi1jSckRHDlyEFyKDroCi2zj8il66MYkoL6+\nbkS1fQW6gri6IrC91LXeJ52dHcH/HY3gOT0AoKPDqqZJcYHf7xv4QSOEkLvcmFvQ7+OMOcHfnzpF\nhVwztLQ0Y8fOT0E4A/ikcWqb0wOG04NPnoAOazs++0zbEewdHVa88carwdSxuUMPcOsL4/QUMAYO\nW7ZsGFG55d09EP6Af0R6JCKhvb0NAOBwtYPvSkHTek1sLUA/T5cJCfNAQs4ZTRBS0nHuXJkmjz1H\nnJBLkoR3330bfp8vGCnOaGc3HkJInQLC6bF584Zwj1ytEQgE8OqrL8Nut8MwPQVcQt9uqaHC8AzM\n89MhiiJWr34xfCY63LnSPUxriPdOSMgJIdB1CXlbW6uaJsUF3Xu4j2QkScKpUyfA6g3QpWYO+HhT\n7hj4/X5Nxu2MOCE/dOhLHDtWDNaYDi5htGzjyhlkQ1gBuoxZ8Pm8ePPNv2sygOejjz5Eaelp8FlG\n6McNPmc8Uvh0AwyTk9DS0oxXX31pWNWk74srS43SQie909wcXOQSQqATzACA1tYWNU3SLN1zx+Ph\nyC4W1NXVwmpthzGnICJvojGvAIA23esjSsg7Ojrwzj/fCNZTz14oiys44LZC8rkAvwv2C58g4Jbn\njI5LKABrysaZM6dQWLhLljHl4uDB/di2bTNYMw/zggzFmzAYpiSDzzTg1KkT+OijDxWdSwtcmQ9N\nC530TlNTAwCAgEAvBOMzGhsb1DRJs3TfhdNMiCBnzpwEABhyIgt21mfkgHBcOF1NS4woIX/33bfg\ndDggpM8EI8gTmOWq3QcguGOWvDa4a/fJMi4hJLjYYAV8uPZdzbgMq6oq8I9/rAbhGJivyQTDK/8R\nIoTAvCADrJnH1q2bcPDgfsXnVJMr86Fpn/arCQQCaGluDqeN6gQTCCFhcaf0pGe7VyrkQDDQDQCM\nOZF5ZhmWgyEjF7W1Nejo6FDStEEzYoT85MnjOHz4ABhDKvjkCbKMKfpdkLw9e4mLXhtEvzwpMAxv\ngJA+Cx63G++9944sY0aDy+XCyy//FT6fD+b56Yqci/cFI7AwX5MJwjF4482/a7rucbSE+tMz4Z+p\nkF9Jc3MT/AF/WMgJYaAXElBXV6fJoyi16X5cQ7vEBUsgnz1bCt6SBN4c+dFgaPd+9uxppUwbEiNC\nyCVJwoYN6wBA3j7jYh/5mH3dPwT4pLFgDKkoLj6kejGCNWveRHNzE/QTEyHkmGI+P5cgwDQnDV6P\nB6tWvzhso29Dq/3QlzOUZkW5TG1tDQCAdLuEGfSJcLmcNHK9F7ofz9CjmqBn0e129VmWtS+MWUEh\n11rAm6JCfvz4cXznO98BAJw+fRr33XcfHnjgATz33HPhoKWXXnoJ9913H771rW/hxAllggjOnSvD\npUsXwFnywOqTFJlDKQgh0KVNAxDMfVeL0tLT2L+/CGySDsapkbcnlRvdKDN0+WZUVVbg88+3q2aH\nkoRyoZmuBSfNjb6amprgorZ7RUajPlhVUO0FrxbpHndBa9IDZ88GhdiQNTgh16VlgOH4kSPkf//7\n3/HMM8+Ec+5+8Ytf4Omnn8a7774Ls9mMzZs34/Tp0zh06BDWrl2L559/Hr/61a8UseX48RIAwd1t\nPMKaskE4A06cPKZK1LYoinj//aBr3zwnDYRRNrhtIIwzUkEEBhs3rg9X9xpOtLcH4yFCiZFaiY/Q\nEiGxZhgq5JEQOq4BMCy/M4Plcn31wQk5YVjos/JQX18XTn/UAooJeX5+Pl588cXwz42NjZg7dy4A\nYO7cuSguLkZxcTEWL14MQghycnIQCATQ1ib/m1NeXgoQAtaYIfvYsYAQAtaUCbvNhvr6upjPf+JE\nCaqrqyCMMkfVEEUuGB0Lw6QkuFwu7N69U21zZKexsREAwHY5jpuaGtU1SINUVFzsquZ2eVFpMgQ9\nRZWVF1WySrt0F2+PxzOic8l9Ph/KykohJKWAMw0+6DkUHHfmjHai1zmlBl6+fDlqamrCP48aNQqH\nDh3CwoULsXv3brhcLtjtdiQlXXZ1m0wm2Gw2pKT077pNTjaC4yIv5NLU1AiGN4Mwir1cxWF1SfAD\ncLmsSE+fEtO5Cwt3AAAME7VzLKEfkwDXWSsKC3fiu999ADzPq22SLEiShOamBhAAhAAWwqC5uRFp\naWbF0/ziBavVira2ViRZcuHqlu6p403gOT0qKyuQni5fueDhgNcbPBdnCCBKAMv6kJ6eqrJV6nD8\n+HF4vV4kjS8Y0vNDQl5efhpf//odMlo2dGKmbL/97W/xm9/8Bq+99hpmzJgBQRBgNpt7pNo4HA5Y\nLAN/AdvbIw/WcLmcsNlsYE1ZQ7JbKxA+GFx24UIlxo+fHrN5q6oqcOLECfDpBnCJsYtSHwjCMdAV\nWGA9Z8WWLZ9h8eIb1DZJFlpbW2B3OMJfzBSWw6XOTpSXVyIlZWReeK+kpCR4VGY2pvUQckIITIZU\nNDfXory8CsnJ0XfiGy7U1QXT8liWgegXceFCNVg29gGrWmD79mBdDtPooWUvCclp4C1JOHjwIGpq\nmqHT6eU0r0/6W5zGLGr9iy++wG9/+1u8+uqrsFqtuP766zF37lzs3bsXoiiirq4OoigOuBsfLCFX\nNCMoV30sFoTy3mOddrV162YAgH5ComxjypUepB+XCBDg008/6VG5Kp6pqLgE4HKgWzoblPTKykuq\n2aQ1QoFKCaary2qG7tNaMJLatLQEK96xbPBzNVIr4Pn9fhw5cgic0QxDZu6QxiCEwDx2MrxeL44d\nOyqzhUMjZkI+evRo/OAHP8C3vvUtmM1m3HDDDZg+fTrmz5+P+++/HytXrsSzzz4r+7yhZhuMTj4h\nUgNGsACEiWnzkNLS0zh06EuwiQL4TEPU4/k7vBBdfkiuANq3V8PfEd05HWvkoMu3oK6uBrt2fRa1\nfVrg3LmzAC4HumVyQSEvLy9TySLtcfbsaTCEhcWYftXvEs1Z4cdQLtPc3AhCAKYrULW5uUlli9Th\n8OEDcDodMI+ZBMIMXf4SxgWPN7VSdVNR13peXh4+/DBYUvOmm27CTTfddNVjVq5ciZUrVypmQ7AK\nGAFnzlFsjlhAGBacKRs1NVWora1Bbm6eovPZ7Ta88ebfAQKYZepsZjvYGCqCB9Hug+1gI5JvHVzU\n6JUYp6fAV+/ERx99iKlTZyAvL7rx1ObMmdNgCQHbFcSVxfFgoK3AGjVpa2tFdXUVEs3ZYHppeGQy\npIBjdThx4hgkSaJxBQjmjXd0dIBjSVjI1QiaVRtJkvDpp58AhCBp6pyoxhKSUmHMLUBZWSkuXbqI\nMWPUzYga1gVhyspKcfHiebCmTDB89DtKteESCwAAW7duUnQer9eLF174M1qam2CYmCRLpLro9kO0\n9+yDLNp9EN3RFXVhdCyMc1Lh9Xrxl7/+Hu3t8VsMxGptR01NFbJYDiH94QhBFsejurqS5pMDOHHi\nGAAgOaH3hSwhDJIsubBa21FVVRFDy7RLXV0w6JhhCBhCwHNMuKDOSOLMmVOorq6EuWAieEv0gbtJ\n0+cDALZt2xz1WNEybIVcFEW815X7rEufobI18sBZ8sDokvHll3tx6dIFRebw+/1YvfolnD9fDiHP\nBMNUeQKGpEDv5+J93T8YdLlmGKeloL2tDc8//7seObPxREnJEQBAAd8zqDD0c0lJccxt0hrFxYcA\nAMkJfXteUrpEvrj4cExs0jqVlRUALp+Pp6UYUFdXM6K6oEmShI8++gAAkDxjoSxjGnNGQ5eaiSNH\nDobfY7UYtkK+Z89uVFVWgEsYDdYwPKJ9CSHQZc4GALzzzzdkLw4jiiJee+1vKCk5Ai5dD/M85Tub\nyYV+YiL0YxNQW1uNP//5d3FZvero0aCQjxF6CvmYLiE/enRkC5Pdbkdp6RmYDKnQd7Ut7Y0kSy4Y\nhsWRIwdp3XUEc+6By8VzMtOMEEVxRBXOKS4+jEuXLsI8ZhL0aQP3Ho8EQghS538FALB+/QeyjDlU\nhqWQ2+12rFv3PgjDQ5cxW/H5BEFATk4OBEH59CzOlAkuYTQqLl1EUVGhrGN/8MEaHDr0JbhUPRKu\nzQJh40PEgeCXyjgrFbrRFlRWXsJLL/01riLZOzo6UFp6GhksB8sVZ78JLIt0lsOZM6fQ2Tlyq3KV\nlByBKAaQmth/tyqW5ZFkzkVDQ/2IdCFfyfnz5RAEFmzX+XhOpqnr/nNqmhUzAoFAUGgJQercxbKO\nbcotgCE7H6dOHQ93U1ODYSnkRUW74XQ6IKRNVfxsXBAEPPTQQ1i9ejUeeuihmIi5LmM2QBh8+ukW\n2XblBw7sx44d28BaeFiuywLh4u+jQQiBaW4a+Gwjzp49HVe9y48cOQBRFDFB6D0eYYKggyiKKC4+\nGGPLtMORI8HXPpCQA0Bq0ugezxmpdHZ2orGxAdkZxvB9uVlBb8a5cyMjE6KoqBCNjfVImDgTQqL8\ntQXSFiwBAKxb955qHqD4u1pHQGHhLhCGA580TvG50tLSsGzZMgDAsmXLkJaWpvicDG8Al5CPxsYG\nlJefjXo8l8uFt99+HYRjYIlRj3GlIITAPD/Yu3zbts1xE/C0f/9eEADj+hDycV0LxP3798bQKu3g\ndDpw5swpmPQp0OsGLhqVbMkDQ9gRL+Tl5cF8+lHZl9+zRIsAsynY+GO4Hz14PG5s2LgODMcjdc61\nisyhT8uCecwkXLp0UbXPW/xesfvA7/ejubkJjD4FhFV+d9zS0oIdO4IlTHfs2BEuvKA0XFelOjnS\nSA4c2Au32wX9xESwFu1UbxsqDM/AOCMYF/H55ztUtmZgamtrcOnSBYzieJj6yG01MyxGcTwuXDg3\nIlOHjh8vQSAQQEpifkSPZ1keiZZs1NXVjsj3K0Rp6RkAQH7OZSEnhCA/xwK73Yba2mq1TIsJu3fv\nQmdHBxKnzQNn7DuuIlpS5y29o55EAAAgAElEQVQGCMHGjetVaWw17IQ81GuXMLGpve31erFq1Sr8\n8Ic/xKpVq2LWjIAwQcF1OOxRj3XkSDASWF8wfOpT81kGMAYu/Nq0zL59XwAAJg1Q6jH0+717v1Dc\nJq0RikCPVMgBICUh6F4fyUGCZ8+eBs8xyErvWY41JOwhoR+OeL1efPrpFjC8gOTp8xSdS0hIhmX8\nVNTV1YaDVmPJsBNys9kMvV4P0Ru7oCCv14u6urqYdhQKvb709Og7ulmtVhCBBaOP36YyV0IIAWvh\n4XQ6NJ1m4/F4sGfPbhgIE45O74sxvAA9YVC0Z/eI6l7lcrlw8uQxGHSJMOojz/9NTsgDIWTEutfb\n29tRX1+HvGxzOPUsRH5uSMiHbwW8oqJCdHZ2IHHKbLA65euIpMxcBBCCzZs/jvmRxbATcoZhMH78\nRIheG0Rf5M1V4g2/I9jacsKESVGP5XDaQfj4iVCPFNJ11h/y0miRgwf3w+l0YopOB3aAVD+OEEzR\n6WB32LsqFo4Mjh8vgc/niyjIrTs8p0OiOQeVlRVobGxQyDrtUlbW5VbPvdrTlmjRITFBh/LyUlVc\nwUojiiJ27NgGwrJImqbsbjyEkJgCc8FEVFdX4uzZ2Ho6hp2QA8CcOcE/nL9zeOZJin43Ao4GjB49\nRpaOWATDT8S7o9VceFEUsW3bZjAApkXYQWmaTg8GwKfb5MtY0Dr79+8BAKQmFQz6uald1RD37y+S\n0aL4ICQm3c/Hu5OfY4bT6UR1dWUszYoJJ08eR1NTIyxjp4AzxK7LW9LUuQCAnTtj2/thWAr5ggXX\ngGEY+DqHZyCH314LQMKiRdfJMp7P5wNhtCl2UdH1mrTqhj506AAaGxswSdDB3Evd8N6wMCwmCjrU\nN9SNCJdxU1MjTp8+CYsxfVBu9RCpSflgWQF79uyG3x9dOeB44+zZMxAEFhmpxl5/H4pkj/XuMRaE\nmiiFhDVW6DNyoEvLxLFjxWhpaY7ZvMNSyM1mC8aOHQ/R3QYpoM2LeDQEutzqs2ZFX+zG6XTA6XSA\nMcUmODCWsMbgmb8WOz35/X5s3LgOBMBcfe8X2r6YqzeCANiwYd2wF6fPP98OSZKQmTpxSM9nGR7p\nSWPQ0WGNi8BHuWhra0VTUyPysszhRilXMlwD3pqaGnHq1AnoM3KhS40+hmgwEEKQNGUOJEnCnj27\nYzbvsBRyAJg8eSoACQF3m9qmyE7A1QqLJQFZWdF3dDt9+iQAgEuITdpZLKvgsYnBOc6cOan4XIPl\n8893oLGxAdN0eiSwke3GQySyLKbq9GhoqNdMG0UlaG9vx+7dO6HjTWEX+VDITpsKAoJNm9RJDVKD\nUBBbb+fjISxmAUld5+TxVAVxIIqKggKaOHmmKvObx0wCI+hQVFQYs4X2sBXy0Nmx5HerbIm8SJIE\nye9GamqaLGe/oTKvQr5yOZYhYl0FT8g2gvAM9u3bo6mda2dnJzZtXA+BEMwf5G48xAK9EQIh2LBh\nbdw2iRmILVs2wOfzITdjRq8tSyNFr7MgPWUcGhrqR8xZeajt7eh+hDz0e7fbrVgTplgTCARQtPcL\nsDo9zAVD8+JEC8PxsIybio4OK06ePBabOWMyiwqYTMEAh2HnWpdEQAqEX180VFZewqlTJ8Cl6mOy\nI491FTzCMtCNMsNqteLLL7VTEW3t2nfhdDkxX2+EoY8CMANhYBjM1xvhdDrx4YfvyWyh+lRVVaKw\ncCf0ugSkp4yPery8jJlgGBbr1r0Pl0u7WQxyIIoiTp48DrORR3pK/2lXY/ITAVxuDxvvnDp1Ap0d\nHTCPnQyGU++4MGHidADA3r17YjLfsBVyrUYqy4Ucr2/Tpo8BAIbJ0ffmjQQ1quDpJyYBTDC3Uwtu\n1bKyUuzbtwdpLIsZEUaq98UMnR6pLIu9ewtlKdWrFSRJwpo1b0KSJIzJWQCGRH+Z0glm5KbPQGdn\nBzZuXB/1eFrm/Ply2O02jM1PHPA6MTrXApYl4Ra68U6ouFLChOmq2qFPzYSQko7jx0ti0uho2Aq5\n0FWzWhJ9KlsiL6HXI/RRkztSOjqsOHasGGySAD5D+WIJgDpV8FgjB12+GS0tzaoXv/D5fHjrrdcA\nAEuMZjBRLsYYQrCkq+zk22+9rqnjg2jYv78I586VISUhH0mWXNnGzUmfBr1gwc6dnw3rFp6hGgMT\nxw68QBd4FmNGJaC2tgY1NfH9nrjdbhw/XgI+MQW61OhalcpR0CVh3FSIYiAmlQWHrZAnJQW73Eg+\nl8qWyIvUVeQmOTm6Lj6HDh2AJEnQj7bE1HuhRhU83ejgOeGBA/tiNmdvbN26CQ0N9Ziu0yNTJrdf\nFsdjmk6PuvpabNu2WZYx1cRut+ODD9aAYTgU5MyXdWyGYVGQuxCiKOKdd17XhIdGbrxeLw4d+hIm\nA4/RuQkRPWfqhGA80b598R0/cPLkMfh8PlgKJg75muZpb4bfYUfAYUPFutfhaR96ClnojL64WPls\niWEr5FlZ2dDrDfDb6yBJw+cLG8whBwoKxkY1jtXaDgBgk6Lb2ccDXFLw/D/0mtWgvr4Wn2zZABPD\nYJFhaAFufbHIYISRYbB588doaKiXdexYEwrey8uYCZ0gfwBmsiUXKYmjcf78OU3FTcjFgQP74HA4\nMH1Sap9pZ1cybnQijAYORUW74fHEb3Bw6HggmiC3+l2bgnFIAHyd7aj/fOiLY96SCF1qJkpLzyge\nlzFshVwQBFxzzXWQ/E7lKrz1FUkbRYRtf0gBL3zWi9Dr9Zg/f6FMgw7vNoYAAJXXcaIo4s03X4M/\nEMBigwmCDGe+3dERBosNJvj9frz11mtxu9Osq6tFYeEu6HUJyE6fqtg8BdnzwTAs1q//IK6F60rC\nZUkJwZxp6RE/j2MZzJ6aDqfTiaKi+GzII0kSzpaVgtUbIaRE/tq743c64Ovsudj3dbTB73QM2S5j\nbgFEMYDz588NeYxIGLZCDgDLl98OQRDgaSiG6I2+S9iVMJwBROiZ3sEIFjCc/GfOkiTBXX8Ikt+F\nr371TuiiDJQaMya4o/fWD+8IXgDwNgRfY7RejKHyxRe7cO5cGcbyAsZGGdvQF2N5AWN4AWVlpTEt\nRCEn69a9B1EUMTprriwBbn2hE0zITpsKq7Ud27dvU2yeWHP06BHU1tZgyvhkWMyDy0KZPS0dPMdg\n27ZNmm4y1BctLc2wtrfDkJU7ZLe6FOg9xqSv+yPBkJUHAIoHow5rIc/MzMaDD34fkuiDq2YPRAVy\nyg251wNdtcoZwQJ97vWyzyFJErzNJ+C31WDSpCm4886vRz3mrFlzYTSa4K2yQ/LH5w4uEiRJgvti\nBwDguuu+EvP5m5oa8eEH70JHCBYr2A+ZEIKvGE0QCMEHH/xTk9Xs+qOysgLHjh2FxZiO5IRRis+X\nmz4dHKfDZ59thcsV/3E0oihiw4Z1IAS4bl72oJ9vMvCYPS0d7e3tKCz8XAELleXSpYsAAH2GfMGR\ncqDPCBbtUjpPP2IhLysrw+HDh3v8iweuv34Jbr31NoieTrgqP4fol/dLy+qTQHgDwBlgGncH2CHU\ng+6PoIgfh7e1FJmZWfjhDx8BM8Tc4+7wPI9bblkO0ROAq9wqg6XaxFvnhL/Vgzlz5iE7O/pKeINB\nFEW8/voqeLweLDaYYJLh79YfJobFYoMJHo8H//jH6rhysX/yyUYAQF7mzJgEX7Isj+zUKXA6HSgs\n3Kn4fEqzb98e1NXVYNrEVCQnDs1bt3BWJgSexebNH8Vdrn2ou52QmKKyJT1hBR1YowlNTY2KzhPR\nleUnP/kJHn30Ubzwwgvhfy+++KKihskFIQT33/9gUMy9nXBV7ILolb8SlhIXH0kS4Wk4DG/rWWRm\nZeOJJ34RjsaXg9tuuxOJiUlwn+uA6BoeqUvdkUQJrtNtYBgG3/zmAzGf/7PPPgm71Cco5FK/komC\nLuxi3759a0zmjJa2tlYUFx+CyZCCRHPsFltZaZPBMjx27doeV4ueK/F4PNjw8VpwHIPF84f+/hkN\nPBbNzoTdbsfWrfGVAdHUFBRyPkG+66NcCAnJaG1tgc+nXCo0F8mDSktLsXXrVrCDrAmtFUJirtcb\nsGnTR3BW7IRh1BKwhuhbgCqFJPrhqt2PgL0O+fkF+PGPn0Biory7fZ1Oj7vvvhdvv/06nGVWmGcr\nW2kt1ngqbQjYfVi69BZkZQ3e3RgNlZWX8NFHH8LIMFhiNMcsxY8QghuMZjTYrFi//gNMnTod+fkF\nMZl7qBQVFXY1RpkU01RIjhWQmlSAprZzOHXqBGbOjL4JkRps374N7dZ2XDMna9Bn41cyb0YmSs40\nY/v2rVi69BZZ2iTHgo6OoFeRMylfanqwcEYLJEmCzdap2PsZ0Y581qxZqKyM7561hBB8/ev34bvf\n/TdA9MJVtRt+e53aZvWK6PfAWbkbAXsdpk2bgf/6r1/ILuIhFi++ARkZmfBU2BAYRrtySZTgKrOC\n53ncddc9MZ3b6/Vi9eqXEQgEsNRoHnIZ1qFiYBjcZDQjEAjg1dUvazp4SZIk7N27ByzDIy2KxihD\nJTMlmKq0d298Rmt3dnZg69aNMOo5LJydFfV4PM/gKwty4PP58PHHa2WwMDY4nU4QhgVhI9qbxhSm\nq6eE06nccUVEV5hrrrkGd955J2688UbcfPPNuOmmm3DzzTcrZpSS3HjjzVi58ifgWAau6iL4rBfV\nNqkHos8BV+VOiO5WXHvtYvzoR4/DYFCu8hrHcbj99q8BogT3+Q7F5ok13loHRKcfS5YslfU4IhKC\nhV/qMEOnRz4fm65yV5LPC5geLhSzRRUbIqGmphqtrc1IsuSCZWNfG9tkSIFesODUqeNxWRlvy5YN\n8Hg8uHZeNnSCPB7TqRNSkZ5iwP79RaitrZFlTKVxuZxgBJ0mS3MzXcdqSsYdRCTkq1evxltvvYU1\na9bg7bffxjvvvIO3335bMaOUZvbseXj88adhNBnhrj8Eb1u52iYBAESvDa7K4Bn+bbfdhX//9/8A\nxym/wrz22sVITEyC55INojv+LmZXIokSXKXtYBgGy5bdFtO5GxrqsfWTjTAxDBbKXPhlsCwyGGFi\nGGzZsiEcDKQ1TpwoAQAkJ+SpMj8hBEkJeXC73SgrK1XFhqHS0tKM3bt3IjFBh1lT5DsWYxiCryzM\nhSRJ+OijD2QbV0kCgQBIjD1fkRKyS8k4jIheeXJyMubPn4/c3Nwe/+KZ8eMn4sn/ehYJCYnwNB6F\nt1XdL3HA0wFn5S6IPifuvfdb+OY3vx2z1SXP87j77nsh+UU4z6hX/UwuPBXBs/ElS5YiIyO6msuD\nZePG9fAHArhegcIvg0UgDK7rKhSj1UYhFy+eBwAkmmMbw9CdRFNWly3x1cpzy5YNCAQCuH5eNlhW\n3s/a2PwE5GSaUFJSjIoKbXktKVcT0V+/oKAAK1aswF/+8he89NJL4X/xTl7eKDz11LNITk6Bp+k4\nvK3qdJAKeDrhqtoNye/GAw98D3fc8bWY2/CVr9yI7JxceCps8NTIXzyHsL0vSvq6f6j4rR44T7ZC\npw8G8sUSu92O4uJDSGJYjFXJpX4l43gBiQyL4uJDcEZRoUopqqoqwXMGCHxsGvf0hskQTFmqrq5Q\nzYbB0tzchL17v0BKkh5TxsufckUICUfAb9igzUXglUgYAVUq+yAiIc/JycENN9wAnlevv6tSZGZm\n44knnkFSUjI8Tcdi7mYXvfawiP/Lv3wPt9yyPKbzh2BZFv/5Hz+CTqeDo7gZvjZ5i+cweg6Muefn\nhzHzYPTyHR0EnH7YDjRCCkj4wf/9T8UCBPvi8OEv4ff7MVmnnbM6Qggm63Tw+Xw4dOiA2ub0wONx\no7W1BUaZay8MFoE3gmUF1NXVqmrHYNi8eQNEUcR187Ijrqk+WPJzLcjLMuPEiRLFC5pEC8tygEZT\nCKUuu5TM+opIyB966CFMmTIFjzzyCB544AFkZWXh4YcfVsyoWJOZmYX/+q9nwm52X0dFTOYV/S64\nqgoh+V341rcexM03qyPiIXJz8/CDHzwCiIBtbwO8TfIGZ1gWZYaK4IEx88GfZSJg86JzTx1Epx/3\n3LMCc+bI2zkrEsrLywAAY3l5csblaKUIXLbn3LkyWcaTi9bWVgDBkqnREO37RAiBjjehtbVVtvdc\nSRoa6rF//x6kJukxaaxygZyEEFzftSvXegQ7y7JhwdQamhHyX/ziF9i+fXv454MHD+KXv/ylYkap\nQWZmNn7ykydhMBjgrj8Iv0PZ4CBJ9MFV9QVEnx133XUPbr31dkXni5Q5c+bh4YcfAwsG9v2NsrrZ\nuUQBjIEDMbBIvnUUuER53M++Njc699RDdPpx7733484775Zl3MFSXV0FnhAkRBl00xrwwy6KsEsS\n3u1oR2sUtZ4BIJFhwBGiuR7cLS3BMrI6fmi5v053O7w+J7x+J0rOboDTPfT4Dp1ggsfjhs0mf7Eo\nuVm37n2IoojrF+QothsPMSrHjPxcC06dOoHTp08qOlc0MAzRbgOosF3K/a0iuuKcOnUKv//97wEA\nKSkp+OMf/4iSkhLFjFKL/PzR+NGPHgfLsHDX7lekAhzQVf+77iBEjxVLlizF179+nyLzDJW5cxfg\nJz95EjpBB/uhJrjKrLLuVOR0O3vrHLAV1UPyivjud/8Nd9xxtypubZ/Pi4aGOqQwbNTzf2a3hU/7\nOsQAttuj+xwSQpDCsKivr1W0utRgqa6uBgAYhuhaL6v4Inwu6vZ2oqxy6LngBl3Qhtra6iGPEQvO\nnDmFo0cPIyfThIljlD+SIITgxmuCGQXvvfeOZlP04iNqPaDYHBG9clEU0dR0uQlDa2urLPW+tcjE\niZPxve/9G6SAF66avZAUePO9rWfDDVAefPD7mjlP7c7kyVPx9NP/jeSUFDhPt8F5QntuR3dFJ2wH\nGsGzAlau/CluvFG92gY1NdUQRRHpUaYLOkURHVd85qxiAM4o3YZpLIdAIIC6Ou3kBVdVVQAATPrB\nu4e9Phfc3s4e97k9nfD6htZLwWQI2lBZWTGk58cCt9uNN998FYQQ3Hz9qJhdNzLTjJg1JQ11dTXY\nsmVDTOYcLH5/AFA5S6RPutpaK7kIiviM/J577sGjjz6KRx99FN/4xjeG1Rn5lSxefAOWLr0FoqcD\nnuYTso4dcLfD23ISiYlJ+M///FFM8sSHSl5ePp75+XPIzc2D+0InnKfbNCPmnmo7HEdbYDab8dRT\nz2L27Lmq2hPqN5wWZWUpfx/vb1/3R0pogaF0X+RIcblcOH68BDreBJ0weNe6KPW+wO7r/oFIMGUC\nIDh8+MshPV9pJEnCu+++hZaWFiyclYms9OjiCgbLDdfkwWIWsGXLBpw/r426G92x2TrB6tXLfOgP\ntqvltD1Kz1p/RCTkd911Fz766CPccccduPvuu7F27VrceuutAIDdu+Oz9/FArFjxADIysuBrK0Mg\nirO37gR7ih8BJBHf//4PYLEkyDKukiQnJ+NnP/s5MjIz4S7vgKdC/TNEX5sb9iNNMBgM+OlPn8bo\n0WNUtUcURRTu3gkGwCiNZnbk8zwYALt379DEYuzQoS/h9XqQkTJBEx4pgTci2ZKLS5cuhj0FWqKw\ncBf27v0CmWnGIbUpjRadwOL2pQWQJBEvv/wXWK3aqTfh83nhdDrAGmK7uIkUrssuq1W5LpMR+yIy\nMzOxfPly3HzzzcjIyAjf/8ILLyhimNrodHo8+OD/AQB4muTZlftttRDdrZg/f2FcNWhITEzE4z/7\nOXR6PVyn2yF6lTvrGQhJkuA41gpIwCOP/ASjRxeoZkuI48dLUN9QhwmCDmZGm42FzAyL8YIOdXW1\nOH5c3fgWt9uNTZs+AiEM0pPHqWpLdzJTg3XX1659TxOLnRClpafx7rtvwaDncPetY8Fx6riQ83Ms\nuGFRHjo6OvDSS8/D4/GoYseVtLW1AZCvYYogCMjJyYEgyBOMG7Krra1VlvF6I+pPhJY+8HIzbdoM\nTJo0BQFHvSy7cm/rGRBCcM89K2SwLrakpqbhrju/DtEbULUmu6/eiYDVg4ULr8WUKdNUsyOEw2HH\nmjVvggCYpVHXXojZOgMIgDVr3lC1OMzGjevR3t6GnPRpUaeeyUmSJReJ5mycPn0Shw9rI+e+pqYK\nL774PCRJxNeWjUWiJTbtcPti/swMTJ2QgosXL2D16pcQCKi3qA9RXx9sfiVHL3JBEPDQQw9h9erV\neOihh2QRc77LroYG5Zp0RS3kWnCLKQUhBLfeGqzV7bNGVxAh4G6H6G7DzJmzkZ0du57LcrJ06TIQ\nQuBrlrdYzGDwNQeDmW66aZlqNoSQJAlvvvka2tpaMU9vRKoGOy91J5XjMFdvQGtrK95++3VVFuEX\nL57Hjh3boBcsyM2YEfP5+4MQgrG514AhLNaseQs2W+fAT1KQtrZW/OX538PtduH2pQXIz7Goag8Q\nfI++esNojM614NixYqxZ86bqm7n6+mAhHzmEPC0tDcuWBa8ty5YtQ1pa9DXsWb0RjE6PujoNC/lw\nZ+bMOUhMTIK/swrSEANpAMDXcQkAsGTJTXKZFnMMBgPy8vLhb/dAEtX58vraPGA5DmPGjFVl/u4U\nFRWiuPgQsjkO8zS+Gw8xX29EFsvh0KEDKCoqjOncXq8Xr732N4iiiLF514JltLfw0essyMucBZut\nE++88w/VRMrhsOP553+Hdms7bliUq0gZ1qHCsgzuvnUc0lMNKCzcpXoke3NzMKOKT4i+OE5LSwt2\n7NgBANixYwdaWlqiHpMQAiEhGS0tTYo1TlFUyI8fP47vfOc7AIDS0lKsWLEC3/72t/HUU0+FX9CH\nH36Ib3zjG1ixYoUmA+dYlsXChddCCngRsA+tSIwkifB3VsNoNGHGjFkyWxhbcnNzAVGCqFLvctHu\nQ0Z6BniVa5nX19fi3Xffgo4Q3GyygIkTzxRDCG4xWSAQgnfffQsNDfUxm3vjxvVoaKhHVtoUJJqj\n752tFDnpU2ExZuDIkUMoLj4U8/kDgQBefvmvqKurxbzpGVgwS74KiHItTHQCi/tum4AEs4CPP16L\nAwf2yzLuUGhpaQYA8JbEqMfyer1YtWoVfvjDH2LVqlXwer1RjwkAnDkRgUBAsSBBxc7I//73v+OZ\nZ54JB0S89NJLePjhh/Hee+/B6/WisLAQzc3NeOedd/D+++/j9ddfx/PPPy/bGycn11xzPQAMuXRr\nwNEIye/CggWLNJ1uFgkZGcELcKAz9n+ngMsPySfGvKPZlYiiiNWrX4LX68UNRjMsGg1w6wsLy+IG\noxlerxerV7+kaHvFEO3tbdixYxt0vAn5WXMUny8aCGEwbtR1IITB+vUfxPwceO3a93D27BmML0jC\n0uvyZDm+bG5zwe7wwubw4bX3T6G5bWj59t0xm3jcd/t4CDyLN95YjaqqyqjHHAqtra1gdXowMi3u\nvV4v6urqZNUi3hzMUGptjX6H3xsRCfnKlSuvuu973/seAOCDD3rvV5ufn48XX3wx/POUKVNgtQYr\nhDkcDnAchxMnTmDOnDkQBAEWiwX5+fk4e1adDmT9UVAwBrm5efDbayH6B38+7LMG2wAuXnyjzJbF\nnmnTguea3jp567BHgrcuGKA1fbq6Xo0TJ0pQVVWJCYIO4wR1g4+GynhBh/G8gMrKSzh58rji823Z\nsgF+vx95mTM16VK/EoMuARnJ49HY2IAvv9wbs3mPHTuK7du3IiVJj9uXFsgWg7Rx+wWETsPaOzzY\ntEOeJiipyQbcflMBfD4fXnnlr6psxEQxAChYx1wOCKtsT/J+v1GPPPIISktL0dTUhJtvvlw1KxAI\nICsruDPT6Xq/kC1fvhw1NZerSBUUFOB//ud/8Le//Q0WiwWLFi3Cp59+CovlcgCHyWSC3T5wbe/k\nZCM4LrZ/uLvuuhOrVq2Cr60cuoyZET9P9Nrgt9VgzJgxWLRodtwHB6amzkVqairaatoQmJQE1hyb\nvGnJL8J9vgOEECxbdiNSU9UL/Ckq+hwAMEcXH+fifTFbb8R5nxdFRbtwyy1LFJsnEAjgwIH90PEm\nTaWbDURuxgw0tpXj8OH9uOeeOxWfz+1247333gTDEHxt2VjoBHmucXanD+0dPVPF2qwe2J0+mI3R\nf38nFCRh3owMFJ9sxO7d2/Dggw9GPeZgEAQeUClmJ1JCMUWpqRakp8t/7epXyH/3u9/BarXiN7/5\nDZ555pnLT+I4pKamDmqi3/zmN1izZg0mTJiANWvW4He/+x0WL14Mh+NyGozD4egh7H3R3h773eDs\n2dfAYnkXdus5CKmTQNjIdmLeljMAJCxffhdaWuTv860G3/zmv2DVqhdgP9KEhCU5IAo3bgAAx8lW\niA4/br/9axBFAc3N6hSmsdttKCkpQRbLITXOj0nSOQ6ZLIejR4+ioqIeJpnycK/k0qULcLmcXcVf\n4ie+VieYYNQno7S0FLW1rbLlFffFhg3r0NzcgmvmZCE9Rb5FYiDQ+y6wr/uHwuIFOSi/aMW6desw\nb951SEtLl23sgWAYFqLPC0kUNVtvXfQGF1IOh3/I167+FgD9vmqz2Yy8vDz87W9/g9vtRn19Perq\n6lBVVTXopimJiYkwm4MXioyMDHR2dmLmzJkoLi6Gx+OBzWbDhQsXMHHixEGNGysEQcBtt90FKeCD\np+VMRM8JuK3wdVQgOycX8+cvVNjC2LFw4TVYsOAa+Ns8sBc3Kx7Z6yq3wnPJhtzcPNx9972KzjUQ\noQjZjDgX8RCh1xEKGFKCUEnPYBnU+CLBnAW/3694tTefz4vdu3dAr2OxaI52AwH7QuBZXD8/G4FA\nALt374zp3Dk5eZACfvhsylVOixZPezMIIcjKUqYqX0RXo2effRZffPEF8vPzw/cRQvD2229HPNGv\nf/1r/PjHPwbHceB5Hs899xzS09Pxne98Bw888AAkScKPf/zjPl31WuDmm2/F559vR0vrOQjJ48EI\nfa+QJEmCp6kEgIT7VxoMRzsAACAASURBVPzLsGsy8/3v/wDt7a04f/4cHCyBaU6aIscG7gsdcJ5q\nQ3JKCn70o8fBq1wCNRSsotUKboMlFKjX0tKsWKnb9vZg5S29Tv086MGi76oDH3oNSnH06BHYbDYs\nmJUJgY/Pz9aU8Sn44mAtivbsxje+sULR/tvdGT26AF9+uRee1iZZcsnlRpIkeNuakZ2do5i+RSTk\n+/fvx44dOwbtWsrLy8OHH34IAJg/fz7ef//9qx6zYsUKrFgRH5XOeJ7HihUP4JVX/h88jcdgGPWV\nPh8bsNch4GjEtGkz4j7lrDf0ej0ee+wJ/OEPv0ZVRSVACEyzU2UVc/fFTjiOt8JiScDjP/t5TN11\nfRGK4TDEeaxDCH3X6+h+xCU3HR3BSoA8F38xBSGbQ69BKU6dCpaB1lK++GDhOAYTxyTheGkLKiou\nYdy48TGZd+zY4DzOukpYxk6OyZyDwd1cD9HnxdixExSbI6JtYnZ2tmbq6qrNvHkLMXHiZPjttfA7\nGnt9jCSJ8DQdA8Mw+Pa3vxv3AW59YTSa8LOfPY1Ro/LhudQJ53H5Wp26KzrhONYCiyUBTzzxjGIu\nqcESisrlhsnfNPQ6lPx+h7o+8RHGlWgJngvarGTnKgAoKyuFXschIzX+FjvdCVWfKy8vjdmcY8eO\nR0JiIhxV5yHFIJVysDgqgx0H586dr9gc/e7In3rqKQDBqNO7774b8+fP7+Eu+d///V/FDNMqhBDc\nf/+/4LnnfgFP8wmwxluueoyv4xJErw033ngzcnJyVbAydpjNFjz++M/xhz/8BjUXq8AYORgmJkU1\nprfBCUdJsEXpE088g9zcPJmsjZ6Q4A0XIee7XofXq5yQO50OEELAxEHa2ZVwbNALqWRter/fj9bW\nFuRlmeJ+0Z/etRBpbBxa8ayhwDAM5s6Zj8LCXXDVV8OYOzpmcw+EJEmwXyqHTqfHtGnTFZun32/W\nwoULe/xPCTJmzDjMnbsAR48eRsDZ1ON3kiTB11IKjuNw1133qGRhbDGbLfjxj5/Ac8/9AtZTbWDN\nPIScoTXD8Hd6YT/UBI7j8aMfPa4pEQcAtztYSEOI8wtuiNDrCL0uJXA6XWAZIS5FimWCQu5yKff+\nWK3tkCQJZpO61QrlwNL1GpSOKbiSa665HoWFu9BRflJTQu6qr4LP3oHrrvuKotUo+xXye+4JCtGV\nxd4JIZoOSosFX/3qHTh69DB87ed63B9w1EP02XHd4huRnBy/512DJTk5BY899jh+/etn4ShpAZeq\nB6MbXLCLJErBKHi/iH9/6GGMG6fcmdJQcbmCqY9KC7kgCEhLS0NLS4uiRTZCO3Ilhcrn84JRKDhQ\n6fcp5EVQ8m8QKhLCsvG30LkSpus1xKJaYHcmTJiE7OwcNFSeg9/lBGcwxnT+vugoC8Y+3HjjzQM8\nMjoiOiN/+OGHceutt+KRRx7Bww8/jGXLluHee+/FLbfcgi+//FJRA7XKuHETMGpUPvz2WqDbsbDP\nGmyOctNNV7vchzv5+QW49977IXoCcBwffClC9/kOBNo9uPbaxVi48FoFLIyeUIndgIIZd0q0UuyL\nQFdMg5Klg/1+vyL547F4n0J2+/0+2ccOEf5MyZjXrRaBgPKfp94ghOCGG26GJAbQWX4ypnP3hd9p\nh6PyHHJy8hTflET07crMzMT777+Pjz76CB9//DHWr1+P6dOn45133sGf/vQnRQ3UKoQQLFhwDSBJ\nkKRgAxFJDCDgqEd6eoZiqTxaZ9my2zBmzFh4axzwt0Vezlb0BOAqs8JkMuOBB76roIXRYeha6Xsl\n5S66SrRS7Atvl5AbFNzBmM1m+APyn8HH4n3yd5VkNpuVS51LSEgEIQSdduUWC7Gi0x70XCQlRd+J\nbLAsXnwDdDo9OkpLIGmgT7r1TAkkUcSyZV9V/FgpIiGvra3F9OmXD+onTZqEqqoqZGdnx9yFoiVm\nz54XvCEGPzQBVysk0Y9Zs+bG5XmgHDAMg/vu+zYAwHkm8k4/rnNWSD4Rd931dcUqjMlB6LjEKip3\noVCilWJfWLsueEpeeJOSkhEI+BAIyCtUsXifvP7gUUpiYnQBnP3BcRzS0zPQZnWr3ts7WtqswYVP\nZmbss0yMRiOWLFkKv9MO26WymM/fHdHvQ2fZcZjNFlx77WLF54tIyEeNGoU//elPOHfuHMrKyvDn\nP/8Zo0ePRklJybArdDIYcnJyYTKZgK7dWcAVrI41aZL2chljyZQp0zBp0hT4mlzwdwx8tij5RXgu\n2WCxJGDpUm0fSUyZMg0AUO1TbvekVCvF3qjuchlPnapcRG1e3igAgM0pb/W4WLxPNmdwcZCXlz/A\nI6MjP78ALrcf1s74TvOtawzWWRg9ukCV+W+5ZTkIIbCePqLqoqjz3CkEPG4sXXqL4qV9gQiF/A9/\n+AP8fj9++tOf4sknn0QgEMBvf/tbVFdX41e/+pXSNmoWhmG6ihFIgASIrmCkZqhAwUjm1ltvAwC4\nLw5cSMNTZYfkE3HTTctU7zM+EJmZWUhPz0Ct3we/ghcKJVopXolfklDr9yEzI/ialGLKlOAiocMu\nf+9zpd+nDlvQ5ilTpioyfojQ4r+mXrl+DIIgICcnR1Fhqam3g2VZ1a6B6ekZmDdvATytTXA1VKti\ngySKsJ4uBsdxuOmmW2MyZ0RCbjab8eSTT2LTpk34+OOP8cQTT8BsNuNrX/taD5f7SGTUqK5UB0lE\nwGOF2WxR5XxIa8yaNRdJSUnw1jggDRAZ5qm2gRCCJUuWxsi66Jg/fxG8koRKX+xbNsrJJZ8XPknC\n/AXKppdOnDgJHMvBaqsb+MEaIhDwweZsQn5+ASyWBEXnmjRpCgCgWiEhj0VgoMcbQGOLC2PGjFM1\nq2n58jsAANZTxarM76j5/+3deXgUVbo/8G93ujvpdHf2ELKTDQKEQEIggbAYVtmEQURAg6Ajc0cF\nDIMDOqjcwQWHUQbhisvM48LvUa+Iet3vjKMjdxRFRUCWQCAhZCH73mttvz863XSAJN1JL1XJ+3ke\nHro7XVUnlap665w65z1lYNpaMGnSFAQHB3tlmz0Gctvws/T0dIwcOdL+z/aewD7OWe6vg8DoERsb\nN2ifjzuSy+XIy8uHwPBg6rqfrY4zsGAbzUhPHyWZ4Xq2Z17nPJhExRtKLNbnmZMmdZ9q2B38/QOQ\nPnIUDKZmmC2eS6zibi0d1RAEHmPHZnl8WzExcdBqtaio9kwGOW90DKyu6YAgCPabEl9JSUlDYmIS\n9JWlYA3O3xjJ/G7c0767z7vT1jnkbOZM79TGgV4C+fvvvw8AKC4uxtmzZ+3/bO8JMHRoTOcra/CO\njo7p/suDzNix2QAApq77McpMvfVn48Zle6VM7hAXF4/ooTGoZhnwEu2cxAsCqlgWMTGxXsk+mJlp\nDYatHdKpldua1TMzx3l8W3K5HElJKWjrsMBoYt2+fm90DKxpsN6weyvHek+mTSsABAFtJaedXkYR\nqIEyqGtrqjI4DIpA55NbsYYO6CtLkZiYhISEYU4v119ONa3bOpVs2bIFHR0d2Ldvn0ef3UnJkCHW\nZ4u2DG+efNYoNSkpaVAqlWAauh+GxnYGcttzVKlISR0ORhDQ7MHe657UxHFgBQGpqd6ZNnjYMOtw\nTIPJs5OPuJPB1AKZTOa1C3JCgvUxXX2j+5PzeKNjoK3c9seNPpSbOxlKpRLtpa5VOKNn3gJ05g5Q\nBochesYil5ZvLzsHCAKmTr3JpeX6y6lA/sc//hEGgwGnT5+Gn58fysvL8cgjj3i6bJIQGKhBQMDV\niQ7Cw30/Q5dYKBQKxMcngmtnIPA3rrmyrRYolSrJ5aS3BaZG1v21J29o5KzlHjYs2Svbs/19jWbx\nzhl9LaO5FUOGRHlt6tzISOt87bax2O7m6Y6BbR0W+Pn5ISws3CPrd0VgYCDS00fB0twApqPN6eX8\nQyOh0Gjhp9Fh2K13wz/Uteu5odKaECwra7xLy/WXU4H89OnT2LRpExQKBdRqNf70pz+huLjY02WT\nBJlMhtDQq80xjq9JZx8CXgB3g2QXgiCAa2cQExMjuWGMAQEBAABp1sevltv2e3haYKAGCoUCLCuN\nljxBEMByZo+OH7+WbVt6ozQTw+gNjD25jRhkZFinjzZUXXJ52b78DjzLwFhTibi4eK/393Hq6imT\nyWCxWOy/XHNzs2j+WGLgeLJ788SXgiFDrLUMXn99zZU3cQAv2GsiUmLLHc5Dos/IO8vtzRsohUIB\nXpDKrY91/zjO9uhpGo31WazJLM1WHpOF82gGPFfZciMYa6u8sj1zQy0EjvVoTobuOHUWr169GmvX\nrkV9fT2efPJJ3Hrrrbjrrrs8XTbJsJ2A174mVx81cIbraxm24C7FfgUKRWcgl2Yct5fbz8Ueuf2h\nUvmD56URpLjOcnojmYeNLU2u2SKVm52rBEGAxcJ5rYXHGdHRMfD3D4C5wTtTqpoaawEAw4aleGV7\njpw6i+fPnw+9Xo/m5mYEBwdj7dq1Xk+KL2ZqtcbhtThm3RELW5C+YY28M7hLM5B3TnQh0Rq5rdxK\npffO48DAQBgNzqft9SWOsz4CCHShx3J/2caq6w3SuNlxpDdayxwU5J1x086Qy+VITByG8yXnwDMW\nyD2cbMp2w2DrP+NNTp3FDz74IOrr65GSkoKqqqvNFEuWLPFYwaTEMfmB1J71elpUlLXZnGu//tko\n1y7dQG7LB98m0bkG2jpn2vJmoNJqdaitqQHHMfDz804Hsr4yM9bx7t5sKtbpdFAoFGj3UGc3T7KV\nWWy5IBITk3D+fDHMTfVQR3m2Q62poRYBAQH2x4ne5FQgLy0txeeff+7pskiWN5vfpEar1SE4OATt\nbdcnZmDbrCd/fLxn81h7QnJyKrQaLcqMBkwVBEn1GeEFAWWMBTqtDklJ3msGTE8fhQsXzqOlvRrh\nIb4fotST5rZKAJ5PzepIJpMhPj4B5eVlsDAcVErvPZ/vryt11hsfsZ3LttqxubHWo4GcZyxgWpuQ\nPGKkTypzTm0xISEB1dXSSeTgbfSYoWeJiUngjSx4h0QXgiCAa7b2ChZTc5yz/Pz8kD1+Agw8j1I3\npmpVdHND0N3nfVHKWGAUeGSPn+DVzlzjx08AANS3lPZ7XXLZjcvd3eeu4HkOjS2XoFL5Y/ToMf1e\nnyvS00eD5wVUeTDnuieUV1qHeNkmFRIL23TSpnrPPic3dz4f99VkMT1GoMLCQshkMjQ1NWHRokVI\nT0/vcuK/8cYbHi+gFCgU4m4m9LW0tOE4efJnMI1XE8PwBha8iUNaxggflqx/Zs+eh2+//T98bdAj\nSqGAVt7/IBIolyNY7odWh0QzIXI/BLrpLr+d53DYoIdSocSsWTe7ZZ3OSkgYhuTkVJSWXkBzWyVC\ng+L6vC6VUo0AVRBMlqtjhAP8g6BSqntYyjlVdb/AzOgxc+Zcr0/iM25cNj777COcOt+IpARp3ODq\nDQxKK9oQFxePiAhx5dEYOjQaGq3W4xOoGGqsLThpab6Z+bLHQL5+/XpvlUPSbD2YyY2lpVmDNVt/\nNZDbUrMOHy7dKV9jY+OwYkUh/t//exVf6NuxSBsMPzfUnOdqdXi3rQU8rEF8jpue07KCgC/07TAL\nPFavWmufJ8BbZDIZ1qz5NbZv/wPKqr6HTjMECr++B8oRw6bj5PmPIUBAgH8QRiRO73cZDaZmVNWf\nQkhIKJYuva3f63NVaupwxMTE4nxZNTr0DLQa8VcSThY3gOcFTJ8+w9dFuY5cLseI4SNx7NgPYNpb\noNR5Zniw8Yr1RmH4cN9UTHq8zZ84cWKP/4iVN4fwSFFycipUKhWYhqupJ5nOoJ6e7r1nkJ5QUDAL\n48dPxBWWxd/17eDckHs93E8BjVwOrUyGlcGhCHfD8cUJAv6ub0MNyyInJ9dnF924uAQsXLgYZkaP\nksuHIQh97ywYGBAKlTIQKkUgskYsQWBA/5IxMawJ5y59BUHgsXr13T4ZgSKTyTBr1s3geQE/nKz1\n+vZdZWE4/PRLHdRqtccn3+krW3O/vvKSR9bPMxaYaqsQH5/g8VnyukNdrN3Am88ZpUihUCAlJQ1c\nGwN0Bjq20QSNRiO51KzXkslkuPfe+zBy5GhcYiz4Qt/utolU3NWBjhcE/EPfjnKGwahRGbj33t/6\ntHPeLbcsxZgxY9HSXo3yK/2fatIdvwvPczhf/jVMlg4sXLgE48Z5N8Wmo/z8aQgNDcWJM/UwiDzL\n24mzDTCaWMyePQ+BgeIcemubvU5/+YJH1q+vugSB53x6zFAgdwPq7Na7lJQ0AIBfqD+UUWrwBhYp\nKWkDYrieSqXChg2bMXx4OkoZC/6p7xDNrGi8IOCf+naUMRaMGDES69f/zuvPfa8ll8vxm9+sR3R0\nDK40nEVtY4lPyyMIAsqqj6JNX4vx4ydiyZJlPi2PUqnEvHm3gGF5/Hiyzqdl6QnD8vjhRC38/f29\n3t/CFRERkYiPT4TxSgU4D0w9rC+33iB4O7+6I+lfRUWAauS9s/XmVIYFwD/WOgbbm9P8eZq/vz82\nbnwIqalpuMCY8ZXB98GcFwR8aejABcaCtLQR2LjxoS45D3wpMDAQGzc+BI1Gg7Lq79Ha4Z3sWzdS\n01iMuqYSxMcn4te//g9R3FxOm1aAoKAg/Hy6HmazODO9nTrXAL2BwYwZc6DVan1dnB6NHz8BAs+5\nvVbOsyz0ly8gPDzC3kPeF3x/xA4AYjjxxS462tqEzrUz9uQwUm9Wv5ZarUZR0RYkJ6fgvMWMw4YO\nCD4K5oIg4GtDB0osZqSkpOHBB38vqvSZgDUP//33F0EmA86Xfw2zRe/1MrR2XMGl6h8RFBSMjRs3\nw99fHPtIpVJh9uz5sDAcfjnn/rnD+0sQBBw7VQ+FQoE5c+b7uji9mjhxEoDOaUbdyFBVBp6xYMKE\nPJ8+rqII5AZSSgbiK+HhEQAA3siC60znaPtsIFGrA7Fp01YkJgzDWYsZx0zun1vaGT+ZjCi2mJGY\nmISioi1Qq/s/LMsT0tNHYdWqu8ByZlyo+He/Or+5imFNuFDxb8jlMjzwQJEopt90NG3aTVAqlfj5\ndL3Pbgi7U17VjqYWEyZOnITgYPEPkxs6NNravF51CZzZfedke6n1xmDixDy3rbMvKJATr/D394c6\nMBC8yTp+HABCQgbmlK+BgRpsfPAhhIWF46jJgPNmU+8LudF5swk/mAyICI/Agw/+XrSdkGwKCmYh\nO3sC2vS1qKo75ZVtCoKAi5XfwsIY8atfLUdq6nCvbNcVOl0QJkzIQ0ubGZUiSxDzS7G1laCgYJaP\nS+K83NxJEHgeHZfc0yeDZywwVFzEkCFRPm1WByiQEy/SaXUQLDyEzmd+QUG+GarhDSEhofaa8L+M\nejSw3pkIo55l8S+jHoHqQDxYtEUStSXr+PJ7ERISisq6kzCa23pfqJ+aWsvR3FaJ9PRRmDdvoce3\n11dTpljHxp8619jndfj53fgy393nvTGZWZRcakF0dAySk1P7XC5vszevlxa7ZX0dly+CZxnk5eX7\nvFWWAjnxGq1WB97MgbfwUCgUUKnE0fHKU2Jj43Dvvfd3juFuh8XDzcZmgbePZV/3mwck1QdBq9Xi\njjvugiDwKKv6zqNNySxnwaUrP0KhUOCuu+4RdR+X4cPTERERgXOlzbAwfev0pg1UIjS467kWFuIP\nbWDfks0UX2wGxwmYPHmazwOYKyIiIpGamgZjTQVYQ//7Y3R03hDYbhB8SbxHMBlwtFotIFjTs2o0\nWkldBPpq3LhszJu3CK08h6/1nu3MdVjfgTaew4IFi5GZOc6j2/KE7OwJyMzMQmtHDZrbPJdSs7r+\nNCyMAfPn34KoqGiPbccd5HI5Jk+eBoblcb60pc/rWTwnBfLO0y0sxB+3zO77ZDmnzjVCJpNh8uQp\nfV6Hr0yYMAkQBHRc6l+nN85sgqHqEuLi4kVxw0yBnHiNbepPwcxBo/He9Jm+tnTpciQnp+ACY0aZ\nB8axAkCZxYwLjAUpKWk+HwfdVzKZDMuXr4JMJkNF7XGP1MoZ1oiahrMICgrGvHmL3L5+T5gyZTpk\nMhmOn6nv8zoiw9TQalTQaZS45/YMRIb1rfNjbYMBV+r0GDNmrOimLHVGTk4uZDJZv3uv6y9fhMBz\n1hsDEaBATrzGce5rW1AfDPz8/LB27W+g8PPDYaMeZjfPYW7meRw26qFQKHD33eskndcgJiYWkyZN\ngcHUgqbWy25ff3X9GXA8i0WLfiWaMfW9iYiIxJgx43ClTo+a+v616vS3FeznU9YENQUFs/u1Hl8J\nDQ1FWtoImGqrwBr7vi87yq0d5nJyxJGqnAI58RrHWrjYe1K7W2xsHBYu+hUMPI8Tbhz+AgA/m40w\n8DwWLVpqH68vZQsW3AIAqG0679b18jyHuuYL0Gp1mDatwK3r9rTZs62Z044e913+9Q49gzMlTRgy\nJApjxoz1WTn6y5aBTV/Rt+l0eZaBofoSoqNjEB0d486i9RkFcuI1jmOZHWvng8XcuQsQFBSEk2YT\nTG6qlRt5HqfMJgQHh2DuXPEn5nBGdHQs0tJGoLXjCkyWdrett7mtAixrRn7+NCiV4p9VzNGoURlI\nSBiG82XNaG717nBGm59+qQXHC7j55oWi7iDYm6ysHADW5vG+MF65DIFlfZpb/VrS/WsQyQkIUN/w\n9WDh7++P+fMXgxEEnHLT2PJfzEYwgoAFCxZDpfJtDnV3mjzZOpNWS1uV29bZ3G5d16RJ+W5bp7fI\nZDLMn78IguCbWrnJzOL4mQYEBwcjP1+cs5w5a8iQKEQOiYKxpgJCH26oDdXWRz5iapWgQO4GYsu6\nJFaO6S/Fli7UW6ZNK4BSqcQFpv+d3gRBwAWLBSqVClOn9n8ubjGxzevcbuh7B69rtevroFYHIi4u\nwW3r9KacnFxERQ3FqfONaNdbvLrtn0/Xw8JwmDt3oc8n3XGHUSNHg7eYYWpwPce/obocSqXKPhGU\nGFAgd4PBMIzKHVSqq82ZUmvadJeAgABkZIxFM8ehietfkpgmnkMrz2HMmHGiyRHuLlFR0VCrA6E3\nNrllfRzHwGRpx7BhSZJtFpbL5Zg3bxF4XsCxU96bFY1leRw7VYfAwECfzWPvbrY5yo01lS4tx5kM\nsDQ3IC1tuKiuYdI8ookkKRQUyAHr2HIAqGL6N9e0bXnb+gYSuVyO0NBQMKx7HkHY1iO2fOqumjQp\nHzpdEE6caehzghhXnbnQBIORxfTpM0Wbs99VtpS8prpql5Yz1l3psrxYUCAnXuM4b7uf3+Cdw92W\n1rK+nzVy2/JSSpPpiqCgYLCcGbwbMuLZArlOJ+20wEqlCgUFs2C2cCi+2OyVbR4/XQ+ZTIaZM+d4\nZXveEBYWjrCwcJjqql16NGoL/IMqkJ84cQKFhYUAgKKiIhQWFqKwsBAzZsxAUVERAGDfvn1YtmwZ\nVqxYgZMnT3qyOMTHHMc3S7V50x2io2Pg7++Pun7mX69jWQQEBCAqaqibSiYutlwDHNf//gRs5zp0\nOl2/1+Vr06YVQCaT4UQ/EsQ4q6Zej9oGA8aNy5Z8a8a1UlPTwJkMYNqdz5hnqquCTCYT3c2zx6pF\nr7zyCj788EN7U8zu3bsBAK2trVi9ejUefvhhnD59GkePHsXBgwdx5coVrF+/HocOHfJUkYiPOQZy\nKSct6S+5XI6kpBQUF5+BReChkrl+U2MWeLTwHEYmpQ/YmyJb3gGWtUCp6F+Tri2QD4RERGFh4cjM\nHIcTJ35GfZOxz1nanPFLsXWylmnTBsazcUepqSNw9Oh3MNVWQRXU+0yMAs/BVF+D2Nh40eXB8NgV\nICEhAXv37r3u87179+LOO+/EkCFD8NNPP2HKlCmQyWSIiYkBx3FoanJP5xYiPo4BZzAHcgAYNiwZ\nAPpcK6/vXC4pqe85s8XONs2tmen/FJ5mizWLV3BwSL/XJQb5+dMA9G9WtN6wHI/ii00IDg5GRkam\nx7bjK6mp1l7nxlrnhjiaGmohcKx9OTHxWI187ty5qKzs2iOwsbERR44cwcMPPwwA6OjoQEjI1RNL\no9Ggvb0dYWE95/ANDQ2EQiGeQJCTMxZ//asMy5YtQ2Sk9JvuPKWt7erzydBQ7aDeVxMmZOHzzz9G\nJcMgrg/DeSo6O7pNmJA1YPdjRkY6PvwQ0BubEaLrX8Y6vclaQcjKGo3wcOnvr1mzpuONN/6KsyVN\nmJ4bC7nc/SNnLpa3wmTmcPO8AgwdOjBugByFhWVAo9HAUF0OQRB6HX1k7Bw/npubI7pzzqs9jj7/\n/HMsXLjQXhvTarXQO8wIpdfrnXqG1dxs8FgZ+0Kp1GHPnheh0WhRX+++TFQDTXv71bGvBgMzqPdV\nTEwylEolLjEW5MH1LHeXGOv48ZiYpAG7H0NCogBYx3/3hyDw6NDXQ6fTgeOUA2Z/TZw4GV9++Q+U\nVbQiJdH9gdZW28/OnjRg9tm10tNH4aeffgDT3tJr87qhuhwymQyxsck+2R893Tx49eHakSNHMG3a\nNPv77Oxs/Pvf/wbP86iurgbP873WxsVKq9XRePJeOLaiOPZgH4z8/f2RkZGJZt718eSNLIsWnkNG\nxtgBkZyjOxERkYiLS0BLRzVYtu8d3tr0dbCwRmRl5Qyoc3Tq1JsAACeLG9y+7vYOC8oqWpGUlIy4\nuHi3r18sRo+2PjIwVJb1+D3OYoaprgoJCcOg1YqrNg54OZCXlZUhPv7qQZGRkYGcnBzcfvvtWL9+\nPR577DFvFod4mWPQcRxTPlhNmmSdz7nY7FqQKraYuiw/kOXmToYg8GhsLe/zOhpaSu3rGkgSE5OQ\nmDgMF8vb3J7p7WRxAwQBmD59plvXKzaZmeMAAB295F03VJZB4Hn7hCti49FAHhcXh3feecf+/pNP\nPkFQUNdxnOvXr8fBgwdx6NAh5OTkeLI4xMcca+FK5eCukQPA2LHZ0Gg0OM+YwTk5lpUTBJy3WKDV\najF2bJaHS+h7O0QSCwAAIABJREFUkyblQy6Xo6axuE+pkBnWjIaWMoSHR2LEiJEeKKFv3XTTLAiC\ngBNn3Fcr5zgBJ842ICBAjYkTxTHftqeEhYUjMTEJxpoKcJbub6htE6yINfnSwBy3QkTJMZBTjdya\n3W7SpCkw8jwuM87VqMoZC0wCj0mTpg6KxxNhYeHIyZkIg6kFbXrXJwupayoBz3OYNWvOgByml5c3\nGYGBgTh5tgEs554Z9UrKmqE3MJgyZfqgmBMhK2s8wPPdNq8LPAd9ZSnCwsIRH5/o5dI5Z+Ad2US0\nHIP3YAhCzpgyxTrZSXEPtQFHtmZ123KDwaxZ1rm4rzScdWk5QeBR03gOKpW//XnyQOPvH4Bp0wqg\nNzJuy/T24y91nZncZrtlfWJnm460o/zCDX9urKkEbzEjK2u8aPtYUCAnXkMpWq+XkDAM8fGJuMxY\nep2j3FpzZzqXkeYMXn2RkpKGpKRkNLdVuDQ/eVNrBSyMHlOmTENgoOsjA6Rixow5kMlk+PFkbb9n\nYqyq6cCVOj3Gjs1CVFS0m0oobvHxCQgPj4ChquyG05rqK6x9LMQ0//i1KJATr3Fs2qQa+VV5eZPB\nAyjtpXm9lDFD6Pz+YCKTyey18trG804vV9NYDAADKkf4jURERCInJxf1jUZcrurfsKgfT1ofX8yZ\nM98dRZMEmUyGMWPGWqc1rb9y3c8NVWVQqVQYPjzdB6VzDgVy4hODPbObowkT8gAAF3tpXr9gsXT5\n/mCSkzMRgYEa1DdfdGoSFaO5DW36WowYMRLR0f1LJiMFc+daA+8PJ13vR2DT3GpGyaUWJCYOG5Ad\nA3tiH4ZWdanL50xHGywtTUhPHy3qGRspkBOfoEB+VUREJJKSklHFMt02rxt5HldYBsnJKQgPj/By\nCX1PqVRh8uQpYFgTWtp6n0O6vtnay3jatAJPF00UkpNTkZY2AmUVbahvMvZpHT/9UgtBAObOXSDa\nZ8GeMnLkKMhkMhhrKrp8bpuvfNSo0b4oltMokBOfGIg9iPsjO3siBFgztt1IOWOBAGD8+IleLZeY\n5OdbO/jVt/ScvEMQBDQ0lyIgIADZ2RO8UTRRuPnmhQCAH0+4Xis3mlicOtfYOUog191FE73AQA1i\nYmJhaqgFHLoZiHXa0mvR1ZT4BNXIu8rOtuZQ6C6Ql3V+bvveYJSQkIiYmFi0tFWC5brvT9BuqIOZ\n0WP8+Inw9/f3Ygl9a+zYLAwdGo0zF5rQoWdcWvb4mXowLI85c+YN2v4rKSlpEFgGAs/ZPzPVX4FC\noURCwjDfFcwJFMiJT1Ag7yo6OgZRUUNRyTJgr+l5zAgCKlmm8zuDoyfxjchkMuTl5YMXODS1Xu72\new0tlwAAeXn5XiqZOMjlcsyZMx88L+DYKefz07Mcj59P1SMgQD1gh+k5wzYjoS2QCzwPS3MDYmPj\nRH9zQ4Gc+AQ1rV9v3LjxYAQB1WzX2lR1Z3AX8/AXb7FlGusuZasg8GhqLYdOp0N6+ihvFk0UJk+e\nCq1Gi5PFDWAY5xLEFF9sht7IYPr0GVCrxTXPtjfFxsYBgH0IGtPWDIHnJJFrnq6mxCeoRn69MWPG\nAgAqrmlet723/XwwGzIkComJSWjtqL5h83qbvg4Ma8L48RMH5TGmUqkw/aaZMJpYnLnQ+1zlgiDg\nmD0BzMAeptcbWyBHZyC3tFinvo2JEf+oBwrkxCdkMjr0rpWWNhxKpdI+17hNJcPAX+WPlJQ0H5VM\nXLKzcyAIAlraqq77WXNbhf07g9WMGbMhl8udyr9eU29AbYMB48aNR0REpBdKJ16BgRpoNNqrNfL2\nFgDAkCFDfVksp9DVlPjEYKwt9UapVCEtbQSaeQ62x+RGnkczzyG1M8gT2GegamqruO5nTW0VCAgI\nwIgRg69Z3SY0NAxjx2ahtsGAmnp9j989edYa7AsKBvYsZ86KiIgEOvMUMB2tAIDISPHf4FAgJz5B\nz8hvzFbr5jrHwNSy1rnKxT78xZtiY+MREhKKNn2N40ghmCwdMFs6MHKkuJN3eIOt09qZkqZuv8Oy\nPIpLmxEWFoZRo8Z4qWTiFhHRmaNBEMB2WLPkSSFvA11NiU9QIL+xlJRUAADXGaHqOKbL58Taez09\nfRQY1gTBIctbW0cNACA9XdzJO7whI2MsNBoNii82g+dvnH+99HIrLBYOubn5dD52Cg4OAWDt8MYa\nO6BQKCWRp5/+esQnBlvmKGfZpknkO+uaTRzX5XNiZct7LQhXx/y2G+oBACNGiDcntrcoFApkZ0+A\n3sDgSt2Nm9dLLlmfAU+YMPgSwHQnODjU+kIQwBn0CAkJkcS1igI58QkpnBy+EBISisBADWzhqZFj\nodVqERQU7NNyiU1SknXMr2Pedb2xEQqFAjExcb4qlqiMG5cNwFrzvpYgCCiraENISCgSE5O8XTTR\nCg62nmeCIIAzGSVz3lEgJ0REZDIZYmJiIQAQBKCd5xETE0c3PteIjY2HXO5nb1oXBB4GUwvi4hJE\nn7zDW0aOzIBcLkf5DWZEq2s0wmhikZGRSceWA41Ga30h8BB4Dlqt1rcFchIFckJEZuhQa/Y2FgIE\nh/fkKoVCgSFDhkAQrA8hzBY9BIFHdHSMr4smGgEBAUhKSkFNvQEWhuvys4pqa3AfjElzemIL3LYh\naPbALnIUyIlXDRuWTB1rehEVZR23ynWOQbO9J10NHWoL2gKM5rZrPiMAkJY2AoIgoKbe0OXz6lq9\n/efkKq1WB+BqILe9FztqgyJetWnTVphMfZtmcbCIjIzq8T2xiowcAgAI0kTBbGnv8hmxSk62jna4\ntsNbTb0eOp1u0CeBuZath7pMJoMAQKMRf491gGrkxMu0Wi1dPHphS0DBXPOedGUb3xsWlAAzYw1U\n9nHABAAwbJi1I1tdw9UaudHEorXdgsTEZHo+fg1b4BY4a/4GKQw9AyiQEyI6YWER17wP91FJxM22\nX8yM3h7IaV91FR4eAbVajVqHQF7faG0RS0igIY3XUqlUUCiuJhOiGjkhpE90Oh0UftanXkqlUjLP\n6bwtNNQ65pdhjWAYI2QymWSGC3mLTCZDfHwiWtrM9ix49U3WQB4Xl+C7golYoObqDHBSmQ2OAjkh\nIiOXyxEcYs0wFRISSs2f3bBl4bIwBlgYA7RaHQ09u4GYmFgIAuwZ3ho6A7l9ti/SRaBD8A4MpEBO\nCOkjnS6oy//kerbkHQxrAsOZ7O9JV7YEObZA3thigkwmw9ChNBriRtQUyAkh7mCrWapUKh+XRLyU\nShUCAtQwW/TgOIZuerphG1tvC+TNLSZERg6BUknH1o04Bm9qWieEEA/T6XQwWdo6X1MgvxFbHgKe\nFyAIAgwmlnIT9CAgIOCGr8WMAjkhIkTPxZ3j2BFQp6NOgTcSFhYOPz8/cLwA20RoQ4ZQboLuBASo\nb/hazCiQEyJiFNB75phCUyrpNL1NLpcjIiISAi/Ym9cpl0P3/P397a/9/Px8WBLnUSAnhEiW4zhf\nqSTv8IXw8AgIAEKDrUGKAnn3VCr/3r8kMhTICRExQRB6/9Ig5tgxSSo9jH3BlignwN+vy3tyPSl2\nMKVAToiIUdN6zyiQOyc0NAwAcKXO0OU9uZ4Ue/NTICdExKhG3jPH4UFSGSrkCyGdCYaMJpYy4PVC\nqZReUiEK5ISIENXEnSPFHsa+4Bi4tVodTSXcAz8/CuSEEOI1jj2MAwKk10nJWxzH2AcF0Xj7nkil\np7ojCuSEiBA1qTvHMZBLsbext9AwPedJsbVCeiUmZBChJvaeOXZMkmInJW9xHJpHnQJ7RjVyQohb\nUc28Z0ql8oavSVdqtdrhNQXynkjx5pkCOSFEshynLaUpTLvn+AjC8TW5HgVyQohbSPFi4guOPYyl\n2CTqLY7HE/UlGHg8GshPnDiBwsJCAEBjYyN++9vf4o477sCKFStw+fJlAMA777yDpUuXYvny5fjq\nq688WRxCyADj53f1EibFTkq+IMVx0qRnHvuLvvLKK/jwww/tz2Z27dqFRYsWYf78+fjuu+9QWloK\ntVqNAwcO4NChQzCbzVi1ahXy8/MlmSKPEHeiZ+POkcupFu4qhYL6Egw0HruFTUhIwN69e+3vjx07\nhtraWqxZswYfffQRJk6ciJMnTyIrKwsqlQo6nQ4JCQkoLi72VJEIIQMMNae7jm5+Bh6PBfK5c+d2\n6XxSVVWFoKAgvPbaa4iOjsYrr7yCjo6OLnMIazQadHR0eKpIhJABRi6nvgSuUigokA80XntYEhIS\nghkzZgAAZsyYgd27dyMjIwN6vd7+Hb1e3yWwdyc0NJAORjKgqVTWU1Op9ENkZO/nxGDFMFezlNF+\nco5Op6Z91QOdLsD+Wir7yWuBfPz48fj666+xZMkS/PDDD0hNTUVmZib+8pe/wGw2w2Kx4OLFixg+\nfHiv62puNnihxIT4jsXCAgAYhkN9fbuPSyNeLS1G+2vaT84xGBjaVz1obzfZX4tpP/V0U+G1QL5l\nyxZs27YNb7/9NrRaLZ599lkEBwejsLAQq1atgiAIKCoqojGOhDigYWg9o57qrqNjauDxaCCPi4vD\nO++8AwCIjY3Fq6++et13li9fjuXLl3uyGIRIFvVe7xkFctfRPht46C9KiIhR7alnFJRcRx0EBx46\nCwgRMaqR94xudFwnk9Flf6ChvyghIkaBqme0f1xHrRgDD/1FCSGSRYHcdZREZ+ChQE6IiFHTes8o\nkLuOauQDD/1FCRExClQ9o/3jOgrkAw/9RQkRMaqR94YCOXEvKZ5zFMgJETGqcfaMdo/r6JgaeCiQ\nE0Iki4ZSuU6KNU7SMzoLCBExuuj2jCqXrqMa+cBDgZwQEaKLrbNoP7mKbg4HHgrkhIhQbu4kAMDE\niZN8XBJxoxse19E+65kU94/XZj8jhDhv+vSZSExMwrBhyb4uiqhJ8Jrrc1QjH3gokBMiQnK5HMnJ\nqb4uhgRQJHeVFGucpGfUtE4IkSwKSq6jGvnAQ4GcEEIGEbr5GXgokBNCyCBCNfKBhwI5IUSyqHbp\nOtpnAw8FckKIZFFQct6aNfciPDwCo0aN8XVRiJtRr3VCCBkEpk0rwLRpBb4uBvEAqpETQiSLauSE\nUCAnhEgYBXJCKJATQgghdlLs1U+BnBBCCJEwCuSEEEKIhFEgJ4QQQjpJsd8FBXJCiOT5+fn5ugiE\n+AyNIyeESNp//McGhIWF+boYhPgMBXJCiKRNnJjn6yIQ4lPUtE4IIYRIGAVyQgghRMIokBNCCCES\nRoGcEEIIkTAK5IQQQkgnnU4HAEhIGObbgriAeq0TQgghnUaNGoNly1YgKyvH10VxmkyQYIb4+vp2\nXxeBEEII8ZrISF23P6OmdUIIIUTCKJATQgghEkaBnBBCCJEwCuSEEEKIhFEgJ4QQQiSMAjkhhBAi\nYR4N5CdOnEBhYSEA4PTp05g6dSoKCwtRWFiITz/9FACwb98+LFu2DCtWrMDJkyc9WRxCCCFkwPFY\nQphXXnkFH374IdRqNQDgzJkzWLt2Le6++277d06fPo2jR4/i4MGDuHLlCtavX49Dhw55qkiEEELI\ngOOxGnlCQgL27t1rf3/q1Cn861//wh133IFHHnkEHR0d+OmnnzBlyhTIZDLExMSA4zg0NTV5qkiE\nEELIgOOxGvncuXNRWVlpf5+ZmYnbbrsNGRkZ2L9/P/7rv/4LOp0OISEh9u9oNBq0t7cjLCysx3WH\nhgZCofDzVNEJIYQQyfBarvXZs2cjKCjI/nrHjh2YOXMm9Hq9/Tt6vd6esL4nzc0Gj5WTEEIIEZue\nUrR6LZDfc889ePTRR5GZmYkjR45g9OjRyM7Oxq5du3DPPfegpqYGPM/3WhsHev6FCCGEkMHEa4F8\n+/bt2LFjB5RKJSIiIrBjxw5otVrk5OTg9ttvB8/zeOyxx7xVHEIIIWRAkOTsZ4QQQgixooQwhBBC\niIRRICeEEEIkjAI5IYQQImEUyAkhhBAJo0DeBxUVFdiwYQOWL1+O1atXY926dSgpKcHevXvx1ltv\n2b/39NNP47777oPFYvFhaZ1XUlKCdevWobCwELfeeiuef/55uNoX8r//+7/BMEyftp+fn9+n5Wxm\nzJgBs9ncr3X0pKKiAuvXr0dhYSFWrFiB7du3o6Ojo9vv/+Mf/0BtbW23P3/ggQeu++ytt97qkhGx\nJ99//z2Kioqc+u6NVFZWYvny5X1e3hW+PrZ68/LLL18314PZbMaMGTM8sr1rie3YckZRUdF117bD\nhw9j69atbttGX1RWViI7O9s+r0dhYSH27dvn9XIUFRXh+++/987GBOISg8EgLFiwQDh27Jj9sxMn\nTgh33nmn8PzzzwtvvvmmwPO88Mc//lH43e9+JzAM48PSOq+1tVVYuHChUFZWJgiCILAsK9x///3C\nm2++6dJ6CgoKBJPJ1KcyTJ48uU/LuWPbvTEajcLChQuF48eP2z977733hHXr1nW7zJ133ilcuHDB\npe28+eabwvPPP+/Ud7/77jvhwQcfdGn9jioqKoTbbrutz8s7SwzHVl+YTCahoKDA49sR47HVV19/\n/bWwZcsWj26jN946rnvz4IMPCt99951XtuW1ceQDxVdffYW8vDxkZWXZP8vMzMQbb7yBffv2QRAE\nPP7442BZFn/6058gl0uj0eOf//wncnNzMWzYMACAn58fnnnmGSiVSjz77LP44YcfIAgC1qxZg3nz\n5qGwsBDp6ekoKSlBR0cH9uzZg2+//Rb19fUoKirCCy+80O1yoaGhaGtrw9/+9jf4+V1NtWuxWFBU\nVIQrV65gxIgR2L59O2pra7F9+3aYzWa0tLTg/vvvx6xZs/DVV1/Z77JHjRqF//zP/7Sv56233sI3\n33yD5557DiqVyi3751//+hcmTJiAsWPH2j/71a9+hbfeegu///3vsXDhQkybNg2HDx/Gp59+iptv\nvhlnz57Fli1b8Nprr2Hz5s3o6OiAyWTCQw89hNzcXOTn5+Obb77Bjz/+iKeeegrBwcGQy+UYN24c\nAODAgQP4+OOPIZPJMH/+fKxevfq6cpWXl+Oee+5Bc3MzVq5cidtuuw1Hjx617xuTyYRnnnkGSUlJ\neOGFF/DFF1+A4zisXLkSU6ZMAQBwHIetW7ciLS0N69atc8v+ciSGY2v27NnIyspCeXk58vLy0N7e\njpMnTyIpKQm7du3C1q1bMX/+fIwfPx6bN29GW1sbEhIS3L4vbkSMx9b333+Pl19+GUqlEjU1NVix\nYgW+++47FBcXY/Xq1Vi1ahVmzJiBzz77DJWVlXjkkUegVquhVqsRHBzslf3mqp07d+Knn34CACxc\nuBB33XUXtm7dipaWFrS0tCA0NBT33XcfxowZg7lz52Lz5s2YPXs27r77bjz99NP4xz/+gb///e9g\nWRY6nQ579+7Fxx9/jEOHDoHneWzYsAGlpaU4ePAgIiMj0djY6LXfjQK5iyorK7uc4L/97W/R0dGB\nuro65OTk4N1330VSUhL8/Pwgk8l8WFLX1NXVIT4+vstnGo0GX3/9NSorK/H222/DbDZj+fLl9ibw\nzMxM/OEPf8Du3bvxySefYN26ddi/fz92797d43KLFi3C7NmzryuDyWTC5s2bERsbi40bN+LLL7+E\nWq3G2rVrkZubi2PHjmHv3r246aabsGPHDhw8eBDh4eHYt28fampqAFgvUGfPnsWePXu6XMj7q6Ki\n4oYX9ri4OPz4449YuHBhl89vuukmjBw5Etu3b8eVK1fQ0NCA1157DY2Njbh06VKX7z799NN49tln\nkZSUhMcffxwAcOHCBXz66ad48803IZPJsGbNGkyZMgXJycldlmUYBvv37wfP81i8eDFmzpyJkpIS\n7Nq1C1FRUXjxxRfx+eefY/r06Th8+DAOHjwIi8WCZ599Fvn5+WBZFps3b0ZOTg7uuOMOt+0vR2I4\ntqqqqvD6668jMjISEydOxMGDB/Hoo49i5syZaGtrs3/v/fffx/Dhw1FUVIQTJ054pWlUrMdWTU0N\nPvjgA5w+fRobN260N+c/8MADWLVqlf17e/bswYYNG5Cfn4+XX34ZpaWlbtozfXfhwgX7FNoAsHTp\nUlRWVuKdd94By7JYtWoV8vLyAAB5eXlYs2YNPvjgAxw+fBghISHw9/fHN998g7y8PJjNZkRGRqKl\npQWvvfYa5HI57rnnHvzyyy8AgKCgIOzfvx/t7e3Yvn07PvroI8hkMixdutRrvy8FchcNHToUp06d\nsr/fv38/AGD58uXgOA4zZ87EY489hg0bNmD//v247777fFVUl8TExODMmTNdPquoqMAvv/yC06dP\n208KlmVRXV0NwFoTBqz7pKGhocuy58+f73a5pKQkAMDu3btx7NgxAMBrr72GmJgYxMbGAgCysrJQ\nVlaG6dOnY//+/Xj33Xchk8nAsiyam5sRFBSE8PBwAF2fBx45cgR+fn5uDeIAEBUVdd0zVAC4dOkS\ncnJy7O+FGzz3TUtLwx133IFNmzaBZdkuFxgAqK2tte+T7OxsXL58GefPn0d1dTXWrFkDAGhtbcXl\ny5fxzDPPwGAwYPjw4ZgzZw7GjRtnb3VISUlBZWUloqKi8OSTTyIwMBC1tbXIzs5GWVkZMjMz4efn\nB7VajW3btqGyshLnzp2DVquFweC5+QvEcGyFhIQgJiYGABAYGIjU1FQAgE6n69KvoqSkBFOnTgUA\njB07FgqF5y+RYj220tLSoFQqodPpkJCQAJVKheDg4Ov6oZSUlCAzM9O+DTEE8tTUVBw4cMD+/q9/\n/StycnIgk8mgVCoxduxYXLx4EcDVY6agoAD33XcfQkNDce+99+LVV1/F4cOHUVBQALlcDqVSiU2b\nNiEwMBA1NTVgWbbL8qWlpUhNTbWfj7Z94g3SaPcVkZkzZ+LIkSM4fvy4/bPy8nLU1NRAJpMhLS0N\nALBjxw68++673uvs0E8FBQX4v//7P1y+fBmAtaa3c+dOBAUFITc3FwcOHMDrr7+OefPmIS4urtv1\nyGQy8DyP5OTkbpeztVQUFRXhwIEDOHDgAPz8/FBTU4O6ujoAwLFjx5CWloY9e/Zg8eLF2LVrF3Jz\ncyEIAsLDw9HW1oaWlhYAwBNPPGG/EL7wwgsICgrq0unQHWbOnIlvv/22ywX34MGDCAsLQ0BAAOrr\n6wGgS8CSyWQQBAHnzp2DXq/Hyy+/jJ07d2LHjh1d1h0ZGWm/qNju8pOTk5Gamoo33ngDBw4cwNKl\nSzF8+HC89NJLOHDgAB599FH79liWhcFgwMWLF5GQkIBt27bhqaeews6dOzFkyBAIgoDk5GScOXMG\nPM+DYRisXbsWFosFo0ePxssvv4wPP/wQxcXFbt1nNmI4tpxtHUtOTraf27Z962liPbZc2Wc///wz\nAHSp5IhJSkqKvVmdYRj8/PPPSExMBHD19wwODkZAQAA+++wzTJ06FTExMXj99dcxZ84cFBcX44sv\nvsBf/vIXPProo+B53n5jZXt8Gh8fjwsXLsBkMoHjOJw9e9Zrvx/VyF2k0Wiwf/9+PPvss/jzn/8M\nlmWhUCiwY8eOLidicHAwnnnmGfzud7/De++9h4iICB+WundarRY7d+7Etm3bIAgC9Ho9CgoKUFhY\niJ07d2LVqlUwGAyYNWsWtFptt+vJycnBunXr8MYbb+Do0aNOLwcAISEheOKJJ1BbW4usrCxMnz4d\n7e3tePLJJ/HSSy8hOjoazc3NkMvlePzxx/Gb3/wGcrkco0aNwpgxY+zr2bZtG2677TZMmjTJ/ly2\nvzQaDV588UU89dRTaGlpAcdxGDFiBJ577jmUl5fjkUcewUcffdRle1lZWfj973+P/fv34+jRo/jg\ngw+gVCqxYcOGLuvetWsXtmzZAo1GA41Gg+DgYKSnp2PSpElYuXIlLBYLMjMzERUVdV25/P39ce+9\n96KtrQ3r169HSEgIFi9ejOXLlyMoKAgRERGoq6vDyJEjMXXqVKxcuRI8z2PlypX2mkNAQAC2b9+O\nLVu24ODBg27rV2AjhmPLWXfccQcefvhhrFy5EsnJyVAqlW5Zb0/Eemw56/HHH0dRURH+9re/ISws\nDP7+/n1el6cUFBTg6NGjuP3228EwDG6++WaMHj36uu/NnDkT7733HkJCQjBlyhS8+eabSEhIgNFo\nhFqtxtKlS6FSqRAZGWmvdNiEhYVh48aNWLFiBcLCwqBWq73161GudUIIIUTKqGmdEEIIkTAK5IQQ\nQoiEUSAnhBBCJIwCOSGEECJhFMgJIYQQCaNATsgAV1lZiYyMDCxevBhLlizBggULsHbtWns2PGf9\n85//xJ49ewAAzz//PH788UcAwB/+8Af7GGVCiPfR8DNCBrjKykqsXr0aX375pf2znTt3oq6uDs89\n91yf1llYWIgHHngAubm57iomIaSPqEZOyCCUm5uLkpISHD9+HLfddhtuueUW3HXXXSgvLwcAvPrq\nq7jllluwZMkSPPbYYwCA9957D1u3bsUHH3yAU6dOYdu2bTh37hwKCwvtGQxffPFFzJ8/H4sWLcLO\nnTvBcRwqKyuxZMkSPPTQQ/bJKmxZ+Qgh/UeBnJBBhmEY/O///i8yMjKwadMmPProo/jwww+xYsUK\nbNq0CRzH4aWXXsKhQ4fw3nvvgWGYLnNfL1myBBkZGXjiiScwYsQI++dff/01vvzySxw6dAjvv/8+\nysvL8fbbbwMAiouLsXbtWnz88ccICgrCRx995PXfm5CBigI5IYNAXV0dFi9ejMWLF+OWW26BIAhY\nunQpgoKC7JM7zJs3D5cvX4bBYEBWVhaWLVuGffv2Ye3atU6l8Pzuu++wYMECqNVqKBQK3HrrrThy\n5AgAIDw83D4RSlpaGlpbWz33yxIyyFCudUIGgSFDhuB//ud/unx2o0lSBEEAx3F44YUXcPz4cRw+\nfBi//vWv8ec//7nXbfA8f91ntklHHPNv2yb8IIS4B9XICRmkkpOT0dLSYp/s59NPP0VMTAx4nsf8\n+fMxfPgHQ7puAAAA1klEQVRwbNy4Efn5+Th37lyXZf38/MBxXJfP8vLy8Mknn8BkMoFlWRw6dMg+\n5zMhxHOoRk7IIKVSqbB7927s2LEDRqMRwcHB2L17N8LCwnD77bdj2bJlUKvVSEpKwq233orPP//c\nvuzUqVPx+OOP45lnnrF/VlBQgLNnz+LWW28Fy7KYMmUK7rzzTpeHuRFCXEPDzwghhBAJo6Z1Qggh\nRMIokBNCCCESRoGcEEIIkTAK5IQQQoiEUSAnhBBCJIwCOSGEECJhFMgJIYQQCaNATgghhEjY/wcC\nh3l8fkGFrgAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x29e62fb1d30>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.violinplot(x='Position', y='height_cm', data=fifa, order=pos_order)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Yes, it is clear that the forwards are the most spread out in terms of height. For numerical data, we can turn to the standard deviation."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Position\n",
       "Center-back     4.766720\n",
       "Center-mid      5.793662\n",
       "Forward         6.515699\n",
       "GK              4.604998\n",
       "Outside-back    5.088083\n",
       "Outside-mid     5.319471\n",
       "Name: height_cm, dtype: float64"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fifa.groupby('Position')['height_cm'].std()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's calculate the linear correlation between height and weight per position."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th>height_cm</th>\n",
       "      <th>weight_kg</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Position</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th rowspan=\"2\" valign=\"top\">Center-back</th>\n",
       "      <th>height_cm</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.625164</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>weight_kg</th>\n",
       "      <td>0.625164</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"2\" valign=\"top\">Center-mid</th>\n",
       "      <th>height_cm</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.700717</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>weight_kg</th>\n",
       "      <td>0.700717</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"2\" valign=\"top\">Forward</th>\n",
       "      <th>height_cm</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.731472</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>weight_kg</th>\n",
       "      <td>0.731472</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"2\" valign=\"top\">GK</th>\n",
       "      <th>height_cm</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.587178</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>weight_kg</th>\n",
       "      <td>0.587178</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"2\" valign=\"top\">Outside-back</th>\n",
       "      <th>height_cm</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.633062</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>weight_kg</th>\n",
       "      <td>0.633062</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"2\" valign=\"top\">Outside-mid</th>\n",
       "      <th>height_cm</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.665286</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>weight_kg</th>\n",
       "      <td>0.665286</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                        height_cm  weight_kg\n",
       "Position                                    \n",
       "Center-back  height_cm   1.000000   0.625164\n",
       "             weight_kg   0.625164   1.000000\n",
       "Center-mid   height_cm   1.000000   0.700717\n",
       "             weight_kg   0.700717   1.000000\n",
       "Forward      height_cm   1.000000   0.731472\n",
       "             weight_kg   0.731472   1.000000\n",
       "GK           height_cm   1.000000   0.587178\n",
       "             weight_kg   0.587178   1.000000\n",
       "Outside-back height_cm   1.000000   0.633062\n",
       "             weight_kg   0.633062   1.000000\n",
       "Outside-mid  height_cm   1.000000   0.665286\n",
       "             weight_kg   0.665286   1.000000"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fifa.groupby('Position')[['height_cm', 'weight_kg']].corr()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The position with the lowest correlation between height and weight is goalkeeper. Since goalkeepers aren't required to run miles on end during the game, they can come in a variety of shapes and sizes. While some goalkeepers are extremely tall and lanky, others are short and stout (with unusually long arms)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Top 5 Leagues <a name=\"leagues\"></a>\n",
    "\n",
    "It is widely acknowledged that the top 5 leagues in the world are the\n",
    "* Spanish Primera División\n",
    "* English Premier League\n",
    "* Italian Serie A\n",
    "* German Bundesliga\n",
    "* French Ligue 1.\n",
    "\n",
    "While the exact order is up for debate, I will keep them in this order, as per the [current UEFA coefficients](https://www.uefa.com/memberassociations/uefarankings/country/).\n",
    " To begin with, let's take a look at the average overall score per player per league."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "league\n",
       "English Premier League      72.409786\n",
       "French Ligue 1              70.453177\n",
       "German Bundesliga           72.428305\n",
       "Italian Serie A             72.588551\n",
       "Spanish Primera División    73.686047\n",
       "Name: overall, dtype: float64"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "leagues=['Spanish Primera División', 'English Premier League', 'Italian Serie A', 'German Bundesliga', 'French Ligue 1']\n",
    "fifa_sub = fifa.loc[fifa.league.isin(leagues)]\n",
    "fifa_sub.groupby('league')['overall'].mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It seems that the Spanish league has the highest average quality of players and that the French league is far behind the other 4. Let's look at a strip plot, conditioned on position, to get a better sense of things."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.legend.Legend at 0x29e646b2b70>"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x29e644e7668>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "_ = sns.stripplot(x='league', y='overall', hue='Position', data=fifa_sub, dodge=0.6, jitter=True, alpha=.5, order=leagues, hue_order=pos_order)\n",
    "loc, labels = plt.xticks()\n",
    "_.set_xticklabels(labels, rotation=45)\n",
    "plt.legend(bbox_to_anchor=(1.04,1), loc=\"upper left\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It's tough to glean insight from this plot due to the sheer number of points. A boxplot will be more useful."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.legend.Legend at 0x29e646b65c0>"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\nDJMmTeKDDz7AZDLRs2dPQ469MkrGREREpMacf5vy9ddfp127dphMJgICArjyyiv55ZdfAGjcuDEA\nXbt25dFHHyU6OpqHH36YRYsWsWHDBrp27YrZbCYgIICRI0cSGhrK0aNHKSkpKff6AwcO0LRpUwID\nAwFsk5S7CyVjIj6msqpVVaw6jyqDRezXpEkT3n33XQYNGkRxcTHbt2/n7rvvBsBkMgEQFRVFcHAw\nH3/8MbNnz+bf//43b775Ji+99BJ79+5l/fr1rFy5kvz8fHr27InVagXAbDYD0KBBA37++WcKCgoI\nCAhgz5493HnnncYccAWUjIn4MFWtup7OsUjVunbtypYtW/j73/9OcXExt956a7lqyzLdunXj3Xff\npVatWiQmJvLOO+/QsGFD8vPzCQkJoWfPngQGBhIbG8vx48fLvTYmJoYRI0bQp08fYmJiCAkJqanD\ns4uSMREfo6pV19M5Fk8REx1tVwWkI9urSv369VmxYsUFy8eOHXvBsmnTppX7u1+/fvTr1w+APn36\n0KdPHwBCQkJYvHjxRWO7/fbbuf322y+6nhGUjImIiPioqsYEk5pjNjoAEREREV+mZExERETEQLpN\nKSIiHkcVq+JN1DImIiIeraio0Fa1KuKJ1DImIiIeRxWr4k1clowVFxczbtw4fvvtN8xmM5MnT8bf\n359x48ZhMplo1qwZEydOtA3IJiIiIuKLXJaMff3115SUlLBs2TI2btzIK6+8QnFxMY8//jgJCQk8\n88wzfP7559x0002uCkFERETE7bmsWapx48aUlpZisVjIycnB39+fXbt20b59ewA6d+7Mt99+66rd\ni4iIiHgEl7WMhYaG8ttvv3HbbbeRmZnJvHnz2Lp1q22eqbCwMM6cOVPlNqKjQ/H393N4335+Z3PM\n2NgIre8i7nZM7ra+s7jTcblTLM7kbsflbus7g7sdk7utL+KyZCw1NZXExERGjRrFkSNHuP/++yku\nLrY9n5ubS2RkZJXbyMzMq9a+S0stAJw4UXWy56vrO4O7HZO7re8s7nRc7hSLM7nbcbnb+s7gbsfk\nbuufT0mc73HZbcrIyEgiIs5eUFFRUZSUlNCqVSs2bz47LsyGDRto166dq3YvIiIi4hFc1jI2aNAg\nxo8fT79+/SguLiY5OZm//vWvTJgwgZkzZxIXF8ctt9ziqt2LiIiIeASXJWNhYWGkpKRcsPytt95y\n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\nM2fOHCZMmEBoaKjRYfqEsuQhJSWFsLAwHn/8cZ5++mnbZ0SvXr2Ijo4mMDCw3PryP+cOU/HOO+/w\n+eef88Ybb3DPPfdQWFjI0KFDmTVrlqY8khqj25QewGw207FjRzZu3MiAAQO4+eabWbRoEe3btycs\nLIxPP/2Uzp07Gx2mR5lf6PAAACAASURBVHv++edJSEhg+vTpfP/99+zZs4cGDRrw3HPPMWjQIP7z\nn/8wa9Ysevbs6VOJ2Lm3caxWK6WlpZhMJtLS0qhfvz533303l112mabVqQFlt9LLEqu4uDjCw8OZ\nOHEit9xyC7GxsYSGhtKpUydatWple50SsfLKEjGr1cqKFSvo3Lkz8fHxjBo1CoBu3bpx+eWXa0gW\nqVG6TenmyuaYS05OpmXLltSrV485c+Zw/fXXk5WVxapVq+jbty+dOnUyOlSPcu7cffn5+Rw8eJBr\nr72WN998k1tuuYUNGzZw+PBhrrjiCiIjI9mxYwdDhgyhWbNmBkdec8q+tI4fP87y5cvJy8sjISGB\nH374gYyMDC655BIuv/xyrr76aiIiIowO16ud20dszpw55OXlUVBQQJ8+fYiNjSUyMpLU1FRuvvlm\nGjRoYHS4bqukpMR2HlNSUli/fj3Z2dn06dOHHTt2MG/ePD744ANGjhzJVVddZXS44kM0Ar+HWL58\nOadPn2bQoEG88cYbbNiwgddee43w8HDb7Qixz7l9xA4ePEhISAghISF89tlnAPTq1Yv77ruPJ554\nwmerJssSsZMnT/Lwww/zj3/8g+XLl9OuXTsSExNZunQprVq14v7777dNcySuVVpaypAhQ2jbti0F\nBQWkp6dz9913k52dzb///W/uueceunbtanSYbs9qtTJ48GDatGlD06ZN2b17N1arlX/+8598//33\n1KpVSwVQUuN0m9INff311xQVFdke5+Tk0KFDB9LS0gAYMmQI1113HYcPH1YiVg3nVqSuXbuW/v37\ns3XrVuLi4njppZdISkpi0KBBtkTM136vFBcX2247btmyhaSkJJKSkmx9j/z9/Xnqqae48847lYi5\n2L/+9S+2bdsGwJ49e2jdujVDhw5l165dxMfHExwcTFJSEi+99JISsSrMnz+fDRs2AHDmzBmioqIY\nPnw4t912G126dGH//v0sXrzYVonua+95MZ6SMTfz22+/ARAYGMjatWvZvHkzDz30ENnZ2aSnp7Nk\nyRIAhg0b5rOtNs6QkpJCQkICycnJXHLJJXz00Uc0bNiQN998kxkzZpSb9NtX+txYLBYmTZrEqFGj\nWLp0KXB2KIv33nuPpKQkXnvtNdq2bctbb71lG9ldXKe4uJiIiAhSUlLYu3cvUVFRrFmzhv79+zN0\n6FA6derE/PnzycjIUP+mixgwYACdO3dmzZo1REZGsm/fPlauXAlg+0Fx4MABW+LrK+95cR/qM+ZG\nSkpKiIiIoHHjxnz55Zds2bKF5ORkateuzb59+zhw4ABZWVl069ZNLRJ/0rFjxzh+/DgLFy5kxIgR\ntGjRgi1bttCtWzcuueQSo8OrcVarlaeeeopGjRrZ+iAGBARgMpkICgri4MGDBAUF8frrrzN+/Hgl\nYi5WNqBr8+bN2bRpE+vXr+eWW26hTp06rF27lptuuolp06YxePBgWrZsaXS4bq20tJSgoCBycnJ4\n4IEHiIiIYMSIETz55JMcPXqUN998k2eeeYb09HSCgoJ0PsUQ6jPmJqZMmUJhYSH79+/n/vvvJzs7\nm5ycHPLz8xkwYABRUVEcPHiQU6dO0a5dO6PD9Sh5eXm2YRfKbrWtX7+et956i4YNG9KvXz/Gjx/P\n6NGjue666wyO1hjr1q1j69atTJw4EYCpU6dy7NgxSktL6dixI23atGH37t1cd911NGzY0OBofYPV\namX06NFcfvnllJaW8sMPPzB58mR+//13jh49St26denQoYPRYbqttLQ027VaNoVcRkYG/fr144EH\nHqBnz56kpaXx66+/EhkZSUpKClOmTOHyyy83OHLxRUrG3MDMmTM5fvw406ZNY+3atRw5cgSz2UzD\nhg355ZdfyMvLo1+/flx22WVGh+pxVqxYwffff8+4ceOIjo4u99yaNWvIysriu+++o0+fPiQmJhoU\npfG2bNnCZ599htVq5cyZMxw4cIAnn3ySn3/+mYyMDIYMGaLxqmrY559/bhvHDc4O/PzBBx8wZcoU\nmjZtanB07u3bb7/lww8/5N577+Xqq68GoKioiMDAQDIyMujZsydJSUkMHz6c5cuX88MPPzB48GCf\nnW9WjKfblAZ79tlnOXToECkpKQDEx8fj7+/P3r17ufLK/9/enYdlWWePH3+zr4rigogssokiioKS\nIihGpmaaYzpjpda44gKpuMvAuAZINpNOmUuaFprmIKSWkAuKQjigfkvjSaVcERVEAYFn+/3RxfPD\n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\n8gAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x29e646648d0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "_=sns.boxplot(x='league', y='overall', hue='Position', data=fifa_sub, order=leagues, hue_order=pos_order)\n",
    "loc, labels = plt.xticks()\n",
    "_.set_xticklabels(labels, rotation=45)\n",
    "plt.legend(bbox_to_anchor=(1.04,1), loc=\"upper left\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It is clear that the Spanish teams have a higher lower-floor, i.e., their teams have much greater depth from the bench. While the English league seems to be well balanced by position, note that the outside-mids in the Italian league are far worse than the other positions, while the outside-mids in the German league are far better. To savvy soccer fans, this last observation makes perfect sense; the Bundesliga is known for its frenetic pace, sending wingers tearing down the sidelines, while the Serie A has a slower, more defense, play-not-to-lose style.\n",
    "\n",
    "Let's take a look at the rankings of the top 50 players in each league. (Since this is a ranking, the lower the number the better)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[Text(0,0,'Spanish Primera División'),\n",
       " Text(0,0,'English Premier League'),\n",
       " Text(0,0,'Italian Serie A'),\n",
       " Text(0,0,'German Bundesliga'),\n",
       " Text(0,0,'French Ligue 1')]"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAfIAAAGkCAYAAADKRqc6AAAABHNCSVQICAgIfAhkiAAAAAlwSFlz\nAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMS4wLCBo\ndHRwOi8vbWF0cGxvdGxpYi5vcmcvpW3flQAAIABJREFUeJzs3XlgFOX9P/D3M7NHkt3cCWC4JIBy\nKFUMlwLWiqK2eCJyaLWVqlVpPaulcthS1B8tflUqth5Yb0DqrfVAEUULeACKiChyXwm5N9lr5vn9\nERKy2TXEZCazM3m//nIesskn42Y/81yfR0gpJYiIiMiWFKsDICIiotZjIiciIrIxJnIiIiIbYyIn\nIiKyMSZyIiIiG2MiJyIisjGX1QG0RnFxldUhEBERtZv8/PQf/Df2yImIiGyMiZyIiMjGmMiJiIhs\njImciIjIxpjIiYiIbIyJnIiIyMaYyImIiGyMiZyIiMjGmMiJiIhsjImciIjIxpjIiYiIbIyJnIiI\nyMaYyImIqMPQtTCC1duhRWusDsUwtjz9jIiI6McKVe9E8dZnoWtBQKjI7XEufDnHWx1WmwkppbQ6\niB+Lx5gSEXU8S5Y8jbVrV7f69RedkYmCfHfDdW1Qx6MvlKK1WXDIkGGYMGFKq+P5MXiMKRERdXj+\ntNiUl+IVcKnComiMwx45ERF1COW730HlgY8arlMy+qJT70kWRtRy7JETEVGHl1nwM2QVnIHte8L4\nZGMN8o6+0OqQDMFETkREHYIQCjI6j8DLKyrx8foaKKrX6pAMwURORERkY0zkRERENsZETkREZGMs\nCENERB2ClBLVJWvx89HpKC7ToGthKKrH6rDajNvPiIioQyjf8y4q93/YcJ2aeSzyCy+xMKKW4/Yz\nIiLq8AJlX8Rc11Zshq6FLIrGOEzkRETUIaguf8y1oqZCKPafYWYiJyKiDiGr6xgIpW7vuKZLZHU9\nA0KoFkfVdkzkRETUIaT4e6LrcTfgxeUVePzFUvhzT7A6JEOYOqZw/vnnIz29boK+W7duuOSSS/DX\nv/4Vqqpi5MiRuP7666HrOmbPno3NmzfD4/Fgzpw56Nmzp5lhERFRB6WoXuzcH7E6DEOZlshDoboF\nBE8++WRD23nnnYcHHngA3bt3x1VXXYWNGzdi9+7dCIfDWLx4MdatW4e7774bCxcuNCssIiIiRzEt\nkX/99deora3Fr3/9a0SjUUybNg3hcBg9evQAAIwcORIff/wxiouLMWrUKADACSecgC+//NKskIiI\niBzHtESekpKCK6+8EhdffDG2bduG3/zmN8jIyGj4d5/Ph507d6K6uhp+/+GVhKqqIhqNwuX64dCy\ns9Pgctl/gQIREbU/Va1bHtbc3mw7MS2R9+rVCz179oQQAr169UJ6ejrKy8sb/j0QCCAjIwPBYBCB\nQKChXdf1ZpM4AJSV1ZgVNhEROZym6QDsVVzMkoIwzz//PO6++24AwP79+1FbW4u0tDTs2LEDUkp8\n+OGHKCoqwuDBg7Fy5UoAwLp163DMMceYFRIREZHjmNYjHz9+PP74xz9i0qRJEEJg7ty5UBQFt9xy\nCzRNw8iRI/GTn/wExx9/PFatWoWJEydCSom5c+eaFRIREZHjsNY6ERF1KLfe+jsAwLx591scScux\n1joREZFDMZETERHZGBM5ERGRjTGRExER2RgTORERkY0xkRMREdkYEzkREZGNmXqMKRERUTKpKf8a\npxb5UFIWhZQ6hLB/f5YFYYiIqEOo3P8xyve83XDtyzkBuT3PtTCilmNBGCIi6vCqitfEXAdK10PX\nwhZFYxwmciIi6hB0rbZJiwQgrAjFUEzkRETUISScD5da+wdiMCZyIiLqEFIzj4259qQVQHGlWBSN\ncZjIiYioQ8juNha+nBNQFdCwdVcIeUePtzokQzCRExFRh6CoKcjteS4ef6kMr62sgsubZXVIhmAi\nJyIisjEmciIiIhtjIiciIrIxJnIiIupQFIdlPtZaJyKiDiEarsDBbS/guol5OFgeRahmD7xpBVaH\n1WYOey4hIiJKrGzXfxEK7AAA5Ga5cHDbf2DD40biMJETEVGHEK7ZE3MdDZVCakGLojEOEzkREXUI\nXn/PmGt3SmcorlSLojEOEzkREXUI2d3OQmpWfwTDOnbtDyOv10VWh2QIJnIiIuoQVFca8ntdjIef\nL8ULyyvhTsmzOiRDMJETERHZGBM5ERGRjTGRExER2RgTORERkY2xshsREXUYocBunDQgFcVlUatD\nMYyQNixrU1xcZXUIRERkM5UHVqN895sN176cE5Db81wLI2q5/Pz0H/w3Dq0TEVGHULH3vZjrQOk6\n6HrEomiMw0ROREQdgkyQtGW01oJIjMVETkREHYI7tUvMtVBToXoyLIrGOEzkRETUIXTqPRGetALo\n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\ncH3OKYX47UWLDIiMiJyooCDL6hAcLT//TJTnF6Dy4DdIS++K3IIiCAecz5AUiXzw4MF47733cM45\n52DdunU45phjmv36MpvMNf/qrGNxTEEGvtlZjuN752Jo/84oLo4vYEJERO1E9ERqXk9IACUH7ZFL\nACA/P/0H/01IKS0f761ftf7NN99ASom5c+eid+/eP/j1TIZERNSRJH0i/7GYyImIqCNpLpGzQgkR\nEZGNMZETERHZGBM5ERGRjTGRExER2RgTORERkY0xkRMREdkYEzkREZGNMZETERHZGBM5ERGRjTGR\nExER2RgTORERkY3ZstY6ERER1WGPnIiIyMaYyImIiGyMiZyIiMjGmMiJiIhsjImciIjIxpjIiYiI\nbIyJnIiIyMaYyDsYlg0wj67rVodA1GKapsVc87PBvpjIOxBN0yCEsDoMR9I0DYpS9+e0Z88eRKNR\niyNKPlJKPProo/j4449j2vkA1P50XYeqqpBS4uWXX8b+/fv52dAKCxcuxOOPP251GHBZHQC1j/o/\nXF3Xcdttt6Fr164YPnw4hg4d2pCAqPUa31uXy4Xs7GyMGjUKI0aMsDq0pPHuu+/iX//6F7KysjBu\n3Djouo7f/va3De8/KSWTSTtRFAW6ruP6668HACxatAhz5szBwIEDLY7MXjRNw7333gsAuOKKKyyL\nQ509e/Zsy346tQspJRRFgZQSDz74INxuN1RVxdatW6GqKrp27coPUAP85S9/wXHHHYeLLroICxcu\nRKdOndC7d294vV6rQ0sKhYWFSEtLw9ChQ3H66afj4Ycfxosvvojdu3cjEong6KOPtjpEx2v8sDR/\n/nwMHDgQt99+O1566SW8+uqr6Nu3L3Jzc+FysY93JNXV1fjggw8wefJkLFq0CDU1NTjppJMsiYVd\nMYcLh8MNf7gzZszAxo0bcdttt2HatGno3Lkz3nvvPaxatcriKO2p6ZyiEAJ5eXm4//77cc0118Dt\nduOzzz6zKLrkI6VEZWUlSkpK4PV6kZ+fj7PPPhvp6emYM2cOKisrrQ7R0XRdj3lg79+/P7xeL2bN\nmoUZM2agf//+WLhwIQKBgIVR2off78eIESPw85//HP/617+wdOlSPPLII5bEwkTuYG+99Ra2bNnS\ncD1lyhR89913ePXVV+FyuXDxxRcjPz8fXbt2tTBK+6r/UFy4cCHWr1+P4cOH409/+hN69uyJMWPG\n4JVXXoHP57M4yuQhhMAvf/lLvPLKK7j88svxq1/9CpdffjmmTp2KF198ERkZGVaH6Fj1aziklPj7\n3/+O+fPn49RTT0VeXh7S09ORk5OD0tJSXHXVVcjNzbU6XNv46U9/CgDo3r07Hn/8cSxatAgPPfRQ\nu8fB088cKhqNYseOHSgsLMScOXMQCoUwdOhQFBQUYPr06fjtb3+L888/H7quc478R2p8z6qrq/H8\n88/j66+/xtlnn43y8nK89tprUBQF48ePx5gxYyyONnlomgZVVfHEE0+guroa1157LSKRSMMwLqd3\nzKXrOmbMmIFgMAhN09CnTx+cdtppeOKJJ7B27VrMmjULp556qtVh2kbjaYpoNAqXy4Vdu3Zh9+7d\nGDZsWLvGwkTuYFJK/PGPf0Tnzp1x1lln4Y477sDkyZPRv39/XHvttVi6dClyc3OZyFtp8+bN6Nu3\nL6qqqrB8+XKsXr0av/rVr9C3b19UVFQgJyfH6hAt09wD4ieffIJbbrkFjz76KHr37t3OkXUsH3/8\nccOCy3vvvReBQAB33HEHNmzYgGXLliErKwuXXnopotEojjrqKIujTV71D6FNNX6fN/6a9l64yU9w\nh3nuueewb98+AMDWrVtRWVmJ6667Dv3798f999+PxYsXY8CAAXjhhReQn5/PJP4jNN53+/rrr+Oh\nhx7C559/Dp/Ph9NOOw26ruOhhx5CbW0tk7ii4ODBg1iyZAnWr1+P/fv3N/x7UVERfvnLXyIlJcXC\nKJ2vpqYGX331VcP2Pr/fj2OPPRYAMGjQIGRlZWHjxo14/fXXcdRRR3Ef+Q9ovONnxowZWLhwIRYu\nXAgAMZ+fjRN9e48ucWmiw/Tp0wddunTB1q1b4ff7kZWVhW3btuGYY45BMBhESkoKKioqkJmZaXWo\ntlL/tC2lxMMPP4yxY8eitLS0Yb2BpmlwuVyYOnUq/H6/1eFaSlEU7N+/H9OmTcOYMWPw4IMPYtCg\nQZgwYQLy8/MB1G3V4UOkeZ599ll4PB5ceeWVmDlzJrp3744xY8bgsssug9/vR35+Pr788ksMGTIE\nxcXFADi18UPq1xbceuutOPHEEzFgwABcf/316NatG8aNG2d1eACYyB2jfo6mqKgIH374IebPn4+7\n7roLBQUFeOSRR5Cbm4sNGzZg6tSpTOI/kpSy4Yn8zjvvxKpVq/D2229j/vz5iEQiWLp0KT755BNM\nnz69ocfTES1duhTnnXcePB4P3nnnHVxxxRU488wz8d///hdutxtlZWUNiZxJ3DyRSARdunTB66+/\njoyMDFx77bW4/PLL0bVrVyxatAiPPvooQqEQpk+fjr1792LRokUIBAJcmNlE46HyAwcOIDMzE6ec\ncgr+7//+D7feeisqK/Cu71YAACAASURBVCuxf/9+dO7c2eJIuY/cEep7g1JKrFy5EqNHj4aqqli8\neDEuvfRS9O7dG927d8epp57KAiWtUN9TufPOO5Gfn48FCxZg9+7deOaZZ3DllVfijDPOwBlnnIFB\ngwZZHKl1Dhw4AI/Hg/z8fIRCIezduxePPvoo3njjDdx33304ePAgVqxYgVNOOYVJ3ET1nwUFBQXI\nzMzEyy+/jJycHFxzzTW4/fbbkZ+fjxtvvBEulwtbt27FwoUL8de//jUpklGyqe+Jf/XVV8jJycG7\n776LZcuWYdy4cQ0JfcyYMUmx24J/UQ5Q31ucOnUqPvvsM7z00ksYP348Ro0ahTlz5sDj8WDEiBE4\n4YQTrA7VVprWoq7/gASAG2+8EaqqYubMmQiHw+jevXuHnmPs1KkT+vfvj+effx6zZ89GUVERBg4c\niGAwiK1bt+Kpp57CpEmTEi4YImPU9yB1XceGDRvQt29fjB8/Hi+//DI2btyIJ554Ao8++iiKi4vR\nr18/dO7cGQsWLOCCwyYalwxeuXIlbr75ZuzatQsjR46Ez+dDVVUVbr75ZlxzzTXo1q2bhZEexh65\njT399NPo1asXvF4vFi1aBJ/Ph5tvvhmPPPIIXn/9dfz85z9HdnY2cnNz0aVLF6vDtZXGc+Jr1qyB\n3+9HOBzGjh07UF1dDU3TsH79ekgp8fnnn2PMmDEdco6xfnVuSUkJbrrpJvzsZz9DeXk5PvzwQ/zm\nN79BdnY2tm3bhquvvpoJw2T1ZVdvuOEG7Nu3DwUFBTj22GPRpUsXPP/888jOzsb06dORkZGBjIwM\nHH300ZxmS0AI0fC+Pvroo5GamorHHnsM55xzDk4++WR06tQJI0aMSKrRTc6R25Su6ygsLER6ejoq\nKyuRk5ODt956C9OnT8fkyZPx+eef44033sBNN91kdai2VN+zueWWW1BcXIyTTjoJhYWFyM3Nxfvv\nv49t27bhz3/+M/bt24cVK1b84PYUpxNCoKqqCn/729/Qp08fjBgxAt26dcOyZcvw4IMPYsaMGUhL\nS7M6TMerTzz33XcffD4fbrjhBtxxxx0NnxEXX3wxsrOz4fF4Yr6eDmu8leyZZ57B8uXL8dhjj+Gi\niy5CKBTCddddh3vvvdeyMqzN4dC6TSmKghEjRmDVqlW47LLLcOaZZ2LRokUYOnQofD4f3nrrLYwe\nPdrqMG1t7ty5GDZsGO655x58+umn2LRpE7p3744///nPuOKKK/DBBx/g3nvvxYUXXtjhknjj4Ucp\nZcPJejt27EC3bt1wwQUXoGvXriz3abL66Z/6pFxYWAi/349Zs2Zh7NixyM/PR1paGk455RQMGDCg\n4XVM4rHqk7iUEkuWLMHo0aPRr18/3HzzzQCA008/HT179kzaLZMcWreh+prJN954I/r374+CggI8\n+OCDGDVqFMrLy/H8889j0qRJOOWUU6wO1VYa16Kura3F999/jyFDhuDf//43xo4di5UrV2LXrl04\n/vjjkZGRgQ0bNuCaa65B3759LY68fdV/6B04cACLFy9GTU0Nhg0bhnXr1qG0tBR5eXno2bMnBg8e\njPT0dKvDdazGc+IPPvggampqEAwGMXHiROTn5yMjIwOPP/44zjzzTHTv3t3qcJNWNBptuI/33Xcf\n3nnnHVRWVmLixInYsGEDHnroIbzyyiu46aabcOKJJ1odbkKs7GZjixcvRkVFBa644go89thjWLly\nJRYsWAC/398whEYt03hO/Pvvv0dqaipSU1Px9ttvAwAuvvhiXHrppfjDH/7QoVen1yfxkpIS/OY3\nv8Gvf/1rLF68GEVFRRg5ciSeffZZDBgwAJdffjlP0GoHmqbhmmuuwQknnIBgMIidO3figgsuQGVl\nJd58801cdNFFOO2006wOM+lJKXHVVVdh0KBB6NOnD7766itIKXH11Vfj008/RVZWVlIvFubQuk28\n//77CIfDDf9dXV2N4cOHY8eOHQCAa665BieffDJ27drFJN4KjVf+v/TSS5gyZQrWrl2LwsJC/O1v\nf8O4ceNwxRVXNCTxjvj8G4lEGobK16xZg3HjxmHcuHEN860ulwt/+tOfcO655zKJm+jhhx9uOFVv\n06ZNGDhwIK677jps3LgR/fr1Q0pKCsaNG4e//e1vTOLN+Oc//4mVK1cCAKqqqpCZmYlp06bh7LPP\nxqmnnootW7bgiSeeaNjxk8x/80zkNrB7924AgMfjwUsvvYTVq1dj6tSpqKysxM6dO/Hkk08CAK6/\n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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x29e5c14f240>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fifa_sub_top = fifa_sub.groupby('league').head(50)\n",
    "_ = sns.boxplot(x='league', y='Rank', data=fifa_sub_top, order=leagues)\n",
    "_ = sns.stripplot(x='league', y='Rank', data=fifa_sub_top, order=leagues)\n",
    "loc, labels = plt.xticks()\n",
    "_.set_xticklabels(labels, rotation=45)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It's very interesting to see that when just looking at the top 50 players in each league, the English league appears have the best ranking. However, with rankings, there are some nuances with boxplots that don't make them the best visual representation. Let's instead turn to a stackplot. The x-axis will represent the cumulative rankings, and the y-axis shows the percentage of players ranked at that point (i.e., at x=10, players ranked 1-10 will be represented) per country. Let's first perform this visual up to rank 100, then we will expand to 1000. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5,0,'Player Ranking')"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAowAAAFlCAYAAABhkLkBAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz\nAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMS4wLCBo\ndHRwOi8vbWF0cGxvdGxpYi5vcmcvpW3flQAAIABJREFUeJzs3XlcVPX+x/HXmQ0Y9k3AXUFcM8Qs\nlVtm3dyXbHGNfpY3y/I+UtOrpeaWpWbRrqmZZqbXvc3MtMzrmllumQsgi4osAsIAM8PMfH9/IJPE\nLtug3+fj0UPmzDnf85lhiDff8z3fryKEEEiSJEmSJElSKVR1XYAkSZIkSZLk2GRglCRJkiRJksok\nA6MkSZIkSZJUJhkYJUmSJEmSpDLJwChJkiRJkiSVSQZGSZIkSZIkqUwyMEoVdvHiRdq2bcvgwYPt\n/w0aNIhNmzYBsGXLFp599tlarysyMpIHHnjAXtPAgQPp3bs327Ztq1K7rVu3Jj09vdj2wYMHk5WV\nVaW2C+Xn57No0SIGDhzIoEGDGDhwIEuXLqVwtqs9e/bw7rvv3nT7kZGR7Nix46aPT09Pp3Xr1qU+\n/9NPPxEZGcngwYPp378/EyZMICkpCai+z8OMGTM4depUldupiPfff5+5c+fWyrkkSZLqE01dFyDV\nL87Oznz55Zf2x8nJyQwYMIAOHTrUYVXwn//8hz59+tgfnzx5khEjRvDPf/4TNze3aj3Xja+/qlav\nXs3FixfZunUrGo2G7Oxs/u///g9vb2+GDRvGyZMnuXbtWrWdrzp9/fXXLFmyhCVLltCsWTOEECxb\ntownn3ySb7/9ttrOc+DAAYYNG1Zt7UmSJEmVJwOjVCUBAQE0a9aMuLi4ItuPHTvGm2++idlsJjU1\nle7du/P666+zZMkSoqOjeeuttwD49ddfee2119i2bRu//fYbixcvJi8vD5VKxfjx4+nZsydbtmxh\n06ZN5OXl4ebmxpo1a8qtKzExEb1ej06nw2az8frrr3P8+HFycnIQQvDaa6/RuXNnpk2bhpubG2fP\nnuXKlSu0bt2ahQsX4urqam8rNTWVp556ihEjRjBq1Chat27NwYMH2bNnDz/88AMqlYr4+HicnZ1Z\nuHAhwcHBxMfH88orr3Dt2jX8/f0RQjBo0CAeeeSRInWmpqaSn5+P2WxGo9Hg7u7OokWLsNlsHD9+\nnPXr12O1WnF3d+fZZ59l9uzZxMfHk5mZiaurK4sXL6Zly5akpqYya9YsYmNjUalUDB8+nCeffNJ+\nHovFwksvvYRGo2HhwoXk5eUxf/58zp07R35+Pt26deM///kPGo2GnTt3EhUVhYuLS5l/CERFRTFv\n3jyaNWsGgKIojB07lqCgIMxms/31jR07lqSkJNRqNW+99RbBwcGlfj4uXrzIqFGjCA4O5tKlS3Tu\n3JmUlBQmT57MokWLuPPOO+3n37JlCzt27MBms3H58mUCAgJYsGABAQEBZGdnl/r6OnTowIMPPsiZ\nM2dYvHgxd9xxR7mfJ4CYmBjmz59PZmYmVquVyMhIHnvssTI/X+np6bz88sskJCTg5eWFv78/rVq1\n4t///rf9c+Tj4wNQ5PGPP/7IkiVLyM/Px9nZmalTp9KpU6cK1SlJklQjhCRVUGJioggLCyuy7bff\nfhNdunQRly9fFps3bxZjx44VQggxceJEcejQISGEEAaDQdxzzz3i5MmTIi0tTYSHh4uMjAwhhBBT\npkwR69atE5mZmaJXr14iMTFRCCHElStXxH333ScuXbokNm/eLLp06SKys7NLrOuJJ54QPXv2FIMG\nDRL333+/6Natm5g4caL4448/7DX++9//FlarVQghxMcffyyeffZZIYQQU6dOFcOGDRMmk0mYzWbx\n8MMPi02bNgkhhAgNDRWnT58W/fr1E19++aX9fKGhoeLq1ati8+bNonPnziIpKUkIIcTcuXPFf/7z\nHyGEEEOHDhVr164VQggRHR0t7rzzTrF58+ZitSclJYkhQ4aIO+64QzzxxBPi7bffttcthBDvvfee\nmDNnjhBCiO+++07MmzfP/tzMmTPF3LlzhRBCvPDCC2LhwoVCCCGysrJE//79RVxcnHjiiSfEV199\nJZ5//nkxZ84cYbPZhBBCTJs2TXz22WdCCCEsFouYPHmyWLZsmUhNTRWdO3cW58+fF0IIsXTpUhEa\nGlqs7vT0dBEaGipyc3NL/J4IIcTmzZvFXXfdJeLi4oQQQsybN0+8/PLLQojSPx+JiYkiNDRUHDly\nxN5Oz549xYkTJ0psPywsTMTGxgohhHjzzTfFv//97zJfnxAF37+tW7eWWPON7/eN8vPzRb9+/cSp\nU6fs73Hfvn3F77//Xubna+LEiWLRokVCCCGSk5NFRESEeO+99+x1XL161X6OwscXLlwQAwYMEOnp\n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\nIiKacD5bGHfu3AmHw4Ft27Zhw4YNeOyxx/qPVVdX41//+hdeeeUVbNu2DXv37kVxcXFACyYiIiKi\nieWzhfHQoUNYsWIFAGD+/Pk4ceJE/7GkpCS88MILUKlUAACXywWtVhugUomIiIgoGHy2MFosFuj1\n+v6vVSoVXC4XAECj0cBkMkFRFDz++OOYPXs2srKyvN5PEIVxlkxEREREE8lnYNTr9bBarf1fy7IM\ntXqgYdJut+P++++H1WrFz372M59vqMjKGEslIiIiomDwGRgXLlyI3bt3AwCOHj2K3Nzc/mOKouC7\n3/0uZs6ciZ///Of9XdNEREREFD58jmFctWoV9u3bh7Vr10JRFGzevBkvvvgi0tPTIcsyDh48CIfD\ngT179gAA7rvvPixYsCDghRMRERHRxBAURZnQPuK1P30bVptrIt+SiIgoaN789Y3BLoFo3LhwNxER\nERF5xcBIRERERF4xMBIRERGRVwyMREREROQVAyMRERERecXASEREREReMTASERERkVcMjERERETk\nFQMjEREREXnFwEhEREREXjEwEhEREZFXDIxERERE5BUDIxERERF5xcBIRERERF4xMBIRERGRVwyM\nREREROQVAyMRERERecXASEREREReMTASERERkVcMjERERETkFQMjEREREXnFwEhEREREXjEwEhER\nEZFXDIxERERE5BUDIxERERF5xcBIRERERF4xMBIRERGRVwyMREREROQVAyMRERERecXASERERERe\nMTASERERkVcMjERERETkFQMjEREREXnFwEhEREREXjEwEhEREZFXDIxERERE5BUDIxERERF5xcBI\nRERERF4xMBIRERGRVwyMREREROQVAyMRERERecXASEREREReMTASERERkVcMjERERETkFQMjERER\nEXnFwEhEREREXjEwEhEREZFXDIxERERE5BUDIxERERF5xcBIRERERF4xMBIRERGRVwyMREREROSV\nz8AoyzIeeeQRrFmzBuvWrUNVVdWg46+++ipuueUWrF69Gh999FHACiUiIiKi4FD7OmHnzp1wOBzY\ntm0bjh49isceewzPPvssAKC5uRlbt27Fa6+9Brvdjttvvx3Lli2DJEkBL5yIiIiIJobPwHjo0CGs\nWLECADB//nycOHGi/1hBQQEWLFgASZIgSRLS09NRXFyM/Pz8Ye+Xbjagx+byQ+l0PrVGhMspB7uM\n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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x29e6491b518>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "top=100\n",
    "fifa_top = fifa.head(top)\n",
    "\n",
    "top_vec=[None]*(len(leagues))\n",
    "for L in range(len(leagues)):\n",
    "    top_vec[L] = [((fifa_top.Rank<=x+1) & (fifa_top.league==leagues[L])).sum() for x in range(top)]\n",
    "#need to calculate the 'other' league\n",
    "other = [None]*top\n",
    "top_vec_numpy = np.array(top_vec)\n",
    "for r in range(top):\n",
    "    other[r] = r-np.sum(top_vec_numpy[:,r])+1\n",
    "\n",
    "#now let's make the data frame\n",
    "top_df = pd.DataFrame({leagues[0]:top_vec[0],\n",
    "                     leagues[1]:top_vec[1],\n",
    "                     leagues[2]:top_vec[2],\n",
    "                     leagues[3]:top_vec[3],\n",
    "                     leagues[4]:top_vec[4],\n",
    "                     'Other Leagues':other}, index=range(1,top+1))\n",
    "\n",
    "top_df_perc = top_df.divide(top_df.sum(axis=1), axis=0)\n",
    "plt.stackplot(range(1,top+1), top_df_perc[leagues[0]], top_df_perc[leagues[1]],\n",
    "              top_df_perc[leagues[2]], top_df_perc[leagues[3]],\n",
    "              top_df_perc[leagues[4]], top_df_perc['Other Leagues'],\n",
    "              labels=[*leagues, 'Other Leagues'])\n",
    "plt.legend(bbox_to_anchor=(1.04,1), loc=\"upper left\")\n",
    "plt.margins(0,0)\n",
    "plt.title('Player Ranking Stacked Chart per League')\n",
    "plt.xlabel('Player Ranking')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It appears that the Spanish league has a high-percentage of the very, very best players in the world. The French league gets an early boost from Neymar, ranked 3rd in the world, but doesn't get another player ranked until rank 30. Let's take a look at the percentages at the top 10 and the top 100."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "English Premier League      0.2\n",
       "French Ligue 1              0.1\n",
       "German Bundesliga           0.2\n",
       "Italian Serie A             0.1\n",
       "Other Leagues               0.0\n",
       "Spanish Primera División    0.4\n",
       "Name: 10, dtype: float64"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#top-10\n",
    "top_df_perc.iloc[9]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "English Premier League      0.32\n",
       "French Ligue 1              0.08\n",
       "German Bundesliga           0.16\n",
       "Italian Serie A             0.16\n",
       "Other Leagues               0.01\n",
       "Spanish Primera División    0.27\n",
       "Name: 100, dtype: float64"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#top-100\n",
    "top_df_perc.iloc[-1]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "While the English league gets off to a slow start, they actually have more top-100 players than any other league. One thing that is remarkable is the utter dominance of the top 5 leagues. There is only 1 player ranked in the top 100 who is not in the main 5 leagues. Let's find out who it is."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>Rank</th>\n",
       "      <th>club</th>\n",
       "      <th>league</th>\n",
       "      <th>nationality</th>\n",
       "      <th>overall</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>67</th>\n",
       "      <td>Pepe</td>\n",
       "      <td>68</td>\n",
       "      <td>Beşiktaş JK</td>\n",
       "      <td>Turkish Süper Lig</td>\n",
       "      <td>Portugal</td>\n",
       "      <td>86</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    name  Rank         club             league nationality  overall\n",
       "67  Pepe    68  Beşiktaş JK  Turkish Süper Lig    Portugal       86"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fifa.loc[~fifa.league.isin(leagues)][['name', 'Rank', 'club', 'league', 'nationality', 'overall']].head(1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We now perform the same actions, but this time we get the stack plot for the top 1000 players instead of the top 100."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5,0,'Player Ranking')"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAowAAAFlCAYAAABhkLkBAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz\nAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMS4wLCBo\ndHRwOi8vbWF0cGxvdGxpYi5vcmcvpW3flQAAIABJREFUeJzs3Xd0FdX68PHvzCnpvQOhJYBUQ4JK\nuYLoFZGOBRSIr8oV5ScuAeGCAtKMAqIRUAFBBZEi0hQFLBS5gCBFmvRgChBSSELa6We/fxxzICQh\nAUJC2Z+1XOZM2fPMZEie7KoIIQSSJEmSJEmSVAa1ugOQJEmSJEmSbm0yYZQkSZIkSZKuSiaMkiRJ\nkiRJ0lXJhFGSJEmSJEm6KpkwSpIkSZIkSVclE0ZJkiRJkiTpqmTCKFXYmTNnaNy4MT179nT+16NH\nD1asWAHAqlWrePnll6s8rtjYWB5++GFnTN27d+exxx5jzZo1N1Ruo0aNyMrKKrG9Z8+e5Obm3lDZ\nRSwWC9OmTaN79+706NGD7t27M2fOHIpmu9qyZQszZsy47vJjY2PZsGHDdZ+flZVFo0aNyty/efNm\nYmNj6dmzJ127dmXo0KGkpqYClfc+jB07lsOHD99wORUxa9YsJk2aVCXXkiRJup1oqzsA6fbi6urK\nd9995/yclpZGt27daNasWTVGBf/973/p3Lmz8/OhQ4d49tln+fe//42np2elXuvy+79RCxcu5MyZ\nM6xevRqtVkteXh7/7//9P/z8/Ojbty+HDh3i4sWLlXa9yrR27Vpmz57N7NmzqVOnDkIIPvvsM557\n7jl+/PHHSrvOjh076Nu3b6WVJ0mSJF07mTBKNyQkJIQ6deqQmJhYbPv+/ft5//33MZvNZGRk0LZt\nW959911mz57NqVOn+OCDDwDYs2cP77zzDmvWrGHfvn1Mnz4dg8GAqqoMGTKEjh07smrVKlasWIHB\nYMDT05NFixaVG1dKSgru7u7o9XrsdjvvvvsuBw4coKCgACEE77zzDjExMYwePRpPT0+OHz/O+fPn\nadSoEVOnTsXDw8NZVkZGBi+88ALPPvss/fv3p1GjRvz+++9s2bKFX375BVVVSUpKwtXVlalTpxIR\nEUFSUhJvvfUWFy9eJCgoCCEEPXr04IknnigWZ0ZGBhaLBbPZjFarxcvLi2nTpmG32zlw4ADLli3D\nZrPh5eXFyy+/zIQJE0hKSiInJwcPDw+mT59O/fr1ycjIYPz48Zw+fRpVVXnmmWd47rnnnNexWq28\n8cYbaLVapk6disFgIC4ujhMnTmCxWGjTpg3//e9/0Wq1/Pzzz8THx+Pm5nbVPwTi4+OZPHkyderU\nAUBRFAYNGkRYWBhms9l5f4MGDSI1NRWNRsMHH3xAREREme/HmTNn6N+/PxEREZw9e5aYmBjS09MZ\nMWIE06ZN495773Vef9WqVWzYsAG73c65c+cICQlhypQphISEkJeXV+b9NWvWjEceeYRjx44xffp0\nmjdvXu77BJCQkEBcXBw5OTnYbDZiY2N56qmnrvp+ZWVl8eabb5KcnIyvry9BQUE0aNCA1157zfke\n+fv7AxT7vGnTJmbPno3FYsHV1ZVRo0bRsmXLCsUpSZJ0UwhJqqCUlBQRFRVVbNu+ffvEfffdJ86d\nOydWrlwpBg0aJIQQYtiwYWLnzp1CCCHy8/PFAw88IA4dOiQyMzNFdHS0yM7OFkIIMXLkSLF06VKR\nk5MjOnXqJFJSUoQQQpw/f160b99enD17VqxcuVLcd999Ii8vr9S4BgwYIDp27Ch69OghHnroIdGm\nTRsxbNgw8ddffzljfO2114TNZhNCCDF37lzx8ssvCyGEGDVqlOjbt68wmUzCbDaLXr16iRUrVggh\nhGjYsKE4cuSI6NKli/juu++c12vYsKG4cOGCWLlypYiJiRGpqalCCCEmTZok/vvf/wohhOjTp49Y\nvHixEEKIU6dOiXvvvVesXLmyROypqamid+/eonnz5mLAgAHiww8/dMYthBAzZ84UEydOFEIIsX79\nejF58mTnvnHjxolJkyYJIYR49dVXxdSpU4UQQuTm5oquXbuKxMREMWDAAPH999+L//u//xMTJ04U\ndrtdCCHE6NGjxVdffSWEEMJqtYoRI0aIzz77TGRkZIiYmBhx8uRJIYQQc+bMEQ0bNiwRd1ZWlmjY\nsKEoLCws9XsihBArV64UrVq1EomJiUIIISZPnizefPNNIUTZ70dKSopo2LCh2L17t7Ocjh07ioMH\nD5ZaflRUlDh9+rQQQoj3339fvPbaa1e9PyEc37/Vq1eXGvPlz/tyFotFdOnSRRw+fNj5jB9//HHx\n559/XvX9GjZsmJg2bZoQQoi0tDTRrl07MXPmTGccFy5ccF6j6PPff/8tunXrJrKysoQQQpw4cUK0\na9dOFBQUlPmsJUmSbjZZwyhdE6PRSM+ePQGw2Wz4+fnx/vvvExYWVuy4KVOmsHXrVubMmcPp06cx\nmUwUFhYSEBDAQw89xHfffUevXr3Ytm0b48ePZ8+ePWRkZPDqq686y1AUhePHjwOO2perNS0XNUln\nZWXx0ksvERISQpMmTQBo2bIlPj4+LFu2jJSUFHbt2lWsBvHBBx9Er9cD0LBhw2JNwC+99BKhoaF0\n79691Os2bdqU0NBQAJo0acIvv/zCxYsXOXjwIF9//TUAERERtG7dutTzQ0NDWbVqFadOnWLXrl3s\n2rWLvn37Mnr0aPr371/s2M6dOxMeHs6iRYtISkrijz/+cNY67dixg5EjRwLg5eXFDz/84Dxv6tSp\nFBQU8Msvv6AoCuDoG3no0CFn/1Oj0QjA3r17adiwIZGRkQD07duXDz/8sETcquro/my320u9ryIt\nWrRw1kA2btyYX375BSj7/fD19UWr1RIVFXXVcou0a9eOevXqAdCnTx/nu1nW/RVp1apVhcovkpiY\nSHJyMm+99ZZzm9Fo5MiRI/Tr16/M9+u3335j9erVAAQHBxfrNlGW7du3k56ezvPPP+/cpigKycnJ\n3HPPPdcUtyRJUmWRCaN0Ta7sw1iWAQMG0KhRIx588EEef/xxDhw44BzI0b9/fyZMmIBWq6VTp054\neHhgs9mIiIjg22+/dZaRlpaGv78/a9euxd3dvULx+fv789FHH9GtWzdatmxJp06d2LJlC3Fxcbzw\nwgs88sgj1K9fn++//77YPRVRFMUZJ8CkSZOYM2cOX375JS+++GKpz+PKczUaDUCxcoq2XWnatGk8\n/fTTREZGEhkZSf/+/fnuu++YN29eiYRxyZIlLF++nP79+9O9e3d8fX05c+YMAFqt1pkMgqNJ3s/P\nD4AePXoghGDs2LHMmTMHcCR6M2bMICIiAoDc3FwURWHHjh3F4tZqS/8R4ePjQ926dTlw4ABt27Yt\ntu/1119n8ODBJc6//Nle7f3Q6/VlXvdKlz9Xu93u/FzW/RWp6PtUpKhbwOXvfmZmJl5eXld9v7Ra\nbbHnWZRoX6moCb8o9jZt2vDRRx85t6WmphIcHHxNMUuSJFUmOUpaqnS5ubkcOnSIESNG0KlTJ86f\nP09ycrKzNio6OhpVVfn888955plnAIiKiiIpKYndu3cDcPToUR577DHS0tKu+frh4eG88sorxMXF\nUVhYyPbt2+nYsSP9+vWjWbNm/Prrr9hstgqVFRUVxZQpU5g9ezYnTpyo0Dmenp5ER0ezatUqwJG8\n/f7778USliJZWVnMmDEDg8EAOJLMkydPOmtHNRoNVqsVgG3bttG7d2+efvpp6tWrx6ZNm5z30aZN\nG1auXAngHDhT1K+0RYsWDB06lOTkZJYvXw7Av/71LxYsWIAQArPZzODBg/n666+57777OHXqFMeO\nHQNw3kNphgwZQlxcHElJSYAjqfr00085duwY9evXL/O88t6PK13+DK60c+dO5zuybNkyOnbseNX7\nu1716tUr9sdSamoq3bp14/Dhw1d9vzp06OCs5czOzubXX391vgf+/v4cOnQIoFiNcJs2bdi+fTsJ\nCQmAo5ayR48eJWpJJUmSqpKsYZQqnbe3N4MGDaJ37964u7sTEhJCdHQ0SUlJtGnTBoAnnniCdevW\nOZvY/P39mTlzJtOmTcNkMiGEYNq0adSqVYs//vjjmmMYOHAga9asYfbs2TzzzDO88cYbdO/eHavV\nSrt27fj555/LbU4tUr9+ff7v//6PkSNHFqsBvZqpU6cyZswYlixZQkhICLVq1SpWG1lk/PjxxMfH\n06NHD/R6PVarldatW/P2228D0Lp1a0aMGMHkyZN58cUXefvtt50JSFRUlDOJffvtt5kwYQLdu3dH\nCMHLL79cbMCKi4sLU6ZM4cUXX6R169aMGTOGuLg4unfvjsVioW3btvznP/9Bp9Mxffp0RowYgU6n\n47777ivzHouuNXz4cKxWKyaTiaZNm7Jw4UJnE39prvZ+hIeHlzj+0UcfZeTIkUyYMIF//etfxfaF\nhIQwcuRIMjIyiIyMdE6JU9b9VcTy5cudzcjg6A6xbNkyPv30U+Li4pg/fz5Wq5XXX3+dmJgYfH19\ny3y/3nzzTcaOHeusEa5Ro4bzPRg7diyTJk3C29ubtm3bEhQUBOC8j+HDhyOEQKvVMnv27GLdKCRJ\nkqqaIi5vL5GkKmC1WhkyZAg9evSgS5cu1R3OTTF79mw6depEREQEeXl59OjRg3nz5jn7Bko3btWq\nVfz000/MnTu3ukMp0+LFi2nSpAktW7bEbDbTr18/XnvtNTp06FDdoUmSJF0TWcMoValTp04550es\nyACA21XdunUZNmwYqqpis9l46aWXZLJ4F4qMjGTy5MnY7XYsFgudO3eWyaIkSbclWcMoSZIkSZIk\nXVWFBr0cOHCA2NjYEts3bdrEk08+Sd++fZ2d6SVJkiRJkqQ7S7lN0vPmzeP777/Hzc2t2HaLxcJ7\n773HihUrcHNz49lnn6Vjx47OjtuSJEmSJEnSnaHcGsbatWsza9asEtsTEhKoXbs2Pj4+6PV6YmJi\n2LNnz00JUpIkSZIkSao+5dYwPvbYY87JgS+Xn5+Pl5eX87OHhwf5+fnlXvDXX5fjZ999jWHemLPe\nD7E2K6z8AyVJkiSpks3rEl3dIUjSDbvuibs9PT0pKChwfi4oKCiWQJat5OTFN5vWlFXl17ycRgEX\nVamGO5ckSZIkSbpx1z2tTkREBElJSeTk5ODu7s6ePXsYOHBgZcZWadzsF8s/6DIK4KJRcNMouKng\notpxVezoVRt6rOgVC3phQYsFHSa0woxOmNBiRmM3oREmNMLo+NpuRFUcE0R/r+/POWPFJouWJEmS\nJEm6VVxzwrh27VoKCwvp27cvo0ePZuDAgQghePLJJwkJCSn3/OqYw8fVmgk4EkFvnYq3VuCtseKh\nmPDAgBv5uNrzcbXnordfRG+96Ejy7Dj+uxGXVSuG6QrJsrhhtYNVzmYkSZIkSdJtosrnYfzl1xX4\n23dV5SUByNfVws2SioaKrSF8M+1z68kfee7VHYYkSZJUBWQfRulOUOUrvVRXxZqnpeTAneoSJs4S\n4toID9WOu2rFTbHgppjIsXtwMF9X3eFJkiRJkiQVU/UJY1Vf8BYUZtxDb0pOQZSnq81B2lVDRJIk\nSZIkSWW77lHS10smjGXzsiTT2qug/AMlSZIkSZKqUJUnjAg5uczV1LUdwV+vEuxS9d8aSZIkSZKk\n0lR5k/Q1UzQg7NwtdZO+5lP04RRGTQAL6FTd4UiSJEm3ke5vfFep5a39oGe5x3z22Wfs2LEDVVVR\nFIVhw4bRrFmzSrn+kCFD+Pjjj0vdN3r0aLp06UL79u1L3b9r1y6GDh1KZGQkACaTie7duxMbG1vs\nuK1bt5Kamkrfvn0rJebyrFq1ipkzZxIeHo7dbkdRFF599VXatGlz1VgyMjL45JNPmDBhQqnlxsXF\n8cILL1CjRg3AMauN3W6nZ8/yv4cVcUv3YVQ0bhw90ZLGDfYh7MabFtOtyNV2gSAXlQyTnLdRkiRJ\nujWdOnWKTZs2sXTpUhRF4ejRo4waNYrvv/++UsovK1msqNatWxMfHw+A2Wymc+fO9OzZE29vb+cx\nZSWcN1O3bt0YMWIEAJmZmfTv35+vv/76qrEEBQWVmSwCjBkzptjn7t27V0qsRaq+hlFQocVeFI07\n+w5Ec+6sSpNGursuYQSorS8ky+yKj04lyywTR0mSJOnW4u/vz7lz51ixYgXt27encePGrFixAoDY\n2Fjq1avH33//jRCC+Ph4/P39efvttzl//jzZ2dm0b9+eoUOHMnr0aPR6PWfPniU9PZ0pU6bQtGlT\n2rVrx/bt21m8eDFr1qxBVVWio6MZNWoUAN988w3z588nPz+fCRMm0KJFizJjzc/PR1VVNBoNsbGx\n+Pn5kZubS9euXUlKSuKZZ55h2LBhhIWFcebMGbp27crJkyc5cuQIDz30EMOHD+f48eO88847APj6\n+vLuu+9y5MgRpk+fjk6no0+fPri6urJ48WLndWfMmIG/v3+ZcQUGBvLYY4+xZcsWNBoNp0+fJjg4\nmNzcXIYMGYLZbKZHjx7Mnj2bUaNGsXz5cuLj49m5cyd2u52uXbvy/PPPExsby4QJEwgKCmLkyJHk\n5+djs9l4/fXXadOmDd27d+f+++/n+PHjKIrCp59+WsEV+hyqYdBLRbJFLYePtuTcWfWfc+7OqWZa\nGtczUP2GJ+3L0auy76ckSZJ0a/H392f27Nns27ePvn370rlzZzZv3uzcHx0dzaJFi3j88ceZO3cu\nqampREVF8fnnn7N06VKWLl3qPLZGjRp8/vnnxMbG8s033xS7zqpVqxgzZgzffPMN4eHhWK1WAJo2\nbcpXX33FgAEDWLVqVYn4du7cSWxsLM899xwjR45k3LhxeHh4AI4auAULFqDRaJzHp6SkEBcXx9y5\nc5kxYwajR4/m22+/dSbB48aNY/z48SxatIj27dszf/58wNHcvWTJEnr16kViYiKfffYZixYtol69\nemzbtq3c5xgQEEB2drbzc8+ePVm/fj1CCDZu3EjHjh3R6S7lQmvWrGH69OksXrwYV1fXYmXNnj2b\ntm3bsnjxYmbMmMGYMWOw2+0UFBTQtWtXvv76a4KDg9m6dWu5cV2uGuZhFOXWMGZejCLxb81lW+7O\nhFErjP88Kztd3Y9yUQ1kU25g8WMUBX+9gofGzt+F1RKmJEmSdJdKSkrC09OT9957D4BDhw4xaNAg\nHnjgAcDRJAyOxHHTpk34+vpy6NAhdu7ciaenJ2az2VlW48aNAQgNDWXfvn3FrvPee+/xxRdfMH36\ndKKioihac6Rp06aAo5bOaCzZEnl5k/SV6tWrV2JbeHg4Xl5e6PV6AgMD8fX1BUBRHIlLQkICEydO\nBMBisTjLuLysgIAARo0ahYeHB6dPnyYqKqrsB/iPc+fO0aRJE2w2x+IiPj4+NG7cmL1797J69Wpn\njWqRDz/8kA8//JDMzEwefPDBYvsSEhKczdEhISF4enqSlZUFQJMmTQAICwvDZDKVG9flqqEPYznZ\nojacXb8XXwXlbq1hvFyI8U8CFFfOevQiQM3Hn0x8rOfwMJ9Btdmx2XR8pT6NyX53DA6SJEmSqt/x\n48dZunQpc+bMwcXFhXr16uHl5eWstTt8+LAzAYyMjGTVqlV4eXkxadIkkpKSWL58uTP5K0rKSrN8\n+XImTpyIi4sLAwcO5M8//yz3nPKUdm555dWrV4+pU6dSo0YN9u7dS0ZGBgCq6mgRzcvLY+bMmWzZ\nsgWAF154gfIW1EtPT2fjxo0MHjyYTZs2Obf36dOHhQsXYjQaiYiI4MwZxwIkZrOZDRs28OGHHyKE\noGvXrnTt2tV5XkREBHv27KFJkyakpaWRm5tbIvG9HtUwSvpqwSr8eaBOia1CaCvSkH3H0wojHU3L\nim/858FosNDLbQ/fFMQ4PisQ6KISpLVQYNfI2kdJkiSp0nXq1ImEhASefvpp3N3dEULw3//+19k3\nbvXq1SxYsAA3NzemTZtGZmYmw4cPZ+/evbi5uVGnTh3S09PLvU6jRo146qmn8PPzIyQkhHvvvbfU\nJuibbcKECYwaNcpZExgXF1csfk9PT6Kjo+nduzfu7u54e3uXen8//PADBw4cQFVVhBC89957zqSu\nyP3338+4ceMYPHhwse16vR4fHx969uyJj48P7dq1c46MBnj55Zd56623+OmnnzAajUyaNAmt9sbT\nvSpfS3rt+lXU0Pxe6j6bGsmG9TVKbO/8+Dk09lM3O7Q7QopbG/xIx70wEVVxvNA5+gi2iwdIMZT8\nViuAr14lUGfDXzXgSw75iifbc71LHCtJkiRdu7t1LemiQRgRERHVHYpUCW6pGsYjR0JL3W6za9Fp\n/bFbs67vihoPhO3uWEEl3PBPMn7ZY/Y1J9BFnGaVSz/cNYIgjQF/svCzn8fLnITWboTLujJYFVf8\nPO8lmXDn2taeWpV8qxypLUmSJEl3o2oY9FL6dkUXSnJS6YO28/I8OH62Cc3vKX+kUbEyNe6kpDZH\nVaFG4K5rDfWOoiiCJ22LwVb+sVphpJZxF4HaBBp5BOFlSUZvL2ClS385L6QkSZJUIYsWLaruEKRK\ndMusJX0hq2aZ5+zc4U5m5rX1YhSaOvy2PYYDf7qQm3fZiGtFxWBrSoGl+TWVdzdytWYSYDqK3u6o\nnW2qz8BVoxDupqC9gY6zkiRJkiTdXm6ZGsZjx9xL3wGAgqGwol0tFXKN9/K/37woapfNzXHkxYo2\njH37Izh3VuXeliY8gisctgQ0KvyFexQBFjjk1RWj0JNqceecUdY6SpIkSdKd7JaYVkfRhpCddfUa\nKyEUFFWHsFvKPEZRtCSfj+Hgfpdi27OyFC4aWrL9f54I4bjOxRwNtWTCeE0U5VLS3rzwRwDOubbi\nexpUV0iSJEmSJFWBKm+SLk2+oYKZm+JS9i5Vz/G/7y+RLALYrArbtno5k0WA8+c1JJ5rfc2xSsWF\nGfbip78lXiNJkiRJkm6SW6JJOi3Ns0LnKooeReuD3Xrxiu06jiW04tSJit+O0aDw1yEddWtqQFRg\nJIhUKkURPKg/Qb6LD9sLgqtl4nCNAjY5X7kkSRJ9vhlc/kHXYHnf2Vfdv2vXLoYOHUpkZKRzm5+f\nHzNnzrym68yaNYvAwECioqLYuHEjQ4YMKfW4hx9+mPXr1+PiUnoF0qxZs/jhhx8IDnZURFksFoYN\nG+ZceeZGxcXF8cILLxSb97Ai7oQphm6BaXUUEv+uWBhmWyAZmb6EBfxR/PyzMdeULF5+rqLxReAC\n1nPXcT6gqKAJvf7z7wA1jLsBCHRrhEBldWFL/PUKoToTgWoOCZZgkgwCb51KiN5GkJpPgMhguzmS\nfKvAW6eQednoa1WBAL1KkM6Cr1LIznwv7AK8dSpBOjsBmkL8yMbHnoaXOYV012YkU5tEowsXLbI/\npSRJUlW62vJ716px48bOJQKv1/PPP8+zzz4LOJbJGzFiBKtXr66M8BgzZkyllHM7qoY+jMWrglSt\nH4bCio243bYthFrhVgi4tC27oCWHD+mvO56t2xsTEmynYb1rTPgUDSZ7Q/btcazt3KbV3ZswFvE3\nHQfgBc0pNDaLcwqf2poAcBG42rKKzffYSz2CTsnDbtOz36sLfmTjZzuHtzmx2Pl1XOvjZstAb88D\nMyXUNPxBTf6gpltb1llKrhQEjmTTRaXYtECeWhWDzS5rJyVJkm6C2NhY7rnnHk6ePEl+fj4zZsyg\nZs2afPLJJ/z666/4+/tjMBh4/fXXnefs2rWLZcuWER8fz+jRo0lOTsZkMjFw4EC6dOkCOFZbKVom\n7+OPP8bHx6fMGHJycnB3dwyq7dixI/Xr16d+/fq8+OKLjBs3DpPJhIuLC5MnT8ZmszFs2DDCwsI4\nc+YMXbt25eTJkxw5coSHHnqI4cOHO2sKg4ODGTNmDNnZ2QCMHTuWRo0aFbtGecmlxWJh/PjxJCUl\nYbfbGTp0KA888AAbNmxg8eLFzuNmzJiBn58fEydO5PDhwwQGBnL27Flmz57Nxx9/TJcuXWjfvj1b\nt25l3bp1TJkyhfXr17NgwQJUVSUmJoYRI0Zc3zfxMlVfwyiKJ4cWm3+FTy3IVzAYLvWXs6kR7NhW\nsebssuTmqKiqQsN6jql4FFtS8QO0tcB65rINChYasmd3MFkXLt2LwdYUd10Cwl5y8fO7jYbiA5Nc\nbRdKPU5vzwMFNJiJMawpszwfy+kKXbe2YQfdPG38Za9PgMaAHzn42s7jbUlBJwqw2l1J8mqNrz0d\nL0sKenseyZ5tseCCu8hju6URPlo7SYUK1qpdAEmSJOm2tXPnTmJjY52fO3TowH/+8x8AWrRowZgx\nY4iPj+fHH3+kffv2/O9//2PFihVYLBa6d+9eapn5+fns2rWLlStXArB9+3bnvieffJJWrVoxevRo\ntm/f7kwkiyxYsIB169ahqire3t5MnjwZgNTUVFatWoWfnx9Dhw4lNjaWDh068PvvvzN9+nSGDRtG\nSkoKX3zxBUajkUceeYStW7fi5uZGx44dGT58uPMac+bMoXXr1vTr14/ExETefPNNli5dWuwa5fn2\n22/x8/Pj3XffJTs7mwEDBvDjjz+SmJjIZ599hpubG2+//Tbbtm3D3d2dnJwcVqxYQVZWFp06dSqz\n3JycHGbNmsXKlStxc3Nj5MiRbN++nXbt2pUb09VUecJov+IXcX7htSV8RoMjSVO13mzefG19CMqS\nk6WQnNqaw4d0dHksBYQdVevPkRP3cD5Vw0Pt/kkYteH8eaA2585oSpSx6dcAunbNBXtKpcQkXZ9a\nxl3UovRJ2rXCSIRhS7FttQ07nF8/xR6wwQX3JqwztaRArmwjSZJUrqs1STdp0gSA0NBQMjMzSUhI\noHnz5mg0GjQaDc2aNSv1PE9PT8aNG8e4cePIz8+nR48ezn1F5wQGBmI0lqykubxJ+nJ+fn7ORO7E\niRPMnTuX+fPnI4RAp3OsahYeHo6Xlxd6vZ7AwEDn+s7KFXMPnzhxgp07d7J+/XoAcnNzS1yjPCdO\nnGDv3r0cPHgQAKvVSnZ2NgEBAYwaNQoPDw9Onz5NVFSU8/8A/v7+1K9fv0R5RSs9Jycnk5WVxaBB\ngwAoKCggJeXGc5Nq78OYk+2FXoXqAAAgAElEQVR6TWcXFDjOP/l3Uwor2JRdEYcOOpq1VY0fBcYw\ntm70w2p1lK/oQkg+U7fUEdiXO3Y8nPoRHug5VmlxSVUvwHSE9m7+rM8Lr+5QJEmS7iiRkZEsWrQI\nu92O1WrlyJEjpR6Xnp7OX3/9xSeffILJZKJDhw707NkTKJm8VZSqXmqhLGqWjo6OJiEhgd27d19T\n2fXr16dHjx50796dCxcu8O2335a4RkXKCA0N5ZVXXsFoNDJ79my0Wi0zZ85ky5YtALzwwgsIIWjQ\noAHfffcdABcvXiQxMREAvV5PRkYGgPNZ1qpVi7CwML744gt0Oh2rVq264X6hUC19GItLT7+2EAoL\nwKo04NgRXeUFdZkdu5pw4YpVZX78sWGxKXnKknBKi4enD7VrBmKyBKFXjt6UGKWbr45hGxHuz5Ji\nVAjUK6Qa7Qgcf+7IxmpJkqRLrmySBpg3b16pxzZq1IgOHTrQp08f/Pz80Ol0aLUl84CgoCAyMjLo\n1asX7u7uvPjii6Ued71GjRrFhAkTMJlMGI3Gax7M8sorrzBmzBiWL19Ofn5+maO6L/f666+j1zsq\npx544AGGDRvG2LFjGTBgAPn5+fTr1w9PT0+io6Pp3bs37u7ueHt7k56ezhNPPMHWrVt55plnCAwM\nxNXVFZ1Ox9NPP81bb73F2rVrqVu3LuCogXz++eeJjY3FZrNRs2ZNHn/88Wt+RldShKjazlrffPcd\nkW7/rAmtqKz7qV2FkrHLeXoJ8vNuzaXptFqB1QoBgYI2rXZiFhHoOF7dYUnXwYYOVVhQFDjvGo2L\nyMfLnMxptwfR6rR4mFI5RQMO5VdDRb0kSbeNeV2iqzuEW8aFCxfYsGED/fv3x2w207VrVxYuXHjN\n09TcbRISEjh27Bhdu3YlOzubbt26sXnzZmcCWhWqdaUXVeNzzckicMsmi4CzGftCpsLWna3JzVHp\n1uUsiqLDbs2u5uika6HB4uxBEWrc59zesPAX59f+ykmSdb0w2BxvdnXMQylJknS78PPz4/Dhwzz5\n5JMoisLTTz8tk8UKCAsLY/r06SxcuBCbzcaIESOqNFmEaqhhXLbmexq4/8/xQVubH3+sW5WXrxZ+\nAXbcXKFls23VHYp0E1gUD7T2Ai66NCBVW5+tuf5Xbbb20qkE6uwkFUJpw2pks7ck3VlkDaN0J6jW\nPowWq3tVX75aZF9QyQai73VH2AqrOxypkulEASjgaz6Jr/kkeq+O2NHgJ86TroaTJ9zxV3Lws6Xh\nbUlyzid51PsxEi0BBGiN+Cs5+NrS8bYk87frA2zODazu25IkSZIkp2pdGtBouvqo4zuNjRA02jxQ\nNAhLWnWHI90kEYbNzq8DOVzmcY0Lf6IxcMW0lTQq/IVCr54IwI8cfOznAfhDxJBiEPjrVQJ1VixC\nJcngGJSTYxEY5AzkkiRJ0k1SrX0YDYU3Z6TzrWr3nlpcyID72xQS6CUTRqlsLQ3fldjWSZxCaEBj\ns4ENR/9fRaBYIcO1OftphtGmct7kGNEtu1NKkiRJlaUaahgv/RbLL7i7EsbMdEeyvG+PO488EoHG\nnoBdU4+E02E0qLOjnLOlu52q2Ip9VpRL/5aCTId4lEPY0IHGTrZLY/aJ5lywqHJ9bUmSJOmGVevE\n3Xm5JVdMuRtYzAqJScGYzaGcPuV4Bv7+MZhMWmoElr5KiSRVRNGyjIGmw3TiMEZNAKt0ncm12FEB\nX71KllkmkJJ0p9re88lKLa/ddyuvuv/MmTMMHz6c5cuXc/z4cXJzc7nvvvtKPfbydaKHDBnCxx9/\nfN1xZWVlMX78eAoLCxFCUKNGDcaOHYura/mLgRw9epSNGzdWaO7EIj179iQ6Oprx48dfd8y3u2rt\nw5ibV9VXv3VcOfH4zh0e6PWCsH/XQ7H9XU1RSXcaV9sFemo3YdG542VORmO3kO7Rgp9NzcmXSx9K\nklSJfv75ZwIDA8tMGC93I8kiwPz582nbtq1zCcC4uDiWLVvG888/X+65jRs3vqaVT/bu3UvDhg3Z\nuXMn+fn5eHpe25LGd4pqHSVdkFfxJXTuBmazwl9Ha9CooZ7EpADZTC1VCg9rarHPwaaDdNMb2KK9\nn/NGu5zGR5KkG5aWlsbq1avR6XQ0bdqUc+fOsXjxYuf+GTNmFDu+Xbt2bN++nT/++MOZPBqNRqZO\nnYpOp+ONN94gNDSUlJQUmjdvzsSJE4udX7NmTX766Sfq1KlDdHQ0o0aNci7rt2jRIn744QcURaFL\nly4899xzjB49mpycHHJychg4cCDr1q0jPj6e9evXs2DBAlRVJSYmhhEjRpS4t2+//ZbHHnuMsLAw\n1qxZw4ABAyr78d0WqjxjK6phVFRXbLbSj1HVW3di7pst6W8NP/8UwoljWlStY9FzFLmSiFS5fM0n\n6W5dxvMuP9PXfQ8NPGTKKEnS9QsJCaF37948//zztGjRgsTERD777DMWLVpEvXr12Lat9HmIT548\nyfvvv89XX33Fww8/zIYNGwBITEwkLi6Ob7/9lq1btzrXSy7y7LPP0q1bNz7//HMefPBBhgwZQnp6\nOqdOnWLdunUsWbKEJUuW8Ouvv3L69GkAWrduzbJly/D29gYgJyeHWbNmsWDBApYuXUpaWhrbt28v\ndp38/Hz27t3LQw89xJNPPsnSpUsr+9HdNqqtSVpRy56DMchPS9oFS5n77xb5xlpALfbu8aN92z8Q\ndlN1hyTdQTTY0Ngu4Gq7wEMkYXR7ihSDTBwlSbpxAQEBjBo1Cg8PD06fPk1UVFSpx4WEhBAXF4e7\nuztpaWlERzsmOa9du7az6TcoKAiTqfjvv127dtGrVy+eeuopzGYz8+bN49133+Xxxx/n3Llzzqbp\nixcvkpycDEC9evWKlZGcnExWVhaDBg0CoKCggJSUlGLHfP/999jtdl5++WUAMjIy+P3332nTps0N\nPJ3bU7U1SQtK75iqqgoBah5pZey/m2ze6O/8+ujJGO6JkE3U0s2hwcyjtrVkeTYggQgO52tlM7Uk\nSddEURTsdjt5eXnMnDmTLVu2APDCCy9Q1qJyY8eO5ddff8XT05NRo0Y5jytqXi7LwoULSUlJoU+f\nPuj1eho0aMDp06epX78+kZGRzJ8/H0VRWLBgAQ0bNmTDhg0lyqxVqxZhYWF88cUX6HQ6Vq1aVaJv\n44oVK5gzZw4NGjQAHAnk4sWLZcJYJf5ZO9ouSl8D0ddHh86aDTJhLCbhlJZa4S3w1B9E1fqSk1cX\nb7f9qFof7NZcZC806Ubp7XmEGvcRyj5iXAL4SenMeaNjTkfNPz9n5dzgkiSVpVmzZkybNo2IiAii\no6Pp3bs37u7ueHt7k56eTq1atUqc07NnT/r06YO3tzeBgYGkp6dX6FoTJ05k4sSJLFmyBFdXV/z8\n/JgwYQIhISG0adOGZ599FrPZTIsWLQgJCSm1DH9/f55//nliY2Ox2WzUrFmTxx9/3Ln/yJEjCCGc\nySLAY489xnvvvUdqaiphYWHX+IRub1W+lvQXy3/gXt/fsCoN+GlDyYcdEQzexgz+zA2qyrBuC3q9\nILpVIbt3uWOzKUS3MnLgTxcefTQVo9kND92h6g5RusNkuDRHJwx4mZNIc43if+aGZFfhtDwKjqmA\nLlrsxSYilwN1pNuJXEtauhNUW5O0zVb6pN1e5gtobOaqC+g2YjYr7Nzh4fy8b4+jFnbDhhoAPPxI\nM9y0h9HovLBZ7uI5i6RKE2S69EdIDeNunuIARtcAflcf4qJNRadAmsmOqihY7AKtohDoopD2T81k\neTy0KsF6O/4aI4kmd3x1dgLUQvzJxsd+Hm9LChq7gVSPVqSrYfiKLHxs5/Eyp3DIrTM78zzKv4gk\nSZJ0w6pt0IvFWvql3bOSsbj7VmFEd47ftvjT6v4Y9u72oPNjRxDWzOoOSbrDaDDjYU3l3zhGCgqh\nYNdoMWoDsSkueJpTUK02kr3acVHxxV9k4Gs5w1l9U45bgvDXWAhQLuIv0vC2JONqy4Z//j68D6CM\ncV1hxj1c2R4RZfgeN+9H2VkQRKAerEIh1Xip9lOrKFirtgFFkiTpjlV9CaOl9Eu7nD2BvW7po6mk\nq7PZYNfvjhqXnLxa+LhVPGFUtb4ItAhrJorGDWEzFD9A0YKwVma40h1AUQQaLJfmevynr2NtQ/Gp\nKRpaz9EQoJInP2hU+AuNFEe5NnSc8bofL9sFvCzJ2FQ3CrTBJKqNOGfxQAA5VgjSCfy1RvyUPFLt\n/mRZtdgE5JgdK90HuCi4qoLEQplsSpIkFanyhLHo73+zueSygF5eOlSTAcVqvHwFQek6/PWXJ21b\nKaCthdniiV456tx3eUKoagM5c74++/e5UKeuHY2mIYUGlaZNstBoLOg158nOi2TfXk8efugYwppR\n1iUlqVppsFDnskRVZyvE1XaBAI4Sc/mBFpyJa8PLNpt1Xuhs+ShWR6J40uvfbM4PKtZ3UpIk6W5V\nbaOkzeaSc4b7uDp+MmssRih9ELVUQdkXVA4ea0tKkgYPT4GPbzti7j1MTl49/tjlRfuHMkg778vB\nAzqKsvPEvy8l8alnA3FzF5hNYc4J1s+k1qdWqAFhy6+GO5Kkm0tvzyv2h2oDw6/4eNzLekNTDHJ4\nuCRJd7lqGPTi+MFbWsLoqThqvRSzTBgrQ0qSIwEsyFcoyNeQlnqvM/n75afgcs83FBav5t2/zwVj\nk+YA1K93DpPJE73OgGo/XbmBS9ItIth4gL7aM/ztfh97DAEUXLb+thypLUnS3aQa+jCWXcPoZswG\nQLUYqzSmu0VZSzFei2NHdP/8vw4AIWF2WrX4m+r61alqfQAtdmv2P7/Bq27KF+nu4Gq7QGPDBhqi\nJ9OjMQbVC1/bebzMyeS4RLBXRJFskANspFvDpDfWVmp5b3/QvdxjUlJSeP/99zl//jyurq64uroy\ncuTIYvMXVoddu3YxdOhQIiMjEUJgtVqJi4sjIiLiustMSEhgwoQJLFq06JriWLZsGfHx8QwZMsS5\ndvbtptoWKTaXMnOOW24aAIqxsIqjka5XWqqKLcrxj08rkkDRIOxGQMWuqcuphFCCgw2oqsDX8/Q/\nk4yDqvHCbi8EYUfRBl7RN9LR99JidUevJjqXRFQ0nghbPorGDaO1LqcT/DmdoMHXV2CzQcuYXLxc\nDlwqRXXFImoDAp32ImaL7z/lyWmbpGunwUyI6UCxbQGmo3TiKEaXQBRh5aK2Nnph4KDaEqtQ0SiC\no/kl/ziWpDuFwWBg8ODBTJ48mZYtWwJw8OBBJk2adE1J1c3SunVr4uPjAdi2bRvTpk1j7ty51RbP\n7ZosQrXUMP7TJG0qOapFl+lYw1ExFlRpTNKN2bDeMQ9kzfBQMtIU2rS9yOHDPlzIdHyPTx73AqDV\n/Y0ICTpP8pkaHD6op1kLM+fO6si6oNCtix2EmTxDPQ4f8iYzU0VRBKoazH0PFHLqlDtWM4TXtnDk\nLx0226X3JyfH8fWObd60uj8GX5+LnDkbyNEjOmzWouMck7JotCHcG2WiRtB+mThKlcb1nymsgm05\nALTnpHNfjFst9LZczrm0IEnUIM+mJUBrxh0Tewu8MMtRNdJtbPPmzbRu3dqZLAK0aNGCr776CoDU\n1FTGjRuHyWTCxcWFyZMnY7PZGDx4ML6+vrRv356tW7fSqFEjTp48ibu7O61atWLbtm3k5ubyxRdf\noNFoGDNmDHl5eWRnZ/P000/Tr18/YmNjueeeezh58iT5+fnMmDGDmjVrlhlrbm6uc39sbCwTJkwg\nIiKCpUuXkpmZSe/evXnjjTcIDQ0lJSWF5s2bM3HiRNLT0xkxYgRCCIKCLi0q8scffxAfH49GoyE8\nPJxJkyZx5swZ3nzzTbRaLRqNhmnTphWLoV27dmzfvp2DBw8yceJEPDw8CAgIwMXFhSlTpvDBBx9w\n+PBhCgoKiIiI4L333qvMb9cNqbYmaeMVrc5arYo2x7EkkGqzoqoKdvmD9LZyNsVRk/LbltLn0dzz\nhxtwafH3QwdcnF//b0cTLuZcej/A8bXNRrHJynNyyu7carUWTWxe9mTONqvCvj2uiJgo3Nys+Hpn\nY7G5kHbel9o19v9TOypJlcfTcgaAuoZt1C3a+M8o7XquddijtMFVsXK0UI9F/syTbjNnzpyhdu3a\nzs+DBw8mPz+f9PR0Fi5cyNSpU4mNjaVDhw78/vvvTJ8+nWHDhpGRkcHKlSvR6/Vs3bqVFi1aMHbs\nWAYOHIirqytffvklo0aNYvfu3YSFhdG1a1c6depEWloasbGx9OvXD3Akp2PGjCE+Pp4ff/yRQYMG\nFYtv586dxMbGYjabOX78eLm1i4mJiXz++ee4ubnx73//m4yMDL788ku6detGnz59WLduHUuXLkUI\nwbhx41iyZAkBAQF89NFHrF69GovFQtOmTRk9ejR79uzh4sWLpV5n/PjxTJs2jQYNGhAfH09aWhr5\n+fl4e3vz5ZdfYrfb6dq1K2lpaWUubVjVqn5anX9+HpqMxWsYvTyLh6LVqZhNldDpTrot5GRX7TxK\nf+4tWqvc07mtoDCaxg0TENa0Ko1Funt5m5N4mCQAmrnU5Zg2mly7CwFqIR5KIVnCmyyrCwU2BZMd\nAvWCAI0BP+UiHvaL5ChBaBQbOwqCMMqR3FI1CA0N5fDhw87Ps2fPBqBPnz5YrVZOnDjB3LlzmT9/\nPkIIdDpHP/hatWqh11+qAGjatCkA3t7eREZGOr82mUwEBgaycOFCfv75Zzw9PbFaL80J3KRJE2cc\nmZkl5x6+vEn69OnTPPPMM2zdurXYMZevkFy7dm08PR2/F4KCgjCZTJw8eZKePXsCEB0dzdKlS8nK\nyiI9PZ2hQ4cCYDQaadeuHYMHD2bevHn85z//wcvLi2HDhpX63NLT0519PGNiYli3bh0uLi5kZWUx\nfPhw3N3dKSwsxGKp5Mlrb0C1LQ1oumJFB3dd8cEKWq1MGKWqlXBSS35eA+5rmYWw3zr/SKW7g7cl\nkfstiVc/6IpeFEWr39TWBnDWvQXHbWH4a0z4K7n42DPxtp7lgq4+mwwRFFrlgDCp8j3yyCPMmzeP\n/fv3ExXlWHQjKSmJ8+fPoygK9evX58UXXyQ6OpqEhAR2794NgKpWvG/vF198QVRUFP369WPnzp38\n9ttv1xVrYGCg82u9Xk9GRgYREREcOXLEWYunKCUrL+rXr8+ff/7JPffcw6FDjuVS/fz8CA0N5dNP\nP8XLy4uNGzfi7u7Oxo0biYmJYciQIfzwww/Mnz+fXr16lSgzNDSUU6dOERkZyYEDjr7RW7duJTU1\nlY8++oisrCx++eWXYslsdSs3YbTb7UyYMIHjx4+j1+t55513qFOnjnP/559/zo8//oiiKLzyyis8\n+uijVy1PCFDUS3P/FXFXiv8k1GnkzN1S1Us7r7Jzb2va3HcUu1xaUbpNuNouEGHYTGljP2tZ0+mr\nOYZZ54WbNZMTrh04a/PDRbVxzqQjxyITSen6eXh4MHv2bD744AOmT5+O1WpFq9UyefJkatasyahR\no5gwYQImkwmj0ciYMWOu+RodO3ZkwoQJrF27Fl9fXzQaDebSRs6WoqhJWlVVCgoKGD16NK6urjz3\n3HNMmjSJsLAwgoOvPs3c66+/zrBhw1i3bh21atUCHAnvmDFjGDRoEEIIPDw8mDZtGgUFBYwcOZJZ\ns2ahqipvvvkm+fkl5y4eP348b731Fu7u7uh0OkJCQmjRogWffvopffr0Qa/XEx4eTnp6OuHh4df8\nzG4GRZSTvv78889s2rSJKVOmsH//fubOneuscs7NzaVHjx78/PPPGAwGevXqxebNm696wRlfrePB\nmrv4YV2rYtubB+QTvGuF8/Of9w0iK1sOSpCqR41aNlo22yWXQ5TueBlercm1unHYUgNvjQ1/tQCd\nYqVQuOLHRdzIJxdffMQFvK3nsKgeKMJGqrYBOcKLVKsraUaZdF7NvC7R1R2CdItZvHgxjz/+OP7+\n/sTHx6PT6RgyZEh1h3VV5dYw7t27lwcffBCAqKioYn0V3NzcqFGjBgaDAYPBUGpV7pWEECiKrsR2\nF2PxjqF6za1TDSvdfc6d0RAYGIOiQHDQRfTqCTnHo3RHCsrbSRA4aifL+PuoRinbfCx/O78+53U/\nW4wNyJW1lZJUIQEBAbz44ou4u7vj5eXFlClTqjukcpWbMObn5zs7gAJoNBpnlTPgHL1ks9l4+eWX\ny72gAFRNyYTRzZRT7HOw3sD56psmUpI4uL9oFHcwIaHBtL7/L2yWXISwyeRRki5Tw/AHfTRHOOff\nGpPiylmrD8kF4KFTCXKxc9GicrZA1tZLUpHOnTvTuXPn6g7jmpSbkXl6elJQcGleRLvd7kwWt27d\nSnp6Ohs3bgRg4MCBREdH06JFizLLE3aw2Up2dlWyio9M9Ug9DjSt0E1I0s2Wdh62bmtCYQGE17Fx\nIVNLo3sK8PPJlksjShKgteVTO/dXAJzre1gc/9mFilXvyTmXe/nLGk6hTUGrgr/GSqJRI9fqlqTb\nQLkJY3R0NJs3b6ZLly7s37+fhg0bOvf5+Pjg6uqKXq9HURS8vLzIzc29anl2FEBTMpCs88U+u5w7\nAWEyYZRuHdlZji4Xp044/tns3OGBq5s7/36kAKvNCxBoSZYjrCXpCqpiR2/Ppa7hf5fmorQDVmit\n9WWv2785lK+Ta3NL0i2s3ITx0UcfZfv27TzzzDMIIXj33Xf58ssvqV27No888gg7duygT58+qKpK\ndHQ07dq1u3qBAsQVCaOLqxbFWnyAi2ooOapIkm41RoPCDz80cn5u0iyYejV3AgJVGwjYEPaCYqvK\nKBpPTNZauGiTEDYDiuqKVdTCJrRoVTMateCKuSAVVK0ndmteld2XJFUVF1sObW0ruNe1Bpm6eqQT\nzDmLO6lyII0k3VLKHSVd2d7/4kc61jnNunV1ndv8fPVE7/msxLFbGr2IzSZ/aEi3l2YtzGRd0HLu\nrIpeL9DpoWOHUxgtvvyd6MfpkxqEUKhX34abu53jx7SXLWEIXj6Ch/51BJvwIj0ziGNHXTGb4J4m\nZsJrpqJSgN2ahaJxQ9gKUXShKKLQuU63JN0J0l1asM3anHTT7f87QI6Slu4E1bI04JU1jK7a0nNW\nnV7FZrj9f1hId5fDBy+tXmA2K5jN8MOPDUoc9/dpDaV1z8i7qLD2x5LdMQ7ud+Hg/rqAwMvLsWqS\nTutYSzsk1E69+gZsVhWtzoaLiwUv10QEVoTNUIl3J0lVI9h0kF7iLzI9mmJW3MhUQjCjJc3ihg0o\ntCFHZZdi788jK7W8mE7vX3X/mTNn6NGjh3OlFoAHHnig0qeIuXzt59KsWrWK06dPM2LEiGLbhwwZ\nwscff1ypsRRJSkri1Vdf5Ycffrgp5d9qqmWlFyGKD3px0ZS+oou7q4pR/q6TpCso5F3ROp12XiXt\n/JVraPvi6wcPtj2EsBuxUpPMC/4EBmSjsSeA7DEm3eJUxUaw6SAAta7YZ0OPwS2YAjUAk+rJbnNd\ntArkWcFLC1YBWWY7cjzNzRcZGcmiRYuqO4xS3axkcc2aNXz11VdkZ2fflPJvRdVQw1hKwihKn6A7\nWFtAFiWn4JEkqSIUcrJh4+bmmEwKNuffZW7c94AvIf6HEXZjdQYoSddNgxlPyxk8OQNAbbZf2vnP\nDD4FLjU4prufk0YPzHbw0MIFsx27TCJvul27djF9+nR0Oh19+vShRo0axMfHo9FoCA8PZ9KkSaxd\nu5bffvsNo9FIcnIyL730Ek888QQHDhwgLi4OIQQhISFMnz4dgE8++YTMzEwMBgMffvhhhVZAadeu\nHdu3b+fgwYNMnDgRDw8PAgICcHFxYciQIQwfPpzly5cDjvWvP/zwQ3x8fBgzZowzGRw7diyNGjUq\nVq6Pjw9ff/11uavb3UmqPGG0C7CL4s1welvpv7R8sxKAe6ogKkm6cxUWlpxQf/cud1xc7uOeJmZq\nhGag4ZxMHqU7jof1HDHWNUQLBUURYAOL1p2zrq04Za9JqknFRYU8i8BHr2C0Qb5cc/uanTp1itjY\nWOfnogTPZDLx7bffIoSgc+fOLFmyhICAAD766CNWr16NVqslPz+fzz//nMTERF555RWeeOIJxo0b\nR3x8PBERESxevJiEhAQAOnToQM+ePZk1axYbNmzgpZdeqnCM48ePZ9q0aTRo0ID4+HjS0tLKPHbO\nnDm0bt2afv36kZiYyJtvvsnSpUuLHdOxY8dreUR3hOppkrYXr2HUWgpLPVafkwpe96CqCnb5J6Ek\nVSqTSeHAny4coBY1atYg+t4/EbaC8k+UpNuMolz6/aEThdQ1bC02vY9QQbGBVXElxzOSv5UGnDS6\nYxcQoBcEaIx4k0823hwr0GOSv4+KKa1JOjExkXr16gGQlZVFeno6Q4cOBcBoNNKuXTtq167NPfc4\nKoXCwsKc60NfuHDB2Vexf//+zjKbNWsGQGBgIJmZmdcUY3p6Og0aOPqSx8TEsG7duhLHFI0BPnHi\nBDt37mT9+vUA5U4XeLeoliZp+xUJo87kmEJHcXFBmEzO7WphPl41dFitAoNBrhIgSTfLubMqQrQk\nvLYRX59c9GoSwm4q/0RJugMUrWqrFUYCjYcJ5DCtxD/br+gxFaP1JksfyQU1hASzP6lGOwLw1qn4\naAX5NoVCq5BJJaCqjt/1fn5+hIaG8umnn+Ll5cXGjRtxd3cnNTW11CWFg4ODSUxMpG7dunz22WfO\nxPNGhIaGcurUKSIjIzlw4AAALv+fvTuPjvOuD/3//j7brBqNRqu1b5Z3O3Y2QhZKQigJFyhduAQK\nTXsLvxZOTylwyjlwewg0zQm00J5yWAq0bJetuZcGCEtLSghkcxInsRNvsmzLWq19pNmX53l+f4wk\nS5Fs2Y6s0fJ5ncPxPPt3xMnMZ77L5+PxMDY2hm3bJBIJ+voK0xtaW1t585vfzJve9CbGxsZ44IEH\nXvHz14OiBIz2ywJGPa40lJwAACAASURBVF2Ywa/Ky3AHziXw1lIxwj6HybRGahUufikLW0xEs5SU\nmMRikqxZrG2DAxqDA37Aj67X8FuvHcPv6cHJx1CaB3Dn5ZNcCYZVRipbjccYwslHUWYViVQlZ8+W\n0Nw0hGZLlR1xZSwSxwBgOVPUpJ+jhkItsoS3GsuOYbrJQmUbAA1GfTtJa0G6nKYVavHqpWkaH/vY\nx3jve9+L67oEAgE+/elPMzg4uOj5n/jEJ/joRz+KpmlUVlZy9913881vfnPJ5zz44IM88cQTs9tz\nez0//vGP89GPfhS/349pmlRXV1NZWcmNN97I7//+79PY2EhTU+H/qz/7sz/jYx/7GP/+7/9OPB5f\n9hXfa9WK52H82y/9jJtqx/nNo6HZfTfHf401cgZnczPasZPzzh+6/vc560YYHV/ZL6oL8fkMcnmH\nG8Yf4VTrbbSd/C+Ot/42iTQkk3kZPhfrSmOzTX+fRm2dw47tQ+hO1xV4igY4KM2DrWoZnyjn9Ckv\nw0OFH5d+v4vSIBGf+y3ucstvTRHynyTv1OC4BibHUUYFqUwVeVsn6DkC7sLRCc0oI5OvwjRiaGRx\nsVAkcAgxFS9naspDY+0xnPzkFXivYqNZKjWNuPK+/e1vc8cddxCJRPjHf/xHTNOUQPASFaGH0cV2\n5v900+ITaKEScqbOy6tMl4x1M1ZRtnINfBmlCr2iM9qrXDQyBDITWEdP0xH9Nlomxfb49xjb8Tqc\nMoOXxl6e3kSItaunu7BIrfeMTu+ZWlraqtix9TQAObsEQ0/juDq6OwjKIGvXYum9uHYaZVQRS1YT\n8E2h7DOAi9KD5JxahobLMA2HeNLg5AmDmhqX/j5tzmrucxZbuAOKX/+qFDiXFNnrqySdOneurr+a\nts15ysqypFI6huFy6qSH6MTMOdXnfd8nju/mNa/pl1rhQqwD5eXl/Mmf/Al+v5+SkhLuv//+Yjdp\nzVnxHsZ7vvhTXl01xVNPFIIqpeC1Xd9Aa6gjXR7E8/yxeec7Hh+nr7mL7qHirFzbFYlxOBpCNzQ8\nlsY1x76LXVqJNXR60fNzFfX0dLye4bhGMinzLsXG4fW503lTFeUVLrkcTE2eC97aOvLksoqebg04\nz3jfKnTNdSmqK89CvrfYTRFrlPQwivWg6HkYLUtHuS75gBdbf3n/ImiZFJHUWbqpWslmAlBVblG1\n//+hXfsWRo1K6iePoqfj6Onz17k2R/uoDR2gPp9jf/BV5LKSokFsDHN79sZGFwaEJztX/ONmWTz7\ntA9opqKqmaamDJpyGR21CJXmCQazRELdOPmNk7xXCLExFWeVtHvuy8SyCkFi1m9i64v3OgR7DmFW\nvX7R4CsYNInHL33BiddnkL7AymulYPPZQiLYimd+SLBpJ94zL13UvX2nCiuw9u6s5IDeii2lBoRY\n4xSjwzA67J2zTwc8KLWTqmoX04Q9u7vBHgR38epVQgixVi3s0rvCHBTunOEoj1l4nfIa5I3Fm2OO\n9uGxFtbcBWjwnb+373wMU2OLd+SC5zRXKrxnDs9uX2ywOFfw2JPsDI1f8nVCiLXDdRVDZzX6ejV+\n8pNWnnjmBly9BVtrJ2XvRGkelFkFau5nmIZmhIvWZiGEuFQrP0bkuvOGpE2t0PuW9Ck82fP3xFnm\nwt5HXVdE+l4Az/WX1ITmMptgfxeY1y56XDc0Go///JLuuRiVz1J6+gCEX7dg8YwQYn2aGNP46U/n\nliwrfD4Zhktjs4NlOZw+aZDJKK65LsWmyuM4hMAeAHfpKSxKD2K7VSRSJZQGTuPkJamwEOLKK06l\nlzlD0qZW+ICMWS76BUZxyswsL++rqywzMM/0UrLtpgV5EE1TI5db/MO35swTmGP9UD8/YPR4dDIZ\nm/ZIBuPYwEW/pwsxR/vYvjlNWvNxamjxiFHTFY4MWwuxruXzilNdOoWh7ILC/MirAGhsbqK9PYqh\n5xkbL2V42CRY4uD35dF1F8dR9JzxzKYaAvD69tDSmqet+SSuPTobcCrdh6sq0EjguilcexUmshVX\nxHt++tyy3u8rd+5b8pze3l4+/elPE41GyeVybN26lQ9/+MMEg0EGBgY4duwYt956K+9617u45557\nZqu4XI7Pfe5zVFRUcNddd132PcTlKcIcRoU9Z0japBAlTpp5AlnzvNeVT3RxkvZ5ZQIjTKGn4zRb\nY3T5IvOqwbSU5egcXjiMXVNh4nnqBHBu/uNMwLbdM8gxrZaaF3+0LO91xqYnv8fk7tdxivoFxwxD\n4xrnJQ4F9pBMSPJvITaqnm6dnu7yl+3VgfN/LqZTiqOHTY4e3kp5hUtrW4r+Pi8D/YqZleglJS6v\nvnEIwz2B0gO49qVP4xHifNLpNO973/u499572bNnDwD/8R//wYc+9CH+5V/+haeeeopTp05x6623\nFrml4pUq+ipp0y0ESZNGnkr9/B+MwRNPY7R3EA4Zs0m8Q+PdhWNjZ2is8tGZNvF4DQJejdKpEyjV\nhFIKy6PPLnCpT55Lh9NmDnOQMraWpejNlBA++F/s3HYTRmz55x0Gu55Gq2/AtHQqSqB/pNCevVY3\ngUNPc23paV5oeyuTU6snQbkQYu0YG1WMjfoX7I/FFP/58xosTzXZjKJjS46KygyxKYvScIaKsn7s\nfB4nP/dzT1EYD5qzRw8UeiqVQiljuuqPjIxsdL/61a+49tprZ4NFgLe+9a1897vfpaenhy9/+cuk\n02n27t0LwOc//3lGR0dJpVJ89rOfpaGhgc985jM888wzuK7L3XffzR133MG73vUuysrKmJqa4l//\n9V/R9cXXMcz41re+xUMPPYRSijvvvJN3v/vddHZ2cv/99+M4DlNTU/zv//2/2bdvHw888ADf/va3\nKS0txTRN7rzzTgBOnTrFhz/8YTKZDHfccQe//OUvOX78OPfeey8A4XCY++67j1wuxwc+8AFc1yWX\ny/GJT3yCLVu2XKG/8Oqx4gGj47rzVkkb06XGJvQsOc17vstQ+SxVZToahSEXTVP4zhwCwIyNUqY6\nqYzsxavbhJwonqkh6uvbcFyFAwymwOs1CB359ew9K575IbU3vIfKl36EteVGNDtP6KVfLf+bBvTk\nFFURg+boS+h9Uai/kbAbI/TULwt/h8kRrjrzEMc2/w+iMZtMRlZZCiGWTzZT+NztPG7SeXzmx7kF\nbAWgoclmZFijtNRlclJhGBAOu4yOKgIBl7FRDV13sTyQTsGmOodg0KWsLENV5AxOfrQ4b0wUVW9v\nL42NjQv219fXMzg4yHvf+15OnTrFbbfdxte//nVe85rX8Ja3vIXPfe5z/PznP6ejo4O+vj6+973v\nkclkeNvb3saNN94IwJve9CZuv/32JdvQ1dXFT3/6U77zne+glOLuu+/mpptuoquri4985CNs2bKF\nH//4x/zgBz+gubmZr371qzz44INYlsW73/3uC977b/7mb7jvvvtob2/ngQce4Ktf/Sp79+6lpKSE\n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\nx+jbty/PPPNM/Na0iIiIiLQfjd6SHjlyJHv27GHy5MkYY1iyZAmvvPIKeXl5OI7DW2+9RTgc5o03\n3gDgiSeeYNCgQc3ecBERERFpGZqHUUREpBm99sI9rd0Ekc9NX+ESEREREVcKjCIiIiLiSoFRRERE\nRFwpMIqIiIiIKwVGEREREXGlwCgiIiIirhQYRURERMSVAqOIiIiIuFJgFBERERFXCowiIiIi4kqB\nUURERERcKTCKiIiIiCsFRhERERFxpcAoIiIiIq4UGEVERETElQKjiIiIiLhSYBQRERERVwqMIiIi\nIuJKgVFEREREXCkwioiIiIgrBUYRERERcaXAKCIiIiKuFBhFRERExJUCo4iIiIi4UmAUEREREVcK\njCIiIiLiSoFRRERERFwpMIqIiIiIKwVGEREREXGlwCgiIiIirhQYRURERMSVAqOIiIiIuFJgFBER\nERFXCowiIiIi4kqBUURERERcKTCKiIiIiCsFRhERERFxpcAoIiIiIq4UGEVERETElQKjiIiIiLhS\nYBQRERERVwqMIiIiIuJKgVFEREREXCkwioiIiIgrBUYRERERcaXAKCIiIiKuFBhFRERExJUCo4iI\niIi4UmAUEREREVcKjCIiIiLiSoFRRERERFwpMIqIiIiIq0YDo+M4PP3000yaNImCggJOnjzZYPuG\nDRuYMGECEydO5G9/+1uzNVREREREWoevsR127NhBOBxm/fr17N+/n2effZbVq1cDcP78edauXcum\nTZsIhUJMnTqVO+64A9u2m73hIiIiItIyGg2M+/btY9iwYQAMHDiQoqKi+LYDBw4waNAgbNvGtm3y\n8vI4fPgwAwYM+NTj9ezmp6o61ARNl0/jS/AQjTit3Yx2TTVuGapz81ONReRqNBoYA4EAaWlp8cde\nr5doNIrP5yMQCJCenh7flpqaSiAQcD3e/zx6x+doroiIiIi0tEbHMKalpREMBuOPHcfB5/NdcVsw\nGGwQIEVERETk+tdoYBw8eDC7du0CYP/+/fTp0ye+bcCAAezbt49QKER1dTUffPBBg+0iIiIicv2z\njDHGbQfHcVi8eDHvvfcexhiWLFnCrl27yMvL4xvf+AYbNmxg/fr1GGOYNm0ao0aNaqm2i4iIiEgL\naDQwioiIiMgXmybuFhERERFXCowiIiIi4qrRaXWawuVxkEeOHMG2bQoLC+nRo0dLnLpdikQizJ8/\n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\nXP0/rYyKlz/cN48AAAAASUVORK5CYII=\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x29e64a0f358>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "top=1000\n",
    "fifa_top = fifa.head(top)\n",
    "\n",
    "top_vec=[None]*(len(leagues))\n",
    "for L in range(len(leagues)):\n",
    "    top_vec[L] = [((fifa_top.Rank<=x+1) & (fifa_top.league==leagues[L])).sum() for x in range(top)]\n",
    "#need to calculate the 'other' league\n",
    "other = [None]*top\n",
    "top_vec_numpy = np.array(top_vec)\n",
    "for r in range(top):\n",
    "    other[r] = r-np.sum(top_vec_numpy[:,r])+1\n",
    "\n",
    "#now let's make the data frame\n",
    "top_df = pd.DataFrame({leagues[0]:top_vec[0],\n",
    "                     leagues[1]:top_vec[1],\n",
    "                     leagues[2]:top_vec[2],\n",
    "                     leagues[3]:top_vec[3],\n",
    "                     leagues[4]:top_vec[4],\n",
    "                     'Other Leagues':other}, index=range(1,top+1))\n",
    "\n",
    "top_df_perc = top_df.divide(top_df.sum(axis=1), axis=0)\n",
    "plt.stackplot(range(1,top+1), top_df_perc[leagues[0]], top_df_perc[leagues[1]],\n",
    "              top_df_perc[leagues[2]], top_df_perc[leagues[3]],\n",
    "              top_df_perc[leagues[4]], top_df_perc['Other Leagues'],\n",
    "              labels=[*leagues, 'Other Leagues'])\n",
    "plt.legend(bbox_to_anchor=(1.04,1), loc=\"upper left\")\n",
    "plt.margins(0,0)\n",
    "plt.title('Player Ranking Stacked Chart per League')\n",
    "plt.xlabel('Player Ranking')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "English Premier League      0.205\n",
       "French Ligue 1              0.077\n",
       "German Bundesliga           0.139\n",
       "Italian Serie A             0.137\n",
       "Other Leagues               0.241\n",
       "Spanish Primera División    0.201\n",
       "Name: 1000, dtype: float64"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#top-1000\n",
    "top_df_perc.iloc[-1]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "These figures clearly demonstrate that the English and Spanish leagues are ahead of their competitors. Almost every starting player in these two leagues are ranked in the top 1000."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# England vs. Germany PKs <a name=\"PKs\"></a>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "When it comes to Penalty Kicks in international competitions, two teams clearly stand out from the norm: England and Germany. England has a woeful history with PKs, losing all 3 in World Cup competitions, and winning only 1 out of 7 including the European Cup. Their relentless choking during PKs is well documented ([1](https://www.theguardian.com/football/2016/jun/27/england-penalties-20-years-hurt-iceland-germany), [2](https://www.telegraph.co.uk/men/the-filter/10843004/Why-are-England-so-bad-at-penalty-shoot-outs.html), [3](http://blogs.bcu.ac.uk/views/2016/06/15/why-are-england-so-bad-at-penalty-shootouts/), [4](https://www.ft.com/content/f32c2ac6-ec4a-11e3-ab1b-00144feabdc0)) and may be adding to the continuing pressure in a [feedback loop](http://www.popularsocialscience.com/2012/11/28/the-psychology-of-penalty-shootouts-why-do-england-always-lose/). At the opposite end of the spectrum, the German team is legendary for their calm demeanor in expertly executing PKs, winning [all 4](https://en.wikipedia.org/wiki/List_of_FIFA_World_Cup_penalty_shoot-outs) of their PKs during World Cups. In fact, their last PK loss (in the WC or Euro) dates back more than 42 years, at the Euro 1976. There are very few things in international soccer as sure bets as England losing a PK and Germany winning.\n",
    "\n",
    "FIFA 18 includes a **Penalty** stat that describes how good a player is at taking a penalty kick. Let's investigate the differences between England and Germany."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x29e6496a438>"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\nAAAASUVORK5CYII=\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x29e62c1e6d8>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "countries = ['England', 'Germany']\n",
    "fifa_pen = fifa.loc[fifa.nationality.isin(countries)]\n",
    "sns.violinplot(x='nationality', y='penalties',  data=fifa_pen, inner='quartile')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This plot is surprising, it seems that English players have the slight edge over German player in the penalties stat. Let's break this down by position; it could be that players who are unlikely to take PKs in the first place are bringing down the German distribution."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x29e64b3a5f8>"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAfIAAAFXCAYAAABZQMyNAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz\nAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMS4wLCBo\ndHRwOi8vbWF0cGxvdGxpYi5vcmcvpW3flQAAIABJREFUeJzsnXd4HNXVxt9p21ddsiV3425TbVzA\nMRgbDAECppcQHBsIBEJMC+AQAwktQBzAJNjJhyFu9ACGuODeLbnIsi1ZtnrvWmmLts98f4x21aXV\namZ2V7q/59HzrHZn7xyNdufce+4576EEQRBAIBAIBAIhIqFDbQCBQCAQCITgIY6cQCAQCIQIhjhy\nAoFAIBAiGOLICQQCgUCIYIgjJxAIBAIhgiGOnEAgEAiECIYNtQHBUFNjCbUJBAKBQCAoRmKiscvX\nyIqcQCAQCIQIhjhyAoFAIBAiGFkdeUZGBh544AEAQFFREe69917cd999ePnll8HzPADgww8/xB13\n3IF77rkHp06dktMcAoFAIBD6HbI58n//+9946aWX4HQ6AQBvvvkmli5dio0bN0IQBOzcuROZmZlI\nS0vDV199hRUrVuDVV1+VyxwCgUAgEPolsjny4cOHY+XKlf7fMzMzMX36dADAnDlzcOjQIRw/fhyz\nZ88GRVFISUmB1+tFfX29XCYRCAQCgdDvkC1rfcGCBSgtLfX/LggCKIoCAOj1elgsFlitVsTExPiP\n8T0fFxfX7dixsTqwLCOP4QQCgUAgRBCKlZ/RdMvi32azISoqCgaDATabrc3zRmPXKfY+TKYmWWwk\nEAgEAiEcCYvys0mTJiE1NRUAsG/fPkybNg2XXXYZDhw4AJ7nUV5eDp7ne1yNEwgEAoFAaEGxFfnz\nzz+PP/3pT1ixYgVGjx6NBQsWgGEYTJs2DXfffTd4nsfy5cuVModAIBAI/ZA9e3Zi6tTpqKwsx/Hj\nR3HPPb/s03gff7waI0aMhMFghNlsxlVXzcXevbtw3XU3SGRx36EEQRBCbURvIcpuBAKBQOiMJ554\nBK+++gbi4xMkGc/nyOfPXwAAqKgoxzvvvIkVK1b28E5p6S60HpESrQQCgUAYWGze/AMOHz4Im82G\nuroa/PGPr2DLlv+hsDAfjY0NuO22u5CcnILc3PN4440/4/77f4WdO3/Cs8++iL/97a/Iy8sBIODx\nx5/ClCkX4oEH7sIFF4xFUVEBrrrqGixa9BDS0o5g/fpP4fV6YTQa8frr77Q5f11dHerqanD2bCa+\n+eZLfPfd11izZgM4jsPy5S9i8eJHMHLkKMWvDVF2IxAIBEJEwDAMVqxYifvvX4TNm3/E8OEj8Pe/\n/wNvv/0+vvvuG0ydejnGjBmHZctatmkPHtwHQeDx0UcfY/ny1/Dee6Jzrqgox9NPP4/Vqz/Fpk3f\nAgBKSorw1lt/wz/+8W+4XG4UFRV2sOHuu+/HxImTcfvtd2HGjCuQmnoITU021NXVhsSJA2RFTiCE\nJRkZ6diw4VM8++wyJCUNCrU5BEJYcMEFYwAACQkJaGqyoaSkCK+99jK0Wh08Hk+n7ykqKsTkyRcC\nAJKTU2CzWQEAiYlJiIqKAgBoNBoAQGxsPN5++w1oNBpUV1fB6+18TB/XX38j1q1bA4vFgquvnifJ\n3xgMZEVOIIQh69atQW1tDfbs2RlqUwiEMILyPzpz5hRcLhdeeulVzJ+/AL50L4qi0Dr1a9iwEcjK\nygQgrsLVao3/uPZ8+OHf8dJLr+Lpp58HRQGdpZCJ44sS42PGjEV1dTV2796B+fOvk+7P7CVkRU4g\nhCF2u6iV4PV6Q2wJgRCeXHzxZcjKOoNHH12MmJgYCAIPnucxadIULF/+Ih566FEAwM9+dhVSUw/h\nsceWwOPx4I9/fLnLMWfPnoMlSx6ATqdDdHQM6upqOxwTExOL+vp6fPHFBtx99/2YM2cu0tOPIzY2\ndKXTJGudQAhDfve7h2Gz2TBv3nW4//5FoTaHQCB0wcaN65CcnIy5c+fLep6wEIQhEAiBQ9OiBLGv\nSyCBQAg/3nvvHZw6lY45c+aG1A4SWicQwhCfpDEJrRMIymM2m/2JcN2xdOlzCljTM2RFTiCEIQwj\nrsiJIycQlOXkyeNYuvRRHDiwN9SmBAxx5ARCGEIcOYEQGvbvFx349u1bQ2xJ4BBHTiCEIcSRB47T\n6ei0TIhACAbfd46mO5anhSvEkRMIYQjLiukrxJF3j93ehKVLf4v16z8JtSmEfoJPBIZluRBbEjgk\n2Y1ACEN8K/Ku1KoIIvX19XA6Hdi9ewceeGBxqM0hBMBLf3oRDY0Nko0XEx2D1/7yZo/HlZWV4qOP\nPkB1dTU0Gg3UajUee+xJjB59QZvjfN8532Q6EogcSwmEAUTLipw48u6IpPAnQaShsQHMMOlagDaU\nbOnxGIfDgRdeeBrPP/8Spky5CACQlXUGK1b8FR9++K82x7rdbgAAx5EVOYFA6AMMQ0LrgeAr0yMQ\nuuPgwX2YOvVyvxMHgEmTpmDlytWoqqrE22+/AZfLCZVKDYah4Xa7sXPnduTn52PWrCtx+PBBjBkz\nDgUFedBqtbjookuRlnYYVqsVK1Z8CIah8dZbr8FqtaCxsQE337wQCxfegSeeeARjx45Hfn4empqs\n+Mtf/orU1MMoLS3B44//Hl6vF7/+9X34v/9bB5VKFfTfR74FBEIYQkLrgUFR5BZG6Jny8nIMGTLM\n//sLLzyNJ554BPfddzveeONV3HHH3Vi5cjXuvfeXyMk5B0Bcxf/97//A/fc/CACYNGky3n//I7hc\nbmg0Grz33j8xcuQonDx5AqWlpZg//7rmTmzv4YsvNvjPNXHiZLz//j8xbdoMbN++DddeuwD79++B\n1+tFauphXHbZtD45cYCsyAmEsISE1gPDN+EhELpj0KBByM7O8v/+1lsrAACPPLIIZ86cwrp1n2DD\nhv8AAJxOJwwGA6KiotqE18eNmwAAMBoN/nalRmMUXC4n4uPj8eWXG7F3727odPo2E/Bx48b7bair\nq4NOp8cll1yGtLTD2Lx5ExYterjPfx+ZzhIIYYgvtO7xkNB6d5DQOiEQZs++CseOpeHMmdP+50pL\nS1BTU41Jk6bgscd+hw8//Beee24ZjEZR0c0nk+yjs25pPj77bB2mTLkIy5f/BddcM79NOWRn77v5\n5oX44YfvYTKZMGbM2L7+eWRFTiCEIy115GRF3j0k2Y3QMzqdDn/969+xatVKrFpVB6/XA4Zh8Yc/\nLMPw4SPxt7+9BZfLBafT4U+g7E0i5ZVXzsG7776Jn37agujoaDAMA5fL1eXxkydPQVlZCRYuvLPP\nfxtAHDmBEJYQQRhCfyUmOiagTPPejBcIyckpePXVzsvUVqz40P948eL7AAD33fcr/3OtM9tbj/H7\n3z/jf7xx4zcdxm39vltvvcP/mOd5aDRaXHvtgoBs7wniyAmEMIQ4ckJ/JZCa73CgtrZGlnHLy8uw\nbNlzuOWW26DXGyQZk2wwEQhhiG/vl7QxJRBCw9GjqbKMm5IyBJ9+uhELF97R88EBQhw5gRCGEEdO\nkJq0tMPYtOm/oTYjYnA47KE2IWBIaJ1ACEN8jpw0AyFIxapVKwEACxb8HGq1JsTWhCetJ86RNIkm\nK3ICIQzxlaxE0s2EEBmYTKZQmxC22O1N/seR9N0jjpxACEN8imWCEDk3E0Jk0NAgXcOS/obNZgu1\nCUFBQusEQhjiq2ElkXWC1Hg87pCe/6VX/iDpZCImJgavvfJ2t8ecOHEMy5e/6FdkE98Xi9de+2ub\n47pz5B9/vBrx8fFtysh6y8svv4hbbrkdl102LegxOoM4cgIhLPE5crIiJ0hLqB15Q0MDtPOTpBtv\nR3VAx02dOq3LOnIfNptVCpMUhzhyAiEM6UYNkkDoEy5XaB15ONG+O9ltt90FAKirq4PVasXTTz8B\nh8OBhx561P8er9eLd955A9XVVWhsbMTMmVfg4Ycfw+uvvwKO41BZWYG6ulosW/YKxo+fgG+++RI/\n/vgd4uMTZMtPII6cQCAQ+jmtm3i4XM4QWhI6jh8/hieeeMT/+xVXzAYgdif7/e+fwerV/0Bq6mE4\nnU7YbDYMHz4cb775Ln71q3vajFNdXYXJky/ECy/8CU6nE7fd9nM8/PBjAIDBg5Pxhz/8EZs2fYtN\nm/6Lxx57El999TnWrv0cNE1jyZJfyvK3EUdOIIQxZI+cIAUOh8P/2OkcmI68s9D6oUMH2nQny8vL\ngdPphEajAUVRUKs1mDBhYpv3REVF4ezZTJw4cQx6vb5NhGPsWHGspKRBOH06A0VFhRg1arS/TenE\niZNl+dtI1jqBEJaQ2DpBOlqLmzidjm6OHHi07k7mcrmgVqvhcDggCAJcLhfOnz/X5vjNm3+EwWDE\nyy+/hnvu+SWcTodf76F9p7OUlCEoLMyH0+mA1+vtMJZUkBU5gRDWkCU5oe+0XpG3fjyQaB9aBzpG\nJ9xu0ZHr9XoUFxdj2bJnwbIsWLbFVU6dejleeWUZTp06CY1Gg6FDh3Wpyx4bG4uHHnoUjz66GDEx\nsdBqtdL/YSCOnKAwHo8HNE2TPtI90F3vY0LnCIJArlsXtF6RtxY9CQUxMTEBZ5oHOl5PXHbZNPz4\n4/Zuj7n11jtQWJiPEyeOgWEYjBgxAm+88S4eeOAuJCUNxpIlv/Efu3btFx3e/8c/vuJ/PHPmFZg5\n8woAwLx512HevOsC/GuCgzhygqK88soyxMbG4plnXgy1KYR+htfrbbNyIrTQ2pE3NYXWkfdU8x1K\nrFYrGIaBw+FAUVERfvvbh3DTTbdi8ODBoTatW8innqAo5eWlKC8vDbUZYQ/RWA+MsrKWzxJx5F3T\n1NR6RR45zUCUxmazgqIov+NeseJDREVFhdiqniHxTQIhrCGh4u4oKyv2Pw610Ek4E06h9XDGarW0\n+T1SBGKIIycQwpBIaqEYShyOlmQlInTSNa2dd1NTZOqJyw3P8x22HYgjJxDaQcLFgZOVdRoAwPPe\nEFsS3rQupRqoQieB0DqcHuo98nDF4bB3uEdZrcSREwht8HqJUwqU+vp6AGTy0xOtndJALasKBBJa\n7xn/Z4li/M9ZLOYQWdM7iCMnKAZx5MFA9si7o6mpZcVEtiO6htSR94x/y4FuceTt98zDFeLICYpB\nHHnvIXXR3WM2t6yYImU/MxS0dt48z5NITyf4th8oivM/R1bkBEI7SFZx7yF+vHsaG1v6WnfXS3qg\n016W1eVyhciS8MXvyFuJVbWeKIYzxJETFKN1ByZCYFAU+Yp2h8lU739MVuRd016KdKA2TukO/2SH\natEiII6cQGiH201W5L2FSNl2jdfrbbOytFgiYz8zFLTfFyfRsY74JzdtVuQNXRwdXpC7BEExiCPv\nPTRNYutd0b5RBXHkXdM+tE6iYx1xu32Twha32NBAHDmB0IaWLwohUEhovWvaS/1aLI0hsiT8sbfL\n6BcEPkSWhC9utzi5af2ds1jMETHpIXcJgmKQBJveQ0LrXVNSUtzm90jZzwwFDnvbFTnPk6z19vgj\nhq0cuSAIaGgwhciiwFG0w4Db7cYLL7yAsrIy0DSNv/zlL2BZFi+88AIoisLYsWPx8ssvk5tXP4Ws\nyHsPKT/rmqKigja/m81kRd4ZPM93CK2Te2xH/HkDPkdOUwAvoK6uFgkJiaEzLAAU/W/u3bsXHo8H\nn3/+OR5//HG89957ePPNN7F06VJs3LgRgiBg586dSppEUBCyIu89xJF3jiAIKCjIb/Oc2Wwm9dGd\n0Jn0KHHkHfGF0H3fOUYvrnNraqTrnS4Xiv43R40aBa/XC57nYbVawbIsMjMzMX36dADAnDlzcOjQ\nISVNIigIaWoRGK1vusSRd47JVI+GBhModaz/ObfbRVTLOqGz+nqW5To5cmDTkowrukXaIF6jysqK\nEFkUOIqG1nU6HcrKynDDDTfAZDJh1apVOHr0qP9mpdfrA8o8jY3VgWWZHo8jhBcaTcu8MTHRGEJL\nwpvW+uEcx5Jr1QnZ2ScBAIwmFh5nyx4mx3nJ9WpHQ0Nlh+cGD45BVBS5Tq3xt7JvDq0zRg7uCqCm\npiLsP1OKOvJPP/0Us2fPxjPPPIOKigo8+OCDbUqSbDZbQE3cTSYi+h+J1NW1JCPV1JBSoa6oq6v1\nP/Z6eXKtOuHEiQwAAKONg6exJcReWFgOljWEyqywpLi4oyO3Wt1wOsnnqjWNjc2CQs2OnFYzoLUs\nzp/PCYvvYHeTCUVD61FRUTAaRWOio6Ph8XgwadIkpKamAgD27duHadOmKWkSQUFIsltgEIWynsnN\nzQEoGrQ6ps3zjY0k4a09rWVsfZDQekdaJFpb1rdsrAqNjQ0dNAvCDUUd+aJFi5CZmYn77rsPDz74\nIJ566iksX74cK1euxN133w23240FCxYoaRJBQUiyW2BESg/kUOF0OlBcXAhaE9umVAiIHCUuJWnv\nyCmKIrkXndBZ9zM2QQsAyM7OCoVJAaNoaF2v1+P999/v8Pz69euVNIMQIoiyW2C0bp1IsrA7UlhY\nAJ7nwWkT/M9RGgaCwxsxSlxK4tejp2hA4KFSqUJrUJjS2NgAitGAatU6mEsSHXlGRjpmz74qVKb1\nCKlBICgGceSB0VrYhOeJAld78vNzAQCMNt7/HK0R1yStm6gQROrr68QHlLjSVKs1IbQmPBEEASZT\nPSi27bVhjBxoA4fTZzI61OKHE8SRExSDOPLAaC1sQlbkHSkqKgQAMJo4/3O0VnRS4b6XGQrq6mpB\n0Zx/G4KsyDvS2NgAl8sFWtU2UZKiKKiH6uFyOnHixLEQWdczxJETFMPnyMn+XPe0duSRoPOsNCUl\nRaBoDhSn9z9HMRRoDUMceTsEQUBtbQ0oTud/jmUV3VGNCCoqygEAtKpj1ZR6uJigvW/fbkVt6g3E\nkRMUw+MRk93IiqB7Wms7e73EkbfG4/GgqqoSlDq6w4SQ1nOoq6sl1RGtsFotcDgcoLmWlSZx5B0p\nLBRLGGlNbIfXGAMHLlGLc+fOoqystMPr4QBx5ATF8Cm7kdKX7mntyMl2RFtqaqrA8zxoVceaWiaK\ngyAIqKgIfyUupaiuFuVFqVYhY9JRryO5uTkARF2CzlCPFlfqO3duU8ym3kD+owTF8K2UyIqge+rq\n6vyPiSNvi0/3uv1eJgAwUWKkp7S0uMNrAxX/9Wq1DUFamLaF53mcO3cWFKdvc51ao0rRgdaxOHhw\nX5uqknCBOHKCYvicksVC2k12hdPpJIIw3WAyidEKmtV1eI2NVQNAh2YqA5mamioAbSc+JO+iLXl5\nOWhqsoHVD+ryGIqioBkTDbfbjT17wq+xF3HkBMVwOp0ASElVd9TX1/Z80ADGJ27SvkwIANhoFUBT\nyM/PUdqssKWmRkz+a71HThrLtCU9XcxGZw1Duj1OPcIIiqWxa9d2eL1eJUwLGOLICYrhcjlDbULY\nU1tLHHl3+Dp5UYy6w2sUQ4ONUaGoqBB2O+nHAAC1tc175K1Cxq2b8gx0eJ5HWtoRUDQHRj+422Np\njoZquAENDSacPHlcIQsDgzhygmL4tIwJXePvfUy3JASSffIW/HrYTOcJk1yitnnPM1tJs8KW2toa\nUKwWVCvZUZfLScLrzeTknEN9fR0Y49A216grNKPEpLf9+/fKbVqvII6coBjEkfdMdbXYqYpiWkr0\nSE5BC/6oDtV5wqRPUvPMmQylTApbeJ5vVivrmE9AFPBEDh7cBwDgokcGdDwbrQITo8aZMxlt9B5C\nDXHkBEXgeR4OB3HkPVFZ6XPkLaHjzrpXDVR8lQ9drZ7YeA0ojkbGqfQBr4rX2NgIr9cLmuvoyH0C\nKAMZu90uhtU5PRhdUsDvUw/Tg+d5pKeHT3idOHKCIjQ1NQ34G2sgVFSUi06canFUrevKBzpud3NI\nuItaaIqmwA3Soq62FqWlJQpaFn6YTGIZI9WJIy8pKVLanLDj6NEjcLmc4KJH9UptUpUi5hv4kuTC\nAeLICYpgsbQNQxGn3hGXy4Xa2uoOMpH+pheEFqW7bkRNVMnijfbEiaNKmBS2+MLnNKvt8FpeHsns\nP3BA3OfmYkb16n2MngNj5HD2bGbYtGYmjpygCI2NbR15uJVvhAMVFWUQBAG0JrrN860FYgY6YuIf\n1a06GTdYB9DUgHfkvkgO1c6RU2oG586dHdAJb1VVlcjNPQ9GP6hLEZju4Abp4Ha7kZt7Xgbreg9x\n5ARFaL+qJHrYHSkuFsOdtDqmzfP+THYCXC5Xj9nFNEeDS9KipKQYVVWVClkWfvjEcyiurSNXDdLC\nbrcjJ+dcKMwKC44cOQgg8CS39viSKrOyzkhlUp8gjpygCO1XlaSkqiM+R860a9zgU+ciQEyYpHvW\n6lcNEVdZx46lyW1S2NISWm+7R84lD+xrIwgCUlMPARQD1jA0qDG4BA1AU8jMPC2xdcFBHDlBEdo7\no3DZWwonCgvzAYoCrW4bWq+srCBqeM3YbFaxt3YPqJJ1AAUcO5aqgFXhic+Rtw+tc4ka0GoGaWmH\nB2R4vby8DJWVFWANyV3qEfQExdJg49QoLi7ssG0YCogjJyhCdXUVgJbMUBJab4vb7UZRUQFodQwo\nuqVGmlIzcLlcJOEN4jWy2WydyrO2h1Yx4BK1KCoqGLBbE52JwQBiZr9qmAE2m3VArsr9kqzG4Fbj\nPlTJOgiCgIyME1KY1SeIIycoQnl5WZukEp/uOkGkuLgQHo8HjDa+zfNsc0evcO2DrCS+yUxn5VSd\n4QuvHz8+8JLePB4P6uvr20iztkbT3JZzx46tA66CJCMjHQAF1pDcp3F81RFHjx6RwKq+QRw5QXbM\n5kZYrRZQ6payKuLI23L+vCgpymgT2zzPxIiO3Ld/PpDxiZh01ou8M1Qp+gEbXq+rqwHPeztt9woA\njIEDN1iH/Pxc/2dvIGCzWZGfnwtaG9+pXn9vYAwc2Dg1srLOhDxiRhw5QXZKSsT+0EyrbGziyNty\n7txZAACja+vI2WifIy9Q3KZww9dnvH0OQVfQagZsggb5+bkhv9EqjS+C016ToDXaCeL38fvvvxkw\nq/Ls7LMQBAFsDw1SAkU9wghBEELe2pQ4coLs+Bw5rWlx5KSVYgsejwfZ2WdBq6I6yGnSWha0hkFe\nXm6IrAsf8vPFa8Bo4ns4sgV1ik8cJnxUuJTAP3nWxHR5DBenATdIi+zsLGRmnlLKtJDiKxdjuuk9\n3hvUwwygVAx2794R0nsaceQE2SkuLgTQtqyK6K63kJeXA5fL2eXNhY1To6HBNOBWla3xTXYoTg+a\n66hU1hU+Oc3jxwdWUpdv4kdr4ro9TjdFfP2LLzYMCJGms2fPgKLZDrkowUKxNDSjjbDZrNi9e7sk\nYwYDceQE2SkuLgRFs6C4lv060i+6hVOnTgJAl8k3bLyYpe0Lvw9E8vJy4HDYwep7l6BEa1mw8Wqc\nP58dFmVCSsDzPPLyckBxBtA9ZPiz0WqoRxhRVlaKXbt+UsjC0FBbW4PKygrQuqRulQF7i2ZMNCiO\nxubNm9DUZJNs3N5AHDlBVpxOByoqykGrY9s0JiAtTVvIyEgHKKbLDkxcgrgCPXs2S0mzwgpfwhpr\nHNLr96qGGCAIwoBZlRcW5sNubwKrD6yjl25KHCgVjf9++1W/jvqcPi22tpVqf9wHrWKgHRcDm82G\nH3/8TtKxA7YhJGclDBhKSoqb9cPbqpWFauYablRVVaC8vBSMflCb+vHWMDEqUByNrKzTAyYpqTUe\njwepaYdBMeqg9jZ9ZWipqYekNi0s8UV4mAAdFq1moJsSB6fDgbVrP+63nzFf29FgJoM9oRkTBVrH\n4qeftoSkVJQ4coKs+NoltpcdtdmIIwdakrC4bsQpKEpszVlfX4fy8jKlTAsbTpw4BqvFAjZ6ZFAh\nUUbLgk3QICfnHGpra2SwMLxITz8GUHSvtiHUI4zgkrQ4deok9u/fI59xIcJsNiMr6wxoTWxQTVJ6\ngmJo6C+OB8/zWLv2Y8WVGIkjJ8iKvxFIu+xZ4shFjh5NBSgKrKH7VYJqkJjNfupUuhJmhQ2CIGD7\n9i0AAFXMBUGPox4u5mf4mmX0V8rLy1BSUgxGP7hX8qMURUF/WSIojsbGz9aiqqpCRiuVJy3tMHje\nCy5qpGznUCXroUrRISfnHHbtUjbxjThygqyUlpYAoDrUs9ps1tAYFEZUV1ehsDAfjG4QKLZ7cQqu\n2ZGLqlQDh5ycc8jLywFjSAGt7romuidUQwygGAr79+/p17r1hw/vBwBwUSN6/V5Gx0J/SQJcTic+\nWrWy38goC4IgOlaKBhvd++vSG/SXJIBSMfjyq42KhtiJIyfIhiAIKCsrBa0ydtB7tlqJI09NPQwA\n4KKG93gsrWHAxquRk3MOZrNZbtPChu+++xoAoI6f1KdxaI6GaogeNTXVOHs2UwrTwg6Px4P9+/eC\nYlRB7wOrhxmgHmFEcVEhPvtsncQWhobTp0+isrIcrHFYj1n8fYXWsNBfmgCP241Vqz5QTPiKOHKC\nbDQ2NsDhsHe6khroK3JBEHDkyAFxlRBg8wZVsh6CIODkyeMyWxceZGaeRnZ2Fhh9MhhdQp/HU48S\nP4dKhz2VIj39GMzmRrBRI7pMnAwE/SXxYKJV2LNnZ8TvlwuCgO+//y8AQBU/UZFzqofooR4dhbKy\nUvznP/9WJHmQOHKCbFRVVQLoXBvbZrP26xBnTxQWFqCiohysYQgoRhXQe1QDSKXM6/Xi88/FFaE6\n6SJJxmTj1GBj1Th58ni/2wMGgO3btwIAVLFj+zQOxdAwzhgESsVg7bo1yMvLkcK8kHDixFEUFOSB\nNQ7tVuVOavQXxoONU+PIkUPYuvVH2c9HHDlBNsTWpQDVSeMGQRAGtLrboUPNe5nRIwN+D2PgwESr\nkJl1ut8L6uzZswNlZaXgokd1qHgIFoqioBkbDUEQsGWL/DdXJcnJOYfc3PNg9Ml9yiXwwRg4GC5P\nhNfrwcqVf0NdXa0EViqLy+XCF19sACga6kRpJoOBQjEUjDMGgday+Oqrz2Rv3EMcOUE2fF/+rso9\nBuo+ucfjwZEjB8W66F62UlSl6OH1ePy1wv2RhgYTvvnmS1CMCqqkiyUdWzVED8bA4cCBvf2qT/nm\nzZsAAKoE6cLHqkE66C6Kh9mFMuUCAAAgAElEQVRsxvvvvxtxIk7ff/8NamtrwMWOlWRy01toLQvj\nrEGgWBr/+tc/kJ0tn6ATceQE2TCZ6gEANNt5/+iBWoJ26lQ6bDYr2OgRva6LVqWI17K/htcFQcC6\ndWvgcNihSrxI8uQkiqKgnRgLnufx/fffSDp2qCgszEdGRjoYbUKHNrh9RTM6CupRUSgtLcbq1Ssj\nRo+9oCAP27b9DzSnhzrxwpDZwcaoYZiRBA/vxfsfvIuiInm6GBJHTpCNhgYTAIDqosnFQFV3O3jQ\nF1Yf1ev3MlEq0HoWp0+fhMfjkdq0kJOaegjp6cfB6BLB9aFuvDtUQ/VgolU4dGg/CgvzZTmHkvgm\nJKrEKW1kkKWAoijoL44HN0gUi9m4cW3YK7/Z7XasWrUSPM9DnTw96MQ/e3YDTFuLYdpajKbM+g6v\nmw9W+F83bS2G+XBlh2Nsp+tgS68FxVJwOhx49903ZSlLI46cIBtmsxmgGFB058IU/X2ftzMsFjNO\nnUoHrY4Jau+XoiioBuvgcDj6XROV+vo6rFv3CSiahSZ5uuROyQdFUdBfJHa/2rjxPxGddJmbe15c\njesSweikac3ZHoqmYJg+CEyUCrt3b8eOHVtlOY8UCIKAtWs/Rk1NNVTxE8BK1K60r1AsDUpFw2az\n4p13XvcnAktF8DUKBEIPWCxmUEzXQicDMbSelnYEXq8X6viRQY/BJevgyDMjIyMdkyeHLmwoJTzP\n4+OPV8Fub4J68LROKx2khEvUQpWiR25uDvbt242rr54n6/nkQBAEfPXVZwAAVeJFsk18ALEO33jF\nYJj3lOHzz9cjMXEQLrnkMtnOFyw7dmxFauoh0Np4qPoYUtdOiIF2bNeZ7lFX9pzfor8wHvoLW1qm\n2nMbYT5Vh3fffQMvvvgy4uKkaadKVuQE2WhqsnVbWhVpyTNScPjwAQAU2CCUt3xwCVpQLI0zmaek\nMyzEbNv2P5w9mwnGkCJbSL09+ovjQXE0vvxyoz+fI5I4ceIYcnLOgTUMAauTdm+8MxgdC+OswQAN\nrP7Xh2Gn+7906WN+ERvB3QRXTUfhn6bivbDmbvL/2Ev2dzjGY5N2tdwa7ZhoaCfFoq6uFn9b8ZZk\nehrEkRNkged5OByObvWeB1povaamGvn5uWD0SaC7yBsIBIqmwCZoUFlR3i/aTubl5eCbb74AxWqh\nSZ4h68qyNbSWhW5KHBwOOz7+eFVEhdjdbje+/HIDQFGSZ/Z3Bxurhv6yRDgdDnzwwbth8x2uqCiH\nxSIqHlKMBlDoMxQM2vEx0FwQhYryMqxcuUKSXBfiyAmy4HA4AAAU3d2KPDxuAkqRlnYEQHA62O3h\nksSJQGbm6T6PFUpsNis+ak5M0qTMBN2D5rzUqEcawQ3SIivrTEQpvm3fvgU1NdXgYsaCUbi0Sj3M\nAM24aFRXV+E///m/kCe/mc1m/P3vb0MQBGiSZ8Aw7lYYxvyiUyEh3fCrYBjzC/+PdtjPOhwjdb/y\n9lAUBd1F8VAN0eP8+Wy/8FFfII6cIAt+sZfOMkabJ8sDLbR+/Hia2OksQEnW7uASRUcuZ22q3AiC\ngDVr/oX6ulqoEiaHJDGJoigYLksErWLw5ZcbUFJSrLgNvaW+vg6bNn0LilFDnTglJDboJsWBjVMj\nLe0IDhzYGxIbAFH0ZeXKv6G2thqq+EngYnpfCRIKKIqCYWoimCgVdu3a7p/kBwtx5ARZcDp9K/KO\njpxSiR+7pqaBsyKvr69r7nSWFLAka3cwURwoFYPs7KyQr4iCZceObUhPPwZGlwRVwuSQ2UFrWein\nJsDj8eCjjz7wR5PClY0b18LlckKddLEkn6Vg8GWyUyyNzz9f5y81VRKe5/Hvf/8DeXk5YKNG9Dm5\nTWkoloZx5iBQDIX1Gz6B1WoJeiziyAmy4O/6067rGSB+gIGB1TjFp8TWU9/xQKEoClyCBiZTfUTK\nZxYU5OPLLzeAYjXQpMzqtTCO1KiS9dCMiUZlZTnWr/8kbCdH6enHcOLEUTDaBLBB6BBICaNjoZsc\nC7vdLkqhKszXX3+G48ePgtElyVquKCeMgYN2UiysFou/018wEEdOkAWXS+xlTFGdhdYpUBw9oBz5\n6dM+R947SdbuYBNE1bNIqycXBTs+gNfrhSZ5Zp8S/6RENyUOTKwahw7tD2m4uCtsNivWrl0jaocn\nXx4Wjks9OgpMjAqpqYcU3ZbYt283tm79H2hVFLRDZ3dokxxJaC6IBq1jsW/fbjQ2NgQ1BnHkBFlw\nubpekQMApWYGTF9tnueRnX0WFKeXtD6ai1BHvmHDp82CHRPBGuRNLOoNFE3BOD0JFEdj3fpPUFpa\nEmqT2vD55+vR2NgAVcJkMOroUJsDoDlxa1IcAODHH79T5Jy5ueexbt0aUIwK2mE/C9n2glRQtNjM\nx9eDIRiIIAxBFpzO5hV5F/KItIaBtc4Cr9cLhonc2XQglJQUw25vkjwUykSrQHF0RCW8HTuWikOH\n9oPWxEEVokSt7mD0HAxTE2E5UoWPVn2A5X96DWq1spn0nZGefgwHD+4DrYntc1/thu0l/vIs9TAD\ndJPj2rxuPlgBr8Xt/52JViFqVtsJl+10HVxlrQSdaLFlqMVihtEoXxa92dyIf/7zfXi9PLTD58gq\nHGTPboAjr+vFhvGKwWCjup9EdLhOnaAeYYRmlBFNGXVITz+OBQtu7LWtiq/IV69ejbvvvhu33XYb\nvvrqKxQVFeHee+/Ffffdh5dffjmiajkJXeNfkXcWWofoyAVBCDqUFEnk54v9nKUW7aAosZ68trYG\ntbU1ko4tB2ZzI9auXQOKYqBJmQmKCs8JnCpF76/zlaI0qK80Njbi00//D/Bft/ALpFIsDa/Xi+PH\nj8p2DkEQ8J//fIyGBhNUiReGjfyqFNAaFky0CoWF+UH5QEVX5KmpqUhPT8dnn30Gu92ONWvW4M03\n38TSpUsxY8YMLF++HDt37sS1116rpFkEGWipI+/CkevE52traySTKQxXCgrExhy0Jq6HI3sPl6SF\nu6IJZ86cCnuZ0S++2ACr1QJ10qWK1z73Ft2UeLhrHdi7dxcuvXQaLrrokpDYIQgCPvnkX7BYzM3X\nre8h9Zhrh/kTTjsjGOlRr8WFhu2lyM7OlO1zmJZ2uLnKIbHPUYlA6EmiNRDaX6fuYIwcXI02mEz1\niI9P6NV5FJ3aHThwAOPGjcPjjz+ORx99FFdffTUyMzMxffp0AMCcOXNw6NAhJU0iyISvjrwrR87o\nRcW3/tQTuitKSooAipalJ7JqkNjW9PTpDMnHlpKzZzNx+PAB0Jo4cHFjQ21Oj1CMWOcLmsInn/wr\nZKWSu3b9hFOn0sHoB4GLGxcSGwKBNnCg1Qxyc3NkGd/tduPrrz8XoxIRmqHeE5RKjFAFo6+h6Irc\nZDKhvLwcq1atQmlpKR577DEIguD/p+j1elgsPdfSxcbqwLLhGZYj+GiWHewiEYUxiI7cbK5DYqK8\nDTJCidfrRXl5GWhVlCwhUcbAgTFwyMo6DaORg0Yjbf9uKfB6vfj6640AAM3gaWEZGu4MNkYN7fgY\nNJ41YceOH7FkyRJFz19QUIAvvtwIilVDkzwzrJ0XRVGgjRxMdfWIjlZDpZI2AW3Lli2oq6sFFzde\n9oY6ocL37zUaVb2+JyrqyGNiYjB69GioVCqMHj0aarUalZUtAvU2mw1RUT2vWkymgSMkEqnU1jb3\nIu+ihSljFJ/Pzc1HTU3wQgjhTk1NNdxuN9gAPtfBohqih/1cA3bvPoBp02bIdp5gOXz4AAoKCsBG\njwSjlX57QU6046LhLLZi06ZNmDbtSqSkSKMD0BNOpwNvvPEmPG43tEPnhE2JXncwOhaeWgfOny/C\noEHSViNs27YdAAVV3ARJxw0nBI+4N+50otN7YnfOXVFHPnXqVKxduxa//vWvUV1dDbvdjlmzZiE1\nNRUzZszAvn37MHPmTCVNIsiE1SrWiHfVxpRSM6DUTERIYvaF6uoqAJB1FeFz5Kmph8POkYvtSVcD\nALy2KlhzN4GLGtlBB7upeC94V6P/d0Yd20EH21GVDo+lVUkYxUCTMgsA4Kpogmmr+FmSLhObQux1\nw6C/MA6WI1X48cdv8cgjT/TyCgTHhg1rUVlZAdAsHFXHgCr0/bp5nbLa7FNs9MszS0RjYwPy8nIA\nikZTUfd6+NphV/WYR9Dhc9QOwevu8jU54Zu8AICoqN7nQSjqyOfOnYujR4/ijjvugCAIWL58OYYO\nHYo//elPWLFiBUaPHo0FCxYoaRJBJvydiNjOQ2wURYGNVqG2ugZWqxUGg0FJ8xSjulqMOMnpyJlo\nFZgoFdLTj6GxsRHR0eFRYwyIinY87xWrF8I4NNwdXLIOTLQKqamHceutdyIpSd5saVG/fA8Autum\nQ+EGxfgcubQSt/52qWFa5SAVXosLMbGxQW2PKV5H/oc//KHDc+vXr1faDILMNDY2gGLU3ZYYsbFq\nuKvtKCjIw4UXKteKUUlqasSyMIrTy3YOiqKgbq5DPXhwL37+81/Idq7esmfPTgCAbuQ8MJrYLo/T\nDb+qx7E0gy4FBl3a5jmPXewjrkrWwTi9awcbTCa2D4qioB0XA+vRauzduwt33nlvj2MFS319Hf7z\nn3+DolnoRl7XY4Jkb66b5fy38q7KaXGiJnUJsa9VrzrpEqhi+96rvrPPUWuc1afgqlNWm8Hb5Abv\n8GL0pDFBvT8ysk4IEYfJZALFdj+zZOPF13NyzilhUkiorRWz8mlO3oiDepgBFENh566fJOlvLAVm\nsxlnzmSA1sR168QjAVWKDhRH40jqQdm0LsQmIP+E3W6HKulSWaocZKU54OL1eiUdluOa82yE/qsx\n4q4StyPGjw8uB4A4coLkNDU1weGw97gKZeM1ABV5EqO9oaamGqCYHic1fYVWMVCPNMJUX4/U1PAo\n4UxPPwae58FFDQ+1KX2GYmioknUw1dejqKhQlnPs3PkTzp07C9YwBFzMaFnOISdU84pcakfu2zPm\n3d0rpEUyzhIxp2jq1OlBvZ84coLk+GrD6R4cOc3RYGLUyMvLCfvWkcEgCAKqq6tBc3pFSoc0Y6IB\nCti8eVNYKCT6attZozKZ3nLDJYmZ43JEkKqrq/D115+LPcbDpCFKb6EY0WZ/50OJGDVqNGiahrcp\n/NULg8FjcsJT68DEiZODFscijpwgOVVVvgSvnsPJqiRtc1ORTLnNUhyz2Qy7vUmxuldGz0E93IiK\ninIcPnxAkXN2Bc/zOHs2U/JGMaHEtxWUlyet6IkgCFi3bg3cbhfUgy4FLXP0Ri58giY2m7TlpGq1\nBmPHjgfvqAPv6l+lqoIgoClLzPPoS24LceQEyamsLAcQWKY2N1hUJsvISJfVplBQXl4KAIrudWon\nxgI0he+++xpud2jKaACgsrICdnsTGIn15UMJrWNBMZS/EkEqjh8/iszM02D0g8FGjZB0bCWhtaIj\nr62tlXzsOXPmAgBcplzJxw4lrnIb3FV2TJgwGZMmBd9EiDhyguSUlfkcWM9lUGycGpSKQfrJ42ER\nDpaSkpIiAACtYKIXo2OhGR2Furpa7NixVbHztqewUNSXZ2TQlw8VFEWB1rOollBW2O1248svNwAU\nDc3gqREZUvfBGMVSOd/3X0qmTZuB2Ng4eBpywbulrVPvCnt2A0xbi2HaWoymzPoOr5sPVvhfN20t\nhvlwxwme7XRdm2NMP7XUr3ubPGg6WQeWZfHgg4v79L8njpwgOSUlRaBoDhSr6/FYiqKgStbB3Ngo\necgy1PiapTDqvjVe6C3aCTGgVAw2/fAtGhsbe36DDPh6edMaZf92uaHUDOxNTZJVBuzduwu1tTXg\nYsdE/BYErWZA61jk5p6XfFLOcRx+8YvbIPBeuGpOSTp2KBC8PKypVeCdXtxzzwMYNKjn8sjuCMiR\nNzQ0+JuZrF69Gk8++SSKi/u3IhchOBwOB6qqKkFrYgOeYaqGiElxaWmH5TRNUQRBwPnz2aBYDSiF\nb9C0ioFuYgycDgf++98vFD23j4oKUcSDUYWPOI0U0Jx4y5SiiYrb7cbmzZtA0SxU8ZP6PF44wCVq\n0dRk80dkpGT27KswdOhwuBsL4G2SPnzfHu2EGMRePxyx1w/voBQIiNoEvtdjrx/eQSkQELUJWh8T\ne90wCIIA69FqeExOzJo1G3Pnzu+zrQE58meeeQZnz57FoUOHsHXrVlxzzTX44x//2OeTE/ofhYX5\nEAShV+FkLkkLWs0gNe1w2NRA95Xq6iqYTPVgtAkhCZeqR0WBiVLhwIG9yM9Xfl+xsrJCFARiO5fo\njVia1cvcblefh0pLO4yGBhPYmAsiNsGtPapkMQqXlnZE8rEZhsEDD/waAOCoTIPAS1vmpgSCIMCW\nXgtXeRPGj5+IRYseluT+EJAjb2xsxJIlS7Bz504sXLgQt956K2y2/lvTRwgeX3ic0QbeT5eiKaiG\n6mG1WMK+HWeg+JL3GEPfQmbBQtEU9BfHQxAErN/wqaL5B16vFzU1NaACqFqINHyN26Sold61S9QN\nV8WGf1vXQOEG60CpaBw5ckCWSfnYseMxd+588E4zXLWRVekiCAJsJ+vgLLRg2LAR+N3vnmkRu+kj\nATlynudx5swZ7NixA3PnzsXZs2clL/qPdKxWKwRBCLUZIcdXY9sbRw4A6hFi+Hn//j1SmxQSTpw4\nCgBg9Skhs4FL1EI1VI/CgnwcPLhPsfPW19eB572yq9mFBEoaGdLKygoUFOSB0ScHVKYZKVA0BfVw\nA8xmM44dS5PlHHfccS/i4uLhqjsLr71jElo44nfiBWYMHToczz23DDpdzzlEgRKQ1vpzzz2Ht99+\nG4sXL8awYcNw11134cUXX5TMiEgnN/c83nzzVdx55724/vqbQm1OyOB5HufPnwOtMva67SIbowYT\no8KpU+kwmeoRGxu52c51dbU4fz4bjC4x5O0ndRfGw11px1dff4apUy+HTief5ruPlo5v/cdBtaev\nk/ajR1MBAFy08qp3DdtLum1gY7xiMNio7pu1dOgU1wqBF6/N9u1bMGPGLMm3lrRaLRYv/g3effcN\nNBVuB8Vq/fKwUnTWk7r7mSAIsJ2ohbPIgmHDhuOZZ5bBYJA2byagFfmsWbPw0UcfYcaMGRAEAZ9+\n+ilpN9qK06czIAgCvvkmNIlF4UJBQT4cDnvQtcOaUVHgeR579+6S2DJlOXRIFGMJh5pgRstCOz4a\nVosFP/zwnSLn7I0gUOTSN0eemSlmXrOG0EVs5IKiKXDJOhQU5MnWR2HSpCmYO/daAAIEPnR6CT0h\n8AKsx2vgLLJgxIhReO65lxAVJb2uREAr8sOHD2P58uXwer344osvcPPNN+Pdd9/F7NmzJTcoEmFZ\n8TIO9O2GrKzTAABG3zF7MxDUwwxoOlOPPXt24qabbvVf10hCnIjsBEWz4MLAkQOidKujwIIdO7dh\n3rzrkJAgr0hLiyOPsKYfgSDB4tLj8SAvLxe0OhYUo3wyYMy1w0Cxfas87qpTnA93rR3uiiZs374V\n48YF1wikJ+68816cPn0StbW10A6/Goy2c3t621lPqu5nAi/AeqwarlIbRo8eg6effl62iFhAd8oV\nK1Zg48aNePjhh5GYmIj169fj6aefJo68GakSFiIdMVGNAqsPrl8zxdJQjzDCnNuIo0ePYNasyPt8\nZWScENsuUixsBVsABB/ukwqKoaGbFAvrsRr8979f4pFHHpflPD4qKgJX9pMKV0UTTFu7Lonta7jY\nB6USHSDPB78ir6wsh9frAXgLrLmbujxOO+wqMD2IKrUOCXcFFz0a6sTgVcOCgY3XgIlWIT39GBoa\nTIiJkV4USaPRYPHi3+Dtt1+DoyIVupELQNHh0bNc4MUSM1eZDWPHjsfSpX+AVivfNlvAyW6JiS2z\n+DFjguuZ2l8hjhywWi3Iy8sBo43v0ypDc4G4itu+fWtEJg9u3fo/AADFhNdnQjXMACZahdTUQ6is\nrJD1XBUVZWL9PNO944xImvd7+/LZrKysbDNWf4SiKP9WmZzd+CZMmIS5c68Vs9gV7iHeFa2d+Lhx\nE/DUU8/L6sSBAFfkgwcPxu7du0FRFMxmMzZs2ICUlP63txMsKlU/q5UNgoyMdAiCAKaPe36MngOX\nrENhYT5ycs7JFpaTg7y8XOTknAOjT+4xnBdIuE9KKIqCdkIMrKnV2Lx5ExYv/o0s57Hb7airqwWj\nCy4qEyyqZB2M0/t2zp7CxQBgy6iF1+TsU9Z6Y2MDAEAzeBq46L5tv7QOCYcbqhQdbCfFe8OCBTfK\ndp477rgHJ08eh6kuC6xxGJgQqgkKQnM4vXkl/tRTf4BaLb9GQECO/M9//jNef/11VFRUYP78+Zg5\ncyb+/Oc/y21bxKBWE0d+4sQxAABnHNrnsbRjo+GuaMK2bZsjypFv3vw9AEAVL53NlrRqf3tI9TBD\nB4Up88EKeC0tyT5MtKqDwlTrkDFj5HDo0H7cdttdsoQ7y8rEMK/XUadI2JjRK1yn37yI7suK3OUS\n23xSdOTlgPQGWsOCiVYhJ+cceJ4HTcujCK7VavHgg0vw3nvvwFFxFLqR80BRyquPC4IA2/EauEpt\nGDNmLJYuVcaJAwE68vj4eKxYsUJuWyKWgR5at9vtOHMmA7QqSpJOX2y8BkyMGidPHkd1dRWSkpRd\n3QVDaWkJ0tOPg9bGg9ElhdqcLtFcEA3byVocPLgfN94YfNvErigpad6nDsGNVBmkqSNvPVZ/hjFy\ncDW6YDLVIz6+d9oSveGiiy7F9OmzkJZ2GG5TLlRx42Q7V2cIggBbRh2cxVaMHDVakXB6a7p15L/5\nzW+wevVqXHPNNZ3WAu7cuVM2wyKJwsKCUJsQUjIy0uF2u6FKkObLQ1EUtGOjYT1aje3bt+D++xdJ\nMq6c/PjjtwAAdfxkSetmjdOTwCV2fUOIurLnFWnrkDHv8qLpdB327duFn//8ZslrfH0d33TD54Lp\nY9e3QMLGHns9PA15fTpPr/BfruBX5FqtKAQi8H2XeQ13aLWvR7lVVkcOAPfe+yucOXMK9ppTYI1D\nQHPyayb4sGeZ4Mw3Y8jQYXj6qRf8/2Ol6NaR/+UvfwEArFu3ThFjIpX+IisaLEeOHAQAsFHSiVuo\nhuhBn2Gx/8BeLFx4pyJCJsFSUVGGo0dTQWtiQybJGii0igGXokdNSTVKSoowfPhISccvKioAKFrR\nHuyhoC+hdd+WBu/ue+OVcId3iZELqQVQOiM6Ohp3330/PvnkX3BUHod26M8U6XNgz2mA/VwDkpIG\n4dlnXoTBoLx+Qrfxr6QkMUT41ltvYciQIW1+li1bpoiBkcBArh83m804c+YUaHVsj3uevYGiKWhG\nR8HldGLfvj2SjSsHP/74PQRBgEri1bhc+Bpb+PTgpcLr9aK0tAS0KhoUFR5lQJLT7L8ZJvi/b8gQ\nMY+EdzZIYVFY4zU5oVKpEBWlTBe82bOvwoQJk+C1lsNjlr9Dp7PYgqbT9YiJicWzzy5DdHRoEu26\nXZE/8cQTyMrKQnV1NebNm+d/3uv1YvDg4EQ/+iNeb0tzALfbPaD2zI8cOQie90IdPVLysdWjjLBn\nm7Bz1zZcd90NsiXL9IXq6iqkph4CrY4GaxwSanMCgksSJS1Pn87AzTcvlGzciopy8fMfopuZEvjk\nRxkm+ES1hIREGAxG2JpqIAiC4pO/1hKtUiRQAgBoCrHXDWtzTNNZE7xWNy6Zerli4k4UReHBBx/C\n8uUvwFl9Aox+MGiZOvC5qptgPV4LnU6HZ555UXahpe7o9uq+9dZbaGhowOuvv46XXnqp5U0si/j4\n7ss0BhJud8uH3mq1RLROeG8QBAH79+8GKBqsDI6cVjFQDTOgrrAWGRkncOml0yQ/R1/ZuvVH8DwP\nTfykiFiNA+J1ZaJUKCzMh8fjkewm68tY700L24jDI4aKVarga+QpisKUKReJk2BnQ59zCcIVV6Xo\n6GfMuFLR8w4aNBgLF96JL7/cAGfVcWiHXCH5OTxmF6yp1WAYBk8++aw/yhIquv0Gnz17FgCwePFi\nlJeXt3mtuLgYl19+uXyWRRCtHbnFYh4wjjwn5xzKykrBGofJNuvVXBANZ6EFO3f+FHaOvKHBhP37\n94JWGcBGDev5DWEEG6eBs9GMkpJijBo1WpIxy8vLAKBf748LzY68rxnJU6dejiNHDsLdWKC4I+9J\norW3CZSd4a5zwGtyYeTIUbjsMuW/t9dddwOOHTuC/Pw8uKOGS1IW64N3eWE9UgXBzWPJI78NixLZ\nbh35Bx980OVrFEVh7dq1khsUibR25I2Njd0c2b/YtesnAAAnYz9lNloFNkGDrKwzqKgoQ3Jy+ISv\nt2/fCq/XA3XihJDUrfYFNkYFJ4DSUukceU2Nr+uZctKsSsO7eLGqoo9ZyRdffBkMRiNsjYUQEi8E\nRfef7Tje5YU1rRoUReGeex4IyZYYTdNYvPhRvPLKi3BWHgOrS5RE117sZFYDr9WNG264GTNnSr/a\nD4ZuHTnJVg8Mt7uljMSn2tTfqa2twbFjaaDVMUF3OwsUzegoWGsd2L17B+6770FZzxUodrsde/bs\nAMVqwEWPCrU5vYZp1h2vqCiTbMz6erE3NMWGtnWrnPB2D4zGqD5vR7Asi/nzFuC7774W657jJ0pk\nYWgReAHWtGrwdg9uvfWOkK5WU1KG4NZb78DXX38OR+UJaIfM6vOYziIrXOVNGD9+Im6//W4JrJSG\ngD6NJ0+exOrVq9HU1ARBEMDzPMrLy7FrV2S3m5QKj6cl2c1kioxG931l27bNzXvD42XfG1al6EFr\nGBw4sA+33XY3NBpl1JK64+DBfbDb7VAlTAmbRg29gTGIK0BfgxMpsFgsoBh1xEUnAkUQBAgOL2KH\nSrN1Nn/+Amzb9j846s6Cix4NSqbtKaXwyZO6q+246KJLcdNNt4baJCxYcCOOHz+KgoI8uKOG9SnE\nzjtEDQaNRoOHHnosrP0WHL0AACAASURBVJJvA3Lky5Ytw5IlS/Dtt9/igQcewE8//YRJkybJbVvE\n0Frlqa6uNoSWKIPJVI+dO7cBoOCsPg1nzemAO3wFA0VTUI80wp7dgCNHDuLqq+f1/CYZ4Xke27dv\nASgaXGxkNhCi1QwojkZ1dZVkY3o87n6s6Abwdi8Er4BBg6RRGtTp9PjFL27DF19sgDX3B1BsSwJd\nsB3zOsjaUgwMF8inc+5DEATY0mv98qSPPfZkWDg6hmGwZIk0IfamrHoIbh6333WP7OI2vSWgK61S\nqXD77bdj+vTpiIqKwttvv40DBw7IbVtEMhAc+Q8/iCpmYDjFVCY1o6IACti5c1vIu6KdPp2Bmppq\ncFEjQbOhjw4EC61nUVNTLZHcKJojM5HXsS5QvBZxCy0pSbrS23nzFiA5ZQggeACJ/g9K49MYdxZa\nMHz4CDz55HNh1X8iJWUIbrnlDggeBxxVJ4Maw9vkhrPIguTklJAvJDojoBW5Wq1GQ0MDRo0ahYyM\nDMyaNWtAi6B0R3WNdCuccKSsrBR79+4CrTJCN/qGbsOonXX4spz9PKjz0loWqiF6lJWWIjs7CxMn\nTg5qHCnYubM5yS9OviQ/JWD0HFwNNjQ0mBAX1/dyUqPRiOqa6pDURiuB1yw68mHDpFMwZFkWSxb/\nBq+//jIomoFu1IIu278G0jFP6W5ogrel29eoURfg6aefh16vvLJZT1x//Y04evQIiosL4IkeCVbf\nu6iKI9cMCMDPf/6LPokByUVAK/JFixbhqaeewty5c/H999/jxhtvxJQpyjaqjxTqamvb7Jn3JwRB\nwGefrYUgCFAnXar4XqjmAlEdaseOrYqetzXV1VU4cyYDjDYh4ut/ffvkVVWVkowXF5cACAIET/+U\nHvU0+Bx531qPtmf06DG48cZbwLttcFSkhTziFCiCm4f5UAVcZTaMHz8Rzz77Ylg6cUAMsT/44EOg\nKArOyuMQhMAXogIvwFVihV5vwIwZ4ZGl3p6A7sQ33HAD1qxZA4PBgG+++QbvvPMO3n33Xblti0h4\nnpfsxhhuHD58AFlZZ8Dok0OiKc7GqcHGqnHy5AlUVVUofn4A2LtXTPCM1L3x1vgceWWlNNdy5Egx\ne99rr5NkvHDDa3JCq9XK0o3vlltux9ix4+GxlMJdf17y8aWGd3jRuL8cnhoHLr10Gp5++nnFG4X0\nllGjRuPqq+eBd5nhrs8J+H2eWgd4pxfTp89UTKGutwRkVVlZGdavX4/GxsY2s8U333xTNsMiEVrD\ngHd4UVZWGnKlH6lpbGzAZ5+tA0Wz0AyeGpLQKUVR0IyNhjWtGj/9tAUPPLBY0fN7PB4cOLAXFKMC\na4wsAZjO8JWg+RTZ+sr48WIJlcdaDk7CBjrhAO/ywmt1Y9Sk8bIkcTEMg0cffRKvvroM5uqToDXR\nYPXhKYPttblhOVAJr82Nn/3savzqV0vCMtzcGQsX3oXU1MOw12WBixkVUOKbq1qMMF166VS5zQua\ngD6RS5cuBQBMmzYN06dP9/8Q2sJEizfG0lL5xfqVRBAErFmzGjabFarEi0CrQhc+U6XoQetYHDiw\nF2azWdFzZ2ScgMViBhs9MiJLztrDRInJiv4e4n1k1KgLEB+fAK+lDALfv7aXPHUOAMAFF8iXFxEb\nG4snnngKDEPDUXYIvFPZz3cgeMwumPdWwGtz48Ybb8GiRQ9HjBMHAIPBgJtuuhWC1wVn7dmA3uOu\ncYBhGIwdG3oFt64IyJF7PB48//zzuO2227Bw4UL/D6EtbLQ4uysq6l/9yXfu/AmnT2eA0Q+WVcUt\nEChaXJW73W7F98oPHNgLAOCipVFCCzUUQ4MxcCgqLpQkc52iKFx55RwIvBvuhnwJLAwf3M2OXG6B\nkzFjxmHRoocheF2wl+4D73HKer7e4DE5YdlXAd7hwT33/BK33353RCY1zpt3LWJiYuFpyO3x+gpe\nHt4GJ4YPHxlWmfjtCSi0PnXqVOzatQuzZ8/uU7OA/g6lpkHrWBQW5vebzN2Cgjx88cV6UKwamuQZ\nkvxNvM0N01ZxFRhM9yXNCCOazoi17NdffxN0Ovn35szmxua2nzTspfu6PE477Koe27l2qPXtDIXy\nndg4DZxFFpSVlUqSjX3NNddh85Yf4KrPhqsuu015opy10a6Kpj59poDuO3q5q+1gGEbWFbmPK6+c\ng8rKCvzvf9/DXrofuuFzQx4B8picMB+oADwCfv3rR/Czn10dUnv6AsepcMMNN+Gzz9bBbToPdeKF\nXR7raXQBAjB69AUKWth7AlqRb926Fb/97W9x0UUXYeLEiZgwYQImTuwfkoJS0DoBgo1Rw2Kx9It6\ncovFjH/88314vV5okmeB5sJDepNiabDRKtjtduzevV2Rcx49mio+oMMz2SVY2DhxlZGbK02CVVRU\nFK6dfz0EdxME3t3zGyIA3umFt8GFMWPGKaYquHDhnZg+fRZ4ey0c5UdCmsne2ok/9NBjEe3EfcyZ\nMxdarQ7uhjwIfNcZ7N7mSoXhw0cqZFlwBHRXIuIv3cNxKn/JGRunhqvchvz8vJD2p+0rXq8Xq1d/\niPq6WqgSpoA1SJd4Q+u5Dr2LWxNI9yXjlclo2FqMbdv+h/nzF0CtlvcGe+yY6Mj1o68HzfUtAhBI\nra+tcKciZVxcgnjdzp07i7lz50sy5o033oL9+/fA1tQE3fBrus2pkKo2WpWsg3F619nkfeno5a62\nAwAmT+565SY1NE1jyZJHYTLVIyfnHJzVGdAMukSx8/vwWt2wHKr0O/FZs2YrboMcqNUazJkzF9u2\n/Q8ea1mXyZmeBjH0PmJEePdTCGhF7nK5sGrVKjz//POwWq348MMP4XK5en7jAEGlaulcxMaKK5zC\nwrxQmSMJ//3vl2KpmSEFqoTQia90Bc3R0FwQBavV6i8Jkwur1YLz57NBaxP67MTDDdrAgdYwyD6X\nJdmqT6fT4b77fgWB98JRcTRi6qK7wlUuhtuVbqPLcRx+97tnMHhwMtz12XD1omRKCninF5aDleCd\nXvzyl4v6jRP3MWfO1QDQbT6Ht9EFhmGQkhI+XRc7IyBH/uc//xlNTU3IzMwEwzAoKirCsmXL5LYt\nYuC4lrwBnyMvKIjcZJ+0tMPYsuUH0CojtCkzw3avXzMmGhRLY8uWH9t0oJOaM2dOQxAEsIYU2c4R\nKiiKApuggbmxEZWV0jVQmTHjClx88aXwNlXBbVLWAUmJ4OHhrrIjKWlQSG7mBoMBTz31PIzGKDir\nTsBjke5/1B0CL8CSVgWvzY2bbroVc+deq8h5lSQ5eQhGj74AXlsVeI+j4wGCqOaXnDwkbOvHfQTk\nyDMzM/H000+DZVlotVq8/fbbyM7Oltu2iKH1P5liaTBGDkVF0mQCK01paQnWrFkNiuagGTq7S7nI\ncIBWMVCPNqKxscGfUS4H2dmZABC2db19hUsUcx+ys7MkG5OiKCxa9DAMBiOc1RnwOiKzva+zzAbB\nw2PmzCtDNqFNTEzC73//LDiOg6P8kCLXsinL1Cz2MhW33nqH7OcLFZdfPhOAAI+ltMNrXpsHwv+3\nd9/hUZVp48e/Z2omvZACoYaETiAYKdJEQBBBEKQXKQICimBZfV0V9tUVXNd1FX/i+u5eq+Li7quy\nrm1910oEKSIivUsJpPdk+jnn98eYQAjpU5Pnc11elzM5c86dYTL3ec55nvuWVdq39/+aEQ1K5JIk\nVbuUXlRU5LejNF+49mxNG2HAarUE3IQ3s9nMK6+8iN1ux9h2UL2zr/2BKTkCSSvx6acfeaw07tmz\nZ5A0OjRBkR7Zf13K9uZS9NmFWv9zltZ/JaLiUEGd+zAfKwLg2DH3JXKAiIhIFi1aBqqM9fJ3Abm2\n3HauDICbbhpez5aelZSUzNKlK1AVJ9bMjOuPIN3EkW/FerKYuLh4lizxr3ad7nbDDa56KM6ySzV+\nVllbv8Uk8gULFrBo0SLy8/P57W9/y7Rp07j77rs9HVvAuLYgQmXFrMuXa344/JWqqrzxxuvk5mZj\niOmJPjwwKtNpgnQYO4dRUJDPnj3fuX3/TqeTy5czkYyRLbbPtqSR0Bi1nD590u33s9PSbmD06HEo\ntlJsOfvdum9PcxRacRZY6du3n0fKsjZWevog7rxzBorDjDVzR6PqhTeUKitU/JCHJEncc88Kryzt\n9KU2bWJJTGyPbM6pcaJZ2e0uMdH/E3mDLvxPmDCB7OxsDhw4wNtvv83jjz/OtGnTPB1bwKiRyH+p\nYe3OXs+e9u2337Bv3160pjYY6lhX6Y+CUiKxni3l008/ZMiQYW4dQRQVFaIoCjp9iNv22RhhA+Oq\nLn03VW2zsa9WtjuH4stFFBTku321xYwZszl16gQXLpxFGxyPPsK9TUc8xXrSdQl73DjP9/NuqIkT\nJ5OZeYHvv9+NLftHgtq6dwKe9XQpcoWDsWNvIzm5m1v37a/69u3PpUuZyOY8dFf1kFDtrlujbdv6\n/9yYBn3jPfnkkxw/fpxNmzaxadMm9u7dy7PPPuvp2ALGtSM1jcl1flRUVOiLcBotPz+PrVvfRNLq\nCUocEnAjT22wDmOHULKyLv9StMV9SkpcX+Ytbbb6tSrXk5875/6qhHq9gRUr7sdoNGLL3odiL3P7\nMdzNUWjFftlMUlKyT1vmXkuSJBYvXk779h1xFJ/GUey+fy/FJmM5UUxISCiTJ0912379XeWyQmdF\nzYGXVqcLiGXEDfrG/umnn/jjH//ILbfcwpgxY3jppZfYuXOnp2MLGNfOF9AYXSP08nL//8JSVZW3\n3/6r6754/AA0Php5NldQN9f9688++9it+6267x5gJzeNVdkn4MKFcx7Zf3x8WxYsWIKqOLBc2uWR\ny8Luoqoq5kOuk/Dp02f73Xwgo9HIqlUPEBRkwpbzA7KtpP4XNYD1bCmqU2HixMkEBwfm90BTJCd3\nQ6vVIZtrJvI2MbEBMUegQRG2b9+e8+fPVz3Oz88nPt7394z8laRz/eFbrZ6bkOIuP/20n4MHD6AN\njkcX3tnX4TSZLtyAPt7EqVMnOHv2tK/DCTi6iMpOaDVn77rLkCHDuOmm4SjWQux5hz12nOaynS/D\nWeBqz1nZ0c3fxMe3ZfHiZa7Jb5eaP5FQlRVsZ0oJCQlh5MjRbooyMBiNRrp2TUaxFqHK1SePtmnT\nxkdRNU6Dm6ZMnjyZe+65h3vvvZfbb7+dnJwcFixYwIIFCxp90IKCAkaOHMmZM2c4f/48s2fPZs6c\nOaxbty4gl2zVUHUG79+FMBRF4Z//fBcAY8IAvxt5NFZQsmuWvTubqYSHu/apOi1u26c/koxaJK3k\n8ZUWc+cupE2bOOwFx3BW5Hr0WE2hWJyYDxdiDApi7lz/ntCbnj7I1V/bVoIt71Cz9mW/bEaxy4wY\ncYvXytD6k8pmOLKl+uc/OrruuSX+okGT3VauXFnt8eLFTe8D7XA4eOqpp6o+LBs2bGDNmjUMGjSI\np556ii+//JKxYwOr+MC1M31V2fVYq/XvIgIHDx7g4sUL6MI7BcRSs/ro40xow/R8//0eZsyYS2Rk\nVLP3GRXlar6h2Cvq2TKwSZKEZNJRUJDn0eOYTCaWL1/Fhg2/wZa1G22X8X5Tq0BVVcp/yEO1K0yf\nNzsgvsRnzpzH8eNHyc4+gS60HbqQpl0ptZ133QZsCXXUmyIlpTsAsrl6InfHd4g3NCjTuLP3+HPP\nPcesWbN4/fXXAVexmcr9jxgxgp07dwZcIr/2KoLqdD02mfyjyUhtdu50FVGRK3IoP/1hrdu5q6OX\np9t/SpJEUNcIKg7k8+2325k0aUqz92kymUhIaEtObj6qqgTcRMDG0Bi1mAvNHu/c17VrChMnTuHD\nD7dhzdmPqd1gjx2rMaynSnDkWkhNTXNb3XlPMxqNLF26kmeeeQpb1vdok8YjNbKxj2KTceRZ6NIl\niYSE+mvSt0RduyYjSRKyJR+t6crl9IgI79eOaAqvDhm3bdtGdHQ0w4cPr0rkV39phISEUFZW/wSx\nqKhgdDr/aWYvSdVH5IrVdb+qXbt4YmPDfBFSvcxmMwcO7AekFjWRy9AhFPPhQr7d8TULF851y0SV\nvn37kP355yjWIrQm/x+lNZWklVBVlfBwg8cvry5aNJ8jRw5y5sxpHGHt0Yf5tm6BI8+C+UghkZGR\nPPLIg0RGhvs0nsaIje3P1KlTef/997HlHXI1mWkEe7YZVBgxYrjffl95XhgdOnTgYuZlNEFX/sYT\nE+MC4j3xaiJ///33kSSJXbt2cezYMR599FEKC68s0aqoqCA8vP4/oKIiz3eFagyrtXpzeqXClciN\nxlDy8vxz5vrRo4eRZRlDTE+Mcf2avb+GdKgCsOd7dpKTRq/BkBhC/vk8vv12D7169Wn2Pnv0SOXz\nzz/HUXqhRSdytK4T6qysIkJDa+9Y5i4LFy7jN795HFv2PrSmWDQ6o8ePeT2yxUn53lw0koZ7712N\nw6H127/b2owdO4mMjG/JyzuJPqIL2kZUIXRku75Pk5N7B9zv7U4dOyZx4cKFal0HFUXnN+9JXScU\nXh2K/e1vf+Ptt99my5Yt9OzZk+eee44RI0awZ4+rRWRGRgbp6d7tMOQODkf1vstyheuxP1SDqs3P\nP7u6s2laYGIydnJ94L/77lu37K9Pn1RMpmCcpecpP/Uh5aev/GfLPVhje/OF7dW2sVysGYc158dq\n25Sf+cQtsTbLL3M7DAbv3LNOTGzP1KkzUJ1WbNn7fNIlTZUVynbnoNhkZs6cVzXpKdAYDAbmzVsE\nqNhyfmjwe6mqKo5cC9HRMX7f4cvTunRx3fq7us5BoCzD8/k11UcffZRNmzYxc+ZMHA4H48aN83VI\njWa3Vx+Ry6WuRN62rf/+YVQWqwnUdeN10cUY0QTr2L9/X42TrKbQ6/UMH34zqtOKqgZevfCGUhXX\nl79er69nS/e59dYJJCd3w1l2EWfpBa8dF36Z3LY/H7nIxtChIxgzJvC+e67Wt28/+vcfgGzOu27t\n8OuRi+2oDoVevfoG/KqV5urcuTKRl1c95+/znCr5bFr1li1bqv7/7bff9lUYbnHtenG51E5YWHiD\nbhP4SkWFaxa2v8wYdidJkjC0C8F6uoRjxw6Tmtq4e4bXM3bseNeyNm0QwUnj65z0FtxxZL37a+it\nCG9SrDKhoWFe/ULXaDQsWXIv69Y9hi3nB7TBcWj03vnytJ4sxn6xnOTkFBYsWNIiEtmMGXM5ePAA\n9ryD6MLa1Ts505HnWlbZq5f/VK/zlfbt26PRaFCUK2vJRSJvRWy2KyNy1aGgmJ207+nfhfareqir\n3l+3r1Q4KPqs9tFX2E0J6MLrPsGoOFSA/VLtS8IqlwAePHjALYk8JqYNw4aNJCPja5wl59BHenYG\nvrepqopqcRLT3vsFMOLjE5g+fQ5/+9sbWLP2YuowwuNJ1XapAvORIqKio1m16kGvXoXwpISEtld9\nTs+jj+xS5/aVibxHj17eCM+v6fUGEhLacfnylaJIRmNgrKn3+aX1lsZZVtn6rqOPI6lbSIjrkroq\n2+rZMjBJGglJp+HIkeYVyrja5MnT0OsN2PIOocrNv2TvTxSLq/dybGycT44/atQYevXqg1yRhaP4\nrEeP5Sy2UbEvD4PRyAOrHyEiIvBrKFztjjumotVqsRccRa3jRF1VVJwFNuLjEwJmvbSntW9fffVE\noJzgiRG5m1X2sPX3iSOVHX1ka0m1dZPeoAnRE3Vr865YNKSjV+mOLHJysiktLXXLbY6oqGhuu20i\nH364DVv+4UYv8/FnzkLXCV1SUlefHF+j0bB48XKefPJXWHN/RBcSh8bg/mU/ilWmbHcOqqywbMVK\nOnYMjE5sjREdHcNNNw3n22+/wVl2CX349f/WnMU2VKciRuNXuXZeU6DcbhEj8mayWKqX7qxceubv\nhRU6deoMgGLxbElOX9LFuC6LnTt3xm37nDDhDtq0icNReBLZWuS2/dambG8uRZ9doOizC5iP1Oym\nV7ozq+rnRZ9doHRXdo1tKg4VVNum6D81C/c4C1zzPLp2TXH/L9FA0dExzJu3yFU//PKeOkeTTaEq\nKmV7c1DMTqZMuYsBA2506/79SWXrVUfhyVq3cea7/s39tZ68L/j793ZtRCJvpmt7jstmVyKPifHv\nYvsdOnQiLCwcZ/llt39h+gvtL/fZL19u2AzehjAYDCxYsBhQPZJsfEFVVexZZoKCTFUzd31l8OCh\npKcPQrbkYy844dZ9m48U4sy3csMNNzJp0p1u3be/adcukd69+yJb8mrtjuaoSuRiRF7Jn5cM10Vc\nWm+mrKzL1R6rNld7Rn8v7afRaEhLu4GMjK+RK3LRhSb4OiS304a67m/l5bm3OUefPqkMG3YzO3Z8\ngz3/KMbY5hedqU3YwDj0sbXPnA0fWv8Ior7bEM4iG4rZSdqQwT6/JyhJEgsWLObkyeOU5h9CF9q2\nUcVNamO7VIH1VAnxCW1ZvHh5wFwybY6RI2/hyJFDOIrPor3mNpCqqjgLrMTHJxAVJe6PVwqE3uPX\nIxJ5M2VmVp99rToUtDqdz78QG2LEiFFkZHyNJfNbpKuqaunDO2OMS622rfnCdhT7lTN7rTEKU4fh\n1bapUW9d0hLa9XbPBN8AGqPrglNZWanb9z1r1lwOH/6J4oIj6ELboTVFu/0Y3mL72VUA48Yb/aPm\neWhoGIsXL+OPf3we6+XdBHe5tVk17mWzk4of89Dr9dy3ai0mU7Abo/Vf/foNIDg4BEvpBdS4/tV+\nVrl+XFxWry401P/LsV6PuLTeTOfP/1ztsaqqaLX+Uwe+LklJya7JTarsk2VonibpXB/vq5cHuktw\ncAhLltwLqoo1a3ez+0H7imJxYrtYTlx8Aqmp/et/gZekpqYxfPjNKLZi7PlHm7wfV0ezXFS7wuzZ\nC0hM9G1Nd2/S6/UMGHAjqtNSoz2nI981tydQK9l5SqBeqREj8mZQFIWzZ6tPpJI0Ek6Hw+MdpNzl\njjum8sc/Po8mKJrgDiNq3S4Qi5xUVql0R+OU6+nduy+jR9/Kl1/+B1vuQYISBnjkOJ5kOVkMispt\n4yd67H1qqpkz53H48EGKCo6iC+/QpFa7trOlOPOspKXdwMiRt3ggSv92ww03smPHN8jl1W8BVt4f\nF4m8ZfCvv9wAk5l5EYvFDFe1DZQMWhRFqTGb3V/17duflJTuyOWXcZZn+Toct6qcrxAS4rkGIHfd\nNZuEhHY4ik4G3PvnLLFjPVtKm9g4brppeP0v8LLg4GDmz18MqoI1a2+ja7HLZifmI0WYgoNbTOW2\nxurRoxd6vb76Z1MFudBGZFRUwN4TFqoTibwZjh51FRvRXDVS0Jhcl9Xz8/N8ElNjSZLEnDl3o9Fo\nsGX/ELCXiK+nsnmNJ7+sjEYjy5evQqvVYs3ag+IMjAI7qqpScSAfVJg3d6Hfzuno338A6emDUCwF\nOEoaVyjGfLgA1akwc8Zcv5986ilGo5Hk5G4otuKq22ey2YFik0lJ7u7j6PyT0eibLnzNIRJ5Mxw8\neAAAjfHKrE9tmGvJ06VLNdfq+qtOnTozduxtKI7y63bzClSVa6M7daq7TGVzderU5UoXryaMHH3B\nerIYZ4GVG24Y6Ff3xq9n1qx5GAxG7LkHUWV7/S8AHAVW7JkVdO7chWHD6r8t1JJVTWhTXCe2ziLX\nyWaXLr4p/uPvqspXBxCRyJuotLSUEyeOoTHFoLmq8YguynU2d/bsaV+F1iRTptxF27aVl4gv1/+C\nAGDPNqPRaLwyM3fcuNvp0aMXzvJLOIrdV4DGExx5FsxHi4iMjPplTbx/i46OYdKkKaiyDXvBsQa9\nprJ4zqxZ8/3u3r+3JSUlV3vsLHadDHXu7NkT3ECl0wXe1LHW/Qlvhh9+2IOqqujDqpc/1EUakbQS\nR44e9lFkTeO6RHwfWq0O6+U9KI7aG5IEAmeRDbnYTp8+/QgO9vxyI41Gwz33rCA4OAR77o/INvcv\neXMH2eyg/PtcNJKGFStWExbmvx36rjZ27G1ERUVjLzyJ4qh7/okj34oz30qfPv3EZC5qJmy5xDUi\n79DBv/tB+EqgrDq6mkjkTfTddzsA0IVX/2OQtBK6WBPZWZfJyQmsyU8dO3Zmzpz5qLINS+ZOVEX2\ndUhNZjlVDLiacXhLdHQMCxfeg6rIWC/vQlX96/1T7DJlO7NRrDIzZ84jJSVw7pEaDAZXNTZVxl54\nvM5tLSdd//YTJ072Rmh+LzQ0rFpTFLnUQWRUlEcngQayQLyCE3gR+4GsrMucOXMKbUgCGn3N0Z4x\n0dVZbM+eXd4OrdluvnkMQ4eOQLEWNmmmsD9wFF65P9q3bz+vHjs9fdAv718R9jz/uSqjygplu3KQ\nyxzceusExo4d7+uQGm3YsJFERcXgLD5T671y2ezEkWOmS5ckMRq/SmWTJHAVrWrX1r+bOvmSTuef\nEz/rIhJ5E+zYsR0AfcT17zHp24UgaSV27NiOogRWoZXKEpldu6bgLD2PPd9/klFDqLJCxX5X8Qtf\n3R+dM+du2rSJw15wDKfZveVhm6IyiTsLrNx442BmzJjj65CaRKfTMXbsOFTFib2WeQi2c6Wguk5I\nhSvi46uXYA7UmuLe0K1b4FypqiQSeSMpisJ3u3YgaQ3owq5fJUqj12BoH0p+fp5b+2F7i15v4P77\nH6JNm1js+UewF7l38pZS4fBYRy/z4ULkUjujRo3x2YjMZDKxdOkKJEnCdnmPT3uXq7JK2e4cHLkW\n+vcfwNKlKwPy0mGlESNGodcbcBadqXG1SFVV7JkVGAwGBg70j3Kz/uLaJZhi/XjtKm85BNK98sD9\ni/aRo0cPUVJchC6sI5Km9n/ooCTXJKIvvvjMW6G5VXh4OGvXPkpISCi27H04yjJ9HVK9bBfKsJ4p\nJSGhHTNmzPVpLCkp3Zkw4Q4URwW2nB99EoMqK5TtzsaRY6Fv336sWPFAQM7IvVpwcAjp6QNRHOXI\nluq1GuQSO3K5HCrqXAAAIABJREFUg9TUNIzGIB9F6J+io9tc87j2JjqtnSy75rZotYHztxI4kfqJ\nyvveuohOdW6nizKiiwni0KGfuHQpMyBrPLdt2461a3/F7373DNZLu5A6jEAX0vxLcpoQPVG3dqj1\n503p6OUotFKWkYXJZOL++9f6RVGHyZOncfDgAS5ePIsuLBFdmPfuS6pOpWok3qdPKvfdt9Zvi740\n1k03DWfXrh04Sy+gi7jSdtWRYwZo0X3GmyoysnpBnNZaIKchriTywBnnBk6kfkCWZQ4c+AFJZ0Jr\nqr/fuCnFVfHt3//+yNOheUxSUjL33fcgWo2ENfNbZEuBr0OqwVlqp/y7HFDh3ntX09ZPJvLodDqW\nLl3hqvqWva/BxUyaS3UqlH6XXXU5/f77HwrIIhe16dGjF6GhYTivuUpkz7EgSRK9e3uurWygunaZ\nYVhYYHb58oa2bV0DiX79/KdvRH1EIm+Es2dPU1FRgS40sUF1m/Vtg9GG69m9e6fbe2J7U58+qdx7\n732gylgubke2Fvs6pCqy2elaUmWXWbhwqddnqdenffuO3HHHNFSnBWvOfo8fT3EolO7Mwpnvqtq2\ncuWaFjMSr6TVaklN7Y/qtKLafvksKirOQhsdOnQKmLXx3nRte06x9Kx2w4bdzLx5i5g1a76vQ2kw\nkcgb4egvRV60IQn1bOkiSRKm7lEoisInn/zLk6F53A03DGTx4uWosh3LxW9Q/KDgiWJxUvZtForF\nyV13zWL48Jt9HdJ1TZgwiU6duuAsOefRxiqKQ6FsZxbOAhsDBw7h3nvvD/h74rWpPGFzml33yZ3F\ndlBUUlK6+TIsv3VtUSRvFEkKVHq9nltuGUt4eOO77fmKSOSNcPKkqxCFLqThMz4N7UPQhurZsWN7\nwDRSqc3QoSOYP38RqtPqSuY+rP6m2GRKd2YjVziYOHEKEybc4bNY6qPValm0aCkajcZ1iV1x/yx2\n1aFQtiMLZ6GNIUOGsXTpyoCaddtYPXr0Aqi61aOYXc1+ri1HKrhce1XGYPD9HBLBfUQibyBZljl7\n9gwaQziStuF/BJIkYeoRiaIofPzxBx6M0DtGjRrL9OmzURxmLBe+rrdcpie4Lh9nI5faGTNmPHfe\nOd3rMTRWx46dGT9+IqqjAlveEbfuW3UqlO7KxlnkSuJLltzbopM4uCZrxcXFo9qrXxnq2LGzbwIK\nIBqNplW2dG3JRCJvoMzMi9hsVrTB9U9yu5ahQ2jVqDw3N8cD0XnXbbdNYuLEKSj2ciwXt3ttEhdU\nFjfJRi62MXz4zcyePT9gvpQmTbqTmJg2OIpOuG2egaq41ok7862kpw9i8eLlAb1OvDGuHX1rtdoa\nhU+EmvxhRYfgXq3jL94NTpw4CoDW1PhCCpIkYerlulf+r3+97+7QfOLOO6czatQYFFsxlsxvvVKX\nXVVVyr/P/SVpDeTuu+8JmCQOri/QefMWgapiy9nf7PK3lT3FHbkWUlP7s2zZqhY/Er/ataPvuLj4\nFjsnwJ0MhpazgkFwEYm8gX76yVXUQ9vEddSGxBC0EQZ2795JZuYFd4bmE5IkMXfuQtLTByKb87Bm\n7fF4XXbzoQLsl810794zYCuU9euXRmpqf2Rzbo3lU41lPV2C7VwZHTt2YsWK1a0uiV3bvUuUHa1b\n+/au2g2iWE7LE3jfhD5QVFTI8eNH0QTFXLdJSkNIkkRw72hUVeW99/7u5gh9Q6PRsHTpSpKTu+Es\nvYA9z3PlaK3nSrGeLqVt23YBvy66sga8Pe8nVLVptfgduRbMhwqJiIzkgQceaZVfzlc3AgGIiWn8\nba/WpLKam5jo1vKIRN4An3/+b1fv8cik+jeugz7ehC42iIMHDwRkDfbrcdVlf5C4uHjsBUdxlLr/\naoOz2EbFgQKCg4NZvfrhgF86k5DQ1nVbwl6Oowl17BW7TPkPeWg0Gu6/70GioqI9EKX/u7o1J9Bq\n34eGcjhcqyXEPfKWRyTyemRnZ/H55/+HpDOhj+jcrH1JkkRIH9dZ8T/+8beqUoCBLiwsnPvvfwiD\nwYgtay+yrcRt+1adCuV7c0FRWb78/hYzmWnSpDsxGoOwFxxBVZyNem3Fj/koFidTptzVqpdbaTSa\naklJlB2tm91uAyAoqPVdvWnpRCKvg91u5/X/+X/IshNj/IA6m6Q0lC7KiLFTGJmZF9i+/Ss3ROkf\nEhPbc88996IqTqyXvnPb5Dfz4ULkcgfjx9/ud1XbmiM8PIIxY8ahOq04amnJeT32XDP2SxUkJ3fz\n67Xz3nL1qPza6mVCdTabK5GLS+stj0jktZBlmT//eTPnfj6LLqJzrS1LmyK4dxSSXsO2bf+gtNT3\nFdLcJT190C8z2Uuw5f3U7P05Cq1Yz7q6md155ww3ROhfxo2bgNFoxF5wHFWt/8RHVVXMBwurJhoG\n4mQ/d7u6HGtISIgPI/F/VqsVECPylkh8E1yHw2Fn8+aX2bdvD1pTG4ISbnTrMidNkA5TzyjMZnOL\nmfhWacaMuSQktMVReBLZkt/k/aiqivknV9Wuu+9e0uLqhYNrBDly5GhUpwVnyfl6t7dfLEcutTN0\n6Ag6ders+QADQHj4lURuMgX23AlPqxyRi3vkLY9I5NcoKMhnw4b/Zv/+79EGx2HqOLLBl9Qtx4sp\n+uwCRZ9dwHyksMbPS3dmVf3ceqoEdBI7dnxTVfq1JTAajdx99z0AWLP2NXlWtv1yBc4iG+npA+ne\nvac7Q/QrY8eOd81gLzxZ5/I9VVWxnC5BkiQmTbrTixH6t+DgK6NwMdKs25VELt6nlkYk8qvs27eX\n9esf59w51+V0U4cRSBoPjQQl0EW6zozfeusvOJ2Nm/Dkz7p378nQoSNQbMU4Sn5u9OtVVcVyvBhJ\nkpg6daYHIvQfMTFtSEtLR7EVo1hrbxHrLLIhF9vp338AsbFxXozQv129gkEUOqlb5WQ3MSJveVpX\nBYlalJaWsHXrW+zduwtJ0mJMSEcf2bXRl9NNPSIxpdQ+czZ8aNsaz5Xvz+PyuUt88cVnjB8/sdGx\n+6upU2ewZ+8u7HlH0Id3btREQUeeBbnEzo03DiYhoeZ71tLcfPNofvhhL/aiM5hq6XNvv1gOwKhR\nY7wZmt+7enTZEm+/eIJI5C1Pqx6RK4rC119/zn/910Ps3bsLjSmG4C7jMEQle630Z3DvaDRGLR/8\n632Kioq8ckxviIqKZszocahOM46Sc416re1sGQC33jrBA5H5n549exMdHYNclnndpWiqqmLPMmMy\nmejRo7cPIvRfVyclnU4k8oYQl9ZbnlabyE+dOsHTTz/Jli1/xWpzYIwfQHCn0WiM4fW/2I00Ri2m\nXlHYbTbee+8drx7b08aOvQ2tVouj8ESDy7cqNhl7tpnE9h1ISurq4Qj9g0ajYciQoaiKA2f55Ro/\nl0sdKGYnqalpra4Ma32urvDXmurMN4cYkbc8rS6RFxYW8Kc/vcKGDb/h/Pmf0YV3IjhpAobobkiS\nb94OY+ewqjrsFy6c80kMnhAVFcXAgUNQ7KXI5ob1YrdfqgBFZehNIwKqIUpz3XjjYIDr1l93FrqW\nDbXkSX9NFRZ2Ze24WI7XMIFc3li4vlbzyXc47Hz00Qc8/vhD7NnzHZqgaII7jcGUOASN3uTT2CRJ\nIriPqw77Bx+0jO5olUaMGAWAo+Rsg7a3X64A4MYbB3ksJn/UoUMn2rSJRS7PqrGm3FnomqTUtWuK\nL0Lza9269fB1CAHHYBC3IFqaVnGd7tixI7z55p/Jzc1B0gUR1HYguogufjXi08eZ0EUbOXDgBy5d\nyiQx0X0FaHwpJaU7MTFtKCy6VG/RE8Wh4Mi30qlT51bXAEOSJPr1S+PLL/+DbKk+e91ZYken09Gu\nXaKPovNfvrqKFsjEiLzladGJ3Gaz8c47b5GR8bXrCY0O0KDYy2skcfOF7Sj2KzXCtcYoTB2GV9vG\nmvMjzrKLV56QtIR2vd0tsUqShKlbJGW7c/jqq8+ZP3+RW/braxqNhgEDbuTzz/+NXJFb57bOPAso\nKqmpaV6Kzr/06tXXlcjLs6s9r1Q4aBvXTtwDFtxCzO5veVrs6WxW1mWeeebJX5K4hKQNQtIawH8G\n4TXoE4LRBGnZs+e7FrWuvH//AQA4y7Pq3M6eawGgd+++Ho/JH3Xv3gNJkpAtV+YTKDYZ1aG0imV4\ngndotS16/NYqtch/0UuXMtm48b+pqChHH5WCMa5/veuYgzuOrHe/QfFpEO+50aKkkTC0C8F8tpST\nJ4/Tq1cfjx3Lm5KTU9DpdMjm+kfkBqOx1Xb0Cg4OITGxA5mXLqEJcjUDUSyuE7rWdqtB8Byx8qHl\naXH/oqWlJfz+9xuoqCjHmJCOIcp7ScFyvBjrmdqboITdlIAuvO77U/IvX9wnThxrMYlcrzeQnNyN\n48eP1rqNYnUilzno0btvq/6iSUrqSmbmBVSna4KbYnHNKxC9toXmuv32yezYsZ24uHhfhyK4WYu7\ntP7ppx9SUlKEIbavV5O4u2iCXEmsJS1DA+odZTsKxBIrgE6dugCgOl23GRSr68QuMlL02haaZ9q0\nmbzwwiuYTL5dpSO4X4sb+mRkfIOkM2GI9v6ylPpKtDZEaFob7JcqyMnJrn/jANK5c1KdP3fmi0QO\n0L59B9f/qK4ErthcI/Kr23UKQlOJtfYtk1cTucPh4PHHH+fSpUvY7XZWrFhBcnIyjz32GJIkkZKS\nwrp165r8YbPb7VitFpA0VJz9pM5tTR1GojVG1LlNjVnq16GPqDtBNYXGqKGsrOX0KYerElQtHPlW\n9Hp9vQm/pWvbtvoSM9Xm6h4nErkgCLXx6unZhx9+SGRkJFu3buV//ud/ePrpp9mwYQNr1qxh69at\nqKrKl19+2eT963Q6QkPDQFWgYRVB/ZNWg91u93UUbhUXF1/rbFnFLiOX2OnaNaXVL40JDQ11fYZ/\nodgrR+Rhtb1EEIRWzqsj8vHjxzNu3Liqx1qtliNHjjBw4EAARowYwc6dOxk7dmyT9q/RaEhPH8g3\n33yJIbY3hsjm1epu6Cx1W+7BZh2nJtWvitW4g0ajITY2luzsmkvQHHmuy+o9evTydlh+KTY2jvJy\nV+MY9ZdEHhoa6suQBEHwY14dkYeEhBAaGkp5eTmrV69mzZo1qOqVpBUSEkJZWVmzjjFx4hSMRiP2\n3J9Q7OXuCNvrVKfaIhsb1NZH25FrBmgxs/Sbq02b2CsPFFefbVGNSxCE2nh9sltWVharVq1izpw5\nTJo0ieeff77qZxUVFYSH138vMCoqGJ3u+uvCY2PDWL58OS+//DKWzG8J7jQGSRtYl2tVu0JEXASx\nsS3rcmq7dgkcOvRTtedUVcWRY8EUbGLgwP6iehmQmJjA999feRweHt7iPgvuotFcuQUl3iOhtfJq\nIs/Pz2fx4sU89dRTDBkyBIBevXqxZ88eBg0aREZGBoMHD653P0VF5jp/3r//YEaPPs6XX/4Hy6Ud\nmDqMQJICI0GoiopqlwkJCSMvr3lXJ/yNyVTzi1Ypd7Xo7HXDAAoL6/53bS0MhpBqj4ODQ1rcZ8Fd\nCgquTAoV75HQktV1ourVS+uvvfYapaWlvPrqq8yfP5/58+ezZs0aNm3axMyZM3E4HNXuoTfHrFnz\n6d9/AHJFDtas7xvcD9vXKit5RUfH+DgS9wsPr7lKwJ7tSt6pqf29HY7fioio/j6FhIj747WR5bob\n8QhCa+DVEfkTTzzBE088UeP5t99+2+3H0mq1LF9+P7/73TP8/PMZ7PpQjLH+fw9WqXAl8mr3SVuI\n6828tmeZkSSp1TZKuZ5rl5qJGeu1UxTF1yEIgs+16OoARqORBx54mDZtYrHnH8ZRlunrkOolVzgA\nWmQZxeDg6peMFZuMs8BKly5JNUahrdm1M9RDQkQir42qikQuCC06kYPrcu599z2IXm/AdnkPiqPC\n1yHVSS5vyYk8uNpjR44ZVEhLS/dRRP7p6nXkIEbkdQmQO2aC4FEtPpEDdOzYiXnzFqIqDqyXd/v1\n/fLKRB4f3/LaVgYFBVV7bM9y3R/v3/8GX4Tjt6494bk2sQtXJCS0JTU1jSVL7vV1KILgMy2u1npt\nhg0byYED+/nxx304is9iiGpesRhPkcscBAeHtMhRmMFwJZGrimvZWWxsHO3aJdbxqtYnKKh6U4uW\n+FlwF41Gw5o1j/g6DEHwqVYxIgeQJIl58xZiDArCnvcTqmzzdUg1qIqKUuGgbdt2La6yG4DBcGU9\nvzPfiupU6NdvQIv8XZvj2l4DYkQuCEJdWk0iB1dP58l3TEOV7djyDvk6nBrkMgeokJjY3teheITB\ncKU6mT2nctlZP1+FEzBEIhcEoS6t5tJ6pTFjxpGR8RXZ2adxlmWC5DqX0Yd3xhiXWm1b84XtKPaS\nqsdaYxSmDsOrbWPN+RFH8VkALMeLsZ5xFagwdggluHd0tW1Ld2a5knXl/iIMhA9JqHosl7qqVCUm\n1t0pLFBd3TTFkWtBp9PRrVvrblvaEOLSuiAIdWlVI3JwdUibNWs+AKps96suac5i1+X+jh07+TgS\nz9BoNOh0OlSHq9tZcnK3aqN04fpEQRhBEOrS6kbk4KoilpaWzo8/7sMY2wd95PV7YAd3HFnvvoLi\n05AkLfaCo5h6RGJKiax12/Chdc9EdxbakCSJTp261HvcQBUcEkJpiesqR0pKdx9HExjEyY4gCHVp\ndSPySnPmLMBoNGLLPYDitPg6HFRZwVlko337jjWWabVUXbum+DqEgCAmAwqCUJdWm8hjYtpw112z\nUWW7X9Rid+RbQVHp2bP19OTu3LnlXnkQBEHwllabyAFGjRpDz569kcsv4yg+49NYHL80D+nbt3U0\nDwmPiLhuExVBEAShcVp1ItdoNCxZci/BwSHYc39EtpXU/yIPUBUV+6UKQkJC6d69Zc/itttcE/oS\n27XMJXbuptO1ymksgiA0QqtO5OBqF7po0TJURcZ66TtUxen1GBzZZhSrzMCBg1v8F7fVagVaZi15\nT9Dr9fVvJAhCq9bqEznADTfcyKhRY1FsJdhy9nv9+JbTrisBo0aN8fqxfaUltmn1BJ1OJHJBEOom\nEvkvZs2aS4cOnXAUn8VRcs5rx3XkW3HmW+nTpx/t23f02nF9LSoquv6NBDEiFwShXiKR/0KvN7By\n5WqMQUHYsvd55X65qqqYDxcAcMcdd3r8eP4kIqL29fbCFVqt1tchCILg50Qiv0p8fFuWLF6Oqjix\nZu5AlR31v6gZbOfLcRbaSE8fRHJyN48ey9+IsqN1q6zmdm1LU0EQhGuJRH6N9PRBjBt3O4q9zKO9\nyxWLE/PhQoxGI7NmzfPIMfxZcHCIr0Pwa5GRUYC4BSEIQv1EIr+Ou+6aRY8evXGWX8LugS5pqqpS\nvj8P1S5z112ziY6Ocfsx/J3JZKp/o1ZMUWRATHYTBKF+IpFfh1arZeXK1bRpE4e94KjbJ79ZT5Xg\nyLHQp08qt9wy1q37DhRGY+soQ9tUDofrto6Y7CYIQn1EIq9FaGgYa9Y8gslkwpq1F6c51y37deRb\nMB8pIjw8giVLVrTaOtotfb18c8ly5YhcvE+CINRNJPI6tGuXyKpVa9FIYM3c0eyZ7LLFSfmeXDSS\nxIoVq4mIECVKhetzOl2FicSsdUEQ6iMSeT169erjqvwm27FezGhypzRVVijblYNik5k5c16LL8Uq\nNE/lPXKtVozIBUGom0jkDTB06AimTLkLxVGB5eK3jS7j6prclo9cbGPo0BGMGTPOQ5H6v5SU7qJ9\naQPExSUAEBoa6uNIBEHwd+J0v4EmTbqTvLxcdu7MwHp5D0GJNzX4/rb1dAn2i+V06dKVBQsWt9r7\n4gCPPvqkr0MICHffvYRPPvmw1U6GFASh4cSIvIEkSeLuu++hW7ceOMsu4ig83qDXOfIsmA8XEh4e\nwX33PYheb/BwpP5No9Gg0YiPXX06duzMihWrCQsL93UogiD4OfGN2gg6nY4VKx4gIiIKW+5BZEtB\nndsrVifle3PRSBpWrVpDVFSUlyIVBEEQWguRyBspIiKC5ctXAaqr8tsvk5Kupaoq5fvyUGwyM2bM\nISWlu3cDFQRBEFoFkciboEePXowefSuKvQxH0anrbmM9U4oj10Jqahpjx97m5QgFQRCE1kIk8iaa\nMuUugkNCsBccRVWrj8plswPLkUJCQkJZtGhpq57cJgiCIHiWSORNFBISypjR41BlO3JF9apv5oOF\nqLLKrFnzRLtOQRAEwaNEIm+GkSNHI0kSiq2o6jlHoRX75QqSkpK56abhPoxOEARBaA1EIm+GqKgo\nunZNrvac5XgxANOnzxaX1AVBEASPE4m8ma4utSqXO3Fkm+naNUWUYBUEQRC8QiTyZurUqUvV/9su\nlAGIalyCIAiC14hE3kyVNbEBkFX0ej0DBqT7LiBBEAShVRGJvJmio6OrPe7duy9GY5CPohEEQRBa\nG5HImykkpHp3qh49evsoEkEQBKE1Eom8ma6dmZ6U1NVHkQiCIAitkUjkbpaY2N7XIQiCIAitiEjk\nbmYyBfs6BEEQBKEVEYncjdLSbvB1CIIgCEIrIxK5G2i1WgASEtr5OBJBEAShtRGJ3A1MJhMAVqvF\nx5EIgiAIrY1I5G4QFFSZyK0+jkQQBEFobUQid4OgIFcBGJHIBUEQBG8TidwNjEYjAHa7zceRCIIg\nCK2NSORuoNcbALDb7T6ORBAEQWhtdL4OAEBRFNavX8+JEycwGAw888wzdOrUyddhNZherwdEIhcE\nQRC8zy9G5F988QV2u51//OMfPPTQQ2zcuNHXITVK+/YdAejQIXBOPgRBEISWwS9G5D/88APDhw8H\noH///hw+fNjHETXOhAmTMBgM3HzzaF+HIgiCILQyfpHIy8vLCQ290kVMq9XidDrR6a4fXlRUMDqd\n1lvh1Ss2Nox77lno6zAEQRCEVsgvEnloaCgVFRVVjxVFqTWJAxQVmb0RliAIgiD4hdjYsFp/5hf3\nyAcMGEBGRgYABw4coFu3bj6OSBAEQRACg1+MyMeOHcvOnTuZNWsWqqry7LPP+jokQRAEQQgIkqqq\nqq+DaKy8vDJfhyAIgiAIXuP3l9YFQRAEQWgakcgFQRAEIYCJRC4IgiAIAUwkckEQBEEIYCKRC4Ig\nCEIAE4lcEARBEAKYSOSCIAiCEMACch25IAiCIAguYkQuCIIgCAFMJHJBEARBCGAikQuCIAhCABOJ\nXBAEQRACmEjkgiAIghDARCIXBEEQhAAmEnkjXbx4kdWrVzNjxgwWLFjAsmXLOHXqFJs2beKdd96p\n2m7Dhg2sXLkSu93uw2gb59SpUyxbtoz58+czbdo0Xn75ZRq7OvEf//gHDoejSccfOnRok15X6ZZb\nbsFmszVrH3W5ePEi999/P/Pnz2fWrFmsX7+e8vLyWrf//PPPycnJqfXn9913X43n3nnnHTZt2tSg\nePbs2cPatWsbtO31ZGZmMmPGjCa/vjF8/dmqz+uvv87BgwerPWez2bjllls8crxr+dtnqyHWrl1b\n4/stIyODxx57zG3HaKzMzEwGDBjA/Pnzq/575ZVXvB7H2rVr2bNnj/cOqAoNZjab1dtvv13dv39/\n1XM//fSTOm/ePPXll19Wt27dqiqKov73f/+3+tBDD6kOh8OH0TZOSUmJOnHiRPXnn39WVVVVnU6n\numrVKnXr1q2N2s+oUaNUq9XapBhuuummJr3OHceuj8ViUSdOnKgeOHCg6rlt27apy5Ytq/U18+bN\nU0+fPt2o42zdulV9+eWXG7Tt7t271TVr1jRq/1e7ePGiOn369Ca/vqH84bPVFFarVR01apTHj+OP\nn62m2r59u/roo4969Bh18dZnuj5r1qxRd+/e7bXj6bx3yhD4vv76awYPHkxaWlrVc6mpqbz11lu8\n8sorqKrKunXrcDqd/O53v0OjCZwLHl9++SWDBg2ic+fOAGi1Wp577jn0ej0vvPAC33//PaqqsnDh\nQm677Tbmz59Pjx49OHXqFOXl5bz00kt899135OXlsXbtWl599dVaXxcVFUVpaSl/+ctf0Gq1VTHY\n7XbWrl1LVlYW3bt3Z/369eTk5LB+/XpsNhvFxcWsWrWKMWPG8PXXX1edaffq1Yvf/OY3Vft55513\n2LlzJ3/4wx8wGAxueX+++eYbbrzxRvr161f13J133sk777zDr371KyZOnMiIESPIyMjg008/Zfz4\n8Rw7doxHH32UN954g4cffpjy8nKsViuPPPIIgwYNYujQoezcuZN9+/bx7LPPEhERgUajoX///gBs\n2bKFjz/+GEmSmDBhAgsWLKgR1/nz51myZAlFRUXMnj2b6dOns3fv3qr3xmq18txzz9GlSxdeffVV\nvvjiC2RZZvbs2QwbNgwAWZZ57LHHSElJYdmyZW55v67mD5+tsWPHkpaWxvnz5xk8eDBlZWUcPHiQ\nLl268Pzzz/PYY48xYcIEbrjhBh5++GFKS0vp2LGj29+L6/HHz9aePXt4/fXX0ev1ZGdnM2vWLHbv\n3s3x48dZsGABc+bM4ZZbbuHf//43mZmZPP7445hMJkwmExEREV553xpj48aN/PDDDwBMnDiRu+++\nm8cee4zi4mKKi4uJiopi5cqV9O3bl3HjxvHwww8zduxYFi9ezIYNG/j888/5z3/+g9PpJCwsjE2b\nNvHxxx/z/vvvoygKq1ev5uzZs7z77rvExsZSUFDg1d9PJPJGyMzMrPbHvWLFCsrLy8nNzSU9PZ33\n3nuPLl26oNVqkSTJh5E2Xm5uLh06dKj2XEhICNu3byczM5O///3v2Gw2ZsyYUXUJPDU1lV//+te8\n+OKLfPLJJyxbtozNmzfz4osv1vm6SZMmMXbs2BoxWK1WHn74YRITE3nggQf46quvMJlMLFq0iEGD\nBrF//342bdrEzTffzNNPP827775LTEwMr7zyCtnZ2YDrC+rYsWO89NJL1b7Im+vixYvX/WJv3749\n+/btY+LR4xsWAAAKXUlEQVTEidWev/nmm+nZsyfr168nKyuL/Px83njjDQoKCjh37ly1bTds2MAL\nL7xAly5dWLduHQCnT5/m008/ZevWrUiSxMKFCxk2bBhJSUnVXutwONi8eTOKojB58mRGjx7NqVOn\neP7554mPj+e1117js88+Y+TIkWRkZPDuu+9it9t54YUXGDp0KE6nk4cffpj09HTmzp3rtvfrav7w\n2bp06RJvvvkmsbGxDBw4kHfffZcnn3yS0aNHU1paWrXdP//5T7p168batWv56aefvHJ51F8/W9nZ\n2XzwwQccOXKEBx54oOpy/n333cecOXOqtnvppZdYvXo1Q4cO5fXXX+fs2bNuemea5vTp08yfP7/q\n8dSpU8nMzOR///d/cTqdzJkzh8GDBwMwePBgFi5cyAcffEBGRgaRkZEYjUZ27tzJ4MGDsdlsxMbG\nUlxczBtvvIFGo2HJkiUcOnQIgPDwcDZv3kxZWRnr16/no48+QpIkpk6d6tXfWSTyRkhISODw4cNV\njzdv3gzAjBkzkGWZ0aNH89RTT7F69Wo2b97MypUrfRVqo7Vr146jR49We+7ixYscOnSII0eOVP1h\nOJ1OLl++DLhGwuB6X/Lz86u99uTJk7W+rkuXLgC8+OKL7N+/H4A33niDdu3akZiYCEBaWho///wz\nI0eOZPPmzbz33ntIkoTT6aSoqIjw8HBiYmKA6vcDd+3ahVardWsSB4iPj69xDxXg3LlzpKenVz1W\nr3PfNyUlhblz5/Lggw/idDqrfckA5OTkVL0nAwYM4MKFC5w8eZLLly+zcOFCAEpKSrhw4QLPPfcc\nZrOZbt26ceutt9K/f/+qqw5du3YlMzOT+Ph4fvvb3xIcHExOTg4DBgzg559/JjU1Fa1Wi8lk4okn\nniAzM5MTJ04QGhqK2Wx211tVgz98tiIjI2nXrh0AwcHBJCcnAxAWFlZtXsWpU6cYPnw4AP369UOn\n8/xXpL9+tlJSUtDr9YSFhdGxY0cMBgMRERE15qGcOnWK1NTUqmP4OpEnJyezZcuWqsd//vOfSU9P\nR5Ik9Ho9/fr148yZM8CVz8uoUaNYuXIlUVFRLF26lL/+9a9kZGQwatQoNBoNer2eBx98kODgYLKz\ns3E6ndVef/bsWZKTk6v+FivfD28JnGu/fmD06NHs2rWLAwcOVD13/vx5srOzkSSJlJQUAJ5++mne\ne+897052aKZRo0bx7bffcuHCBcA10tu4cSPh4eEMGjSILVu28Oabb3LbbbfRvn37WvcjSRKKopCU\nlFTr6yqvVqxdu5YtW7awZcsWtFot2dnZ5ObmArB//35SUlJ46aWXmDx5Ms8//zyDBg1CVVViYmIo\nLS2luLgYgGeeeabqi/DVV18lPDy82sRDdxg9ejTfffddtS/cd999l+joaIKCgsjLywOolrAkSUJV\nVU6cOEFFRQWvv/46Gzdu5Omnn66279jY2Kovlsoz/aSkJJKTk3nrrbfYsmULU6dOpVu3bvzpT39i\ny5YtPPnkk1XHczqdmM1mzpw5Q8eOHXniiSd49tln2bhxI3FxcaiqSlJSEkePHkVRFBwOB4sWLcJu\nt9O7d29ef/11PvzwQ44fP+7W96ySP3y2GnqFLCkpqervu/K99TR//Ww15j378ccfAaoNdPxF165d\nqy6rOxwOfvzxRzp16gRc+R0jIiIICgri3//+N8OHD6ddu3a8+eab3HrrrRw/fpwvvviCP/7xjzz5\n5JMoilJ1UlV5+7RDhw6cPn0aq9WKLMscO3bMq7+jGJE3QkhICJs3b+aFF17g97//PU6nE51Ox9NP\nP13tjzAiIoLnnnuOhx56iG3bttGmTRsfRt0woaGhbNy4kSeeeAJVVamoqGDUqFHMnz+fjRs3MmfO\nHMxmM2PGjCE0NLTW/aSnp7Ns2TLeeust9u7d2+DXAURGRvLMM8+Qk5NDWloaI0eOpKysjN/+9rf8\n6U9/om3bthQVFaHRaFi3bh3Lly9Ho9HQq1cv+vbtW7WfJ554gunTpzNkyJCq+7LNFRISwmuvvcaz\nzz5LcXExsizTvXt3/vCHP3D+/Hkef/xxPvroo2rHS0tL41e/+hWbN29m7969fPDBB+j1elavXl1t\n388//zyPPvooISEhhISEEBERQY8ePRgyZAizZ8/GbreTmppKfHx8jbiMRiNLly6ltLSU+++/n8jI\nSCZPnsyMGTMIDw+nTZs25Obm0rNnT4YPH87s2bNRFIXZs2dXjR6CgoJYv349jz76KO+++67b5hVU\n8ofPVkPNnTuX//qv/2L27NkkJSWh1+vdst+6+Otnq6HWrVvH2rVr+ctf/kJ0dDRGo7HJ+/KEUaNG\nsXfvXmbOnInD4WD8+PH07t27xnajR49m27ZtREZGMmzYMLZu3UrHjh2xWCyYTCamTp2KwWAgNja2\nasBRKTo6mgceeIBZs2YRHR2NyWTy1q8HiO5ngiAIghDQxKV1QRAEQQhgIpELgiAIQgATiVwQBEEQ\nAphI5IIgCIIQwEQiFwRBEIQAJhK5ILRwmZmZ9OnTh8mTJzNlyhRuv/12Fi1aVFUNr6G+/PJLXnrp\nJQBefvll9u3bB8Cvf/3rqjXKgiB4n1h+JggtXGZmJgsWLOCrr76qem7jxo3k5ubyhz/8oUn7nD9/\nPvfddx+DBg1yV5iCIDSRGJELQis0aNAgTp06xYEDB5g+fTp33HEHd999N+fPnwfgr3/9K3fccQdT\npkzhqaeeAmDbtm089thjfPDBBxw+fJgnnniCEydOMH/+/Koqhq+99hoTJkxg0qRJbNy4EVmWyczM\nZMqUKTzyyCNVDSsqq/IJgtB8IpELQivjcDj4v//7P/r06cODDz7Ik08+yYcffsisWbN48MEHkWWZ\nP/3pT7z//vts27YNh8NRrff1lClT6NOnD8888wzdu3even779u189dVXvP/++/zzn//k/Pnz/P3v\nfwfg+PHjLFq0iI8//pjw8HA++ugjr//egtBSiUQuCK1Abm4ukydPZvLkydxxxx2oqsrUqVMJDw+v\navBw2223ceHCBcxmM2lpadx111288sorLFq0qEElPHfv3s3tt9+OyWRCp9Mxbdo0du3aBUBMTExV\nI5SUlBRKSko898sKQisjaq0LQisQFxfHv/71r2rPXa9JiqqqyLLMq6++yoEDB8jIyOCee+7h97//\nfb3HUBSlxnOVTUeurr9d2fBDEAT3ECNyQWilkpKSKC4urmr48+mnn9KuXTsURWHChAl069aNBx54\ngKFDh3LixIlqr9VqtciyXO25wYMH88knn2C1WnE6nbz//vtVfZ8FQfAcMSIXhFbKYDDw4osv8vTT\nT2OxWIiIiODFF18kOjqamTNnctddd2EymejSpQvTpk3js88+q3rt8OHDWbduHc8991zVc6NGjeLY\nsWNMmzYNp9PJsGHDmDdvXqOXuQmC0Dhi+ZkgCIIgBDBxaV0QBEEQAphI5IIgCIIQwEQiFwRBEIQA\nJhK5IAiCIAQwkcgFQRAEIYCJRC4IgiAIAUwkckEQBEEIYCKRC4IgCEIA+/9bzPBMB40ONgAAAABJ\nRU5ErkJggg==\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x29e62bd9668>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.violinplot(x='Position', y='penalties', hue='nationality', data=fifa_pen, split=True, inner='quartile', order=pos_order)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Wow, it seems like England really does have the edge over Germany in penalty stats for offensive players.\n",
    "\n",
    "PKs are a two-sided coin though, and goalkeepers play a huge role in the outcome. Let's see if there are any differences in the overall quality of GKs between these two countries."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x29e64b58cf8>"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x29e64ab17f0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.violinplot(x='nationality', y='overall', data=fifa_pen[fifa_pen.Position=='GK'], inner='quartile')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This is quite illuminating. The median overall metric for German GKs is at the same level as the 75th percentile overall metric for English GKs. Also note that England doesn't seem to really have any world-class GKs at the top of the violin plot. Since only the very best GKs per country really matter during an international tournament, let's see how the top GKs from each country compare."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>club</th>\n",
       "      <th>overall</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>M. Neuer</td>\n",
       "      <td>FC Bayern Munich</td>\n",
       "      <td>92</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>79</th>\n",
       "      <td>B. Leno</td>\n",
       "      <td>Bayer 04 Leverkusen</td>\n",
       "      <td>85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>80</th>\n",
       "      <td>M. ter Stegen</td>\n",
       "      <td>FC Barcelona</td>\n",
       "      <td>85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>104</th>\n",
       "      <td>T. Horn</td>\n",
       "      <td>1. FC Köln</td>\n",
       "      <td>84</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>117</th>\n",
       "      <td>R. Fährmann</td>\n",
       "      <td>FC Schalke 04</td>\n",
       "      <td>84</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>240</th>\n",
       "      <td>O. Baumann</td>\n",
       "      <td>TSG 1899 Hoffenheim</td>\n",
       "      <td>82</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>353</th>\n",
       "      <td>K. Trapp</td>\n",
       "      <td>Paris Saint-Germain</td>\n",
       "      <td>81</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              name                 club  overall\n",
       "4         M. Neuer     FC Bayern Munich       92\n",
       "79         B. Leno  Bayer 04 Leverkusen       85\n",
       "80   M. ter Stegen         FC Barcelona       85\n",
       "104        T. Horn           1. FC Köln       84\n",
       "117    R. Fährmann        FC Schalke 04       84\n",
       "240     O. Baumann  TSG 1899 Hoffenheim       82\n",
       "353       K. Trapp  Paris Saint-Germain       81"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fifa_pen.loc[(fifa_pen['Position']=='GK') & (fifa_pen['nationality']=='Germany')][['name', 'club', 'overall']].head(7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>club</th>\n",
       "      <th>overall</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>288</th>\n",
       "      <td>J. Hart</td>\n",
       "      <td>West Ham United</td>\n",
       "      <td>82</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>320</th>\n",
       "      <td>J. Butland</td>\n",
       "      <td>Stoke City</td>\n",
       "      <td>81</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>376</th>\n",
       "      <td>T. Heaton</td>\n",
       "      <td>Burnley</td>\n",
       "      <td>81</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>502</th>\n",
       "      <td>B. Foster</td>\n",
       "      <td>West Bromwich Albion</td>\n",
       "      <td>80</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1057</th>\n",
       "      <td>J. Pickford</td>\n",
       "      <td>Everton</td>\n",
       "      <td>77</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1109</th>\n",
       "      <td>F. Forster</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>77</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1812</th>\n",
       "      <td>A. McCarthy</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>75</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             name                  club  overall\n",
       "288       J. Hart       West Ham United       82\n",
       "320    J. Butland            Stoke City       81\n",
       "376     T. Heaton               Burnley       81\n",
       "502     B. Foster  West Bromwich Albion       80\n",
       "1057  J. Pickford               Everton       77\n",
       "1109   F. Forster           Southampton       77\n",
       "1812  A. McCarthy           Southampton       75"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fifa_pen.loc[(fifa_pen['Position']=='GK') & (fifa_pen['nationality']=='England')][['name', 'club', 'overall']].head(7)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "These latest stats provide some deep insight. The 6 best German GKs are all ranked higher than J. Hart, the highest rated English GK. In addition to the mounting pressure the English players feel to break the PK curse, it can't help that they do not have a single choice for a world-class GK. On the other hand, the German players can keep their nerve, knowing they have a choice between some of the best GKs in the world."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Southpaws <a name=\"southpaws\"></a>\n",
    "Lefties make up roughly [10%](https://en.wikipedia.org/wiki/Handedness) of the population. However, it is well documented that in some sports, lefties make up a much larger proportion (e.g., 39% of hitters and 28% of pitchers [played left-handed](http://www.gamesensesports.com/knowledge/2017/3/17/righties-vs-lefties-the-importance-of-handedness-training-in-baseball-hitting) in the 2012 MLB season).\n",
    "\n",
    "In soccer, we expect to see higher than 10% of players as left-footed since being left-footed is an advantage when playing on the left side of the field. This is especially true for left wingers who race down the sideline in order to whip in a cross. Let's investigate the percentages."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.23624541513837946"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fifa[fifa.preferred_foot=='Left']['ID'].count()/fifa.shape[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We see that 23% of the players in the dataframe are left-footed, which agrees with our intuition. Let's see if there is any significant difference in the overall quality of players based on foot preference."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "preferred_foot\n",
       "Left     66.679840\n",
       "Right    66.121007\n",
       "Name: overall, dtype: float64"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fifa.groupby('preferred_foot')['overall'].mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "These scores are very close together, hinting that there is no discernable difference between the overall quality of left-footed player and right-footed players on average. However, in order to see if this difference of 0.5 is likely due to noise, our analysis must go one level deeper. Here, we use the [bootstrapping method](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)), in which we resample our players (with replacement). The advantage of the bootstrapping method is that it gives us intuition as to whether this 0.5 difference is statistically significant without having to assume any underlying distribution."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x29e664d26a0>"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\nw8yZM/H5558n1f0URREnn3xy5PNmxowZuO2224Z/P8UU8/3334vXX3+9GAgERKfTKT799NPiO++8\nI7788stDOv66664T//vf/4qiKIq33XabuGXLFinDHbH+ynnnnXeKn3zyiSiKorhmzRpx1apVBx3z\n2WefiXfeeacoiqK4adMm8YYbbhBFURTnz58v7t27VwwGg+JvfvMbsaKiIqZlGchIyvjuu++KDz/8\nsCiKotjW1iaecsopoiiKw3oPxNpIytnV1SWed955fc4Vr/dSFEdWzp7uv/9+8e233xZFURSffPJJ\nceXKlbEIe9j6K2eYzWYT58+fLzY1NR10zCuvvBJ53scffyw+9NBDotfrFU877TTRZrOJHo9HvOCC\nC8Tm5uaYlmUwIynnU089Jb766quiKIri7t27xfPPP18UxeS7nzU1NeL1119/0GMjuZ8p14T+zTff\nYOLEibjxxhtxww03YM6cOaioqMB//vMfXH755bj77rvhdDr7Pfbzzz+H2WzGSSedBADYunUrVqxY\ngQULFmD58uWxLMYh9VfOjRs3oqmpCVdeeSU++uijPt9gN2zYECnbjBkzUFFRAafTCa/Xi8LCQgiC\ngBNPPBFr1qyRo0h9jKSMZ555Jm655ZbIz0qlEgCG/B6Qw0jKuWPHDrjdblx99dW44oorsHnz5ri+\nl8DIyhm2ZcsWVFVV4ZJLLgEQ+tt87733cNlll2HZsmXw+/2xLMqg+itn2DPPPINf/epXyM3NPeiY\nnn+bJ598MtasWYPdu3ejsLAQ6enp0Gg0mDVrFtavXx/LogxqJOW88sorcemllwIAAoEAtFotgOS7\nn1u3bkVTUxMWLlyIa6+9FtXV1SO6nymXwNvb21FRUYGnnnoKDzzwAG6//XZMnz4dd9xxB958802M\nHz8ezz33XL/HLl++/KAmx7PPPhv3338//vznP2PDhg1YtWpVrIpxSP2Vs76+HmazGa+99hry8vLw\n0ksvHXSM0+mE0WiM/KxUKvs8ZjAY0NHREbNyDGYkZTQYDDAajXA6nbj55puxePFiABjye0AOIymn\nTqfDNddcg5dffjlyTDzfS2Bk5Qxbvnw5brzxxsjPJ5xwAu699168+eab6OzsxNtvvx2rYhxSf+UU\nRRFWqxVr1qzBBRdc0OcYp9MZ6Q4J37eej4Ufj6cvniMpp9lshk6nQ0tLC5YsWYJbb70VQPLdT4vF\nguuuuw6vv/46rr/++ki3wXDvZ8ol8IyMDJx44onQaDQoLS2FVqvFnDlzMG3aNADA6aefjm3btvU5\nrqqqCmazGUVFRQBCfRi//vWvkZWVBY1Gg1NOOaXf4+TSXzkDgQBOPfVUAMCpp56KioqKg44xGo1w\nuVyRn4PBYJ/HXC4XzGZzbApxCCMpIwA0NjbiiiuuwHnnnYdzzz0XQOi+H+o9IJeRlLOkpATz58+H\nIAgoKSlBRkYGAoFA3N5LYOT30+FwoLq6Gscee2zksQsvvBDjx4+HIAiYN29e3N/PtrY2rFy5Euec\nc06kVainnn+H4fvW399mzwQgt5GUEwB27tyJK6+8Ev/7/9u7e5DW2TCM43/RFIeCIhWlbkZcdDHt\n4vdQN8VFNxep4GgtWEUoohSKCAEHQUERxMHFwc3ZWixFh+Km6KCDGHRwqAaE8rzD4YTXD86hHU6N\n3r8tgQSu3iEXPElJNOqsuHy3eba3txMKhQAIBoNYllXSPH9cgQcCAY6Pj1FKYVkWtm0zOTnJ+fk5\nAJlMhra2tg/HnZyc0NfX52zn83mGhoZ4fn5GKUU2m3UK4Cv4LGcoFOLo6AiA09NTWlpa3hxjGAap\nVAqAXC5Ha2srXq8XTdO4vb1FKUU6nSYYDP7zPJ8pJePj4yPhcJhYLMbo6Kizf2Ji4q/XQLmUknN/\nf5/l5WUALMsin8/T0NDwZWcJpeX8vb+rq8vZVkoxPDzM/f094I551tbWkslk3txj/s8wDOd3SKVS\nBAIBdF3n5uaGp6cnXl9fOTs7o6Oj419G+aNScl5dXRGJRDBNk/7+fuB7znNtbY2dnR3g1+Muv99f\n0jx/5MdMVlZWyGazKKWIRqPU1dWRSCTQNA2fz0cikcDr9RIOh9nY2MDj8bC0tER3dzcDAwPOeQ4O\nDtjd3cXj8dDZ2cnU1FQZU330PmdzczPxeBzbtvF6vZimSU1NDbOzs0xPT9PY2Mji4iKXl5copUgm\nk+i6Ti6XI5lMUigU6OnpIRqNljuao9iM29vbHB4evvm3wObmJtfX159eA19FsTl9Ph/z8/Pc3d1R\nUVHBzMwMhmF86VlC8Tn9fj9bW1tUVVUxPj7unCedTrO6ukp1dTW6rhOPx9E0rXzB3nmfs7e3l8HB\nQfb29t6sivy+BxUKBebm5nh4eEDTNEzTpL6+3nlrWSnFyMgIY2NjZUz1UbE5I5EIFxcXNDU1Ab9W\nHtbX17/dPG3bJhaL8fLyQmVlJQsLC+i6XvQ8f2SBCyGEEG7345bQhRBCiO9AClwIIYRwISlwIYQQ\nwoWkwIUQQggXkgIXQgghXEgKXAghhHAhKXAhhBDChaTAhRBCCBf6D8PvNLziwSn8AAAAAElFTkSu\nQmCC\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x29e661066a0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "iterations=10000\n",
    "boot=[]\n",
    "for i in range(iterations):\n",
    "    boot_mean = fifa.sample(frac=1, replace=True).groupby('preferred_foot')['overall'].mean()\n",
    "    boot.append(boot_mean)\n",
    "    \n",
    "boot=pd.DataFrame(boot)\n",
    "boot.plot.kde()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It does appear that the difference, albeit small, is real. In fact, over the 10000 bootstrapping iterations, not once did the right-footers have a higher overall mean than the left-footers (as shown with the following code)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "((boot['Left']-boot['Right'])<0).sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's breakdown the left-footed percentages by nationality. We only consider countries that have 100 or more players in the dataframe."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0,0.5,'Percentage of Players Left-Footed')"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x29e66513a20>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fifa_sig = fifa.groupby('nationality')\n",
    "fifa_sig = fifa_sig.filter(lambda x:x['nationality'].count()>=100)\n",
    "\n",
    "fifa_left = pd.DataFrame(fifa_sig[fifa_sig.preferred_foot=='Left'].groupby('nationality')['ID'].count())\n",
    "fifa_left['left_perc']= fifa_left['ID'].divide(fifa_sig.groupby('nationality')['ID'].count())\n",
    "fifa_left_sorted = fifa_left.sort_values('left_perc')\n",
    "\n",
    "_ = fifa_left_sorted.left_perc.plot.bar(rot=90)\n",
    "plt.ylabel('Percentage of Players Left-Footed')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Glancing at the order of countries, there doesn't appear to be any geographic or political correlations with the percentage of left-footed players.\n",
    "\n",
    "Let's try to go one step deeper with a bubble plot.\n",
    "* On the x-axis, we take the average overall score for the best 11 players per country.\n",
    "* On the y-axis, we have the percentage of total players in the country that are left-footed.\n",
    "* The size of the bubble corresponds to the raw number of player (for the given country) that are ranked in the top 1500."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5,0,'Average Overall Rating if Top 11 Players')"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x29e663e27f0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fifa_best11 = fifa_sig.groupby('nationality').head(11)\n",
    "#calculate average overall raiting per coutnries best 11\n",
    "fifa_best11 = fifa_best11.groupby('nationality')['overall'].mean()\n",
    "fifa_left['Overall'] = fifa_best11\n",
    "#now we want to calculate the number per country in the top 1000\n",
    "fifa_top1000 = fifa_sig[fifa_sig.Rank<=1500].groupby('nationality')['ID'].count()\n",
    "\n",
    "#bubble plot\n",
    "plt.scatter(fifa_best11, fifa_left.left_perc, s=10*fifa_top1000, alpha=0.5)\n",
    "plt.ylabel('Percentage of Players Left-Footed')\n",
    "plt.xlabel('Average Overall Rating if Top 11 Players')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It is impossible to draw correlation/causation results from this plot. However, it is worthwhile to note that the 7 countries at the elite level (who's average overall score for their starting-11 is over 85) also have a higher than average percentage of left-footed players."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Similarity <a name=\"similarity\"></a>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "For fun, let's build a function such that when given a name, it returns the 5 players who are the most similar. The idea of similarity when it comes to soccer players is subjective, but we will be basing it solely on the subjective numeric stats. We will not include any categorical features such as club, league, nationality, position, etc. We also will not include objective physical features such as age, height and weight. There are two major steps to this process.\n",
    "* First, we perform principle component analysis (PCA). We will be using 45 different metrics to begin with, but many of these are highly correlated with one another. We will use PCA to reduce this number to 10. This reduction in dimension helps to reduce the bias possibly introduced by EA's selection of specific metrics that are similar. Note that these remaining 10 dimensions do not necessarily correspond to any specific metrics, but rather a correlated cluster of them.\n",
    "* Second, we perform the nearest neighbors calculation to find the closest neighbors based on the numbers in reduced dimensions."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>overall</th>\n",
       "      <th>potential</th>\n",
       "      <th>pac</th>\n",
       "      <th>sho</th>\n",
       "      <th>pas</th>\n",
       "      <th>dri</th>\n",
       "      <th>def</th>\n",
       "      <th>phy</th>\n",
       "      <th>international_reputation</th>\n",
       "      <th>skill_moves</th>\n",
       "      <th>weak_foot</th>\n",
       "      <th>crossing</th>\n",
       "      <th>finishing</th>\n",
       "      <th>heading_accuracy</th>\n",
       "      <th>short_passing</th>\n",
       "      <th>volleys</th>\n",
       "      <th>dribbling</th>\n",
       "      <th>curve</th>\n",
       "      <th>free_kick_accuracy</th>\n",
       "      <th>long_passing</th>\n",
       "      <th>ball_control</th>\n",
       "      <th>acceleration</th>\n",
       "      <th>sprint_speed</th>\n",
       "      <th>agility</th>\n",
       "      <th>reactions</th>\n",
       "      <th>balance</th>\n",
       "      <th>shot_power</th>\n",
       "      <th>jumping</th>\n",
       "      <th>stamina</th>\n",
       "      <th>strength</th>\n",
       "      <th>long_shots</th>\n",
       "      <th>aggression</th>\n",
       "      <th>interceptions</th>\n",
       "      <th>positioning</th>\n",
       "      <th>vision</th>\n",
       "      <th>penalties</th>\n",
       "      <th>composure</th>\n",
       "      <th>marking</th>\n",
       "      <th>standing_tackle</th>\n",
       "      <th>sliding_tackle</th>\n",
       "      <th>gk_diving</th>\n",
       "      <th>gk_handling</th>\n",
       "      <th>gk_kicking</th>\n",
       "      <th>gk_positioning</th>\n",
       "      <th>gk_reflexes</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>94</td>\n",
       "      <td>94</td>\n",
       "      <td>90</td>\n",
       "      <td>93</td>\n",
       "      <td>82</td>\n",
       "      <td>90</td>\n",
       "      <td>33</td>\n",
       "      <td>80</td>\n",
       "      <td>5</td>\n",
       "      <td>5</td>\n",
       "      <td>4</td>\n",
       "      <td>85</td>\n",
       "      <td>94</td>\n",
       "      <td>88</td>\n",
       "      <td>83</td>\n",
       "      <td>88</td>\n",
       "      <td>91</td>\n",
       "      <td>81</td>\n",
       "      <td>76</td>\n",
       "      <td>77</td>\n",
       "      <td>93</td>\n",
       "      <td>89</td>\n",
       "      <td>91</td>\n",
       "      <td>89</td>\n",
       "      <td>96</td>\n",
       "      <td>63</td>\n",
       "      <td>94</td>\n",
       "      <td>95</td>\n",
       "      <td>92</td>\n",
       "      <td>80</td>\n",
       "      <td>92</td>\n",
       "      <td>63</td>\n",
       "      <td>29</td>\n",
       "      <td>95</td>\n",
       "      <td>85</td>\n",
       "      <td>85</td>\n",
       "      <td>95</td>\n",
       "      <td>22</td>\n",
       "      <td>31</td>\n",
       "      <td>23</td>\n",
       "      <td>7</td>\n",
       "      <td>11</td>\n",
       "      <td>15</td>\n",
       "      <td>14</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>93</td>\n",
       "      <td>93</td>\n",
       "      <td>89</td>\n",
       "      <td>90</td>\n",
       "      <td>86</td>\n",
       "      <td>96</td>\n",
       "      <td>26</td>\n",
       "      <td>61</td>\n",
       "      <td>5</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>77</td>\n",
       "      <td>95</td>\n",
       "      <td>71</td>\n",
       "      <td>88</td>\n",
       "      <td>85</td>\n",
       "      <td>97</td>\n",
       "      <td>89</td>\n",
       "      <td>90</td>\n",
       "      <td>87</td>\n",
       "      <td>95</td>\n",
       "      <td>92</td>\n",
       "      <td>87</td>\n",
       "      <td>90</td>\n",
       "      <td>95</td>\n",
       "      <td>95</td>\n",
       "      <td>85</td>\n",
       "      <td>68</td>\n",
       "      <td>73</td>\n",
       "      <td>59</td>\n",
       "      <td>88</td>\n",
       "      <td>48</td>\n",
       "      <td>22</td>\n",
       "      <td>93</td>\n",
       "      <td>90</td>\n",
       "      <td>78</td>\n",
       "      <td>96</td>\n",
       "      <td>13</td>\n",
       "      <td>28</td>\n",
       "      <td>26</td>\n",
       "      <td>6</td>\n",
       "      <td>11</td>\n",
       "      <td>15</td>\n",
       "      <td>14</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>92</td>\n",
       "      <td>94</td>\n",
       "      <td>92</td>\n",
       "      <td>84</td>\n",
       "      <td>79</td>\n",
       "      <td>95</td>\n",
       "      <td>30</td>\n",
       "      <td>60</td>\n",
       "      <td>5</td>\n",
       "      <td>5</td>\n",
       "      <td>5</td>\n",
       "      <td>75</td>\n",
       "      <td>89</td>\n",
       "      <td>62</td>\n",
       "      <td>81</td>\n",
       "      <td>83</td>\n",
       "      <td>96</td>\n",
       "      <td>81</td>\n",
       "      <td>84</td>\n",
       "      <td>75</td>\n",
       "      <td>95</td>\n",
       "      <td>94</td>\n",
       "      <td>90</td>\n",
       "      <td>96</td>\n",
       "      <td>88</td>\n",
       "      <td>82</td>\n",
       "      <td>80</td>\n",
       "      <td>61</td>\n",
       "      <td>78</td>\n",
       "      <td>53</td>\n",
       "      <td>77</td>\n",
       "      <td>56</td>\n",
       "      <td>36</td>\n",
       "      <td>90</td>\n",
       "      <td>80</td>\n",
       "      <td>81</td>\n",
       "      <td>92</td>\n",
       "      <td>21</td>\n",
       "      <td>24</td>\n",
       "      <td>33</td>\n",
       "      <td>9</td>\n",
       "      <td>9</td>\n",
       "      <td>15</td>\n",
       "      <td>15</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>92</td>\n",
       "      <td>92</td>\n",
       "      <td>82</td>\n",
       "      <td>90</td>\n",
       "      <td>79</td>\n",
       "      <td>87</td>\n",
       "      <td>42</td>\n",
       "      <td>81</td>\n",
       "      <td>5</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>77</td>\n",
       "      <td>94</td>\n",
       "      <td>77</td>\n",
       "      <td>83</td>\n",
       "      <td>88</td>\n",
       "      <td>86</td>\n",
       "      <td>86</td>\n",
       "      <td>84</td>\n",
       "      <td>64</td>\n",
       "      <td>91</td>\n",
       "      <td>88</td>\n",
       "      <td>77</td>\n",
       "      <td>86</td>\n",
       "      <td>93</td>\n",
       "      <td>60</td>\n",
       "      <td>87</td>\n",
       "      <td>69</td>\n",
       "      <td>89</td>\n",
       "      <td>80</td>\n",
       "      <td>86</td>\n",
       "      <td>78</td>\n",
       "      <td>41</td>\n",
       "      <td>92</td>\n",
       "      <td>84</td>\n",
       "      <td>85</td>\n",
       "      <td>83</td>\n",
       "      <td>30</td>\n",
       "      <td>45</td>\n",
       "      <td>38</td>\n",
       "      <td>27</td>\n",
       "      <td>25</td>\n",
       "      <td>31</td>\n",
       "      <td>33</td>\n",
       "      <td>37</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>92</td>\n",
       "      <td>92</td>\n",
       "      <td>91</td>\n",
       "      <td>90</td>\n",
       "      <td>95</td>\n",
       "      <td>89</td>\n",
       "      <td>60</td>\n",
       "      <td>91</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>15</td>\n",
       "      <td>13</td>\n",
       "      <td>25</td>\n",
       "      <td>55</td>\n",
       "      <td>11</td>\n",
       "      <td>30</td>\n",
       "      <td>14</td>\n",
       "      <td>11</td>\n",
       "      <td>59</td>\n",
       "      <td>48</td>\n",
       "      <td>58</td>\n",
       "      <td>61</td>\n",
       "      <td>52</td>\n",
       "      <td>85</td>\n",
       "      <td>35</td>\n",
       "      <td>25</td>\n",
       "      <td>78</td>\n",
       "      <td>44</td>\n",
       "      <td>83</td>\n",
       "      <td>16</td>\n",
       "      <td>29</td>\n",
       "      <td>30</td>\n",
       "      <td>12</td>\n",
       "      <td>70</td>\n",
       "      <td>47</td>\n",
       "      <td>70</td>\n",
       "      <td>10</td>\n",
       "      <td>10</td>\n",
       "      <td>11</td>\n",
       "      <td>91</td>\n",
       "      <td>90</td>\n",
       "      <td>95</td>\n",
       "      <td>91</td>\n",
       "      <td>89</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   overall  potential  pac  sho  pas  dri  def  phy  international_reputation  \\\n",
       "0       94         94   90   93   82   90   33   80                         5   \n",
       "1       93         93   89   90   86   96   26   61                         5   \n",
       "2       92         94   92   84   79   95   30   60                         5   \n",
       "3       92         92   82   90   79   87   42   81                         5   \n",
       "4       92         92   91   90   95   89   60   91                         5   \n",
       "\n",
       "   skill_moves  weak_foot  crossing  finishing  heading_accuracy  \\\n",
       "0            5          4        85         94                88   \n",
       "1            4          4        77         95                71   \n",
       "2            5          5        75         89                62   \n",
       "3            4          4        77         94                77   \n",
       "4            1          4        15         13                25   \n",
       "\n",
       "   short_passing  volleys  dribbling  curve  free_kick_accuracy  long_passing  \\\n",
       "0             83       88         91     81                  76            77   \n",
       "1             88       85         97     89                  90            87   \n",
       "2             81       83         96     81                  84            75   \n",
       "3             83       88         86     86                  84            64   \n",
       "4             55       11         30     14                  11            59   \n",
       "\n",
       "   ball_control  acceleration  sprint_speed  agility  reactions  balance  \\\n",
       "0            93            89            91       89         96       63   \n",
       "1            95            92            87       90         95       95   \n",
       "2            95            94            90       96         88       82   \n",
       "3            91            88            77       86         93       60   \n",
       "4            48            58            61       52         85       35   \n",
       "\n",
       "   shot_power  jumping  stamina  strength  long_shots  aggression  \\\n",
       "0          94       95       92        80          92          63   \n",
       "1          85       68       73        59          88          48   \n",
       "2          80       61       78        53          77          56   \n",
       "3          87       69       89        80          86          78   \n",
       "4          25       78       44        83          16          29   \n",
       "\n",
       "   interceptions  positioning  vision  penalties  composure  marking  \\\n",
       "0             29           95      85         85         95       22   \n",
       "1             22           93      90         78         96       13   \n",
       "2             36           90      80         81         92       21   \n",
       "3             41           92      84         85         83       30   \n",
       "4             30           12      70         47         70       10   \n",
       "\n",
       "   standing_tackle  sliding_tackle  gk_diving  gk_handling  gk_kicking  \\\n",
       "0               31              23          7           11          15   \n",
       "1               28              26          6           11          15   \n",
       "2               24              33          9            9          15   \n",
       "3               45              38         27           25          31   \n",
       "4               10              11         91           90          95   \n",
       "\n",
       "   gk_positioning  gk_reflexes  \n",
       "0              14           11  \n",
       "1              14            8  \n",
       "2              15           11  \n",
       "3              33           37  \n",
       "4              91           89  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fifa_stats1 = fifa.loc[:,'overall':'weak_foot']\n",
    "fifa_stats2 = fifa.loc[:,'crossing':'gk_reflexes']\n",
    "fifa_stats = pd.concat([fifa_stats1, fifa_stats2], axis=1)\n",
    "with pd.option_context('display.max_rows', None, 'display.max_columns', None):\n",
    "    display(fifa_stats.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "First we standardize all the metrics to have a mean of zero and unit variance. This standardization provides a fair way to measure the various attributes since they have different means and distributions."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import StandardScaler\n",
    "fifa_stats = StandardScaler().fit_transform(fifa_stats)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#PCA\n",
    "from sklearn.decomposition import PCA\n",
    "pca = PCA(n_components=10)\n",
    "components = pca.fit_transform(fifa_stats)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#NearestNeighbors\n",
    "from sklearn.neighbors import NearestNeighbors\n",
    "nbrs = NearestNeighbors(n_neighbors=6).fit(components)\n",
    "distances, indices = nbrs.kneighbors(components)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now that we have the nearest neighbors indices, we are ready to create our function. (Both the *fifa* dataframe and the *indices* numpy array are accessible in the scope of the following function.)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def similar_players(player):\n",
    "    #First let's make sure there is exactly one player with the matching name\n",
    "    if fifa[fifa.name==player].size==0:\n",
    "        print('No player by that name.')\n",
    "        return\n",
    "    elif fifa[fifa.name==player].shape[0]>1:\n",
    "        print('Multiple players by that name, sorry.')\n",
    "        return\n",
    "    #First we get the index of the player\n",
    "    idx = fifa[fifa.name==player].index[0]\n",
    "    #Get the indices of the 5 neighbors\n",
    "    n_idx = indices[idx,1:]\n",
    "    #Subset the fifa dataframe\n",
    "    fifa_similar = fifa.iloc[n_idx]\n",
    "    #Print out the results\n",
    "    display(fifa_similar.loc[:,['name', 'club', 'league', 'nationality', 'Position']])\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now it's time to try it out. Even though we didn't pass in information about the players’ position, it stands to reason that the most similar players would have similar roles. Let's try the function with a few players."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>club</th>\n",
       "      <th>league</th>\n",
       "      <th>nationality</th>\n",
       "      <th>Position</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>551</th>\n",
       "      <td>A. Romagnoli</td>\n",
       "      <td>Milan</td>\n",
       "      <td>Italian Serie A</td>\n",
       "      <td>Italy</td>\n",
       "      <td>Center-back</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>370</th>\n",
       "      <td>D. Astori</td>\n",
       "      <td>Fiorentina</td>\n",
       "      <td>Italian Serie A</td>\n",
       "      <td>Italy</td>\n",
       "      <td>Center-back</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>303</th>\n",
       "      <td>D. Sánchez</td>\n",
       "      <td>Tottenham Hotspur</td>\n",
       "      <td>English Premier League</td>\n",
       "      <td>Colombia</td>\n",
       "      <td>Center-back</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>417</th>\n",
       "      <td>M. Nastasić</td>\n",
       "      <td>FC Schalke 04</td>\n",
       "      <td>German Bundesliga</td>\n",
       "      <td>Serbia</td>\n",
       "      <td>Center-back</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>219</th>\n",
       "      <td>A. Rüdiger</td>\n",
       "      <td>Chelsea</td>\n",
       "      <td>English Premier League</td>\n",
       "      <td>Germany</td>\n",
       "      <td>Center-back</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             name               club                  league nationality  \\\n",
       "551  A. Romagnoli              Milan         Italian Serie A       Italy   \n",
       "370     D. Astori         Fiorentina         Italian Serie A       Italy   \n",
       "303    D. Sánchez  Tottenham Hotspur  English Premier League    Colombia   \n",
       "417   M. Nastasić      FC Schalke 04       German Bundesliga      Serbia   \n",
       "219    A. Rüdiger            Chelsea  English Premier League     Germany   \n",
       "\n",
       "        Position  \n",
       "551  Center-back  \n",
       "370  Center-back  \n",
       "303  Center-back  \n",
       "417  Center-back  \n",
       "219  Center-back  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#My favorite defender, John Brooks\n",
    "similar_players('J. Brooks')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>club</th>\n",
       "      <th>league</th>\n",
       "      <th>nationality</th>\n",
       "      <th>Position</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1484</th>\n",
       "      <td>Daniel Podence</td>\n",
       "      <td>Sporting CP</td>\n",
       "      <td>Portuguese Primeira Liga</td>\n",
       "      <td>Portugal</td>\n",
       "      <td>Forward</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1207</th>\n",
       "      <td>L. Bailey</td>\n",
       "      <td>Bayer 04 Leverkusen</td>\n",
       "      <td>German Bundesliga</td>\n",
       "      <td>Jamaica</td>\n",
       "      <td>Outside-mid</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>835</th>\n",
       "      <td>L. Acosta</td>\n",
       "      <td>Club Atlético Lanús</td>\n",
       "      <td>Argentinian Superliga</td>\n",
       "      <td>Argentina</td>\n",
       "      <td>Outside-mid</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1009</th>\n",
       "      <td>J. Aquino</td>\n",
       "      <td>Tigres U.A.N.L.</td>\n",
       "      <td>Mexican Liga MX</td>\n",
       "      <td>Mexico</td>\n",
       "      <td>Outside-mid</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3303</th>\n",
       "      <td>B. Fernández</td>\n",
       "      <td>FC Metz</td>\n",
       "      <td>French Ligue 1</td>\n",
       "      <td>Argentina</td>\n",
       "      <td>Forward</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                name                 club                    league  \\\n",
       "1484  Daniel Podence          Sporting CP  Portuguese Primeira Liga   \n",
       "1207       L. Bailey  Bayer 04 Leverkusen         German Bundesliga   \n",
       "835        L. Acosta  Club Atlético Lanús     Argentinian Superliga   \n",
       "1009       J. Aquino      Tigres U.A.N.L.           Mexican Liga MX   \n",
       "3303    B. Fernández              FC Metz            French Ligue 1   \n",
       "\n",
       "     nationality     Position  \n",
       "1484    Portugal      Forward  \n",
       "1207     Jamaica  Outside-mid  \n",
       "835    Argentina  Outside-mid  \n",
       "1009      Mexico  Outside-mid  \n",
       "3303   Argentina      Forward  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Best American prospect, Christian Pulisic\n",
    "similar_players('C. Pulisic')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>club</th>\n",
       "      <th>league</th>\n",
       "      <th>nationality</th>\n",
       "      <th>Position</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>584</th>\n",
       "      <td>Y. Konoplyanka</td>\n",
       "      <td>FC Schalke 04</td>\n",
       "      <td>German Bundesliga</td>\n",
       "      <td>Ukraine</td>\n",
       "      <td>Outside-mid</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>560</th>\n",
       "      <td>E. Višća</td>\n",
       "      <td>İstanbul Başakşehir FK</td>\n",
       "      <td>Turkish Süper Lig</td>\n",
       "      <td>Bosnia Herzegovina</td>\n",
       "      <td>Outside-mid</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>965</th>\n",
       "      <td>Y. Salibur</td>\n",
       "      <td>En Avant de Guingamp</td>\n",
       "      <td>French Ligue 1</td>\n",
       "      <td>France</td>\n",
       "      <td>Outside-mid</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>607</th>\n",
       "      <td>A. Ljajić</td>\n",
       "      <td>Torino</td>\n",
       "      <td>Italian Serie A</td>\n",
       "      <td>Serbia</td>\n",
       "      <td>Center-mid</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1989</th>\n",
       "      <td>M. Oršić</td>\n",
       "      <td>Ulsan Hyundai Horang-i</td>\n",
       "      <td>Korean K League Classic</td>\n",
       "      <td>Croatia</td>\n",
       "      <td>Outside-mid</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                name                    club                   league  \\\n",
       "584   Y. Konoplyanka           FC Schalke 04        German Bundesliga   \n",
       "560         E. Višća  İstanbul Başakşehir FK        Turkish Süper Lig   \n",
       "965       Y. Salibur    En Avant de Guingamp           French Ligue 1   \n",
       "607        A. Ljajić                  Torino          Italian Serie A   \n",
       "1989        M. Oršić  Ulsan Hyundai Horang-i  Korean K League Classic   \n",
       "\n",
       "             nationality     Position  \n",
       "584              Ukraine  Outside-mid  \n",
       "560   Bosnia Herzegovina  Outside-mid  \n",
       "965               France  Outside-mid  \n",
       "607               Serbia   Center-mid  \n",
       "1989             Croatia  Outside-mid  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Best player on the LA Galaxy (imo)\n",
    "similar_players('R. Alessandrini')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>club</th>\n",
       "      <th>league</th>\n",
       "      <th>nationality</th>\n",
       "      <th>Position</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>301</th>\n",
       "      <td>Malcom</td>\n",
       "      <td>Girondins de Bordeaux</td>\n",
       "      <td>French Ligue 1</td>\n",
       "      <td>Brazil</td>\n",
       "      <td>Outside-mid</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>354</th>\n",
       "      <td>R. Boudebouz</td>\n",
       "      <td>Real Betis Balompié</td>\n",
       "      <td>Spanish Primera División</td>\n",
       "      <td>Algeria</td>\n",
       "      <td>Center-mid</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>434</th>\n",
       "      <td>Pablo Sarabia</td>\n",
       "      <td>Sevilla FC</td>\n",
       "      <td>Spanish Primera División</td>\n",
       "      <td>Spain</td>\n",
       "      <td>Center-mid</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>607</th>\n",
       "      <td>A. Ljajić</td>\n",
       "      <td>Torino</td>\n",
       "      <td>Italian Serie A</td>\n",
       "      <td>Serbia</td>\n",
       "      <td>Center-mid</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>206</th>\n",
       "      <td>F. Bernardeschi</td>\n",
       "      <td>Juventus</td>\n",
       "      <td>Italian Serie A</td>\n",
       "      <td>Italy</td>\n",
       "      <td>Forward</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                name                   club                    league  \\\n",
       "301           Malcom  Girondins de Bordeaux            French Ligue 1   \n",
       "354     R. Boudebouz    Real Betis Balompié  Spanish Primera División   \n",
       "434    Pablo Sarabia             Sevilla FC  Spanish Primera División   \n",
       "607        A. Ljajić                 Torino           Italian Serie A   \n",
       "206  F. Bernardeschi               Juventus           Italian Serie A   \n",
       "\n",
       "    nationality     Position  \n",
       "301      Brazil  Outside-mid  \n",
       "354     Algeria   Center-mid  \n",
       "434       Spain   Center-mid  \n",
       "607      Serbia   Center-mid  \n",
       "206       Italy      Forward  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Best player in MLS\n",
    "similar_players('S. Giovinco')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>club</th>\n",
       "      <th>league</th>\n",
       "      <th>nationality</th>\n",
       "      <th>Position</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>L. Suárez</td>\n",
       "      <td>FC Barcelona</td>\n",
       "      <td>Spanish Primera División</td>\n",
       "      <td>Uruguay</td>\n",
       "      <td>Forward</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>R. Lewandowski</td>\n",
       "      <td>FC Bayern Munich</td>\n",
       "      <td>German Bundesliga</td>\n",
       "      <td>Poland</td>\n",
       "      <td>Forward</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>S. Agüero</td>\n",
       "      <td>Manchester City</td>\n",
       "      <td>English Premier League</td>\n",
       "      <td>Argentina</td>\n",
       "      <td>Forward</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>L. Messi</td>\n",
       "      <td>FC Barcelona</td>\n",
       "      <td>Spanish Primera División</td>\n",
       "      <td>Argentina</td>\n",
       "      <td>Forward</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>A. Sánchez</td>\n",
       "      <td>Arsenal</td>\n",
       "      <td>English Premier League</td>\n",
       "      <td>Chile</td>\n",
       "      <td>Forward</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              name              club                    league nationality  \\\n",
       "3        L. Suárez      FC Barcelona  Spanish Primera División     Uruguay   \n",
       "5   R. Lewandowski  FC Bayern Munich         German Bundesliga      Poland   \n",
       "16       S. Agüero   Manchester City    English Premier League   Argentina   \n",
       "1         L. Messi      FC Barcelona  Spanish Primera División   Argentina   \n",
       "13      A. Sánchez           Arsenal    English Premier League       Chile   \n",
       "\n",
       "   Position  \n",
       "3   Forward  \n",
       "5   Forward  \n",
       "16  Forward  \n",
       "1   Forward  \n",
       "13  Forward  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#According to EA, the best player in the world\n",
    "similar_players('Cristiano Ronaldo')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>club</th>\n",
       "      <th>league</th>\n",
       "      <th>nationality</th>\n",
       "      <th>Position</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>983</th>\n",
       "      <td>D. Benaglio</td>\n",
       "      <td>AS Monaco</td>\n",
       "      <td>French Ligue 1</td>\n",
       "      <td>Switzerland</td>\n",
       "      <td>GK</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>673</th>\n",
       "      <td>I. Akinfeev</td>\n",
       "      <td>CSKA Moscow</td>\n",
       "      <td>Russian Premier League</td>\n",
       "      <td>Russia</td>\n",
       "      <td>GK</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>680</th>\n",
       "      <td>G. Ochoa</td>\n",
       "      <td>Standard de Liège</td>\n",
       "      <td>Belgian First Division A</td>\n",
       "      <td>Mexico</td>\n",
       "      <td>GK</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>384</th>\n",
       "      <td>C. Carrasso</td>\n",
       "      <td>Galatasaray SK</td>\n",
       "      <td>Turkish Süper Lig</td>\n",
       "      <td>France</td>\n",
       "      <td>GK</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>872</th>\n",
       "      <td>N. Guzmán</td>\n",
       "      <td>Tigres U.A.N.L.</td>\n",
       "      <td>Mexican Liga MX</td>\n",
       "      <td>Argentina</td>\n",
       "      <td>GK</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            name               club                    league  nationality  \\\n",
       "983  D. Benaglio          AS Monaco            French Ligue 1  Switzerland   \n",
       "673  I. Akinfeev        CSKA Moscow    Russian Premier League       Russia   \n",
       "680     G. Ochoa  Standard de Liège  Belgian First Division A       Mexico   \n",
       "384  C. Carrasso     Galatasaray SK         Turkish Süper Lig       France   \n",
       "872    N. Guzmán    Tigres U.A.N.L.           Mexican Liga MX    Argentina   \n",
       "\n",
       "    Position  \n",
       "983       GK  \n",
       "673       GK  \n",
       "680       GK  \n",
       "384       GK  \n",
       "872       GK  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#American GK, hero of the 2016 WC\n",
    "similar_players('T. Howard')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "While not perfect, this is a fun function that can help fans discover new players. For example, next time the EPL is on TV, I'll keep a lookout for Davinson Sánchez, a Colombian CB for Tottenham Hotspur, since he apparently is a top match for my favorite defender, John Brooks."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
