#!/usr/bin/env python
#
# Copyright (C) 2008, 2011-2015 Philipp Winter <phw@nymity.ch>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import math
import argparse


def parse_args():
    """Parse the given command line arguments."""

    parser = argparse.ArgumentParser(description="Generate a random password.")
    parser.add_argument("-l", "--length",
                        type=int,
                        default=30,
                        help="Password length in ASCII characters.")

    return parser.parse_args()


def get_rand_char(alphabet):
    """Get a random character in the given character alphabet."""

    char = os.urandom(1)
    while char not in alphabet:
        char = os.urandom(1)

    return char


def generate(args):
    """Generate and print a random password."""

    # The alphabet which determines the single characters in our password.  We
    # use the full printable ASCII range.

    alphabet = "".join([chr(c) for c in range(ord("!"), ord("~") + 1)])
    password = "".join([get_rand_char(alphabet) for _ in range(args.length)])
    entropy = math.log(len(alphabet) ** args.length, 2)

    print "%d-bit password:  %s" % (entropy, password)


if __name__ == "__main__":
    generate(parse_args())
