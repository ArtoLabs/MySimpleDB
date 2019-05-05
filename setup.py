from setuptools import setup, find_packages

setup(
    python_requires='>=3.0',
    name='MySimpleDB',
    version='1.0',
    packages=['mysimpledb'],
    license='MIT',
    keywords='pymysql, mysql, database',
    url='http://github.com/artolabs/mysimpledb',
    author='ArtoLabs',
    author_email='artopium@gmail.com',
    install_requires=[
        'screenlogger',
        'pymysql'
    ],
    py_modules=['mysimpledb'],
    include_package_data=True,
    zip_safe=False
)
