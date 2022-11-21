# Barrett Hand

![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04-green)
![ROS](https://img.shields.io/badge/ROS-noetic-yellow)
![Python](https://img.shields.io/badge/Python-3.x-blue)

ROS packages to control the [Barrett Hand](https://advanced.barrett.com/barretthand).
Supported models: BH8-280 and BH8-282

## Quick start with real Barrett

1. Prepare [prerequisites](#prerequisites)
2. Catkin build
3. Connect to hand

   ```sh
   roslaunch bhand_controller bhand_controller.launch
   ```

4. Testing through ROS services
   1. `rosservice call /bhand_node/actions "action: 1"` : INIT_HAND
   2. `rosservice call /bhand_node/actions "action: 6"` : CLOSE_HALF_GRASP
   3. `rosservice call /bhand_node/actions "action: 3"` : OPEN_GRASP

## Prerequisites

For Python3, please check the Barret manual from the RISE Notion.

### 1. Essentials

```sh
sudo apt-get install swig libelf-dev libpopt-dev
```

### 2. Peak-CAN driver

The PEAK driver is included in the Linux kernel, but there is a problem that some packages cannot be built. Therefore, it is recommended to overwrite and install the PEAK driver according to the following install guide.

1. Download `peak-linux-driver-8.x` from [here](https://www.peak-system.com/fileadmin/media/linux/index.htm). Scroll down and you will find the 'Download PCAN Driver Package' button.
2. Build and install
   ```sh
   tar -xzf peak-linux-driver-X.Y.Z.tar.gz
   cd peak-linux-driver-X.Y.Z
   make clean
   make NET=NO_NETDEV_SUPPORT
   sudo make install
   ```
3. Load PCAN driver w/o reboot and check the result. Example:
   ```sh
   $ sudo modprobe pcan
   $ pcaninfo
   PCAN driver version: 8.15.2
   PCAN-Basic version: 4.6.2.36

     * pcanusb32: "PCAN_USBBUS1" (0x051), PCAN-USB #1, devid=0x00 (/sys/class/pcan/pcanusb32)
   ```

### 3. pcan_python

The [pcan_python](https://github.com/RobotnikAutomation/pcan_python.git) is a Python 2.x wrapper for the Peak-CAN driver. We need to build this for Python 3.x.

1. Git clone `git clone https://github.com/RobotnikAutomation/pcan_python.git`
2. Fix some files. The below are examples for python3.8.
   1. Line 11 of `Makefile`: `INC = -I/usr/include/python3.8 -I/usr/include`
   2. Line 01 of `setup.py`: `#!/usr/bin/env python3`
3. Change the code style and build

    ```sh
    sudo apt install python3-dev
    cd pcan_python
    2to3 -w -n .
    make
    ```

4. Modify lines 12 to 15 of `pcan_python/pcan_module.py`(generated file) as follows:

   ```py
   # if __package__ or "." in __name__:
   #     from . import _pcan_module
   # else:
   #     import _pcan_module
   import _pcan_module
   ```

5. Install

   ```sh
   sudo make install
   ```

6. Add `/usr/lib` to PYTHONPATH

   ```sh
   export PYTHONPATH=/usr/lib:$PYTHONPATH
   ```

## Collections

### bhand_controller

- ROS controller based on the Barrett pyHand library to command and read the state of the hand.
- `bhand_controller` is forked from [RobotnikAutomation/barrett_hand (kinetic-devel)](https://github.com/RobotnikAutomation/barrett_hand/tree/kinetic-devel)

### rqt_bhand

- RQT plugin to control and monitor the hand
- `rqt_bhand` is forked from [RobotnikAutomation/barrett_hand (kinetic-devel)](https://github.com/RobotnikAutomation/barrett_hand/tree/kinetic-devel)

### barrett_hand_description

- Barrett Hand description (urdf and meshes)
- `barrett_hand_description` is forked from [RobotnikAutomation/barrett_hand_common (kinetic-devel)](https://github.com/RobotnikAutomation/barrett_hand_common/tree/kinetic-devel)

### barrett_hand_sim

- Barrett hand simulation package for ROS
- `barrett_hand_sim` is forked from [RobotnikAutomation/barrett_hand_sim (kinetic-devel)](https://github.com/RobotnikAutomation/barrett_hand_sim/tree/kinetic-devel)

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
