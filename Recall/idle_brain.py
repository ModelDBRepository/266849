# -*- coding: utf-8 -*-
"""
Recall phase of the same neural network based on hippocampal circuitry. 
"""
# pragma: no cover

__author__ = 'Simone Copppolino (CNR)'

#from hbp_nrp_cle.brainsim import simulator as sim
import nest
import hbp_nrp_cle.tf_framework as nrp
import numpy as np
import logging
import csv
from pyNN.nest import *
import pyNN.nest as sim
logger = logging.getLogger(__name__)


"Function for reading files"
def read(k,csv_file):
    import csv
    with open(csv_file,'rt') as infile:
        read = csv.reader(infile)
        rows = list(read)
        if(k == 0):
            m = (rows[1][2])
            new = m.replace(")","")
            new_bis = new.replace("]","")
            new_float = float(new_bis) #convert new_bis from string to float
            return new_float
        elif(k > 0):
            m = (rows[1][k+3])
            new = m.replace(")","")
            new_bis = new.replace("]","")
            new_float = float(new_bis)
            return new_float
"""
Initializes PyNN with the minimal neuronal network
"""



sim.setup(rng_seeds=[1234])

# Following parameters were taken from the husky braitenberg brain experiment (braitenberg.py)

SENSORPARAMS = {'cm': 0.025,
                    'v_rest': -60.5,
                    'tau_m': 10.,
                    'e_rev_E': 0.0,
                    'e_rev_I': -75.0,
                    'v_reset': -60.5,
                    'v_thresh': -60.0,
                    'tau_refrac': 10.0,
                    'tau_syn_E': 2.5,
                    'tau_syn_I': 2.5}
syn_params = {'U' : 1.0, 'tau_rec': 1.0, 'tau_facil': 1.0}

