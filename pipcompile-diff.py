#!/usr/bin/env python3

import argparse

def is_pypi_req(line):
    return '==' in line

def requirements_set(filename):
    requirements = set()
    with open(filename) as old_reqs:
        for line in old_reqs:
            if is_pypi_req(line):
                req = line.split('==')[0]
                requirements.add(req)

    return requirements

def compare_reqs(old, new):
    old_reqs = requirements_set(old)
    new_reqs = requirements_set(new)

    old_not_new = old_reqs - new_reqs
    new_not_old = new_reqs - old_reqs

    return {
        'old_not_new': old_not_new,
        'new_not_old': new_not_old,
    }

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('old_file', type=str)
    parser.add_argument('new_file', type=str)

    args = parser.parse_args()

    compared_reqs = compare_reqs(args.old_file, args.new_file)

    print("Present in old but not new:")
    for x in compared_reqs['old_not_new']:
        print(x)

    print("\n")

    print("Present in new but not old:")
    for x in compared_reqs['new_not_old']:
        print(x)