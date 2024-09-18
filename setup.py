from setuptools import setup, find_packages
from setuptools.command.install import install as _install
import subprocess

class install(_install):
    def run(self):
        _install.run(self)t
        subprocess.call(['python3', 'post_install.py'])

setup(
    name='netspawn',
    version='1.0.0',
	py_modules=["netspawn"],
    packages=find_packages(),
    cmdclass={'install': install},
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
