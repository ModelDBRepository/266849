#Activation of the input stream sensors. 
import sensor_msgs.msg
import numpy as np
@nrp.MapSpikeSource("red_sensor", nrp.brain.sensor_neuron[0:1], nrp.poisson,rng=1234)
@nrp.MapSpikeSource("blue_sensor",nrp.brain.sensor_neuron[1:2],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("green_sensor",nrp.brain.sensor_neuron[2:3],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("black_sensor",nrp.brain.sensor_neuron[3:4],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("brown_left_sensor",nrp.brain.wall_sensor[0:1],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("brown_right_sensor",nrp.brain.wall_sensor[1:2],nrp.poisson,rng=1234)
@nrp.MapVariable("red",initial_value = 0.000000001,scope = nrp.GLOBAL)
@nrp.MapVariable("blue",initial_value = 0.000000001,scope = nrp.GLOBAL)
@nrp.MapVariable("black",initial_value = 0.000000001,scope = nrp.GLOBAL)
@nrp.MapVariable("green",initial_value = 0.0000000001,scope = nrp.GLOBAL)
@nrp.MapVariable("brown_left",initial_value = 0.0000000001, scope = nrp.GLOBAL)
@nrp.MapVariable("brown_right",initial_value = 0.0000000001, scope = nrp.GLOBAL)
@nrp.MapVariable("flag_red", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("flag_blue", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("flag_black", initial_value = 0, scope = nrp.GLOBAL)
@nrp.Robot2Neuron()


def eye_sensor_transmit (t,red_sensor,blue_sensor,green_sensor,black_sensor,brown_left_sensor,brown_right_sensor,brown_left,brown_right,red,blue,black,green,flag_red,flag_blue,flag_black):
    
    import numpy as np
    def gaussian ( x, mi, sig):
        return np.exp(-np.power(x-mi,2.) / ( 2 * np.power(sig,2.)))
    
    if(red.value < 0.05):
        red_sensor.rate = gaussian(red.value, 0.05,0.012)*35
    if(red.value > 0.05): 
        red_sensor.rate = red.value/10
    if(blue.value < 0.05):
        blue_sensor.rate = gaussian(blue.value, 0.05, 0.012)*35
    if(blue.value > 0.05):
        blue_sensor.rate = blue.value/10
    if(black.value < 0.05):
        black_sensor.rate = gaussian(black.value, 0.035, 0.005)*35
    if(black.value > 0.05):
        black_sensor.rate = black.value/10
    green_sensor.rate = gaussian(green.value, 0.05, 0.012)*30
    
    brown_left_sensor.rate = gaussian(brown_left.value/10, 0.07, 0.01)*100
    brown_right_sensor.rate = gaussian(brown_right.value/10, 0.07, 0.01)*100