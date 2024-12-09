from setuptools import setup

package_name = 'cycle_nodes_pkg'

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
    description='Node cycle base demo',
    license='MIT license',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "payload01 = cycle_nodes_pkg.Payload01:main",
            "payload02 = cycle_nodes_pkg.Payload02:main",
            "payload03 = cycle_nodes_pkg.Payload03:main",
            "normal = cycle_nodes_pkg.Normal:main"
            "switcher = cycle_nodes_pkg.Switcher:main"
        ],
    },
)
