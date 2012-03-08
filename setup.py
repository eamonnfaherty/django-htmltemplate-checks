from setuptools import setup, find_packages
setup(
    name='django-htmltemplate-checks',
    version=__import__('htmltemplate').get_version(limit=3),
    description='A Django application performs basic checks on your html templates for quality control',
    author='Eamonn Faherty',
    author_email='github@designandsolve.co.uk',
    url='https://github.com/eamonnfaherty/django-htmltemplate-checks',
    license='MIT',
    packages=find_packages(),
    install_requires=[
		'BeautifulSoup',
    ]
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Utilities',
        'Topic :: Software Development :: Quality Assurance',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False
)
