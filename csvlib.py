"""Tiny library for handling csv"""


import os
import csv
import itertools


# HELPER FUNCTIONS
def is_type(_type, x):
    try:
        return str(_type(x)) == x
    except ValueError:
        return False


def determine_type(x):
    """Determine the type of x"""
    types = (int, float, str)
    _type = filter(lambda a: is_type(a, x), types)[0]
    return _type(x)


def dmap(fn, record):
    """map for a directory"""
    values = (fn(v) for k, v in record.items())
    return dict(itertools.izip(record, values))


# FUNCTIONS
def read_csv(filename, delimiter=",", skip=0, guess_type=True):
    """Read a CSV file"""
    f = open(filename, 'r')

    # Skip the n first lines
    for i in range(skip):
        f.readline()

    for line in csv.DictReader(f, delimiter=delimiter):
        if guess_type:
            yield dmap(determine_type, line)
        else:
            yield line

    f.close()


def write_csv(filename, fieldnames, data=None, rows=None, mode="w"):
    """Write the data to the specified filename
    
    Usage
    -----
    >>> write_csv(filename, fieldnames, data, mode=mode)

    Parameters
    ----------
    filename : str
        The name of the file

    fieldnames : list of strings
        The names of the columns (or fields):
        (fieldname1, fieldname2, ...)

    data : list of dictionaries
        [{fieldname1: a1, fieldname2: a2},
         {fieldname1: b1, fieldname2: b2},
         ...
         ]
    mode : str
        "w": write the data to the file by overwriting it
        "a": write the data to the file by appending them

    Returns
    -------
    None. A CSV file is written.

    """
    if data == rows == None:
        msg = "You must specify either data or rows"
        raise ValueError(msg)

    elif data != None and rows != None:
        msg = "You must specify either data or rows. Not both"
        raise ValueError(msg)

    header = dict((x, x) for x in fieldnames)
    f = open(filename, mode)
    if data:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if mode == "w":
            writer.writerow(header)
        writer.writerows(data)
    elif rows:
        writer = csv.writer(f)
        if mode == "w":
            writer.writerow(fieldnames)
        writer.writerows(rows)

    f.close()
    print "Saved %s." % filename


def format_to_csv(filename, skiprows=0):
    """Convert a file to a .csv file"""
    input_file = open(filename, "r")

    if skiprows:
        [input_file.readline() for _ in range(skiprows)]
 
    new_filename = os.path.splitext(filename)[0] + ".csv"
    output_file = open(new_filename, "w")

    header = input_file.readline().split()
    reader = csv.DictReader(input_file, fieldnames=header, delimiter="\t")
    writer = csv.DictWriter(output_file, fieldnames=header, delimiter=",")
    
    # Write header
    writer.writerow(dict((x, x) for x in header))
    
    # Write rows
    for line in reader:
        if None in line: del line[None]
        writer.writerow(line)
    
    input_file.close()
    output_file.close()
    print "Saved %s." % new_filename


def fus_to_csv(filename):
    format_to_csv(filename, skiprows=2)


def linelist_to_csv(filename):
    format_to_csv(filename, skiprows=0)


