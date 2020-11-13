#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name='pygments-style-ept',
    version='0.1',
    description='Pygments version of the ept theme.',
    long_description=open('README.md').read(),
    keywords='pygments style ept',
    license='BSD',

    author='Adam Golinski',
    author_email='adam.gol1993@gmail.com',

    url='https://github.com/talesa/pygments-style-ept',

    packages=find_packages(),
    install_requires=['pygments >= 1.4'],

    entry_points='''[pygments.styles]
                    ept=pygments_style_ept:EPTStyle''',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
