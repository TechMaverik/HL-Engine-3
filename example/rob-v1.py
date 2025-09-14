from rob.robsdk import RobSDK

desired_position={  "base":90,"shoulder":90,"elbow":90,"wrist":90,"end-effector":90,"pick":90,}
rob_url="http://example.com/rob/move" #Use your actual URL here
feedback=RobSDK().robot_position(desired_position, rob_url)