from distutils.core import setup

long_description = open('README.md').read()

setup(
    name = "weddingsnap-project",
    description='Weddingsnap Project',
    long_description=long_description,
    author = "Moreno Cunha",
    url = "https://github.com/morenopc/weddingsnap/",
    version = '0.1',
    packages=[
        'weddingsnap',
        'weddingsnap.apps',
        'weddingsnap.apps.albums',
        'weddingsnap.apps.albums.migrations'],
      classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
      ],
      package_data={
        'weddingsnap': ['templates/albums/*.html',
            'templates/*.html']
        }
)