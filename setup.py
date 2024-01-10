from setuptools import setup, find_packages

setup(
    name='lognet',
    version='2.0.0',
    packages=['lognet'],
    author='Noloquideus',
    author_email='daniilmanukian@gmail.com',
    description='A simple logger with a convenient log message format.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Noloquideus/Lognet',
    license='MIT License',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
