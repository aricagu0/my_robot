import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool

class ServiceClient(Node):
    def __init__(self):
        super().__init__('service_client')
        self.client = self.create_client(SetBool, 'my_service')

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('서버 기다리는 중...')

        self.send_request(True)

    def send_request(self, data):
        request = SetBool.Request()
        request.data = data
        future = self.client.call_async(request)
        future.add_done_callback(self.response_callback)

    def response_callback(self, future):
        response = future.result()
        self.get_logger().info(f'응답: {response.message}')

def main():
    rclpy.init()
    node = ServiceClient()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()