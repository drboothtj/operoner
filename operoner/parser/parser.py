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
        '-d', '--distance',
        type=int,
        default=200,
        help=(
            'The maximum intergenic distance allowed between genes in an operon.\n'
            'Default: %(default)s'
            )
    )
    parser.add_argument(
        '-m', '--min-members',
        type=int,
        default=1,
        help=(
            'The minimum number of members required to be considered an operon.\n'
            'Default: %(default)s'
            )
    )
    parser.add_argument(
        '-t', '--target-loci',
        type=str,
        default=None,
        help=(
            'Path to a single line .csv file specifying specific starting loci.\n'
            'Operoner will treat each target as the start of an operon.\n'
            'Default: %(default)s')
    )
    return parser

def get_output_parser(arg_parser):
    '''
    Create an argument group for outputs.
        Arguments:
            arg_parser: the basic argument parser
        Returns:
            arg_parser: the argument parser with arguments added
    '''
    output_parser = arg_parser.add_argument_group(
            'output options', 'output options for operoner'
            )
    #output_parser.add_argument(
    #    '-faa', '--faa-prefix',
    #    type=str,
    #    default=None,
    #    help=(
    #        'Write the amino acid sequence of operon members to inividual .faa files'
    #        'using the prefix provided. \n'
    #        'One file will be written per operon.'
    #        'Default: %(default)s')
    #)
    #output_parser.add_argument(
    #    '-fna', '--fna-prefix',
    #    type=str,
    #    default=None,
    #    help=(
    #        'Write each predicted operon to inividual .fna files'
    #        'using the prefix provided. \n'
    #        'One file will be written per operon.'
    #        'Default: %(default)s')
    #)
    output_parser.add_argument(
        '-txt', '--txt-path',
        type=str,
        default=None,
        help=(
            'Write predicted operons to a .txt file'
            'using the path provided. \n'
            'One file will be written where each line details an operon.'
            'Default: %(default)s')
    )
    return arg_parser


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
        help='Set the logging level\n'
        'Default: %(default)s'
    )
    return arg_parser

def parse_args():
    '''
    get the arguments from the console via the parser
    '''
    arg_parser = get_parser()
    get_output_parser(arg_parser)
    get_config_parser(arg_parser)
    args = arg_parser.parse_args()
    return args
