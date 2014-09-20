import os

from setuptools import setup, find_packages


# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-cked',
    version='0.1.0',
    author='Ivan Gorochov',
    author_email='cwteam@bk.ru',
    description=('CKEditor and elFinder integration for Django Framework.'),
    license='BSD',
    keywords='django, ckeditor, elfinder, wysiwyg, upload',
    url='https://github.com/dead23angel/django-cked',
    packages=find_packages(),
    long_description=read('README.rst'),

    classifiers = [
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    include_package_data=True
)
