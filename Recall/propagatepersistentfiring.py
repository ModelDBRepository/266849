@nrp.MapSpikeSource("persistent_red",nrp.brain.persistent_neuron[0:1],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("persistent_blue",nrp.brain.persistent_neuron[1:2],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("persistent_black",nrp.brain.persistent_neuron[2:3],nrp.poisson,rng=1234)
@nrp.MapSpikeSink("persistent_red_1",nrp.brain.persistent_neuron[0:1],nrp.spike_recorder)
@nrp.MapSpikeSink("persistent_blue_1",nrp.brain.persistent_neuron[1:2],nrp.spike_recorder)
@nrp.MapSpikeSink("persistent_black_1",nrp.brain.persistent_neuron[2:3],nrp.spike_recorder)
@nrp.MapVariable("flag_red", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("flag_blue", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("flag_black", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("time_red", initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("time_blue",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("time_black",initial_value = 0, scope = nrp.GLOBAL)
@nrp.Robot2Neuron()
def propagatepersistentfiring (t,persistent_red,persistent_red_1,persistent_blue,persistent_blue_1,persistent_black,persistent_black_1,flag_red,flag_blue,flag_black,time_red,time_blue,time_black):
    if( persistent_red_1.spiked and flag_red.value == 0):
        persistent_red.rate = 20
        time_red.value = t
        flag_red.value = 1
    
    if( persistent_blue_1.spiked and flag_blue.value == 0):
        persistent_blue.rate = 20
        time_blue.value = t
        flag_blue.value = 1
    
    if(persistent_black_1.spiked and flag_black.value == 0):
        persistent_black.rate = 20
        time_black.value = t
        flag_black.value = 1
    
    if(t > time_red.value + 25):
        if(flag_blue.value == 0 and flag_black.value == 0):
            time_red.value = time_red.value + 5
        else:
            persistent_red.rate = 0
            flag_red.value = 0
            
    if(t > time_blue.value + 25):
        if(flag_red.value == 0 and flag_black.value == 0):
            time_blue.value = time_blue.value + 5
        else:
            persistent_blue.rate = 0
            flag_blue.value = 0

    if(t > time_black.value + 25):
        if(flag_red.value == 0 and flag_blue.value == 0):
            time_black.value = time_black.value + 5
        else:
            persistent_black.rate = 0
            flag_black.value = 0