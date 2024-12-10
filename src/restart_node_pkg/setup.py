from setuptools import setup

package_name = 'restart_node_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Yinghao Xiang',
    maintainer_email='xiangyinghao@buaa.edu.cn',
    description='Node cycle restart demo',
    license='MIT license',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "payload01 = restart_node_pkg.Payload01:main",
            "payload02 = restart_node_pkg.Payload02:main",
            "payload03 = restart_node_pkg.Payload03:main",
            "switcher = restart_node_pkg.Switcher:main"
        ],
    },
)
