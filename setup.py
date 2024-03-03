from setuptools import find_packages, setup

package_name = 'tutorial_controller'

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
    maintainer='Zoé Trejo',
    maintainer_email='enrique.hernandez@ingenieria.unam.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'first_node = tutorial_controller.first_node:main',
            'draw_circle = tutorial_controller.draw_circle:main',
            'pose_subscriber = tutorial_controller.pose_subscriber:main',
            'turtle_controller = tutorial_controller.turtle_controller:main'
        ],
    },
)
