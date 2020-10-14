from distutils.core import setup


setup(name='jaxboard',
        version='0.1',
        description='A tensorboard logger for jax',
        long_description=(
            'An enhanced version of the trax jaxboard'
            'that provides logging capabilities for the jax.experimental.stax package'
        ),
        author='Eduardo Pignatelli',
        author_email='edu.pignatelli@gmail.com',
        url='https://github.com/epignatelli/jaxboard',
        packages=['jaxboard'],
        install_requires=[
            'numpy',
            'matplotlib',
            'tensorboard',
            'tensorflow>=1.15.0',
            'tensorflow-gpu>=1.15.0',
        ]
     )