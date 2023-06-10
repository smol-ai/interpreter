from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gpt_code_ui',
    version='0.42.30',
    description="An Open Source version of ChatGPT Code Interpreter",
    long_description=long_description,
    long_description_content_type='text/markdown',  # This field specifies the format of the `long_description`.
    packages=find_packages(),
    package_data={'gpt_code_ui.webapp': ['static/*', 'static/assets/*']},
    install_requires=[
        'ipykernel>=6,<7',
        'snakemq>=1,<2',
        'requests>=2,<3',
        'Flask>=2,<3',
        'flask-cors>=3,<4',
        'python-dotenv>=1,<2',
        'numpy', # numpy==1.24.3
        'matplotlib', # matplotlib==3.7.1
        'pandas', # matplotlib==1.5.3
        'PyPDF2', # PyPDF2==3.0.1
        'pdfminer', # pdfminer==20191125
        'pdfplumber', # pdfplumber==0.9.0
        'camelot', # Camelot==12.6.29
        'dateparser' # dateparser==1.1.8
        'geopandas' # geopandas==0.13.2
    ],
    entry_points={
        'console_scripts': [
            'gptcode = gpt_code_ui.main:main',
        ],
    },
)