SYN_OBJ = sim.TsodyksMarkramSynapse(weight = 0.00005, delay = 0.1, **syn_params)
SYN_S_PF = sim.TsodyksMarkramSynapse(weight = 0.000037, delay = 0.1, **syn_params)
SYN_R_0 = sim.TsodyksMarkramSynapse(weight = read(0,'angular_red.csv'), delay = 0.1, **syn_params)
SYN_R_1 = sim.TsodyksMarkramSynapse(weight = read(2,'angular_red.csv'), delay = 0.1, **syn_params)
SYN_R_2 = sim.TsodyksMarkramSynapse(weight = read(5,'angular_red.csv'), delay = 0.1, **syn_params)
SYN_R_3 = sim.TsodyksMarkramSynapse(weight = read(8,'angular_red.csv'), delay = 0.1, **syn_params)
SYN_R_4 = sim.TsodyksMarkramSynapse(weight = read(11,'angular_red.csv'), delay = 0.1, **syn_params)
SYN_R_5 = sim.TsodyksMarkramSynapse(weight = read(14,'angular_red.csv'), delay = 0.1, **syn_params)
SYN_R_6 = sim.TsodyksMarkramSynapse(weight = read(17,'angular_red.csv'), delay = 0.1, **syn_params)
SYN_R_7 = sim.TsodyksMarkramSynapse(weight = read(20,'angular_red.csv'), delay = 0.1, **syn_params)
SYN_R_8 = sim.TsodyksMarkramSynapse(weight = read(23,'angular_red.csv'), delay = 0.1, **syn_params)
SYN_R_9 = sim.TsodyksMarkramSynapse(weight = read(26,'angular_red.csv'), delay = 0.1, **syn_params)
SYN_R_10 = sim.TsodyksMarkramSynapse(weight = read(29,'angular_red.csv'), delay = 0.1, **syn_params)
SYN_R_11 = sim.TsodyksMarkramSynapse(weight = read(32,'angular_red.csv'), delay = 0.1, **syn_params)
SYN_B_0 = sim.TsodyksMarkramSynapse(weight = read(0,'angular_blue.csv'), delay = 0.1, **syn_params)
SYN_B_1 = sim.TsodyksMarkramSynapse(weight = read(2,'angular_blue.csv'), delay = 0.1, **syn_params)
SYN_B_2 = sim.TsodyksMarkramSynapse(weight = read(5,'angular_blue.csv'), delay = 0.1, **syn_params)
SYN_B_3 = sim.TsodyksMarkramSynapse(weight = read(8,'angular_blue.csv'), delay = 0.1, **syn_params)
SYN_B_4 = sim.TsodyksMarkramSynapse(weight = read(11,'angular_blue.csv'), delay = 0.1, **syn_params)
SYN_B_5 = sim.TsodyksMarkramSynapse(weight = read(14,'angular_blue.csv'), delay = 0.1, **syn_params)
SYN_B_6 = sim.TsodyksMarkramSynapse(weight = read(17,'angular_blue.csv'), delay = 0.1, **syn_params)
SYN_B_7 = sim.TsodyksMarkramSynapse(weight = read(20,'angular_blue.csv'), delay = 0.1, **syn_params)
SYN_B_8 = sim.TsodyksMarkramSynapse(weight = read(23,'angular_blue.csv'), delay = 0.1, **syn_params)
SYN_B_9 = sim.TsodyksMarkramSynapse(weight = read(26,'angular_blue.csv'), delay = 0.1, **syn_params)
SYN_B_10 = sim.TsodyksMarkramSynapse(weight = read(29,'angular_blue.csv'), delay = 0.1, **syn_params)
SYN_B_11 = sim.TsodyksMarkramSynapse(weight = read(32,'angular_blue.csv'), delay = 0.1, **syn_params)
SYN_K_0 = sim.TsodyksMarkramSynapse(weight = read(0,'angular_black.csv'), delay = 0.1, **syn_params)
SYN_K_1 = sim.TsodyksMarkramSynapse(weight = read(2,'angular_black.csv'), delay = 0.1, **syn_params)
SYN_K_2 = sim.TsodyksMarkramSynapse(weight = read(5,'angular_black.csv'), delay = 0.1, **syn_params)
SYN_K_3 = sim.TsodyksMarkramSynapse(weight = read(8,'angular_black.csv'), delay = 0.1, **syn_params)
SYN_K_4 = sim.TsodyksMarkramSynapse(weight = read(11,'angular_black.csv'), delay = 0.1, **syn_params)
SYN_K_5 = sim.TsodyksMarkramSynapse(weight = read(14,'angular_black.csv'), delay = 0.1, **syn_params)
SYN_K_6 = sim.TsodyksMarkramSynapse(weight = read(17,'angular_black.csv'), delay = 0.1, **syn_params)
SYN_K_7 = sim.TsodyksMarkramSynapse(weight = read(20,'angular_black.csv'), delay = 0.1, **syn_params)
SYN_K_8 = sim.TsodyksMarkramSynapse(weight = read(23,'angular_black.csv'), delay = 0.1, **syn_params)
SYN_K_9 = sim.TsodyksMarkramSynapse(weight = read(26,'angular_black.csv'), delay = 0.1, **syn_params)
SYN_K_10 = sim.TsodyksMarkramSynapse(weight = read(29,'angular_black.csv'), delay = 0.1, **syn_params)
SYN_K_11 = sim.TsodyksMarkramSynapse(weight = read(32,'angular_black.csv'), delay = 0.1, **syn_params)
SYN_G_0 = sim.TsodyksMarkramSynapse(weight = read(0,'angular_green.csv'), delay = 0.1, **syn_params)
SYN_G_1 = sim.TsodyksMarkramSynapse(weight = read(2,'angular_green.csv'), delay = 0.1, **syn_params)
SYN_G_2 = sim.TsodyksMarkramSynapse(weight = read(5,'angular_green.csv'), delay = 0.1, **syn_params)
SYN_G_3 = sim.TsodyksMarkramSynapse(weight = read(8,'angular_green.csv'), delay = 0.1, **syn_params)
SYN_G_4 = sim.TsodyksMarkramSynapse(weight = read(11,'angular_green.csv'), delay = 0.1, **syn_params)
SYN_G_5 = sim.TsodyksMarkramSynapse(weight = read(14,'angular_green.csv'), delay = 0.1, **syn_params)
SYN_G_6 = sim.TsodyksMarkramSynapse(weight = read(17,'angular_green.csv'), delay = 0.1, **syn_params)
SYN_G_7 = sim.TsodyksMarkramSynapse(weight = read(20,'angular_green.csv'), delay = 0.1, **syn_params)
SYN_G_8 = sim.TsodyksMarkramSynapse(weight = read(23,'angular_green.csv'), delay = 0.1, **syn_params)
SYN_G_9 = sim.TsodyksMarkramSynapse(weight = read(26,'angular_green.csv'), delay = 0.1, **syn_params)
SYN_G_10 = sim.TsodyksMarkramSynapse(weight = read(29,'angular_green.csv'), delay = 0.1, **syn_params)
SYN_G_11 = sim.TsodyksMarkramSynapse(weight = read(32,'angular_green.csv'), delay = 0.1, **syn_params)
SYN_PR_1 = sim.TsodyksMarkramSynapse(weight = read(0,'persistent_red.csv'), delay = 0.1, **syn_params)
SYN_PR_2 = sim.TsodyksMarkramSynapse(weight = read(2,'persistent_red.csv'), delay = 0.1, **syn_params)
SYN_PR_3 = sim.TsodyksMarkramSynapse(weight = read(5,'persistent_red.csv'), delay = 0.1, **syn_params)
SYN_PB_1 = sim.TsodyksMarkramSynapse(weight = read(0,'persistent_blue.csv'), delay = 0.1, **syn_params)
SYN_PB_2 = sim.TsodyksMarkramSynapse(weight = read(0,'persistent_blue_1.csv'), delay = 0.1, **syn_params)
SYN_PB_3 = sim.TsodyksMarkramSynapse(weight = read(2,'persistent_blue_1.csv'), delay = 0.1, **syn_params)
SYN_PK_1 = sim.TsodyksMarkramSynapse(weight = read(0,'persistent_black.csv'), delay = 0.1, **syn_params)
SYN_PK_2 = sim.TsodyksMarkramSynapse(weight = read(2,'persistent_black.csv'), delay = 0.1, **syn_params)
SYN_PK_3 = sim.TsodyksMarkramSynapse(weight = read(5,'persistent_black.csv'), delay = 0.1, **syn_params)
SYN_WL = sim.TsodyksMarkramSynapse(weight = read(0,'wall_left.csv'), delay = 0.1, **syn_params)
SYN_WR = sim.TsodyksMarkramSynapse(weight = read(0,'wall_right.csv'), delay = 0.1, **syn_params)

