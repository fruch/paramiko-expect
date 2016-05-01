from setuptools import setup


setup(
    name='paramiko-expect',
    version='0.1.2',
    url='https://github.com/fgimian/paramiko-expect',
    license='MIT',
    author='Fotis Gimian',
    author_email='fgimiansoftware@gmail.com',
    description='An expect-like extension for the Paramiko SSH library',
    platforms='Posix',
    py_modules=['paramikoe'],
    install_requires=[
        'paramiko<2.0,>=1.10',
    ],
)
