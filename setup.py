from setuptools import setup, find_packages

setup(
    name='api',
    version='1',
    url='',
    license='Apache Software License',
    maintainer='',
    maintainer_email='',
    description='',
    long_description='',
    packages=find_packages(exclude=['test', 'test.*', '*.test']),
    install_requires=['flask',
                      'bravado-core',
                      'PyYAML'],
    package_data={'api': ['swagger.yml']},
    zip_safe=False,
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)

