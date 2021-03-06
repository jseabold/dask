#!/usr/bin/env python

from os.path import exists
from setuptools import setup
import dask

extras_require = {
  'array': ['numpy', 'toolz >= 0.7.2'],
  'bag': ['cloudpickle >= 0.2.1', 'toolz >= 0.7.2', 'partd >= 0.3.2'],
  'dataframe': ['numpy', 'pandas >= 0.16.0', 'toolz >= 0.7.2',
                'partd >= 0.3.2', 'cloudpickle >= 0.2.1'],
  'distributed': ['distributed'],
  'imperative': ['toolz >= 0.7.2'],
}
extras_require['complete'] = sorted(set(sum(extras_require.values(), [])))

setup(name='dask',
      version=dask.__version__,
      description='Minimal task scheduling abstraction',
      url='http://github.com/dask/dask/',
      maintainer='Matthew Rocklin',
      maintainer_email='mrocklin@gmail.com',
      license='BSD',
      keywords='task-scheduling parallelism',
      packages=['dask', 'dask.array', 'dask.bag', 'dask.store', 'dask.bytes',
                'dask.dataframe', 'dask.dataframe.tseries', 'dask.diagnostics'],
      long_description=(open('README.rst').read() if exists('README.rst')
                        else ''),
      extras_require=extras_require,
      zip_safe=False)
