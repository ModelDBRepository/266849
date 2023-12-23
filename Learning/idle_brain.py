# -*- coding: utf-8 -*-
"""
This is a prototype model for robot navigation based on Hippocampal Circuitry. 

For any questions contact me: simone.coppolino@ibf.cnr.it
"""
# pragma: no cover

__author__ = 'Simone Coppolino (CNR)'

import nest
import hbp_nrp_cle.tf_framework as nrp
import numpy as np
import logging
from pyNN.nest import *
import pyNN.nest as sim
logger = logging.getLogger(__name__)


sim.setup(rng_seeds=[1234])

# Following parameters were taken from the husky braitenberg brain experiment (braitenberg.py)

SENSORPARAMS = {'cm': 0.025,
                    'v_rest': -60.5,
                    'tau_m': 10.0,
                    'e_rev_E': 0.0,
                    'e_rev_I': -75.0,
                    'v_reset': -60.5,
                    'v_thresh': -60.0,
                    'tau_refrac': 10.0,
                    'tau_syn_E': 2.5,
                    'tau_syn_I': 2.5}

#Network is write in PyNN

syn_params = {'U' : 1.0, 'tau_rec': 1.0, 'tau_facil': 1.0}
SYN_OBJ = sim.StaticSynapse(weight = 0.00005, delay = 0.1)
SYN_S_HD = sim.StaticSynapse(weight = 0.0001,delay = 0.1)
SYN_S_PF = sim.TsodyksMarkramSynapse(weight = 0.000037, delay = 0.1, **syn_params)

cell_class = sim.IF_cond_alpha(**SENSORPARAMS)

# Define the network structure: 

sensor_neuron = sim.Population(size = 4, cellclass = cell_class)
wall_sensor = sim.Population(size = 2, cellclass = cell_class)
wall_neuron = sim.Population(size = 2, cellclass = cell_class)
persistent_neuron = sim.Population(size = 3, cellclass = cell_class)
object_cells = sim.Population(size = 4,cellclass = cell_class)
place_cells  = sim.Population(size = 12,cellclass = cell_class)
head_direction_cells = sim.Population(size = 12, cellclass = cell_class)
neurons = sensor_neuron + persistent_neuron + object_cells + head_direction_cells + place_cells +  wall_sensor + wall_neuron



standard = STDPMechanism(
          weight=0.0000000000000002,  # this is the initial value of the weight
          delay="0.1",
          timing_dependence=SpikePairRule(tau_plus=20.0, tau_minus=20.0,
                                          A_plus=0.01, A_minus=0.01),
          weight_dependence=AdditiveWeightDependence(w_min=0, w_max=0.9))
standard_plus = STDPMechanism(
          weight=0.0000000000000002,  # this is the initial value of the weight
          delay="0.1",
          timing_dependence=SpikePairRule(tau_plus=20.0, tau_minus=20.0,
                                          A_plus=0.01, A_minus=0.01),
          weight_dependence=AdditiveWeightDependence(w_min=0, w_max=4))



#Red Connection:
object_red_connection = sim.Projection(sensor_neuron[0:1],object_cells[0:1],OneToOneConnector(),SYN_OBJ,receptor_type='excitatory')
sensor_red_connection = sim.Projection(sensor_neuron[0:1],persistent_neuron[0:1],OneToOneConnector(),SYN_S_PF,receptor_type='excitatory')
angular_red_connection = sim.Projection(object_cells[0:1],place_cells,AllToAllConnector(),standard)
persistent_red_connection = sim.Projection(persistent_neuron[0:1],object_cells[1:4],AllToAllConnector(),standard)

#Blue Connection:
object_blue_connection = sim.Projection(sensor_neuron[1:2],object_cells[1:2],OneToOneConnector(),SYN_OBJ, receptor_type = 'excitatory')
sensor_blue_connection = sim.Projection(sensor_neuron[1:2],persistent_neuron[1:2],OneToOneConnector(),SYN_S_PF,receptor_type='excitatory')
angular_blue_connection = sim.Projection(object_cells[1:2],place_cells,AllToAllConnector(),standard)
persistent_blue_connection = sim.Projection(persistent_neuron[1:2],object_cells[0:1],OneToOneConnector(),standard)
persistent_blue1_connection = sim.Projection(persistent_neuron[1:2],object_cells[2:4],AllToAllConnector(),standard)

#Green Connection
object_green_connection = sim.Projection(sensor_neuron[2:3],object_cells[2:3],OneToOneConnector(),SYN_OBJ,receptor_type = 'excitatory')
angular_green_connection = sim.Projection(object_cells[2:3],place_cells,AllToAllConnector(),standard)

#Black Connection
object_black_connection = sim.Projection(sensor_neuron[3:4], object_cells[3:4], OneToOneConnector(), SYN_OBJ, receptor_type = 'excitatory')
sensor_black_connection = sim.Projection(sensor_neuron[3:4],persistent_neuron[2:3],OneToOneConnector(),SYN_S_PF,receptor_type='excitatory')
angular_black_connection = sim.Projection(object_cells[3:4],place_cells,AllToAllConnector(),standard)
persistent_black_connection = sim.Projection(persistent_neuron[2:3],object_cells[0:3],AllToAllConnector(),standard)

#Avoidance connection
wall_connection_right = sim.Projection(wall_sensor[0:1],wall_neuron[0:1],OneToOneConnector(),standard_plus)
wall_connection_left = sim.Projection(wall_sensor[1:2],wall_neuron[1:2], OneToOneConnector(),standard_plus)

#Stimulator-HD connection
stimulator_connection = sim.Projection(head_direction_cells, place_cells, OneToOneConnector(), SYN_S_HD,receptor_type = 'excitatory')

circuit = neurons


