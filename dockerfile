FROM osrf/ros:noetic-desktop-full

RUN apt-get update && apt-get -y install \
    python3-pip \
    git \
    ros-noetic-catkin python3-catkin-tools

RUN pip install pyserial

RUN apt-get update && apt-get -y upgrade

ENV NVIDIA_VISIBLE_DEVICES \
    ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES \
    ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics

SHELL ["/bin/bash", "-c"]
ENV DEBIAN_FRONTEND=noninteractive

RUN mkdir -p /catkin_ws/src
COPY . ../catkin_ws/src/dynamixel_as
WORKDIR /catkin_ws

RUN cd src && git clone -b noetic-devel https://github.com/ecoation-labs/DynamixelSDK.git

RUN /bin/bash -c "source /opt/ros/noetic/setup.bash \
        && catkin build"

RUN echo 'source "/opt/ros/noetic/setup.bash"' >> ~/.bashrc \
    && echo 'source "/catkin_ws/devel/setup.bash"' >> ~/.bashrc

ADD my_ros_entrypoint.sh /usr/bin/my_ros_entrypoint
RUN chmod +x /usr/bin/my_ros_entrypoint

ENTRYPOINT [ "my_ros_entrypoint" ]