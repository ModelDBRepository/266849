@nrp.MapSpikeSink("Place_6",nrp.brain.place_cells[6:7],nrp.spike_recorder)
@nrp.MapSpikeSink("brown_left_output", nrp.brain.wall_neuron[1:2],nrp.spike_recorder)
@nrp.MapSpikeSink("brown_right_output", nrp.brain.wall_neuron[0:1],nrp.spike_recorder)
@nrp.MapVariable("var_angle",scope=nrp.GLOBAL)
@nrp.Neuron2Robot(Topic('/husky/husky/cmd_vel', geometry_msgs.msg.Twist))
def follow_place_cell_6 (t,Place_6,brown_left_output,brown_right_output,var_angle):
    
    if(brown_left_output.spiked and brown_right_output.spiked):
        return geometry_msgs.msg.Twist(linear = geometry_msgs.msg.Vector3(-2,0,0))
    elif (brown_left_output.spiked):
        return geometry_msgs.msg.Twist(linear = geometry_msgs.msg.Vector3(-1,0,0),angular=geometry_msgs.msg.Vector3(0,0,2))
    elif (brown_right_output.spiked):
        return geometry_msgs.msg.Twist(linear = geometry_msgs.msg.Vector3(-1,0,0),angular=geometry_msgs.msg.Vector3(0,0,-2))
    
    if Place_6.spiked:
        if(var_angle.value <=210 and var_angle.value > 180):
            return geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(1,0,0))
        elif(var_angle.value <= 180 and var_angle.value >30):
            return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,1))
        elif(var_angle.value <= 30 and var_angle.value > 0):
            return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,-1))
        elif(var_angle.value <= 360 and var_angle.value > 210):
            return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,-1))