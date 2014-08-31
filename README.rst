======
CSVLIB
======

**csvlib** is a tiny library for handling csv in Python. It's a wrapper for the csv module.


Usage
-----

* Read a csv file::

    data = read_csv(filename)


* Write a csv file::

    write_csv(filename, fieldnames, data=data)

    write_csv(filename, fieldnames, rows=rows)