cell_class = sim.IF_cond_alpha(**SENSORPARAMS)

# Define the network structure: 2 sensori(sx/dx), 3 attuatori(dritto,sx,dx),3 neuroni nascosti.
#population = sim.Population(size= 7,
                                #cellclass=cell_class)

sensor_neuron = sim.Population(size = 4, cellclass = cell_class)
wall_sensor = sim.Population(size = 2, cellclass = cell_class)
wall_neuron = sim.Population(size = 2, cellclass = cell_class)
persistent_neuron = sim.Population(size = 3, cellclass = cell_class)
object_cells = sim.Population(size = 4,cellclass = cell_class)
place_cells  = sim.Population(size = 12,cellclass = cell_class)
head_direction_cells  = sim.Population(size = 12,cellclass = cell_class)
neurons = sensor_neuron + persistent_neuron + object_cells + head_direction_cells + place_cells + wall_sensor + wall_neuron



#PyNN Network, in this network there is no need of STDP connection, all the potentiation is made in the learning phase. 

#Red Connection with separated synapse for better recognize which was the potenziated one

red_connection = sim.Projection(sensor_neuron[0:1],object_cells[0:1],OneToOneConnector(),SYN_OBJ,receptor_type='excitatory')
sensor_persistent_red_connection = sim.Projection(sensor_neuron[0:1],persistent_neuron[0:1],OneToOneConnector(),SYN_S_PF,receptor_type='excitatory')

angular0_red_connection = sim.Projection(object_cells[0:1],place_cells[0:1],OneToOneConnector(),SYN_R_0,receptor_type = 'excitatory')
angular1_red_connection = sim.Projection(object_cells[0:1],place_cells[1:2],OneToOneConnector(),SYN_R_1,receptor_type = 'excitatory')
angular2_red_connection = sim.Projection(object_cells[0:1],place_cells[2:3],OneToOneConnector(),SYN_R_2,receptor_type = 'excitatory')
angular3_red_connection = sim.Projection(object_cells[0:1],place_cells[3:4],OneToOneConnector(),SYN_R_3,receptor_type = 'excitatory')
angular4_red_connection = sim.Projection(object_cells[0:1],place_cells[4:5],OneToOneConnector(),SYN_R_4,receptor_type = 'excitatory')
angular5_red_connection = sim.Projection(object_cells[0:1],place_cells[5:6],OneToOneConnector(),SYN_R_5,receptor_type = 'excitatory')
angular6_red_connection = sim.Projection(object_cells[0:1],place_cells[6:7],OneToOneConnector(),SYN_R_6,receptor_type = 'excitatory')
angular7_red_connection = sim.Projection(object_cells[0:1],place_cells[7:8],OneToOneConnector(),SYN_R_7,receptor_type = 'excitatory')
angular8_red_connection = sim.Projection(object_cells[0:1],place_cells[8:9],OneToOneConnector(),SYN_R_8,receptor_type = 'excitatory')
angular9_red_connection = sim.Projection(object_cells[0:1],place_cells[9:10],OneToOneConnector(),SYN_R_9,receptor_type = 'excitatory')
angular10_red_connection = sim.Projection(object_cells[0:1],place_cells[10:11],OneToOneConnector(),SYN_R_10,receptor_type = 'excitatory')
angular11_red_connection = sim.Projection(object_cells[0:1],place_cells[11:12],OneToOneConnector(),SYN_R_11,receptor_type = 'excitatory')

