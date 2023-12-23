#Robot follows the green(exit) object based on input
@nrp.MapVariable("green_left",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("green_right",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("green",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("start_record",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("turn",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("exit",initial_value = 0,scope = nrp.GLOBAL)
@nrp.Neuron2Robot(Topic('/husky/husky/cmd_vel', geometry_msgs.msg.Twist))
def exit (t,green_left,green_right,green,start_record,turn,exit):
    if(turn.value == 0):
        if(green.value > 0.25 and green.value < 0.3):
            start_record.value = 1
            return geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(0.0,0,0))
        if (green_left.value > 0.0 and green_right.value > 0.00014):
            exit.value = 1
            return geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(0.5,0,0))
        if (green_left.value == 0 and green_right.value > 0.00014):
            exit.value = 1
            return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,-2.0))
        if(green_left.value > 0 and green_right.value < 0.00014):
            exit.value = 1
            return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,2.0))