from setuptools import setup

setup(name='gmg',
      version='1.0',
      description='An open source geophysical modelling GUI',
      url='https://github.com/btozer/gmg.git',
      author='Brook Tozer',
      author_email='btozer@ucsd.edu',
      license='BSD-3-Clause',
      packages=['gmg'],
      platforms = "Any",
      scripts = [],
      classifiers = [
       "Intended Audience :: End Users/Desktop",
       "Intended Audience :: Science/Research",
       "Intended Audience :: Developers",
       "Intended Audience :: Education",
       "Environment :: Console",
       "Programming Language :: Python :: 2.7",
       "License :: OSI Approved :: BSD License",
       "Natural Language :: English"],
      install_requires=[
      'scipy',
      'matplotlib',
      'numpy',
      'obspy',
      'wxpython'
      ],
      include_package_data=True,
      zip_safe=False)
