import os
import xacro
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # 1. Paths
    pkg_name = 'robot_bringup_pkg'
    pkg_path = get_package_share_directory(pkg_name)
    xacro_file = os.path.join(pkg_path, 'urdf', 'humanoid.xacro')

    # 2. Process Xacro to XML
    robot_description_config = xacro.process_file(xacro_file).toxml()

    # 3. Robot State Publisher Node
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': robot_description_config,
            'use_sim_time': True
        }]
    )

    return LaunchDescription([
        node_robot_state_publisher
    ])