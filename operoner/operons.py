'''
predict operons from a genbank file
    functions:
        !!!
'''
import logging
from collections import OrderedDict
from typing import List

from Bio import SeqIO

from operoner.utils import utils

def get_colinear(cdses: OrderedDict, target_loci: List, distance: int) -> List[List[str]]:
    '''
    Take in cds infromation and return cds names for each operon
    '''
    operons = []
    seen = set()
    for loci in target_loci:
        if loci not in seen:
            seen.add(loci)
            new_loci = loci
            new_operon = [loci]
            colinear = True
            operon_direction = cdses[loci]['direction']
            while colinear is True and new_loci is not None:
                old_loci = new_loci
                new_loci = utils.get_next_entry(new_loci, cdses)
                if new_loci is None:
                    break
                if (
                    cdses[new_loci]['direction'] == operon_direction
                    and (cdses[new_loci]['start'] - cdses[old_loci]['end'] < distance)
                ):
                    new_operon.append(new_loci)
                    seen.add(loci)
                else:
                    colinear = False
            operons.append(new_operon)
    return operons
    #we need to remove already called loci from targets

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

def get_operons(
    genbank_path: str, target_loci: str=None, ig: int=200, min_length: int=2
    ) -> List[List[str]]:
    '''
    get operons from genbank file
        arguments:
            genbank_path: path to the genbank file
            target_loci: path to a single line .csv containing speciifc loci (optional)
            ig:

    '''
    cdses = get_locus_positions(genbank_path)
    if target_loci:
        target_loci = utils.csv_to_list(target_loci)
    else:
        target_loci = cdses.keys()
    operons = get_colinear(cdses, target_loci, ig)
    operons = [operon for operon in operons if len(operon) >= min_length]
    logging.info(
        "Identified %s operons...", len(operons)
        )
    #add min size filer?
    #add printing to .txt
