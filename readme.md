# Dynamixel Action Server Noetic
### Detatched ROS nodes for giving inputs to a dynamixel servo over u2d2

#### Terminal 1
    clone this branch
    docker-compose up

### Terminal 2
    docker exec -it dynamixel_ros_dynamxiel_operator_1 bash

    rosservice call /dynamixel_workbench/dynamixel_command "command: ''
id: 1
addr_name: 'Goal_Position'
value: 2048"

    rosservice call /dynamixel_workbench/execution "{}"

#### enjoy the demo