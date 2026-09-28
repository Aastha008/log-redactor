import sys
import argparse
from src.core import Redactor
from src.config import load_config

def run_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, help='Input file path')
    args = parser.parse_args()
    
    redactor = Redactor(load_config())
    stream = open(args.file, 'r') if args.file else sys.stdin
    
    for line in redactor.process_stream(stream):
        sys.stdout.write(line)