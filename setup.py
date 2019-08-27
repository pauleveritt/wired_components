from setuptools import setup, find_packages


def readfile(name):
    with open(name) as f:
        return f.read()


readme = readfile('README.rst')
changes = readfile('CHANGES.rst')

requires = ['zope.interface', 'venusian', 'wired']

docs_require = ['Sphinx', 'sphinx_rtd_theme', 'venusian']

tests_require = [
    'pytest',
    'pytest-cov',
    'mypy',
    'pytest-mypy'
]

setup(
    name='wired_components',
    description=(
        'Component, view, request, resource, and more...for wired.'
    ),
    version='0.0.1',
    long_description=readme + '\n\n' + changes,
    long_description_content_type='text/x-rst',
    author='Paul Everitt',
    author_email='pauleveritt@me.com',
    url='https://wired_components.readthedocs.io',
    packages=find_packages('src', exclude=['tests']),
    package_dir={'': 'src'},
    include_package_data=True,
    python_requires='>=3.7',
    install_requires=requires,
    extras_require={'docs': docs_require, 'tests': tests_require},
    zip_safe=False,
    keywords=','.join(
        [
            'ioc container',
            'inversion of control',
            'dependency injection',
            'service locator',
            'singleton',
            'service factory',
        ]
    ),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
