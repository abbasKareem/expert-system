import collections
from pprint import pprint

Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel'
])

scientists = [
    Scientist(name='Ada lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy noether', field='math', born=188, nobel=False),
]
pprint(scientists)