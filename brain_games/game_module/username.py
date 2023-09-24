#!/usr/bin/env python3

# This module asks the user for his name and greets him by name

import prompt


def username():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


if __name__ == '__main__':
    username()
