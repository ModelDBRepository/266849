#This function activates the correct HD cells, based on angular variable from Robot_Position script
import hbp_nrp_cle.tf_framework as nrp
@nrp.MapSpikeSource("HD_0",nrp.brain.head_direction_cells[0:1],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("HD_1",nrp.brain.head_direction_cells[1:2],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("HD_2",nrp.brain.head_direction_cells[2:3],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("HD_3",nrp.brain.head_direction_cells[3:4],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("HD_4",nrp.brain.head_direction_cells[4:5],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("HD_5",nrp.brain.head_direction_cells[5:6],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("HD_6",nrp.brain.head_direction_cells[6:7],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("HD_7",nrp.brain.head_direction_cells[7:8],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("HD_8",nrp.brain.head_direction_cells[8:9],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("HD_9",nrp.brain.head_direction_cells[9:10],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("HD_10",nrp.brain.head_direction_cells[10:11],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("HD_11",nrp.brain.head_direction_cells[11:12],nrp.poisson,rng=1234)
@nrp.MapVariable("angle_var",scope=nrp.GLOBAL)
@nrp.Robot2Neuron()
def propagate_angular_cells_spike (t,angle_var,HD_0,HD_1,HD_2,HD_3,HD_4,HD_5,HD_6,HD_7,HD_8,HD_9,HD_10,HD_11):
    
        
        if (angle_var.value <= 30.0 and angle_var.value > 0):
            HD_0.rate = 15
            HD_1.rate = 0.0
            HD_2.rate = 0.0
            HD_3.rate = 0.0
            HD_4.rate = 0.0
            HD_5.rate = 0.0
            HD_6.rate = 0.0
            HD_7.rate = 0.0
            HD_8.rate = 0.0
            HD_9.rate = 0.0
            HD_10.rate = 0.0
            HD_11.rate = 0.0
        
        if (angle_var.value <= 60 and angle_var.value > 30):
            HD_0.rate = 0.0
            HD_1.rate = 15
            HD_2.rate = 0.0
            HD_3.rate = 0.0
            HD_4.rate = 0.0
            HD_5.rate = 0.0
            HD_6.rate = 0.0
            HD_7.rate = 0.0
            HD_8.rate = 0.0
            HD_9.rate = 0.0
            HD_10.rate = 0.0
            HD_11.rate = 0.0
        
        if (angle_var.value <= 90 and angle_var.value > 60):
            HD_0.rate = 0.0
            HD_1.rate = 0.0
            HD_2.rate = 15
            HD_3.rate = 0.0
            HD_4.rate = 0.0
            HD_5.rate = 0.0
            HD_6.rate = 0.0
            HD_7.rate = 0.0
            HD_8.rate = 0.0
            HD_9.rate = 0.0
            HD_10.rate = 0.0
            HD_11.rate = 0.0
            
        if (angle_var.value <= 120 and angle_var.value > 90):
            HD_0.rate = 0.0
            HD_1.rate = 0.0
            HD_2.rate = 0.0
            HD_3.rate = 15
            HD_4.rate = 0.0
            HD_5.rate = 0.0
            HD_6.rate = 0.0
            HD_7.rate = 0.0
            HD_8.rate = 0.0
            HD_9.rate = 0.0
            HD_10.rate = 0.0
            HD_11.rate = 0.0
            
        if (angle_var.value <= 150.0 and angle_var.value > 120):
            HD_0.rate = 0.0
            HD_1.rate = 0.0
            HD_2.rate = 0.0
            HD_3.rate = 0.0
            HD_4.rate = 15
            HD_5.rate = 0.0
            HD_6.rate = 0.0
            HD_7.rate = 0.0
            HD_8.rate = 0.0
            HD_9.rate = 0.0
            HD_10.rate = 0.0
            HD_11.rate = 0.0
            
        if (angle_var.value <= 180.0 and angle_var.value > 150.0):
            HD_0.rate = 0.0
            HD_1.rate = 0.0
            HD_2.rate = 0.0
            HD_3.rate = 0.0
            HD_4.rate = 0.0
            HD_5.rate = 15
            HD_6.rate = 0.0
            HD_7.rate = 0.0
            HD_8.rate = 0.0
            HD_9.rate = 0.0
            HD_10.rate = 0.0
            HD_11.rate = 0.0
            
        if (angle_var.value <= 210.0 and angle_var.value > 180):
            HD_0.rate = 0.0
            HD_1.rate = 0.0
            HD_2.rate = 0.0
            HD_3.rate = 0.0
            HD_4.rate = 0.0
            HD_5.rate = 0.0
            HD_6.rate = 15
            HD_7.rate = 0.0
            HD_8.rate = 0.0
            HD_9.rate = 0.0
            HD_10.rate = 0.0
            HD_11.rate = 0.0
       
        if (angle_var.value <= 240 and angle_var.value > 210):
            HD_0.rate = 0
            HD_1.rate = 0.0
            HD_2.rate = 0.0
            HD_3.rate = 0.0
            HD_4.rate = 0.0
            HD_5.rate = 0.0
            HD_6.rate = 0.0
            HD_7.rate = 15
            HD_8.rate = 0.0
            HD_9.rate = 0.0
            HD_10.rate = 0.0
            HD_11.rate = 0.0
        
        if (angle_var.value <= 270 and angle_var.value > 240):
            HD_0.rate = 0.0
            HD_1.rate = 0.0
            HD_2.rate = 0.0
            HD_3.rate = 0.0
            HD_4.rate = 0.0
            HD_5.rate = 0.0
            HD_6.rate = 0.0
            HD_7.rate = 0.0
            HD_8.rate = 15
            HD_9.rate = 0.0
            HD_10.rate = 0.0
            HD_11.rate = 0.0
        
        if (angle_var.value <= 300 and angle_var.value > 270):
            HD_0.rate = 0.0
            HD_1.rate = 0.0
            HD_2.rate = 0.0
            HD_3.rate = 0.0
            HD_4.rate = 0.0
            HD_5.rate = 0.0
            HD_6.rate = 0.0
            HD_7.rate = 0.0
            HD_8.rate = 0.0
            HD_9.rate = 15
            HD_10.rate = 0.0
            HD_11.rate = 0.0
        
        if (angle_var.value <= 330 and angle_var.value > 300):
            HD_0.rate = 0.0
            HD_1.rate = 0.0
            HD_2.rate = 0.0
            HD_3.rate = 0.0
            HD_4.rate = 0.0
            HD_5.rate = 0.0
            HD_6.rate = 0.0
            HD_7.rate = 0.0
            HD_8.rate = 0.0
            HD_9.rate = 0.0
            HD_10.rate = 15
            HD_11.rate = 0.0
        
        if (angle_var.value <= 360 and angle_var.value > 330):
            HD_0.rate = 0.0
            HD_1.rate = 0.0
            HD_2.rate = 0.0
            HD_3.rate = 0.0
            HD_4.rate = 0.0
            HD_5.rate = 0.0
            HD_6.rate = 0.0
            HD_7.rate = 0.0
            HD_8.rate = 0.0
            HD_9.rate = 0.0
            HD_10.rate = 0.0
            HD_11.rate = 15
    
