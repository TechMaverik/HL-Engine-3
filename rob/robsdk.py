import requests


class RobSDK:

    def robot_position(self, payload, rob_url):
        response = requests.post(rob_url, json=payload)
        return response
