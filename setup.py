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
          'simplejson',
          'stem',
          'logging',
          'argparse',
          'langdetect'
      ],
      entry_points={
          'console_scripts': [
              "start_onionrunner = caepainvestigatio.entry_points:run_onionscan",
              "json_to_database = caepainvestigatio.entry_points:send_json_to_db",
              "run_scan_onions = caepainvestigatio.entry_points:run_scan_onions",
              "feed_categories = caepainvestigatio.entry_points:feed_category_db",
          ]
      }
     )
