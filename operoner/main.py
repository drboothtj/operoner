'''
this is the main routine for operoner
'''
import logging
from operoner.parser import parser

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

if __name__ == "__main__":
    main()
