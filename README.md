# Barrett Hand

ROS packages to control the [Barrett Hand](https://advanced.barrett.com/barretthand).
Supported models: BH8-280 and BH8-282

## bhand_controller

ROS controller based on the Barrett pyHand library to command and read the state of the hand.

## rqt_bhand

RQT plugin to control and monitor the hand

## barrett_hand_description

Barrett Hand description (urdf and meshes)

## barrett_hand_gazebo, barrett_hand_control

Barrett hand simulation package for ROS

- Launch the Gazebo simulation:

  ```sh
  roslaunch barrett_hand_gazebo barrett_hand.launch
  ```

- How to switch to available hand models:
  - Edit file `barrett_hand_description/robots/bh_alone.urdf.xacro` and change the name of the included file (`bh282.urdf.xacro` or `bh280.urdf.xacro`)
- Publish topics to control the hand:

  ```sh
  rostopic pub /bh_j11_position_controller/command std_msgs/Float64 'desired_angle'
  ```

- Controller list:
  - bh_j11_position_controller -> spread DoF
  - bh_j12_position_controller -> finger 1 grasp
  - bh_j22_position_controller -> finger 2 grasp
  - bh_j32_position_controller -> finger 3 grasp

## External dependencies

### pcan_python

Python wrapper for the Peak-CAN driver

Available at https://github.com/RobotnikAutomation/pcan_python.git

## References

- `barrett_hand_control` is forked from [RobotnikAutomation/barrett_hand_sim (kinetic-devel)](https://github.com/RobotnikAutomation/barrett_hand_sim/tree/kinetic-devel)
- `barrett_hand_description` is forked from [RobotnikAutomation/barrett_hand_common (kinetic-devel)](https://github.com/RobotnikAutomation/barrett_hand_common/tree/kinetic-devel)
- `barrett_hand_gazebo` is forked from [RobotnikAutomation/barrett_hand_sim (kinetic-devel)](https://github.com/RobotnikAutomation/barrett_hand_sim/tree/kinetic-devel)
- `bhand_controller` is forked from [RobotnikAutomation/barrett_hand (kinetic-devel)](https://github.com/RobotnikAutomation/barrett_hand/tree/kinetic-devel)
- `rqt_bhand` is forked from [RobotnikAutomation/barrett_hand (kinetic-devel)](https://github.com/RobotnikAutomation/barrett_hand/tree/kinetic-devel)