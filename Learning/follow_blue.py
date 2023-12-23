#Robot follows the blue object based on input
@nrp.MapVariable("blue_left",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("blue_right",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("blue",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("turn",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("exit",initial_value = 0,scope = nrp.GLOBAL)
@nrp.Neuron2Robot(Topic('/husky/husky/cmd_vel', geometry_msgs.msg.Twist))
def follow_blue (t,blue_left,blue_right,blue,turn,exit):
    if(turn.value == 0 and exit.value == 0):
        if(blue.value > 0.4 and blue.value < 0.62):
            turn.value = 1
        if (blue_left.value > 0 and blue_right.value > 0):
            return geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(0.5,0,0))
        if(blue_left.value == 0 and blue_right.value > 0):
            return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,-2))
        if(blue_left.value > 0 and blue_right.value == 0):
            return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,2))