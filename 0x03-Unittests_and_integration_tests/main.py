#!/usr/bin/env python3
from utilis import *


nested = {'a': {'b': 2}}
output = access_nested_map(nested, ['a',])
print(f'Output: {output}')