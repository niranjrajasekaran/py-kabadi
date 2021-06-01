from distutils.core import setup

setup(
    name = 'py-kabadi',
    version = '1.0.3',
    description = 'Kabadi Wrapper',
    long_description = 'Kabadi Wrapper',

    author = 'Niranj Rajasekaran',
    author_email = 'niranj@fantain.com',
    url = 'https://github.com/niranjfantain/py-kabadi',
    package_dir={'': 'src'},
    packages=[''],
    install_requires=['certifi==2017.4.17', 'chardet==3.0.4', 'idna==2.5', 
                      'requests==2.18.1', 'urllib3==1.26.5'],
    entry_points='''
        [console_scripts]
        pykabadi=src.pykabadi:RcaApp
    '''
)
