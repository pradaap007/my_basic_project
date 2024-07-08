from setuptools import find_packages, setup

package_name = 'activity'

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
    maintainer='praveen',
    maintainer_email='praveen@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "act1_pub=activity.aty1_num_pub:main",
            "act1_sub=activity.aty1_num_sub:main",
            "add_2_ser=activity.add_two_int_service:main",
            "add_two_clt_nooop=activity.add_two_int_client_no_oop:main",
            "add_two_cltoop=activity.add_two_int_client:main",
            "act1_service=activity.activity1_service:main",
            "hw_sts=activity.hardwarestatus:main",

        ],
    },
)
