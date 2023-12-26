from setuptools import setup, find_packages
import os
import pathlib

CURRENT_DIR = pathlib.Path(__file__).parent
README = (CURRENT_DIR / "README.md").read_text()

env = os.environ.get('source')


def get_dependencies():
    dependency = []

    if env and env == "code":
        return dependency

    return dependency + ["ppy-common", "pweb-form-rest", "ppy-jsonyml"]


setup(
    name='pweb-ssr',
    version='0.0.7',
    url='https://github.com/banglafighter/pweb-ssr',
    license='Apache 2.0',
    author='Bangla Fighter',
    author_email='banglafighter.com@gmail.com',
    description='Server Side Rendered UI, Form, Table Header, Item Per Page, Pagination, Jinja Customization things',
    long_description=README,
    long_description_content_type='text/markdown',
    package_data={'pweb_ssr': ['html/**/*']},
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=get_dependencies(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
    ]
)
