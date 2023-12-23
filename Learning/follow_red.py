#Robot follows the red object based on input
@nrp.MapVariable("red_left",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("red_right",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("red",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("turn",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("exit",initial_value = 0,scope = nrp.GLOBAL)
@nrp.Neuron2Robot(Topic('/husky/husky/cmd_vel', geometry_msgs.msg.Twist))
def follow_red (t,red_left,red_right,red,turn,exit):
    if(turn.value == 0 and exit.value == 0):
        if(red.value > 0.45 and red.value < 0.55):
            turn.value = 1
        if (red_left.value > 0.0 and red_right.value > 0.002):
            return geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(0.5,0,0))
        if(red_left.value == 0 and red_right.value > 0.002):
            return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,-2))
        if(red_left.value > 0 and red_right.value < 0.002):
            return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,2))