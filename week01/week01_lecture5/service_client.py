#!/usr/bin/env python3
"""
In this example, the node creates both the Service Server and the Service
Client. The client sends two integers to the server, and the server returns
their sum.

Concepts Covered:
• Declaring and reading ROS2 parameters.
• Creating a Service Server.
• Creating a Service Client.
• Waiting for a service to become available.
• Sending an asynchronous service request.
• Running a ROS2 node using rclpy.spin().

Service Used: example_interfaces/srv/AddTwoInts
Run: python3 03_service_client.py

"""

import rclpy                                     # Import the ROS2 Python client library.
from rclpy.node import Node                      # Import the base Node class.
from example_interfaces.srv import AddTwoInts    # Import the AddTwoInts service definition.

class MyNode(Node):
    """
    A ROS2 node demonstrating:
    1. Parameters
    2. Service Server
    3. Service Client
    The same node contains both the client and the server for demonstration
    purposes. In real applications, these are usually implemented in separate
    nodes.
    """

    # Constructor of the node creates Parameter, Service Server, Service Client
    def __init__(self):
        super().__init__('my_node')                              # Create a ROS2 node named "my_node".
        self.declare_parameter('speed', 1.0)                     # Declare a parameter named "speed"

        self.srv = self.create_service(AddTwoInts, 'add', self.handle_service) # Create a service named "add".
        # Whenever a request arrives, handle_service() is automatically executed.

        self.client = self.create_client(AddTwoInts, 'add')      # Create a client for the same "add" service.
        while not self.client.wait_for_service(timeout_sec=1.0): # Wait until the service becomes available.
            pass
       
        self.send_request()# Send a service request.

    # Service callback: is automatically executed whenever a client sends a request to the "add" service.
    def handle_service(self, request, response):     
        response.sum = request.a + request.b     # Add the two integers.        
        return response                          # Return the response to the client.

    # Create and send a service request
    def send_request(self):      
        req = AddTwoInts.Request()                # Create an empty request object.        
        req.a = 2                                 # Assign values to the request.
        req.b = 3                                 # Assign values to the request.
        future = self.client.call_async(req)      # Send the request asynchronously.
        speed = self.get_parameter('speed').value # Read the value of the parameter named "speed".

        print(f"Speed param: {speed}")


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


# Execute the program only if this file is run directly.
if __name__ == '__main__':
    main()