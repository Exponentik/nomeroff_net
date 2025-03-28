from setuptools import setup, find_packages
import os
import re


def read_version():
    # importing gpustat causes an ImportError :-)
    __PATH__ = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(__PATH__, 'nomeroff_net/__init__.py')) as f:
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                                  f.read(), re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find __version__ string")


# get project version
__version__ = read_version()

# get project long description
# setup.py
long_description = "Nomeroff Net - система распознавания автомобильных номеров"

# get project requirements list


setup(name='nomeroff-net',
      version=__version__,
      description='Automatic numberplate recognition system',
      long_description=long_description,
      long_description_content_type="text/markdown",
      classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        "Operating System :: OS Independent",
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
      ],
      keywords='ai nomeroffnet yolo11 yolov8 ocr rnn opensource license number plate recognition '
               'licenseplate numberplate license-plate number-plate ria-com ria.com ria',
      url='https://github.com/ria-com/nomeroff-net',
      author='Dmytro Probachay, Oleg Cherniy',
      author_email='dimabendera@gmail.com, oleg.cherniy@ria.com',
      license='GNU General Public License v3.0',
      packages=find_packages(),

      include_package_data=True,
      python_requires='>=3.9',
      zip_safe=False)
