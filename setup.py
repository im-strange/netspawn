from setuptools import setup, find_packages

setup(
    name='netspawn',
    version='1.0.0',
	py_modules=["netspawn"],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'spawn=netspawn.cli:main',
        ],
    },
    install_requires=[
        "requests", "tqdm"
    ],
	include_package_data=True,
	package_data={
		'netspawn': [
			"data/*"
		]
	},
    author='im-strange',
    description='A command-line spawning tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/im-strange/spawn',
    license='MIT',
)
