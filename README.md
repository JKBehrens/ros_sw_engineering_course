# ros_sw_engineering_course
This repository holds accompanying material for a course on Software Engineering in ROS. Please see 
[the course website](http://behrens-jan.de/ros-software-engineering-course/) for more details.

## Concepts shown in this ROS package include
* `CMakeLists.txt` and `package.xml` content
* Python library
* python ROS node
* launch files
* python unit tests
* generating documetation with doxygen and rosdoc_lite

## Generating documentation for a ROS package

We can use `rosdoc_lite` to generate documentation from a ROS package. It wraps Doxygen, Sphinx, and Epidoc to 
generate the documentation from annotations and comments in the code. Install `rosdoc_lite` using

```sudo apt-get install ros-melodix-rosdoc-lite```

Generate the doc by invoking 

```rosdoc_lite .```

in the package base folder. You can read the documentation by opening the [index.html](doc/index.html).

## Run tests
Run tests for this package by calling from workspace.

```catkin run_tests ros_example_pkg```

see results in the output or by calling

```catkin_test_results build/ros_example_pkg/```

from the workspace base folder.