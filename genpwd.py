#!/usr/bin/env python
#
# Copyright (C) 2008, 2011 Philipp Winter (phw@7C0.org)
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


import sys, string, random, math, os

# the character set used to generate the password
s = 'abcdefghijklmnopqrstuvwxyz' \
	'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
	'0123456789~!@#$%^&*()_+{}|' \
	':"<>?-=[]\\;\',./`'

chars = 20 # default password length
if len(sys.argv) == 2:
	chars = int(sys.argv[1])

# return a random number <= n
def rand( n ):
	c = ord(os.urandom(1))
	while c > n:
		c = ord(os.urandom(1))
	return c

print string.join([s[rand(len(s)-1)] for x in range(chars)], "")

print "\nPassword entropy: %d bits" % math.log(len(s) ** chars, 2)
