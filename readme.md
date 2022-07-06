# Dynamixel Action Server Noetic
## Detatched ROS nodes for giving inputs to a dynamixel servo over u2d2

### Terminal 1
    clone this branch
    docker-compose up

### Terminal 2
    docker exec -it dynamixel_ros_dynamxiel_action_server_1 bash

    rosrun dynamxiel_as_adapter dynamxiel_action_client_example.py

## If you want to change the zero position, or maximum accleration and velcoity:

    cd  dynamixel_as_adapter/config
    open ecoation_servo_demo.yaml

### Change these or other feilds to you liking:

    Profile_Acceleration: 3 # 214.577 rev/min^2 I wil just guess and set really low
    Profile_Velocity: 87 # 1sec/((0.229rev/min)/(60sec/1min)) = 263.157894737 rev -> 0.229*263 ~ 1rev/sec -> /3 ~ 1/3 rev/sec
    Homing_Offset: 0 # 0.088deg valid range -1,024 ~ 1,024 for position control mode