from setuptools import setup

package_name = 'maintenance_pkg'

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
    description='Node maintenance demo',
    license='MIT license',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "payload01 = maintenance_pkg.Payload01:main",
            "payload02 = maintenance_pkg.Payload02:main",
            "payload03 = maintenance_pkg.Payload03:main",
            "payload03old = maintenance_pkg.Payload03old:main",
            "switcher = maintenance_pkg.Switcher:main",
            "maintainer = maintenance_pkg.Maintainer:main"
        ],
    },
)
