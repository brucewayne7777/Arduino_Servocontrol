import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/sudhaavan/tactile_sensor_ros2_ws/src/servo_controller/install/servo_controller'
