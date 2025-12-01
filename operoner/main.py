'''
this is the main routine for operoner
'''
import logging

from operoner.parser import parser
from operoner.operons import get_operons
from operoner.utils import utils

def initialize_logging() -> None:
    '''
    Set up and configure logging.
        Arguments: None
        Returns: None
    '''
    logging_level = logging.DEBUG
    logging.basicConfig(
        level=logging_level,
        format='[%(asctime)s] %(levelname)-10s: %(message)s',
        datefmt='%H:%M:%S')
    logging.info("Running operoner version 0.0.1...")

def main() -> None:
    '''
    main routine for operoner
        arguments:
            None
        returns:
            None
    '''
    initialize_logging()
    args = parser.parse_args()
    logging.getLogger().setLevel(args.logging)
    operons = get_operons(args.genbank_path, args.target_loci, args.distance, args.min_members)
    #outputs
    printed_output = False
    #if args.faa_prefix:
    #    print('write to faa (NOT IMPLEMENTED)')
    #    printed_output = True
    #if args.fna_prefix:
    #    print('write to fna (NOT IMPLEMENTED)')
    #    printed_output = True
    if args.txt_path:
        utils.lol_to_csv(operons, args.txt_path)
        printed_output = True
    if printed_output is False:
        for line in operons:
            print(','.join(line))
    #else print text output to console

    #add graphing function to iterate ig

if __name__ == "__main__":
    main()