persistent_red_0_connection = sim.Projection(persistent_neuron[0:1],object_cells[1:2],OneToOneConnector(),SYN_PR_1,receptor_type = 'excitatory')
persistent_red_1_connection = sim.Projection(persistent_neuron[0:1],object_cells[2:3],OneToOneConnector(),SYN_PR_2,receptor_type = 'excitatory')
persistent_red_2_connection = sim.Projection(persistent_neuron[0:1],object_cells[3:4],OneToOneConnector(),SYN_PR_3,receptor_type = 'excitatory')

# Blue connection

blue_connection = sim.Projection(sensor_neuron[1:2],object_cells[1:2],OneToOneConnector(),SYN_OBJ, receptor_type = 'excitatory')
sensor_persistent_blue_connection = sim.Projection(sensor_neuron[1:2],persistent_neuron[1:2],OneToOneConnector(),SYN_S_PF,receptor_type='excitatory')
angular0_blue_connection = sim.Projection(object_cells[1:2],place_cells[0:1],OneToOneConnector(),SYN_B_0,receptor_type = 'excitatory')
angular1_blue_connection = sim.Projection(object_cells[1:2],place_cells[1:2],OneToOneConnector(),SYN_B_1,receptor_type = 'excitatory')
angular2_blue_connection = sim.Projection(object_cells[1:2],place_cells[2:3],OneToOneConnector(),SYN_B_2,receptor_type = 'excitatory')
angular3_blue_connection = sim.Projection(object_cells[1:2],place_cells[3:4],OneToOneConnector(),SYN_B_3,receptor_type = 'excitatory')
angular4_blue_connection = sim.Projection(object_cells[1:2],place_cells[4:5],OneToOneConnector(),SYN_B_4,receptor_type = 'excitatory')
angular5_blue_connection = sim.Projection(object_cells[1:2],place_cells[5:6],OneToOneConnector(),SYN_B_5,receptor_type = 'excitatory')
angular6_blue_connection = sim.Projection(object_cells[1:2],place_cells[6:7],OneToOneConnector(),SYN_B_6,receptor_type = 'excitatory')
angular7_blue_connection = sim.Projection(object_cells[1:2],place_cells[7:8],OneToOneConnector(),SYN_B_7,receptor_type = 'excitatory')
angular8_blue_connection = sim.Projection(object_cells[1:2],place_cells[8:9],OneToOneConnector(),SYN_B_8,receptor_type = 'excitatory')
angular9_blue_connection = sim.Projection(object_cells[1:2],place_cells[9:10],OneToOneConnector(),SYN_B_9,receptor_type = 'excitatory')
angular10_blue_connection = sim.Projection(object_cells[1:2],place_cells[10:11],OneToOneConnector(),SYN_B_10,receptor_type = 'excitatory')
angular11_blue_connection = sim.Projection(object_cells[1:2],place_cells[11:12],OneToOneConnector(),SYN_B_11,receptor_type = 'excitatory')
persistent_blue_0_connection = sim.Projection(persistent_neuron[1:2],object_cells[0:1],OneToOneConnector(),SYN_PB_1,receptor_type = 'excitatory')
persistent_blue_1_connection = sim.Projection(persistent_neuron[1:2],object_cells[2:3],OneToOneConnector(),SYN_PB_2,receptor_type = 'excitatory')
persistent_blue_2_connection = sim.Projection(persistent_neuron[1:2],object_cells[3:4],OneToOneConnector(),SYN_PB_3,receptor_type = 'excitatory')


