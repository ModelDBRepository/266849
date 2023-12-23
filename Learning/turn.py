#After following one of the colored marked,the robot turns to search another one. 
@nrp.MapVariable("counter", initial_value = 0.0,scope = nrp.GLOBAL)
@nrp.MapVariable("starting_time", initial_value = 0.0,scope = nrp.GLOBAL)
@nrp.MapVariable("turn", initial_value = 0.0,scope = nrp.GLOBAL)
@nrp.Neuron2Robot(Topic('/husky/husky/cmd_vel', geometry_msgs.msg.Twist))
def turn (t,counter,starting_time,turn):
    if(turn.value == 1):
        if(counter.value == 0):
            starting_time.value = t
            counter.value = 1
        if(starting_time.value + 6.5 > t):
                return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,2.0))
        if(starting_time.value + 6.5 < t):
            turn.value = 0
            counter.value = 0