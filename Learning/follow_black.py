#Robot follows the black object based on input
@nrp.MapVariable("black_left",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("black_right",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("black",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("turn",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("exit",initial_value = 0,scope = nrp.GLOBAL)
@nrp.Neuron2Robot(Topic('/husky/husky/cmd_vel', geometry_msgs.msg.Twist))
def follow_black (t,black_left,black_right,black,turn,exit):
    if(turn.value == 0 and exit.value == 0):
        if(black.value > 0.4 and black.value < 0.6):
            turn.value = 1
        if (black_left.value > 0.0 and black_right.value > 0.0):
            return geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(0.5,0,0))
        if(black_left.value == 0 and black_right.value > 0.0):
            return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,-2))
        if(black_left.value > 0 and black_right.value == 0.0):
            return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,2))