'''
this is the main routine for operoner
'''
import csv
import logging
from typing import Dict, List
from collections import OrderedDict
from operoner.parser import parser

from Bio import SeqIO

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
        else:
            raise Exception(
                f'{csv_path} has more than one line. Please ensure target loci are comma seperated on a single line.'
            )

def get_next_entry(target, odict):
    keys = list(odict.keys())
    try:
        idx = keys.index(target)
        return keys[idx + 1]  # next gene
    except IndexError:
        return None  # target is the last gene
    except ValueError:
        raise

def get_operons(cdses: OrderedDict, target_loci: List) -> List[List[str]]:
    '''
    Take in cds infromation and return cds names for each operon
    '''
    operons = []
    for loci in target_loci:
        new_operon = [loci]
        if cdses[loci]['direction'] == 1:
            print(loci)
            print(get_next_entry(loci, cdses))
        elif cdses[loci]['direction'] == -1:
            print('retreat!')

def get_locus_positions(gbk_path: str) -> OrderedDict:
    '''
    read a genbank file from the path and return cds details
    '''
    cdses = OrderedDict()
    for record in SeqIO.parse(gbk_path, "genbank"):
        for feature in record.features:
            if feature.type == "CDS":
                name = feature.qualifiers.get("locus_tag")[0] #add parameter for qualifier...
                start = int(feature.location.start)
                end = int(feature.location.end)
                strand = feature.location.strand
                cdses[name] = {"start" : start, "end" : end, "direction" : strand}
    return cdses 
      

def initialize_logging() -> None:
    '''Set up and configure logging.
        Arguments: None
        Returns: None
    '''
    logging_level = logging.DEBUG
    logging.basicConfig(
        level=logging_level,
        format='[%(asctime)s] %(levelname)-10s: %(message)s',
        datefmt='%H:%M:%S')
    logging.info("Running operoner version 0.0.1...")

def main():
    '''
    main routine for operoner
    '''
    initialize_logging()
    args = parser.parse_args()
    logging.getLogger().setLevel(args.logging)
    cdses = get_locus_positions(args.genbank_path)
    if args.target_loci:
        target_loci = csv_to_list(args.target_loci)
    else:
        target_loci = cdses.keys()
    operons = get_operons(cdses, target_loci)    #calc distances and operons
    #write to file

if __name__ == "__main__":
    main()
