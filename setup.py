import sys
from os.path import dirname, join
from setuptools import setup


if sys.version_info.major < 3:
    raise NotImplementedError('Sorry, only Python 3 and above is supported.')

# additional metadata, requirements
keywords = ('file files rename renamer')
proj_name = 'prn'

install_requires = (
    # Below broken by pip, Win 10 EOL
    #~ 'colorama;            os_name == "nt" and platform_version < "10.0.10586" ',
    #~ 'win_unicode_console; os_name == "nt" and python_version < "3.6" ',
)
tests_require = ('pyflakes', 'readme_renderer'),
extras_require = dict(
    #~ foo=('foo',),
)

def get_version(filename, version='1.00'):
    ''' Read version as text to avoid machinations at import time. '''
    with open(filename) as infile:
        for line in infile:
            if line.startswith('__version__'):
                try:
                    version = line.split("'")[1]
                except IndexError:
                    pass
                break
    return version


def slurp(filename):
    try:
        with open(join(dirname(__file__), filename), encoding='utf8') as infile:
            return infile.read()
    except FileNotFoundError:
        pass  # needed at upload time, not install time


setup(
    name                = proj_name,
    description         = 'A powerful script to rename files. '
                          'Better, stronger, faster.',
    author_email        = 'mixmastamyk@github.com',
    author              = 'Mike Miller',
    keywords            = keywords,
    license             = 'GPL-3.0-or-later',
    long_description    = slurp('readme.rst'),
    long_description_content_type = 'text/x-rst',
    url                 = 'https://github.com/mixmastamyk/prename',
    version             = get_version(proj_name),

    extras_require      = extras_require,
    install_requires    = install_requires,
    python_requires     = '>=3.6',
    setup_requires      = install_requires,
    tests_require       = tests_require,
    scripts             = (proj_name,),

    classifiers         = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Terminals',
        'Topic :: System :: Filesystems',
    ],
)
