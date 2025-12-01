'''
general utils for operoner
'''
import csv
from collections import OrderedDict
from typing import List

def lol_to_csv(lol: List[List], filename):
    '''
    convert a list of lists to lines of comma seperated text
        arguments:
            lol: the list of lists
        returns:
            lines: lines of comma seperated values
    '''
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(lol)

def csv_to_list(csv_path: str) -> List:
    '''
    Take single line .csv and return the contents as a list
        arguments:
            csv_path: path to .csv
        returns:
            list(row): a list of the file contents
    '''
    with open(csv_path, newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)
        if len(rows) == 1:
            row = rows[0]   # first (and only) row
            return row
        raise Exception( #add custom
            f'{csv_path} has more than one line.',
            ' Please ensure target loci are comma seperated on a single line.'
        )

def get_next_entry(target, odict: OrderedDict) -> str:
    '''
    gets the next entry in an ordered dictionary
        arguments:
            target: the key of the targeted entry
            odict: the ordered dictionary
        returns:
            keys[idx + 1]: the key of the entry after the target
    '''
    keys = list(odict.keys())
    try:
        idx = keys.index(target)
        return keys[idx + 1]  # next gene
    except IndexError:
        return None  # target is the last gene
    except ValueError: #add custom
        raise
