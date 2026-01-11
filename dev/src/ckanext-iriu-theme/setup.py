from setuptools import setup, find_namespace_packages

setup(
    name='ckanext-iriu-theme',
    version='1.0.0',
    description='Custom theme for IRIU DataHub',
    long_description='A custom CKAN theme extension for IRIU DataHub with custom branding, colors, and UI elements.',
    author='IRIU Team',
    author_email='info@iriu.ca',
    license='AGPL',
    url='https://github.com/Farairiu/IRIU_DataHub',
    keywords='CKAN theme IRIU DataHub',
    packages=find_namespace_packages(include=['ckanext.*']),
    namespace_packages=['ckanext'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'ckan.plugins': [
            'iriu_theme=ckanext.iriu_theme.plugin:IriuThemePlugin',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python :: 3.10',
    ],
)
