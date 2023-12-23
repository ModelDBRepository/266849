#This function helps the robot movement at the start of simulation. The firing rate of the first sensor is not strong enough to activate the corresponding object. This function only works for the first monitor, the other one are well activated by the persistent neurons. 
@nrp.MapSpikeSink("sensor", nrp.brain.sensor_neuron[0:4], nrp.spike_recorder)
@nrp.MapVariable("flag", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("fixing_time", initial_value = 0, scope = nrp.GLOBAL)
@nrp.Neuron2Robot(Topic('/husky/husky/cmd_vel', geometry_msgs.msg.Twist))
def starting_move  (t,sensor,flag,fixing_time):
    if(sensor.spiked and flag.value == 0):
        fixing_time.value = t
        flag.value = 1
    if(t < fixing_time.value + 9.0):
        return geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(0.5,0,0))
        
    