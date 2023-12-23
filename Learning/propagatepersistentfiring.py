#This function implements the persistent neural firing concepts. 
@nrp.MapSpikeSource("persistent_red_sensor",nrp.brain.persistent_neuron[0:1],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("persistent_blue_sensor",nrp.brain.persistent_neuron[1:2],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("persistent_black_sensor",nrp.brain.persistent_neuron[2:3],nrp.poisson,rng=1234)
@nrp.MapSpikeSink("persistent_red_sensor_1",nrp.brain.persistent_neuron[0:1],nrp.spike_recorder)
@nrp.MapSpikeSink("persistent_blue_sensor_1",nrp.brain.persistent_neuron[1:2],nrp.spike_recorder)
@nrp.MapSpikeSink("persistent_black_sensor_1",nrp.brain.persistent_neuron[2:3],nrp.spike_recorder)
@nrp.MapVariable("flag_red", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("flag_blue", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("flag_black", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("time_red",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("time_blue",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("time_black",initial_value = 0, scope = nrp.GLOBAL)
@nrp.Robot2Neuron()
def propagatepersistentfiring (t,persistent_red_sensor,persistent_red_sensor_1,persistent_blue_sensor,persistent_blue_sensor_1,persistent_black_sensor,persistent_black_sensor_1,flag_red,flag_blue,flag_black,time_red,time_blue,time_black):
    if( persistent_red_sensor_1.spiked and flag_red.value == 0): #When the first spike starts, saves the time in a variable and stop another entry. 
        persistent_red_sensor.rate = 20
        time_red.value = t
        flag_red.value = 1 
    
    if( persistent_blue_sensor_1.spiked and flag_blue.value == 0):
        persistent_blue_sensor.rate = 20
        time_blue.value = t
        flag_blue.value = 1
        
    if(persistent_black_sensor_1.spiked and flag_black.value == 0):
        persistent_black_sensor.rate = 20
        time_black.value = t
        flag_black.value = 1
    
    if(t > time_red.value + 25):
        if(flag_black.value == 0 and flag_blue.value == 0): 
            time_red.value = time_red.value + 5
        else:
            persistent_red_sensor.rate = 0
            flag_red.value = 0
    if(t > time_blue.value + 25):
        if(flag_red.value == 0 and flag_black.value == 0):
            time_blue.value = time_blue.value + 5
        else:
            persistent_blue_sensor.rate = 0
            flag_blue.value = 0
    if(t > time_black.value + 25):
        if(flag_red.value == 0 and flag_blue.value == 0):
            time_black.value = time_black.value + 5
        else:
            persistent_black_sensor.rate = 0
            flag_black.value = 0