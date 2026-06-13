from setuptools import find_packages, setup

package_name = 'my_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros',
    maintainer_email='ros@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
		'hello_node = my_robot.hello_node:main',
        'publisher_node = my_robot.publisher_node:main'
        ,
        'subscriber_node = my_robot.subscriber_node:main',
        'service_server = my_robot.service_server:main',
        'service_client = my_robot.service_client:main',
        'action_server = my_robot.action_server:main'


        ],
    },
)
