#Store the synaptic weights in different CSV files. 
import hbp_nrp_cle.tf_framework as nrp
nrp.config.brain_root.persistent_red_connection
nrp.config.brain_root.persistent_blue_connection
nrp.config.brain_root.persistent_blue1_connection
nrp.config.brain_root.persistent_black_connection
nrp.config.brain_root.angular_red_connection
nrp.config.brain_root.angular_blue_connection
nrp.config.brain_root.angular_black_connection
nrp.config.brain_root.angular_green_connection
nrp.config.brain_root.wall_connection_right
nrp.config.brain_root.wall_connection_left

@nrp.MapCSVRecorder('recorder', filename='persistent_red.csv', headers=['weight,time'])
@nrp.MapCSVRecorder('recorder_1', filename='persistent_blue.csv', headers=['weight,time'])
@nrp.MapCSVRecorder('recorder_2', filename='persistent_blue_1.csv', headers=['weight,time'])
@nrp.MapCSVRecorder('recorder_3', filename='persistent_black.csv', headers=['weight,time'])
@nrp.MapCSVRecorder('recorder_4', filename='angular_red.csv', headers=['weight,time'])
@nrp.MapCSVRecorder('recorder_5', filename='angular_blue.csv', headers=['weight,time'])
@nrp.MapCSVRecorder('recorder_6', filename='angular_black.csv', headers=['weight,time'])
@nrp.MapCSVRecorder('recorder_7', filename='angular_green.csv', headers=['weight,time'])
@nrp.MapCSVRecorder('recorder_8', filename='wall_right.csv', headers=['weight,time'])
@nrp.MapCSVRecorder('recorder_9', filename='wall_left.csv', headers=['weight,time'])
@nrp.MapVariable("start_record",initial_value = 0,scope = nrp.GLOBAL)
@nrp.Neuron2Robot(Topic('/monitor/spike_recorder', cle_ros_msgs.msg.SpikeEvent))

def weight_record (t,start_record,recorder,recorder_1,recorder_2,recorder_3,recorder_4,recorder_5,recorder_6,recorder_7,recorder_8,recorder_9):
    if(start_record.value == 1):
        recorder.record_entry(nrp.config.brain_root.persistent_red_connection.get("weight",format="list"),t)
        recorder_1.record_entry(nrp.config.brain_root.persistent_blue_connection.get("weight",format="list"),t)
        recorder_2.record_entry(nrp.config.brain_root.persistent_blue1_connection.get("weight",format="list"),t)
        recorder_3.record_entry(nrp.config.brain_root.persistent_black_connection.get("weight",format="list"),t)
        recorder_4.record_entry(nrp.config.brain_root.angular_red_connection.get("weight",format="list"),t)
        recorder_5.record_entry(nrp.config.brain_root.angular_blue_connection.get("weight",format="list"),t)
        recorder_6.record_entry(nrp.config.brain_root.angular_black_connection.get("weight",format="list"),t)
        recorder_7.record_entry(nrp.config.brain_root.angular_green_connection.get("weight",format="list"),t)
        recorder_8.record_entry(nrp.config.brain_root.wall_connection_right.get("weight",format="list"),t)
        recorder_9.record_entry(nrp.config.brain_root.wall_connection_left.get("weight",format="list"),t)