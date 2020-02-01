from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md')) as f:
	long_description = f.read()

setup(
	name='opencc2',
	version='0.1.0',
	description='Open Chinese Convert (OpenCC) 2',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/sgalal/opencc2',
	author='sgalal',
	author_email='ayaka@mail.shn.hk',
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'Topic :: Text Processing :: Linguistic',
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
		'opencc2': ['dict/*.txt'],
	},
	include_package_data=True,
	python_requires='>=3.5, <4',
	install_requires=['pygtrie', 'jieba'],
	entry_points={
		'console_scripts': [
			'opencc2=opencc2:main',
		],
	},
	project_urls={
		'Bug Reports': 'https://github.com/sgalal/opencc2/issues',
		'Source': 'https://github.com/sgalal/opencc2',
	},
	zip_safe=False
)
