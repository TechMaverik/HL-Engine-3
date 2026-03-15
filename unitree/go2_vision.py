import cv2
import sys
import numpy as np
from unitree_sdk2py.core.channel import ChannelFactoryInitialize
from unitree_sdk2py.go2.video.video_client import VideoClient

class Go2Vision:
    
    def get_video_stream(self):
        if len(sys.argv)>1:
            ChannelFactoryInitialize(0, sys.argv[1])
        else:
            ChannelFactoryInitialize(0)
        client = VideoClient()  
        client.SetTimeout(3.0)
        client.Init()
        status, data = client.GetImageSample()      
        while status == 0:         
            status, data = client.GetImageSample()            
            image_data = np.frombuffer(bytes(data), dtype=np.uint8)
            image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)            
            cv2.imshow("Go2 Front Camera Vision", image)
            # Press ESC to stop
            if cv2.waitKey(20) == 27:
                break    
        cv2.destroyWindow("Go2 Front Camera Vision")

    def take_picture(self):
        if len(sys.argv)>1:
            ChannelFactoryInitialize(0, sys.argv[1])
        else:
            ChannelFactoryInitialize(0)
        client = VideoClient()
        client.SetTimeout(3.0)
        client.Init()
        
        code, data = client.GetImageSample()
        
        if code != 0:
            print("get image sample error. code:", code)
        else:
            imageName = "./saved_image_from_go2.jpg"
            print("ImageName:", imageName)
            with open(imageName, "+wb") as f:
                f.write(bytes(data))

