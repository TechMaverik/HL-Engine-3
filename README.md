<image src="hlengine3.png"/></image>
# HL-Engine-3
Why use multiple tools to control different robots when HL Engine does it all?

HL Engine 3 is the latest version of the Human Level Engine which is a middleware, designed to simplify the development and integration of applications in robotics and computer vision. HL Engine 3 offers built-in support for Unitree Go2, Unitree Z1, Unitree G1, and Niryo Ned 2 robots, allowing you to control and manage multiple robot platforms from a single, unified interface.

## How HL ENGINE 3 can be used? 
HL Engine 3 works in 2 modes
* Client Server Mode
* Host Mode
* Custom Mode

## Client Server Mode (API)
In Client-Server Mode, the HL Engine 3 is deployed on a local machine—such as an onboard computer, laptop, or desktop—to which the robot is connected. The key advantage of this mode is that any device on the same network can access the robot’s features by calling its respective functional APIs. This includes devices like Android phones, iPads, development boards, custom boards, and more.

## Host Mode
In Host mode, the HL Engine 3 is installed on your laptop or desktop where the robot is connected, allowing you to access the HL Engine 3 Service Libraries and program the robots independently.

## Custom Mode
In Custom Mode you can add your custom api to the existing HL Engine 3 library for your custom robots which is ideal for research and development.

## Installation
* Install python 3.10 or greater versions
* Download HL-Engine-3
* Create a virtual Environment
<code> python - m venv .hlengine</code>
* Activate Virtual environment
<code>source .hlengine/bin/activate</code> for Linux.
* run <code>python -r requirements.txt</code>
<br>
Designed and Developed by Akhil Jacob



