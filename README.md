# Humanoid Robotic Arm Simulation using ROS2 Humble, Docker & Gazebo

This repository contains the simulation of a humanoid robotic arm developed using ROS2 Humble inside a Docker container environment and simulated in Gazebo.

The project was created to understand:
- Containerized robotics development
- ROS2 environment setup using Docker
- Robot simulation workflow
- CAD to simulation pipeline
- Mesh optimization for Gazebo compatibility

The robotic arm CAD model was exported and integrated into a ROS2 simulation environment.  
During development, multiple simulation and mesh compatibility issues were encountered and resolved, making this project a valuable hands-on learning experience in robot simulation debugging.

---

# 🚀 Technologies Used

- ROS2 Humble
- Docker
- Gazebo
- Python
- URDF / Xacro
- Fusion 360

---

# 📂 Repository Structure

```
humanoid_arm_ws/
│── src/
│   ├── humanoid_arm/
│       ├── launch/
│       ├── meshes/
│       ├── urdf/
│       ├── config/
│       ├── package.xml
│       ├── CMakeLists.txt
```
---

# 🤖 Project Overview

This project focuses on simulating a humanoid robotic arm in Gazebo using ROS2 Humble running inside Docker.

The workflow included:

- Creating a ROS2 Humble Docker container
- Importing CAD models
- Generating robot description files
- Configuring Gazebo simulation
- Solving mesh compatibility issues
- Optimizing simulation performance

The project successfully resulted in a working robotic arm simulation in Gazebo.

---

# 🐳 Docker Environment Setup

A Docker container was created for ROS2 Humble to provide:

- Isolated development environment
- Dependency management
- Consistent ROS2 setup
- Portable simulation workflow

This helped in understanding containerized robotics development workflows commonly used in industry and research.

---

# ⚙️ CAD Model Integration

The robotic arm was first designed and exported from CAD software and integrated into the ROS2 simulation pipeline.

The robot description included:

- Links
- Joints
- Mesh files
- Robot hierarchy
- Visualization configuration

---

# 🔄 STL to DAE Mesh Conversion

One major challenge encountered during development was mesh compatibility and simulation performance.

Initially:

STL files caused rendering and compatibility issues
Simulation performance was heavy

To solve this:

STL mesh files were converted into .dae format
Meshes became lighter and more simulation-friendly
Gazebo compatibility improved significantly

This process also improved simulation loading and rendering performance.

---

# ✨ Features

- ROS2 Humble simulation environment
- Docker-based robotics workflow
- Gazebo robotic arm simulation
- Custom humanoid robotic arm model
- Optimized DAE mesh integration
- URDF/Xacro robot description
- Modular simulation architecture

---

# Screenshot

![Humanoid Arm Simulation](src/robot_bringup_pkg/.github/humandoid%20robot%20sim.gif)

---

# 📚 Learning Outcome

Through this project, I learned:

- Docker-based ROS2 development
- ROS2 Humble setup and workflow
- Gazebo simulation pipeline
- Robot mesh optimization
- STL to DAE conversion workflow
- URDF/Xacro integration
- Simulation debugging techniques
- Robotics development inside containers

**This project significantly improved my understanding of robotics simulation infrastructure and deployment workflows.**

---

# 🎯 Future Improvements
- Add ros2_control integration
- Add trajectory planning
- Implement MoveIt2
- Add gripper control
- Add object interaction
- Add RViz visualization enhancements

---

# 👨‍💻 Author

Zaid Khan | Robotics Enthusiast | ROS2 Developer

---
