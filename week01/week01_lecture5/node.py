#!/usr/bin/env python3
"""
This example demonstrates the minimum structure required to create and run a
ROS2 node using Python (rclpy).

Run: python3 node.py

"""

import rclpy                           # Import the ROS2 Python client library.
from rclpy.node import Node            # Every ROS2 node is created by inheriting from the base Node class.

# ROS2 node (inherits from Node class)
class MyNode(Node): 
    def __init__(self):                # Constructor of the node
        super().__init__('my_node')    # Create a ROS2 node named "my_node".


def main():
    """
    Main function of the program.Typical execution sequence:
        1. Initialize ROS2
        2. Create the node
        3. Spin (keep the node running)
        4. Shutdown ROS2
    """
    rclpy.init()          # Initialize the ROS2 communication system
    node = MyNode()       # Create an instance of our node.
    rclpy.spin(node)      # Keep the node alive.
    rclpy.shutdown()      # Shutdown the ROS2 communication system

# Execute program only when this file is run directly (Not when imported as a module.)
if __name__ == '__main__':
    main()