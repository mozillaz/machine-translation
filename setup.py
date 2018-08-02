"""
PonMatch setup file.
"""
from setuptools import setup, find_packages


with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='ponmatch',
    version='0.1',
    description="Find strings in po files that matches to Pontoon's machine translation results.",
    long_description=readme,
    keywords='l10n, localization, mozilla, pontoon, translation',
    url='https://github.com/mozillaz/machine-translation',
    author='Emin Mastizada',
    author_email='emin@linux.com',
    license='MPLv2',
    packages=find_packages(),
    install_requires=[
        'requests', 'polib'
    ],
    scripts=['ponmatch/ponmatch'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Localization',
        'Environment :: Console',
    ],
    project_urls={
        "Bug Reports": "https://github.com/mozillaz/machine-translation/issues",
        "Source": "https://github.com/mozillaz/machine-translation",
        "Say Thanks!": "https://saythanks.io/to/mastizada"
    },
    zip_safe=False
)
