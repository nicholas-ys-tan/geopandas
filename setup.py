try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

LONG_DESCRIPTION = """GeoPandas is a project to add support for geographic data to
`pandas`_ objects.

The goal of GeoPandas is to make working with geospatial data in
python easier. It combines the capabilities of `pandas`_ and `shapely`_,
providing geospatial operations in pandas and a high-level interface
to multiple geometries to shapely. GeoPandas enables you to easily do
operations in python that would otherwise require a spatial database
such as PostGIS.

.. _pandas: http://pandas.pydata.org
.. _shapely: http://toblerity.github.io/shapely
"""

setup(name='geopandas',
      version='0.1dev',
      description='Geographic pandas extensions',
      license='BSD',
      author='Kelsey Jordahl',
      author_email='kjordahl@enthought.com',
      url='http://geopandas.org',
      long_description=LONG_DESCRIPTION,
      packages=['geopandas'],
      install_requires=['pandas', 'shapely', 'fiona', 'descartes'],
)
