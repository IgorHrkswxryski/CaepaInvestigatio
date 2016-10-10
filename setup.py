""" setup package caepaInvertigatio """

from setuptools import setup

PROJECT_NAME = "CaepaInvestigatio"
LIB_DIRECTORY = "."

setup(name=PROJECT_NAME,
      version="0.1",
      description="Search and corellate data from TOR onion.",
      author='kladgs & totoche',
      install_requires=[
          'cymon',
          'shodan',
          'mongoengine',
          'stem',
          'logging',
          'argparse'
      ],
      docs_require=[
          'sphinx'
      ],
      entry_points={
          'console_scripts': [
              "start_onionrunner = caepainvestigatio.entry_points:run_onionscan"
          ]
      }
     )
