# machine-translation
Find strings in po files that matches to Pontoon's machine translation results.

INSTALL
-------
* Manually
  - Clone the repository
  - Install using `sudo python3 setup.py install`
* Using pip:
  - `pip install ponmatch` (not released yet!)

USAGE
-----
* `ponmatch -h` will give details for usage.

WARNINGS
--------
* Please, do not use `--apply` with `--similarmatch` as it will also match strings that are slightly different.
* You can use `ponmatch file <params here> > output.csv` and then check results in a spreadsheet file for each variation of the match.

TODO
----
[ ] Support for plural strings

LICENSE
-------
Copyright 2018 Emin Mastizada. Package is released under MPLv2 License. Read LICENSE file for more details.
