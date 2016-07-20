genpwd
======

Genpwd is a minimal, pure-Python password generator.  It generates
variable-length, secure passwords using entropy from `os.urandom()`.  It is able
to generate diceware (longer but easier to remember) as well as classical
passwords (shorter but harder to remember).

Running genpwd
----------------

To generate a secure-by-default password, run:

    $ ./genpwd.py

To change the password's entropy, use the `-e` parameter:

    $ ./genpwd.py -e 100

To change the password's length, use the `-l` parameter:

    $ ./genpwd.py -l 15

To use diceware instead of classical passwords, use the `-d` parameter:

    $ ./genpwd.py -d

Feedback
--------

Contact: Philipp Winter <phw@nymity.ch>  
OpenPGP fingerprint: `B369 E7A2 18FE CEAD EB96  8C73 CF70 89E3 D7FD C0D0`
