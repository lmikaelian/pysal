"""test_network_LevonJames.py

Levon Mikaelian & James Gaboardi 2016


to run in ipython: >>> run test_network_LevonJames.py 2 travel_time 8 3 no_seed 1.5 SHP
                        == run [file],
                               two streets, 
                               calculate travel time, 
                               8 source, 
                               3 dest, 
                               no seed, 
                               1.5 congestion,
                               use .shp for points

sys.argv[1] == streets (1,2, or 3)
sys.argv[2] == 'distance' or 'travel_time'
sys.argv[3] == source nodes
sys.argv[4] == destination nodes
sys.argv[5] == seed number or 'no_seed'
sys.argv[6] == congestion factor 
sys.argv[7] == simulated points or .shp points 

new files in the google drive:  1_street.shp
                                2_street.shp
                                2_street.shp
******************************************** GET NEW 'test_points.shp' from the drive ****


"""

import numpy as np
import pysal as ps
import pandas as pd
import sys

if str(sys.platform) == "darwin":       # jgaboardi_mac
    path = "/Users/jgaboardi/Desktop/test_net/"
elif str(sys.platform) == "????":       # LEVON **************************************
    path = "???/???/???"

# How many test streets?
streets = sys.argv[1] # Choose 1, 2, or 3
# Distance or Travel Time?
if sys.argv[2].upper() == 'DISTANCE':
    measure_method = False
elif sys.argv[2].upper() == 'TRAVEL_TIME':
    measure_method = True
# How many test sources?
source_obs = int(sys.argv[3])
# How many test destinations?
dest_obs = int(sys.argv[4])
# Seed or no seed?
if sys.argv[5].upper() == 'NO_SEED':
    np.random.seed(np.random.randint(1000))
else:
    np.random.seed(int(sys.argv[5]))
# With or without congestion?
congestion_factor = float(sys.argv[6])

network = ps.Network(path+str(streets)+"_street.shp",
                     seg_speed='SPEED',
                     conversion_rate=0.000621371,
                     calc_ttime=measure_method,
                     congest_factor=congestion_factor)

if sys.argv[7].upper() == 'SIM':
    sim_source = network.simulate_observations(source_obs)
    sim_dest = network.simulate_observations(dest_obs)                     
    matrix = network.allneighbordistances(sourcepattern=sim_source,
                                          destpattern=sim_dest,
                                          fill_diagonal=0.0)
elif sys.argv[7].upper() == 'SHP':
    network.snapobservations(path+"test_points.shp",
                             "points", 
                             attribute=True,)
    matrix = network.allneighbordistances(sourcepattern=network.pointpatterns["points"],
                                          fill_diagonal=0.0)

matrix = pd.DataFrame(matrix)
print matrix





