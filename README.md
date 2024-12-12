# SR-flight-software

![pic](https://img.shields.io/badge/version-v0.0.1-green)
![python](https://img.shields.io/badge/Python-3.8-green?logo=python&logoColor=ffffff)

A flight software based on ROS2-foxy.

> 2024.12 : Currently working on python, cpp (with lifecycle nodes) version will be done soon.

![fig_20241210_72174](images/fig_20241210_36878_uploaded.jpg)  

## Requirements

- Ubuntu-20.04 with ROS2-foxy (or newer)
- Python3.8 (as required by ROS2)
- colcon
- gcc
- make
- cmake

## install

Ubuntu-20.04 uses ROS2-foxy while Ubuntu-22.04 uses ROS2-humble. We take foxy as an example.

### ROS2-foxy

You can follow the next steps:
```bash
$ echo "deb [arch=$(dpkg --print-architecture)] https://repo.huaweicloud.com/ros2/ubuntu/ $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
$ sudo apt install curl gnupg2 -y
$ curl -s https://gitee.com/ohhuo/rosdistro/raw/master/ros.asc | sudo apt-key add -
```

Then you have to update your pkg list:
```bash
$ sudo apt update 
```

After that, ROS2 is reday to be installed:
```bash
$ sudo apt install ros-foxy-desktop
$ sudo apt install python3-argcomplete
```

You can add ros2 to the system's command via: `echo "source /opt/ros/foxy/setup.bash" >> ~/.bashrc`

### colcon

Easy-to-use tool, you can install it via:

```bash
sudo apt-get install python3-colcon-common-extensions
```

## Packages

Our system demo includes 4 packages, all of them can be compiled by `colcon build`(at `SR-flisght-software/`):

- cycle_nodes_pkg
- maintaince_pkg
- more_interfaces
- restart_node_pkg

### maintaince_pkg

Includes some interfaces, needs compile.

> TODO: note for add more interfaces

### cycle_nodes_pkg

Include basic nodes that can reply to the switcher node.

You can use it by:

```bash
$ cd SR-flight-software
$ colcon build
$ source ./install/setup.bash
$ ros2 run cycle_nodes_pkg switcher
```

(3 new terminals)
```bash
$ ros2 run cycle_nodes_pkg payload01
$ ros2 run cycle_nodes_pkg payload02
$ ros2 run cycle_nodes_pkg payload03
```

### restart_node_pkg

Include demo for cycle verify and restart node.

You can use it by:

```bash
$ cd SR-flight-software
$ colcon build
$ source ./install/setup.bash
$ ros2 run restart_node_pkg switcher
```

(3 new terminals)
```bash
$ ros2 run restart_node_pkg payload01
$ ros2 run restart_node_pkg payload02
$ ros2 run restart_node_pkg payload03
```

Now it's ready for you to interrupt some of them:
```bash
$ ros2 topic pub /destroy std_msgs/msg/Int32 'data: 1'
```

### maintaince_pkg

Include demo for how to do maintaince for a certain node.

You can use it by:

```bash
$ cd SR-flight-software
$ colcon build
$ source ./install/setup.bash
$ ros2 run maintaince_pkg switcher
```

(4 new terminals)
```bash
$ ros2 run maintaince_pkg payload01
$ ros2 run maintaince_pkg payload02
$ ros2 run maintaince_pkg payload03old
$ ros2 run maintaince_pkg maintainer
```

Then you can start to switch `payload03old` to a new one:
```bash
$ ros2 topic pub /command_break std_msgs/msg/Int32 'data: 999'
```
