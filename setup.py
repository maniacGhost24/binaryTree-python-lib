from setuptools import find_packages, setup

setup(
    name = 'binaryTree',
    packages = find_packages(include=['binaryTree']),
    version = '0.2.0',
    description = 'Binary tree implementation.',
    author = 'Rishabh',
    license = 'public',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)