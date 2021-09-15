from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='IncorrectQ-Extension',
    url='https://github.com/jladan/package_demo',
    author='Trivenger',
    author_email='',
    # Needed to actually package something
    packages=['IncorrectQ'],
    # Needed for dependencies
    install_requires=['selenium','random'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='None atm',
    description=' ',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)