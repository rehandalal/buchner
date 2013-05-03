from setuptools import setup, find_packages
import re
import os


READMEFILE = 'README.rst'
VERSIONFILE = os.path.join('buchner', '__init__.py')
VSRE = r"""^__version__ = ['"]([^'"]*)['"]"""


def get_version():
    verstrline = open(VERSIONFILE, 'rt').read()
    mo = re.search(VSRE, verstrline, re.M)
    if mo:
        return mo.group(1)
    else:
        raise RuntimeError(
            'Unable to find version string in {0}.'.format(VERSIONFILE))


setup(
    name='buchner',
    version=get_version(),
    author='Rehan Dalal',
    author_email='rehandalal@gmail.com',
    description='Flask project template and helper library',
    long_description=open(READMEFILE).read(),
    url='https://github.com/rehandalal/buchner',
    license='BSD',
    zip_safe=False,
    scripts=["bin/buchner-tool"],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ]
)
