#!/usr/bin/env python3

from setuptools import setup

setup(name='powerpoint2pdf',
      version='1.0.1',
      description='将PPT的页面导出为PDF',
      long_description=open('README.md', encoding='utf-8').read(),
      long_description_content_type='text/markdown',
      author='OpenHUTB',
      author_email='2929@hutb.edu.cn',
      url='https://github.com/OpenHUTB/ppt2pdf',
      packages=['powerpoint2pdf'],
      entry_points={
           'console_scripts': [
               'powerpoint2pdf = powerpoint2pdf.main:main'
           ]
      },
      install_requires=[
          'comtypes',
          'pdfCropMargins',
      ],
      classifiers=[
          'Programming Language :: Python :: 3',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
      ],
      python_requires='>=3.6'
    )
