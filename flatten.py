#!/usr/bin/env python


def flatten(d, accumulator='', separator='.'):

    new_dictionary = {}

    for k, v in d.items():
        key = accumulator + k

        if isinstance(v, dict):
            recurse_result = flatten(v, key + separator)
            new_dictionary.update(recurse_result)
        else:
            new_dictionary[key] = v

    return new_dictionary


d = {
    "a": 5,
    "b": 6,
    "c": {
        "f": 9,
        "g": {
            "m": 17,
            "n": 3
        }
    }
}

print(flatten(d))
