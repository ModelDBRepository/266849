#This function propagates the avoidance controller to potentiate che STPD synapse. 
@nrp.MapSpikeSink("brown_left_sensor",nrp.brain.wall_sensor[0:1],nrp.spike_recorder)
@nrp.MapSpikeSink("brown_right_sensor",nrp.brain.wall_sensor[1:2],nrp.spike_recorder)
@nrp.MapSpikeSource("brown_left_output",nrp.brain.wall_neuron[0:1],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("brown_right_output",nrp.brain.wall_neuron[1:2],nrp.poisson,rng=1234)
@nrp.Robot2Neuron()
def propagate_brown (t,brown_left_sensor,brown_right_sensor,brown_left_output,brown_right_output):
    if brown_left_sensor.spiked:
        brown_left_output.rate = 50
    elif not brown_left_sensor.spiked:
        brown_left_output.rate = 0
    if brown_right_sensor.spiked:
        brown_right_output.rate = 50
    elif not brown_right_sensor.spiked:
        brown_right_output.rate = 0
    