#! /bin/bash

# source: http://wiki.ros.org/melodic/Installation/Ubuntu

sudo apt update -y && apt upgrade -y
sudo apt install -y curl gnupg2 lsb-release git meld build-essential libfontconfig1 mesa-common-dev libglu1-mesa-dev

cd $HOME

# ROS packages source
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

sudo apt update -y

# ROS install
sudo apt install -y ros-melodic-desktop-full
sudo apt install -y python-wstool python-catkin-tools
sudo apt install -y ros-melodic-moveit

# rosdep setup
sudo apt install python-rosdep
sudo rosdep init
rosdep update


