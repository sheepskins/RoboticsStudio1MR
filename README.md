# Robotics Studio 1 MR

This repository contains a ROS (Robot Operating System) package for Robotics Studio 1. This package is designed to work with ROS Noetic and is designed to perform SLAM using RTABMap and Turtlebot 3 in a custom world

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before using this package, you should have the following prerequisites installed:

1. ROS Noetic: Make sure you have ROS Noetic installed on your system. You can follow the [official ROS Noetic installation guide](http://wiki.ros.org/noetic/Installation) for instructions.

2. TurtleBot3 Packages: You'll need the TurtleBot3 packages installed. You can find them on the [TurtleBot3 GitHub repository](https://github.com/ROBOTIS-GIT/turtlebot3). Follow the installation instructions provided there.

3. RTAB-Map: RTAB-Map is used for mapping and localization. Install RTAB-Map by following the instructions provided in the [RTAB-Map ROS Wiki](http://wiki.ros.org/rtabmap_ros).
   
4. Gazebo Models: Download the models from [Gazebo Worlds and Models Collection](https://github.com/leonhartyao/gazebo_models_worlds_collection) and [AWS Robomaker World](https://github.com/aws-robotics/aws-robomaker-small-warehouse-world)

## Installation

To use this package, follow these steps:

1. Clone this repository into your ROS workspace:

   ```bash
   cd ~/catkin_ws/src
   git clone https://github.com/sheepskins/RoboticsStudio1MR
   ```

2. Build the package:

   ```bash
   cd ~/catkin_ws
   catkin_make
   ```

3. Source the ROS setup script to add the newly built package to your ROS environment:

   ```bash
   source ~/catkin_ws/devel/setup.bash
   ```

## Usage

Once you have installed the package, you can use it with TurtleBot3 and RTAB-Map for mapping and localization tasks. Here are some basic usage instructions:

1. Launch the TurtleBot3 simulation:

   ```bash
   roslaunch rs1 amazon_warehouse.launch
   ```

2. Launch the RTAB-Map mapping node:

   ```bash
   roslaunch rs1 rtabmap.launch
   ```

3. Use the ROS Navigation stack to move the TurtleBot3 around in the simulation to create a map. Or use the keyboard teleop:
   ```bash
   roslaunch turtlebot3_teleop turtlebot3_teleop.launch
   ```

4. Save the map:

   ```bash
   rosservice call /rtabmap/save_db
   ```

6. You can now use the generated map for navigation or localization.
