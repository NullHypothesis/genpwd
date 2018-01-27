#!/usr/bin/env python3
#
# Copyright (C) 2008, 2011-2018 Philipp Winter <phw@nymity.ch>
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
import binascii

import alphabets


def parse_args():
    """Parse the given command line arguments."""

    parser = argparse.ArgumentParser(description="Generate a random password.")
    group = parser.add_mutually_exclusive_group(required=False)

    group.add_argument("-l", "--length",
                       type=int,
                       help="Password length in ASCII characters or diceware "
                       "words.")

    group.add_argument("-e", "--entropy",
                       type=int,
                       default=120,
                       help="Desired amount of password entropy.")

    parser.add_argument("-d", "--diceware",
                        action="store_true",
                        help="Use diceware instead of ASCII characters. "
                        "Passphrase will be longer but easier to remember.")

    return parser.parse_args()


def rand_available():
    """
    Return True if os.urandom is available, and False otherwise.
    """

    try:
        _ = os.urandom(1)
    except NotImplementedError:
            return False
    return True


def rand_int(max_int):
    """Return a random integer in the range [0, max_int]."""

    max_bytes = int(math.ceil(math.log(max_int, 2) / 8))

    num = max_int + 1
    while num > max_int:
        rand_bytes = os.urandom(max_bytes)
        num = int(binascii.hexlify(rand_bytes), 16)

    return num


def generate(length, entropy, diceware):
    """Generate and print a random password."""

    if not rand_available():
        print("Error: Unable to generate password because os.urandom is "
              "unavailable.", file=sys.stderr)
        sys.exit(1)

    password = []

    # Determine which alphabet to use.  We support random ASCII characters and
    # diceware words that are easier to remember.

    alphabet = alphabets.diceware if diceware else alphabets.ascii_chars
    separator = " " if diceware else ""

    # How many elements (i.e., characters or words) do we need?  By default, we
    # want at least 90 bit-strong passwords.

    if length:
        elements = length
    else:
        elements = int(math.ceil(entropy / math.log(len(alphabet), 2)))

    for _ in range(elements):
        rand_idx = rand_int(len(alphabet) - 1)
        password.append(alphabet[rand_idx])

    password = separator.join(password)
    entropy = math.log(len(alphabet) ** elements, 2)
    print("Password with %.1f bits of entropy:\n%s" % (entropy, password))


if __name__ == "__main__":
    args = parse_args()
    generate(args.length, args.entropy, args.diceware)
