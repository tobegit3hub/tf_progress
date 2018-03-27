# Update the code and upload the package to pypi
# 1. python ./setup.py sdist --format=gztar
# 2. twine upload dist/tf_progress-1.0.0.tar.gz

try:
  from setuptools import setup
  setup()
except ImportError:
  from distutils.core import setup

setup(
    name="tf_progress",
    version="0.1.2",
    author="tobe",
    author_email="tobeg3oogle@gmail.com",
    url="https://github.com/tobegit3hub/tf_progress",
    #install_requires=["tensorflow>=1.0.0"],
    description=
    "Easy-to-use library for logging training progress of TensorFlow",
    packages=["tf_progress"],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "console_scripts": [
            #"simple_tensorflow_serving=simple_tensorflow_serving.server:main",
        ],
    })