#Green connection
green_connection = sim.Projection(sensor_neuron[2:3],object_cells[2:3],OneToOneConnector(),SYN_OBJ,receptor_type = 'excitatory')
angular0_green_connection = sim.Projection(object_cells[2:3],place_cells[0:1],OneToOneConnector(),SYN_G_0,receptor_type = 'excitatory')
angular1_green_connection = sim.Projection(object_cells[2:3],place_cells[1:2],OneToOneConnector(),SYN_G_1,receptor_type = 'excitatory')
angular2_green_connection = sim.Projection(object_cells[2:3],place_cells[2:3],OneToOneConnector(),SYN_G_2,receptor_type = 'excitatory')
angular3_green_connection = sim.Projection(object_cells[2:3],place_cells[3:4],OneToOneConnector(),SYN_G_3,receptor_type = 'excitatory')
angular4_green_connection = sim.Projection(object_cells[2:3],place_cells[4:5],OneToOneConnector(),SYN_G_4,receptor_type = 'excitatory')
angular5_green_connection = sim.Projection(object_cells[2:3],place_cells[5:6],OneToOneConnector(),SYN_G_5,receptor_type = 'excitatory')
angular6_green_connection = sim.Projection(object_cells[2:3],place_cells[6:7],OneToOneConnector(),SYN_G_6,receptor_type = 'excitatory')
angular7_green_connection = sim.Projection(object_cells[2:3],place_cells[7:8],OneToOneConnector(),SYN_G_7,receptor_type = 'excitatory')
angular8_green_connection = sim.Projection(object_cells[2:3],place_cells[8:9],OneToOneConnector(),SYN_G_8,receptor_type = 'excitatory')
angular9_green_connection = sim.Projection(object_cells[2:3],place_cells[9:10],OneToOneConnector(),SYN_G_9,receptor_type = 'excitatory')
angular10_green_connection = sim.Projection(object_cells[2:3],place_cells[10:11],OneToOneConnector(),SYN_G_10,receptor_type = 'excitatory')
angular11_green_connection = sim.Projection(object_cells[2:3],place_cells[11:12],OneToOneConnector(),SYN_G_11,receptor_type = 'excitatory')

#Black connection
black_connection = sim.Projection(sensor_neuron[3:4], object_cells[3:4], OneToOneConnector(), SYN_OBJ, receptor_type = 'excitatory')
sensor_persistent_black_connection = sim.Projection(sensor_neuron[3:4],persistent_neuron[2:3],OneToOneConnector(),SYN_S_PF,receptor_type='excitatory')
angular0_black_connection = sim.Projection(object_cells[3:4],place_cells[0:1],OneToOneConnector(),SYN_K_0,receptor_type = 'excitatory')
angular1_black_connection = sim.Projection(object_cells[3:4],place_cells[1:2],OneToOneConnector(),SYN_K_1,receptor_type = 'excitatory')
angular2_black_connection = sim.Projection(object_cells[3:4],place_cells[2:3],OneToOneConnector(),SYN_K_2,receptor_type = 'excitatory')
angular3_black_connection = sim.Projection(object_cells[3:4],place_cells[3:4],OneToOneConnector(),SYN_K_3,receptor_type = 'excitatory')
angular4_black_connection = sim.Projection(object_cells[3:4],place_cells[4:5],OneToOneConnector(),SYN_K_4,receptor_type = 'excitatory')
angular5_black_connection = sim.Projection(object_cells[3:4],place_cells[5:6],OneToOneConnector(),SYN_K_5,receptor_type = 'excitatory')
angular6_black_connection = sim.Projection(object_cells[3:4],place_cells[6:7],OneToOneConnector(),SYN_K_6,receptor_type = 'excitatory')
angular7_black_connection = sim.Projection(object_cells[3:4],place_cells[7:8],OneToOneConnector(),SYN_K_7,receptor_type = 'excitatory')
angular8_black_connection = sim.Projection(object_cells[3:4],place_cells[8:9],OneToOneConnector(),SYN_K_8,receptor_type = 'excitatory')
angular9_black_connection = sim.Projection(object_cells[3:4],place_cells[9:10],OneToOneConnector(),SYN_K_9,receptor_type = 'excitatory')
angular10_black_connection = sim.Projection(object_cells[3:4],place_cells[10:11],OneToOneConnector(),SYN_K_10,receptor_type = 'excitatory')
angular11_black_connection = sim.Projection(object_cells[3:4],place_cells[11:12],OneToOneConnector(),SYN_K_11,receptor_type = 'excitatory')
persistent_black_0_connection = sim.Projection(persistent_neuron[2:3],object_cells[0:1],OneToOneConnector(),SYN_PK_1,receptor_type = 'excitatory')
persistent_black_1_connection = sim.Projection(persistent_neuron[2:3],object_cells[1:2],OneToOneConnector(),SYN_PK_2,receptor_type = 'excitatory')
persistent_black_2_connection = sim.Projection(persistent_neuron[2:3],object_cells[2:3],OneToOneConnector(),SYN_PK_3,receptor_type = 'excitatory')

#Avoidance connection
wall_connection_right = sim.Projection(wall_sensor[0:1],wall_neuron[0:1],OneToOneConnector(),SYN_WR)
wall_connection_left = sim.Projection(wall_sensor[1:2],wall_neuron[1:2], OneToOneConnector(),SYN_WL)

circuit = neurons



