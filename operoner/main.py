'''
this is the main routine for operoner
'''
import logging
from operoner.parser import parser
from operoner.operons import get_operons

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
    print(operons) #print to csv!
    #add graphing function to iterate ig!

if __name__ == "__main__":
    main()
