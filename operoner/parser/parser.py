'''
parser for operoner
'''
import argparse
import logging
from argparse import RawTextHelpFormatter

def get_parser():
    '''
    create a parser object for operoner
    '''
    parser = argparse.ArgumentParser(
        "operoner",
        description="operoner: quick and dirty operon prediction in Python",
        epilog="Written by Dr. Thom Booth, 2025.",
        formatter_class=RawTextHelpFormatter
        )
    parser.add_argument(
      'genbank_path',
      type=str,
      default=None,
      help=('path to genbank file')
    )
    parser.add_argument(
      '-t', '--target-loci',
      type=str,
      default=None,
      help=('path to a list of loci to identify (comma seperated)')
    )
    return parser

def get_config_parser(arg_parser):
    '''
    Create an argument group for basic config details.
        Arguments:
            arg_parser: the basic argument parser
        Returns:
            arg_parser: the argument parser with arguments added
    '''
    config_parser = arg_parser.add_argument_group(
            'basic configuration', 'basic configuration of operoner'
            )
    config_parser.add_argument(
        '-l',
        '--logging',
        default='ERROR',
        choices=[
            logging.getLevelName(level) for level in [
               logging.DEBUG, logging.ERROR, logging.INFO, logging.WARNING
               ]
            ],
        help='set the logging level\n'
        '(default: %(default)s)'
    )
    return arg_parser
  

def parse_args():
    '''
    get the arguments from the console via the parser
    '''
    arg_parser = get_parser()
    get_config_parser(arg_parser)
    args = arg_parser.parse_args()
    return args
