from setuptools import setup

setup(
    name="Mastermind Minion",
    version="0.1",
    url="https://github.com/nobodyisme/mastermind-minion",
    author="Andrey Vasilenkov",
    author_email="indigo@yandex-team.ru",
    packages=['minion',
              'minion.artifacts',
              'minion.watchers',
              'minion.subprocess',
              'minion.db'],
    package_dir={'minion': 'src/minion'},
    package_data={'minion': ['templates/*.html']},
    license="LGPLv3+",
    scripts=[]
)
