from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='Python Codemagic Api',
    version='0.0.1',
    package=find_packages('src', exclude=['test']),
    package_dir={'': 'src'},
    author='Benjamin Hubbell',
    author_email='bdhubbell@icloud.com',
    url='https://github.com/bdhubbell/python-codemagic-api',
    description='Python API wrapper for Codemagic',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['Codemagic', 'API', 'Wrapper'],
    license='MIT',
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries'
    ],
)