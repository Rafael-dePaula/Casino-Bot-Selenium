from re import *
from string import *


def sub_map(sentence, prefix_key='\$\{', suffix_key='\}', **pairs):
    new_str = sentence[:]
    for k, v in pairs.items():
        key = prefix_key + k + suffix_key
        new_str = sub(key, v, new_str)
    return new_str
