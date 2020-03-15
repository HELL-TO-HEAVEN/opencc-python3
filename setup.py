# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md')) as f:
	long_description = f.read()

with open(path.join(here, 'src/opencc-python3/version.py')) as f:
	exec(f.read())

setup(
	name='opencc-python3',
	version=__version__,
	description='Python 3 implementation of OpenCC',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/sgalal/opencc-python3',
	author='sgalal',
	author_email='ayaka@mail.shn.hk',
	license='MIT',
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Text Processing :: Linguistic',
		'Natural Language :: Chinese (Simplified)',
		'Natural Language :: Chinese (Traditional)',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8'
	],
	keywords='chinese chinese-language nlp natural-language-processing',
	packages=find_packages('src'),
	package_dir={'': 'src'},
	package_data={
		'opencc': ['opencc-dict/data/*'],
	},
	include_package_data=True,
	python_requires='>=3.5, <4',
	install_requires=['pygtrie'],
	entry_points={
		'console_scripts': [
			'opencc=opencc:main',
		],
	},
	project_urls={
		'Bug Reports': 'https://github.com/sgalal/opencc-python3/issues',
		'Source': 'https://github.com/sgalal/opencc-python3',
	},
	zip_safe=False
)
