"""test_network_LevonJames.py

Levon Mikaelian & James Gaboardi 2016


to run in ipython: >>> run test_network_LevonJames.py 2 8 3 False
                    == run [file] two streets, 8 source, 3 dest, no seed

sys.argv[1] == streets (1,2, or 3)
sys.argv[2] == source nodes
sys.argv[3] == destination nodes
sys.argv[4] == seed of 333 (True) or no seed (False)

new files in the google drive:  1_street.shp
                                2_street.shp
                                2_street.shp
"""

import numpy as np
import pysal as ps
import pandas as pd
import sys

if str(sys.platform) == "darwin":       # jgaboardi_mac
    path = "/Users/jgaboardi/Desktop/test_net/"
elif str(sys.platform) == "????":       # LEVON **************************************
    path = "???/???/???"

streets = sys.argv[1] # Choose 1, 2, or 3
source_obs = int(sys.argv[2])
destin_obs = int(sys.argv[3])

network = ps.Network(path+str(streets)+"_street.shp",
                     seg_speed='SPEED',
                     conversion_rate=0.000621371,
                     calc_ttime=True)

if sys.argv[4] == str(True):
    np.random.seed(333)
else:
    np.random.seed(np.random.randint(1000))

sim_source = network.simulate_observations(source_obs)
sim_dest = network.simulate_observations(destin_obs)                     
matrix = network.allneighbordistances(sourcepattern=sim_source,
                                      destpattern=sim_dest,
                                      fill_diagonal=0.0)
"""
network.snapobservations(path+"test_points.shp",
                          "points", 
                          attribute=True,)
matrix = network.allneighbordistances(sourcepattern=network.pointpatterns["points"],
                                      fill_diagonal=0.0)
"""
matrix = pd.DataFrame(matrix)
print matrix