#!/usr/bin/env python3
"""
This example demonstrates how a single ROS2 node can act as both a Publisher
and a Subscriber.

The node periodically publishes a message on a topic while simultaneously
listening to the same topic. Every published message is immediately received
by the subscriber callback.

Concepts Covered:
1. Creating a ROS2 Publisher.
2. Creating a ROS2 Subscriber.
3. Publishing String messages.
4. Receiving messages using a callback function.
5. Using a Timer to publish messages periodically.
6. Keeping the node alive using rclpy.spin().

Run: python3 pub_sub.py

"""

import rclpy                      # Import the ROS2 Python client library.
from rclpy.node import Node       # Import the base Node class.
from std_msgs.msg import String   # Import the standard String message type.

# A ROS2 node that acts as both a Publisher and a Subscriber
class PubSubNode(Node): 

    # Constructor of the node: Creates Publisher, Subscriber and Timer
    def __init__(self):         
        super().__init__('pubsub_node')                                           # Create a ROS2 node named "pubsub_node".
        self.pub = self.create_publisher( String, 'topic', 10)                    # Create a Publisher.
        self.sub = self.create_subscription( String, 'topic', self.callback, 10 ) # Create a Subscriber.
        self.timer = self.create_timer( 0.1, self.publish_msg)                    # Create a Timer.

    # Timer callback: Creates a String message and publishes it.
    def publish_msg(self):         
        msg = String()           # Create a new String message.     
        msg.data = "Hello ROS"   # Assign data to the message.       
        self.pub.publish(msg)    # Publish the message.

    # Subscriber callback: function is automatically called whenever a message is received on the subscribed topic
    def callback(self, msg):
        print(f"Received: {msg.data}") # std_msgs.msg.String (Incoming message)


def main():
    """
    Main function Execution sequence:
        1. Initialize ROS2
        2. Create the node
        3. Spin (keep processing callbacks)
        4. Shutdown ROS2
    """
    rclpy.init()         # Initialize ROS2
    node = PubSubNode()  # Create the Publisher-Subscriber node
    rclpy.spin(node)     # Keep the node alive
    rclpy.shutdown()     # Shutdown ROS2


# Execute the program only if this file is run directly.
if __name__ == '__main__':
    main()