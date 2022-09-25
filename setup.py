# coding: utf-8

"""
    Snowflake SQL API V2

    The Snowflake SQL API is a REST API that you can use to access and update data in a Snowflake database.   
    Contact Support: tungnq@gmail.com  # noqa: E501

    OpenAPI spec version: 1.0.0
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "snowflake-sql-api-client"
VERSION = "2.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil", "pyjwt", "cryptography"]

setup(
    name=NAME,
    version=VERSION,
    description="Snowflake SQL API V2",
    author_email="tungnq@gmail.com",
    url="https://github.com/nqtung/snowflake-sql-api-pyclient",
    keywords=["Snowflake SQL API V2"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    The Snowflake SQL API is a REST API that you can use to access and update data in a Snowflake database.   
    Contact Support:  tungnq@gmail.com  # noqa: E501
    """
)
