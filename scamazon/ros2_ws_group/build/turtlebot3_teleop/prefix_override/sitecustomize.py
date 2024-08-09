import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/student/RS1/RS1_group/scamazon/ros2_ws_group/install/turtlebot3_teleop'
