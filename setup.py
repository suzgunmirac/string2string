from setuptools import find_packages, setup

setup(
    name='string2string',
    version='0.0.1.2',
    description='Pattern matching (string to string) algorithms',
    url='https://github.com/suzgunmirac/string2string',
    author='Mirac Suzgun',
    author_email='msuzgun@stanford.edu',
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    tests_require=['pytest'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        "Typing :: Typed"
    ],
    keywords=[
        'string matching',
        'pattern matching',
        'edit distance',
        'string to string correction',
        'string to string matching',
        'Levenshtein edit distance',
        'Hamming distance',
        'Damerau–Levenshtein distance',
        'Jaro–Winkler distance',
        'longest common subsequence',
        'longest common substring',
        'dynamic programming',
        'approximate string matching',
    ]
)    